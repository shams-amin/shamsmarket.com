#!/usr/bin/env python3
"""Checks the website files before they are published. No installs needed.

    python3 tools/check.py

It prints every problem it finds and exits with 1 if there are any.
What it checks: every file the pages and the stylesheet point to exists; the facts for search engines can be read
and agree with the page (hours, phone, address, site name); every phone number and every "9 AM to 9 PM" style time
on the page agrees with them; the page title, description and headline are in shape for search results; the top
photo loads first and every photo has a description and a size; the Dari text uses Persian letters; and the files
GitHub Pages, Google Search Console and IndexNow need are in place."""
import datetime, html, json, pathlib, re, sys
from html.parser import HTMLParser

DOCS = pathlib.Path(__file__).resolve().parent.parent / 'docs'
SITE = 'https://www.shamsmarket.com/'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
SVG_SELF = {'path', 'circle', 'rect', 'use', 'stop', 'line', 'polyline', 'polygon', 'ellipse'}
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
PHONE = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
TIMES = re.compile(r'\b(\d{1,2}(?::\d{2})? [AP]M) to (\d{1,2}(?::\d{2})? [AP]M)\b')
problems, notes = [], []


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.refs, self.imgs, self.links, self.ids, self.anchors = [], [], [], [], [], []
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
        if tag == 'link': self.links.append(a)
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


def exists(ref, base):
    target = ref.split('#')[0].split('?')[0]
    if not target: return True
    file = (DOCS / target.lstrip('/')) if target.startswith('/') else (base / target)
    if file.is_dir(): file = file / 'index.html'
    return file.exists()


def check_page(path):
    name = str(path.relative_to(DOCS))
    text = path.read_text(encoding='utf-8')
    page = Page(); page.feed(text); page.close()
    if page.unbalanced: problems.append(f'{name}: {page.unbalanced[0]}')            # the first mismatch is the real one
    elif page.stack: problems.append(f'{name}: <{page.stack[-1][0]}> opened at line {page.stack[-1][1]} is never closed')
    for tag, ref, line in page.refs:
        if local(ref) and not exists(ref, path.parent): problems.append(f'{name} line {line}: points to "{ref}", which does not exist')
    for ref in re.findall(r'url\(([^)]+)\)', text):                                  # fonts named in a <style> block
        ref = ref.strip('\'"')
        if local(ref) and not exists(ref, path.parent): problems.append(f'{name}: a style points to "{ref}", which does not exist')
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


def clock(hhmm):
    """'09:00' -> '9 AM', '21:30' -> '9:30 PM', the way the page writes times."""
    h, m = map(int, hhmm.split(':'))
    return f'{(h % 12) or 12}{":%02d" % m if m else ""} {"AM" if h < 12 else "PM"}'


