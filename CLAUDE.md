# Shams Market website: instructions for Claude

This repository is the live website of Shams Market, an Afghan bakery, halal butcher, grocery and kitchen at
3510 Auburn Blvd, Sacramento. The owner is Shams Amin. The site is one static page at
https://www.shamsmarket.com.

There is no build step and nothing to install. The files in `docs/` are the website exactly as visitors get it.
GitHub Pages publishes the `docs/` folder of the `main` branch, so **pushing to `main` publishes the change**.

## How to make a change

1. Edit the files under `docs/`. Most requests only touch `docs/index.html`.
2. Run `python3 tools/check.py` and fix anything it reports.
3. If you have a browser tool, look at `docs/index.html` at phone width (about 390 px) and desktop width
   (about 1440 px) before publishing. A layout change needs this; a wording change usually does not.
4. Commit straight to `main` with a short message that says what changed, and push. Do not open a branch or a
   pull request. Shams wants the change live, and `main` is the only branch.
5. Wait about a minute, then confirm the change at https://www.shamsmarket.com/. Browsers and GitHub's servers
   can hold the previous copy for up to 10 minutes. Adding `?v=2` to the address gets a fresh copy.
6. Tell Shams what changed in a sentence or two, in plain words.

To undo a change, `git revert` the commit and push. The page returns to how it was within a minute.

## How Shams wants this handled

- Do the whole job without checking in. Ask first only when the request could be read two ways and the
  difference would be public, such as a price, a date or a phone number.
- The wording on the page was approved. Change the words he asks about and leave the rest alone.
- No photo may show a person or any part of a person. Open every photo at full size and look at all of it
  before it goes on the page.
- Do not use photos from the store's Google listing or from the old website. Use photos Shams sends, or stock
  photos whose license allows business use. Add the source to the photo list in `README.md`.
- Keep the layout one consistent system. Reuse the styles that are there. No decoration for its own sake.
- Dari text uses Persian letters (ی and ک, never the Arabic ي and ك). The store's name in Dari is شمس مارکیت.
  If a new item needs a Dari name and Shams did not give one, ask him for it.

## Where things are

