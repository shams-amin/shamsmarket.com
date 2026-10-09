#!/usr/bin/env python3
"""Tells Bing and the other IndexNow search engines that a page on shamsmarket.com changed. No installs needed.

    python3 tools/indexnow.py                 # the home page
    python3 tools/indexnow.py /some-page/     # other pages, as paths

Run it after a change is live (about a minute after the push), and only when what a page says changed.
Bing feeds Microsoft Copilot and is one of the sources of ChatGPT search; Yandex, Naver, Seznam and Yep also read
IndexNow. Google does not use IndexNow; for Google, Search Console and the sitemap do this job.

The key is the file docs/<32 letters and digits>.txt. It is public on purpose: it only proves that the person
sending the ping controls the site. Do not delete or rename it; if it is ever lost, make a new one with the same
pattern and run this again."""
import pathlib, re, sys, urllib.error, urllib.parse, urllib.request

SITE = 'https://www.shamsmarket.com'
DOCS = pathlib.Path(__file__).resolve().parent.parent / 'docs'
ANSWERS = {200: 'accepted', 202: 'received; the key is being checked', 400: 'the request was malformed',
           403: 'the key was not accepted (is the key file live?)', 422: 'the address does not belong to this site',
           429: 'too many requests; try again later'}


def main(paths):
    keys = [f.stem for f in DOCS.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}', f.stem)]
    if len(keys) != 1:
        print(f'Expected one IndexNow key file in docs/, found {len(keys)}.'); return 1
    key = keys[0]
    urls = [SITE + (p if p.startswith('/') else '/' + p) for p in (paths or ['/'])]
    status = 0
    for url in urls:
        ping = 'https://api.indexnow.org/indexnow?' + urllib.parse.urlencode({'url': url, 'key': key})
        try:
            with urllib.request.urlopen(ping, timeout=30) as r: code = r.status
        except urllib.error.HTTPError as e: code = e.code
        except OSError as e:
            print(f'{url}: could not reach IndexNow ({e}). Nothing is broken; try again from another network.'); status = 1; continue
        print(f'{url}: {code} {ANSWERS.get(code, "")}'.rstrip())
        if code not in (200, 202): status = 1
    return status


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