def main():
    index = DOCS / 'index.html'
    if not index.exists():
        print('docs/index.html is missing'); return 1
    page, text = check_page(index)
    for other in sorted(DOCS.rglob('*.html')):
        if other != index: check_page(other)
    css = DOCS / 'assets' / 'site.css'
    for ref in re.findall(r'url\(([^)]+)\)', css.read_text(encoding='utf-8')):
        ref = ref.strip('\'"')
        if local(ref) and not exists(ref, css.parent): problems.append(f'assets/site.css points to "{ref}", which does not exist')

    def meta(pattern):
        m = re.search(pattern, text, re.S)
        return html.unescape(m.group(1)) if m else None

    # the facts for search engines: one block for the store, one for the website's name
    blocks = []
    for i, raw in enumerate(page.ld):
        try: blocks.append(json.loads(raw))
        except ValueError as e: problems.append(f'index.html: facts block {i + 1} for search engines is not valid JSON ({e})')
    store = next((b for b in blocks if isinstance(b, dict) and 'address' in b), None)
    site = next((b for b in blocks if isinstance(b, dict) and b.get('@type') == 'WebSite'), None)
    if len(page.ld) != 2: problems.append(f'index.html: expected two facts blocks for search engines (the store and the website); found {len(page.ld)}')
    if not store: problems.append('index.html: the facts for search engines have no block with the store\'s address')
    if not site: problems.append('index.html: the facts for search engines have no WebSite block (it sets the site name Google shows)')
    for b in blocks:
        if re.search(r'"(aggregateRating|review)"', json.dumps(b)):
            problems.append('index.html: remove aggregateRating and review from the facts for search engines; '
                            'Google shows no stars for a business\'s markup of reviews about itself')
    if site:
        if site.get('name') != meta(r'<meta property="og:site_name" content="(.*?)">'):
            problems.append('index.html: the WebSite "name" should be the same as og:site_name')
        if site.get('url') != SITE: problems.append(f'index.html: the WebSite "url" should be {SITE}')

    if store:
        want = {d: sorted(tuple(s.split('-')) for s in spans.split(',') if s) for d, spans in page.hours.items()}
        got = {d: [] for d in range(7)}
        for spec in store.get('openingHoursSpecification', []):
            days = spec['dayOfWeek'] if isinstance(spec['dayOfWeek'], list) else [spec['dayOfWeek']]
            for day in days: got[DAYS.index(day)].append((spec['opens'], spec['closes']))
        got = {d: sorted(v) for d, v in got.items()}
        if sorted(page.hours) != list(range(7)):
            problems.append('index.html: the week list should have one data-day for each of 0 to 6')
        else:
            if want != got:
                for d in range(7):
                    if want[d] != got[d]:
                        problems.append(f'index.html: {DAYS[d]} hours differ. The page says {want[d] or "closed"}, '
                                        f'the facts for search engines say {got[d] or "closed"}')
            # every written time on the page ("9 AM to 9 PM") must be one of the real opening times
            real = {(clock(o), clock(c)) for spans in want.values() for o, c in spans}
            for o, c in sorted(set(TIMES.findall(text))):
                if (o, c) not in real:
                    problems.append(f'index.html: the page says "{o} to {c}", but the hours list says '
                                    + ('; '.join(f'{a} to {b}' for a, b in sorted(real)) or 'closed every day'))
            for d in range(7):
                if len(want[d]) == 1:
                    o, c = want[d][0]
                    if f'<span class="sr">{DAYS[d]}, {clock(o)} to {clock(c)}</span>' not in text:
                        problems.append(f'index.html: the hidden text for {DAYS[d]} should read "{DAYS[d]}, {clock(o)} to {clock(c)}"')
        digits = lambda s: re.sub(r'\D', '', s)[-10:]
        phone = digits(store.get('telephone', ''))
        phones = {digits(t) for t in page.tels} | {phone} | {digits(p) for p in PHONE.findall(text)}
        if len(phones) != 1: problems.append(f'index.html: more than one phone number is in use: {sorted(phones)}')
        notes.append('hours: ' + '; '.join(f'{DAYS[d][:3]} {", ".join("-".join(s) for s in want.get(d, [])) or "closed"}' for d in (1, 2, 3, 4, 5, 6, 0)))
        addr = store.get('address', {})
        street = addr.get('streetAddress', '')
        full = f"{street}, {addr.get('addressLocality', '')}, {addr.get('addressRegion', '')} {addr.get('postalCode', '')}"
        if f'id="address-text">{street}<' not in text:
            problems.append(f'index.html: the big address line should read exactly "{street}", as in the facts for search engines')
        if f'data-copy="{full}"' not in text:
            problems.append(f'index.html: the Copy address button should copy exactly "{full}"')
        if f'<li>{full}</li>' not in text:
            problems.append(f'index.html: the footer address should read exactly "{full}"')
        for tag in re.findall(r'<iframe\b[^>]*>', text):
            if street not in html.unescape(tag): problems.append(f'index.html: the map\'s title should name the address "{street}"')
        notes.append('address: ' + full)
        notes.append('phone: (%s) %s-%s' % (phone[:3], phone[3:6], phone[6:]))

    # how the page shows up in search results (see SEO.md)
    title = meta(r'<title>(.*?)</title>')
    desc = meta(r'<meta name="description" content="(.*?)">')
    if not title: problems.append('index.html: there is no <title>')
    elif len(title) > 60: problems.append(f'index.html: the <title> is {len(title)} characters. Google sets no limit, but past '
                                          f'about 60 it cuts the title off on phones; keep it to 60')
    if not desc: problems.append('index.html: there is no meta description')
    elif len(desc) > 155: problems.append(f'index.html: the meta description is {len(desc)} characters; keep it to 155 so it is not cut off')
    if title and meta(r'<meta property="og:title" content="(.*?)">') != title:
        problems.append('index.html: og:title should be the same as the <title>')
    if desc and meta(r'<meta property="og:description" content="(.*?)">') != desc:
        problems.append('index.html: og:description should be the same as the meta description')
    if meta(r'<link rel="canonical" href="(.*?)">') != SITE:
        problems.append(f'index.html: the canonical link should be {SITE}')
    if '<html lang="en">' not in text: problems.append('index.html: the page should start with <html lang="en">')
    if re.search(r'<meta name="robots" content="[^"]*(noindex|nosnippet)', text):
        problems.append('index.html: a robots meta tag keeps the page out of search results or its snippets')
    h1s = len(re.findall(r'<h1[\s>]', text))
    if h1s != 1: problems.append(f'index.html: there should be exactly one <h1>; found {h1s}')
    for tag in re.findall(r'<iframe\b[^>]*>', text):
        if 'title="' not in tag: problems.append('index.html: an <iframe> has no title')
        if 'loading="lazy"' not in tag: problems.append('index.html: an <iframe> should have loading="lazy"')

    # the top photo is the largest thing on the first screen: it must load first and never wait
    heroes = [(a, line) for a, line in page.imgs if a.get('fetchpriority') == 'high']
    if len(heroes) != 1: problems.append(f'index.html: exactly one photo, the top one, should have fetchpriority="high"; found {len(heroes)}')
    else:
        hero, line = heroes[0]
        if hero.get('loading') == 'lazy': problems.append(f'index.html line {line}: the top photo must not have loading="lazy"')
        pre = next((l for l in page.links if l.get('rel') == 'preload' and l.get('as') == 'image'), None)
        if not pre: problems.append('index.html: the top photo should have a <link rel="preload" as="image"> in the head')
        else:
            if pre.get('fetchpriority') != 'high': problems.append('index.html: the top photo\'s preload line should have fetchpriority="high"')
            if pre.get('imagesrcset') != hero.get('srcset') or pre.get('imagesizes') != hero.get('sizes'):
                problems.append('index.html: the top photo\'s preload line must list the same sizes as the photo itself '
                                '(imagesrcset = srcset, imagesizes = sizes), or browsers download it twice')

    # files search engines read
    robots = (DOCS / 'robots.txt').read_text() if (DOCS / 'robots.txt').exists() else ''
    if re.search(r'(?im)^\s*disallow:\s*/\s*$', robots): problems.append('docs/robots.txt blocks the whole site')
    if f'Sitemap: {SITE}sitemap.xml' not in robots: problems.append(f'docs/robots.txt should end with "Sitemap: {SITE}sitemap.xml"')
    sitemap = (DOCS / 'sitemap.xml').read_text() if (DOCS / 'sitemap.xml').exists() else ''
    if f'<loc>{SITE}</loc>' not in sitemap: problems.append(f'docs/sitemap.xml should list {SITE}')
    for day in re.findall(r'<lastmod>(.*?)</lastmod>', sitemap):
        try:
            if datetime.date.fromisoformat(day) > datetime.date.today() + datetime.timedelta(days=1):
                problems.append(f'docs/sitemap.xml: lastmod {day} is in the future')
            else: notes.append(f'sitemap lastmod: {day} (set it to the day the page\'s words last changed)')
        except ValueError: problems.append(f'docs/sitemap.xml: lastmod "{day}" is not a date like 2026-10-08')
    if not list(DOCS.glob('google*.html')):
        problems.append('docs/google….html is missing; Google Search Console needs that file to stay')
    keys = [f for f in DOCS.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}', f.stem)]
    if len(keys) != 1: problems.append(f'docs/ should hold exactly one IndexNow key file (32 letters and digits, .txt); found {len(keys)}')
    elif keys[0].read_text().strip() != keys[0].stem: problems.append(f'docs/{keys[0].name} should contain exactly its own name, {keys[0].stem}')

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