| File | What it holds |
| --- | --- |
| `docs/index.html` | Every word on the page, plus the facts for search engines at the top. Comments mark each section: header, top of page, inside the market, from our kitchen, address/hours/phone, footer. |
| `docs/assets/site.css` | All the styling. Colors, fonts and sizes are named values at the top of the file. |
| `docs/assets/site.js` | The live "Open now" status (worked out in the store's time zone), the copy buttons, and the bar of buttons on phones. |
| `docs/assets/logo.svg`, `logo-full.svg` | The logo: the short version for the header, the full version for the footer. |
| `docs/img/` | The photos, each in a large and a small size. |
| `docs/404.html` | The page shown for an address that does not exist. Its styles are inside the file. |
| `docs/shop/`, `docs/product-page/` | Addresses from the old website. Each one sends the visitor to the new page. |
| `docs/CNAME`, `docs/.nojekyll` | Files GitHub Pages needs. Do not change, move or delete them. |
| `docs/robots.txt`, `docs/sitemap.xml` | For search engines. |
| `tools/check.py` | The check to run before every push. |

Do not rename or move the `docs/` folder. GitHub Pages is set to publish that exact folder.

## Common changes

### Opening hours

The hours appear in six places in `docs/index.html`. Each is marked with a comment that starts `HOURS`:

1. the line shown until the live status loads ("Open every day, 9 AM to 9 PM")
2. the last sentence of the opening paragraph
3. the fact "Open 7 days a week"
4. the Hours block: the headline, the note under it, and the seven `data-hours` values
5. the second line of the footer list
6. the page description and the `openingHoursSpecification` block near the top of the file

`data-hours` is 24-hour time: `09:00-21:00`. A day with a midday break is `09:00-13:00,14:00-21:00`. A closed day
is an empty value, `data-hours=""`. The live status reads these seven values, so they must be right.
`openingHoursSpecification` must say the same thing; `tools/check.py` compares the two and reports any
difference. Also change each day's hidden text (`<span class="sr">Friday, 9 AM to 9 PM</span>`), which screen
readers use.

### A temporary notice (a holiday closure, a new item)

A comment near the top of `<body>` in `docs/index.html` holds a ready-made notice bar. Copy its `<p class="notice">`
line to just below the comment and change the text. It shows as a red bar across the top of the page. Remove
the line when the notice is over. A notice does not change the "Open now" status. For a closed day, also set
that day's `data-hours` to `""` for the week and put it back afterwards, or tell Shams the status will still
say open.

### Phone number or address

The phone number is in `tel:` links, in visible text, in one `data-copy` value, and in `"telephone"` near the top.
The address is in visible text, in one `data-copy` value, in the directions links (the long Google Maps
address that starts `https://www.google.com/maps/dir/`), in the page description, and in the `"address"` block
near the top. Change every one. Search the file for the old value to be sure none is left.

### Menu items

In the kitchen section each dish is one `<li>` inside `<ul class="menu">`. Copy an existing `<li>`, then change
the English name, the Dari name and the one-line description. Prices are not shown today. If Shams wants
prices, add them at the end of the description line, the same way for every dish.

### Market cards

Each card is one `<article class="card">` with a photo, an English and a Dari title, and a short description.
There are five. The first two are large and the last three are small on wide screens. If the number of cards
changes, check the layout at desktop width.

### Replacing or adding a photo

Each photo has a large and a small file. Keep these shapes and sizes so the cards stay lined up:

| Photo | Shape | Large file | Small file |
| --- | --- | --- | --- |
| `hero` (top of page) | 3:2 | 2000 px wide | 1000 px wide |
| `kitchen` | 3:2 | 1600 px wide | 900 px wide |
| `bakery`, `butcher` | 3:2 | 1400 px wide | 800 px wide |
| `produce`, `groceries`, `clothing` | 4:3 | 1200 px wide | 800 px wide |

Save as JPEG in sRGB, quality about 76, each file under 450 KB. The simplest way is to keep the same file
names. If a name changes, update `src`, `srcset`, `width` and `height` on the `<img>`. Always rewrite the `alt`
text so it describes the new photo. The hero photo is also named in the `preload` line and in the `og:image`
and `"image"` values near the top of the file.

### Colors, fonts, spacing

These are named values at the top of `docs/assets/site.css` (for example `--red`, `--black`, `--sans`). The dark
theme overrides some of them in the two blocks just below. Change a value there and it changes everywhere.

## Hosting and domain

- **Repository:** `shams-amin/shamsmarket.com` on GitHub. It is public because free GitHub Pages needs a public
  repository. Do not put anything private in it.
- **GitHub Pages:** publishes branch `main`, folder `/docs`. Custom domain `www.shamsmarket.com`, set by
  `docs/CNAME`. HTTPS is enforced. `shamsmarket.com` without the `www` redirects to `www.shamsmarket.com`.
- **Domain:** `shamsmarket.com` is registered with Squarespace Domains. The DNS records are managed there:
  four `A` records and four `AAAA` records for `shamsmarket.com` that point to GitHub Pages, and one `CNAME`
  record for `www` that points to `shams-amin.github.io`. There is no email on this domain.
- **Cost:** hosting is free. The only cost is the yearly domain renewal at Squarespace.
- The old Wix website is not used any more.

If the site is down, check in this order: the latest run under the repository's Actions tab ("pages build and
deployment"), the Pages settings of the repository, and the DNS records at Squarespace.

## Checking the live site

```
curl -sI https://www.shamsmarket.com/ | head -5        # expect HTTP/2 200
curl -sI https://shamsmarket.com/ | head -5            # expect a 301 to https://www.shamsmarket.com/
```
