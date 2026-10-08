#!/usr/bin/env python3
"""Checks the website files before they are published. No installs needed.

    python3 tools/check.py

It prints every problem it finds and exits with 1 if there are any.
What it checks: every file the pages point to exists; the facts for search engines can be read and agree
with the page (hours, phone); every photo has a description and a size; the Dari text uses Persian letters;
and the files GitHub Pages needs are in place."""
import json, pathlib, re, sys
from html.parser import HTMLParser

DOCS = pathlib.Path(__file__).resolve().parent.parent / 'docs'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
SVG_SELF = {'path', 'circle', 'rect', 'use', 'stop', 'line', 'polyline', 'polygon', 'ellipse'}
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
problems, notes = [], []


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.refs, self.imgs, self.ids, self.anchors = [], [], [], [], []
        self.hours, self.tels, self.ld, self._in_ld, self.unbalanced = {}, [], [], False, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID and tag not in SVG_SELF:
            self.stack.append((tag, self.getpos()[0]))
        for key in ('src', 'href'):
            if a.get(key): self.refs.append((tag, a[key], self.getpos()[0]))
        for key in ('srcset', 'imagesrcset'):
            for part in (a.get(key) or '').split(','):
                if part.strip(): self.refs.append((tag, part.strip().split()[0], self.getpos()[0]))
        if tag == 'img': self.imgs.append((a, self.getpos()[0]))
        if a.get('id'): self.ids.append(a['id'])
        if tag == 'a' and (a.get('href') or '').startswith('#'): self.anchors.append(a['href'][1:])
        if tag == 'a' and (a.get('href') or '').startswith('tel:'): self.tels.append(a['href'][4:])
        if 'data-day' in a: self.hours[int(a['data-day'])] = a.get('data-hours', '')
        if tag == 'script' and a.get('type') == 'application/ld+json': self._in_ld = True; self.ld.append('')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and tag not in SVG_SELF and self.stack and self.stack[-1][0] == tag: self.stack.pop()

    def handle_endtag(self, tag):
        if tag == 'script': self._in_ld = False
        if tag in VOID or tag in SVG_SELF: return
        if self.stack and self.stack[-1][0] == tag: self.stack.pop()
        else: self.unbalanced.append(f'</{tag}> at line {self.getpos()[0]} does not match the tag that is open'
                                     + (f' (<{self.stack[-1][0]}> from line {self.stack[-1][1]})' if self.stack else ''))

    def handle_data(self, data):
        if self._in_ld: self.ld[-1] += data


def local(ref):
    return not re.match(r'^(https?:|mailto:|tel:|sms:|data:|#|//)', ref)


def check_page(path):
    name = str(path.relative_to(DOCS))
    text = path.read_text(encoding='utf-8')
    page = Page(); page.feed(text); page.close()
    if page.unbalanced: problems.append(f'{name}: {page.unbalanced[0]}')            # the first mismatch is the real one
    elif page.stack: problems.append(f'{name}: <{page.stack[-1][0]}> opened at line {page.stack[-1][1]} is never closed')
    for tag, ref, line in page.refs:
        if not local(ref): continue
        target = ref.split('#')[0].split('?')[0]
        if not target: continue
        file = (DOCS / target.lstrip('/')) if target.startswith('/') else (path.parent / target)
        if file.is_dir(): file = file / 'index.html'
        if not file.exists(): problems.append(f'{name} line {line}: points to "{ref}", which does not exist')
    for a, line in page.imgs:
        if 'alt' not in a: problems.append(f'{name} line {line}: an image has no alt description')
        if not (a.get('width') and a.get('height')): problems.append(f'{name} line {line}: an image has no width and height')
    for anchor in page.anchors:
        if anchor and anchor not in page.ids: problems.append(f'{name}: a link goes to "#{anchor}", but nothing on the page has that id')
    dup = sorted({i for i in page.ids if page.ids.count(i) > 1})
    if dup: problems.append(f'{name}: these ids are used more than once: {", ".join(dup)}')
    if re.search('[يك]', text):
        problems.append(f'{name}: the Dari text has Arabic yeh or kaf; use the Persian letters (ی and ک)')
    return page, text


def main():
    index = DOCS / 'index.html'
    if not index.exists():
        print('docs/index.html is missing'); return 1
    page, text = check_page(index)
    for other in sorted(DOCS.rglob('*.html')):
        if other != index: check_page(other)

    # the facts for search engines
    if len(page.ld) != 1:
        problems.append('index.html: expected exactly one <script type="application/ld+json"> block')
    else:
        try:
            ld = json.loads(page.ld[0])
        except ValueError as e:
            ld = None; problems.append(f'index.html: the facts for search engines are not valid JSON ({e})')
        if ld:
            want = {d: sorted(tuple(s.split('-')) for s in spans.split(',') if s) for d, spans in page.hours.items()}
            got = {d: [] for d in range(7)}
            for spec in ld.get('openingHoursSpecification', []):
                days = spec['dayOfWeek'] if isinstance(spec['dayOfWeek'], list) else [spec['dayOfWeek']]
                for day in days: got[DAYS.index(day)].append((spec['opens'], spec['closes']))
            got = {d: sorted(v) for d, v in got.items()}
            if sorted(page.hours) != list(range(7)):
                problems.append('index.html: the week list should have one data-day for each of 0 to 6')
            elif want != got:
                for d in range(7):
                    if want[d] != got[d]:
                        problems.append(f'index.html: {DAYS[d]} hours differ. The page says {want[d] or "closed"}, '
                                        f'the facts for search engines say {got[d] or "closed"}')
            digits = lambda s: re.sub(r'\D', '', s)[-10:]
            phones = {digits(t) for t in page.tels} | {digits(ld.get('telephone', ''))}
            if len(phones) != 1: problems.append(f'index.html: more than one phone number is in use: {sorted(phones)}')
            notes.append('hours: ' + '; '.join(f'{DAYS[d][:3]} {", ".join("-".join(s) for s in want[d]) or "closed"}' for d in (1, 2, 3, 4, 5, 6, 0)))

    # what GitHub Pages needs
    cname = DOCS / 'CNAME'
    if not cname.exists() or not re.fullmatch(r'[a-z0-9.-]+\n?', cname.read_text()):
        problems.append('docs/CNAME must hold the one line "www.shamsmarket.com"')
    if not (DOCS / '.nojekyll').exists(): problems.append('docs/.nojekyll is missing (an empty file with that name)')
    for f in sorted((DOCS / 'img').glob('*')):
        if f.stat().st_size > 450_000: problems.append(f'docs/img/{f.name} is {f.stat().st_size // 1024} KB; keep photos under 450 KB')

    for n in notes: print(n)
    if problems:
        print(f'\n{len(problems)} problem(s):')
        for p in problems: print('  -', p)
        return 1
    print('All checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
