# Shams Market website: instructions for Claude

This repository is the live website of Shams Market, an Afghan bakery, halal butcher, grocery and kitchen at
3510 Auburn Blvd #2, Sacramento. The owner is Shams Amin. The site is one static page at
https://www.shamsmarket.com.

There is no build step and nothing to install. The files in `docs/` are the website exactly as visitors get it.
GitHub Pages publishes the `docs/` folder of the `main` branch, so **pushing to `main` publishes the change**.

## How to make a change

1. Edit the files under `docs/`. Most requests only touch `docs/index.html`. If the words on the page changed, set
   `<lastmod>` in `docs/sitemap.xml` to today's date. Change it only then: Google and Bing trust it only while it
   is honest.
2. Run `python3 tools/check.py` and fix anything it reports.
3. If you have a browser tool, look at `docs/index.html` at phone width (about 390 px) and desktop width
   (about 1440 px) before publishing. A layout change needs this; a wording change usually does not.
4. Commit straight to `main` with a short message that says what changed, and push. Do not open a branch or a
   pull request. Shams wants the change live, and `main` is the only branch.
5. Wait about a minute, then confirm the change at https://www.shamsmarket.com/. Browsers and GitHub's servers
   can hold the previous copy for up to 10 minutes. Adding `?v=2` to the address gets a fresh copy. If the words
   on the page changed, run `python3 tools/indexnow.py` so Bing (and Copilot and ChatGPT search, which use it)
   picks the change up at once.
6. Tell Shams what changed in a sentence or two, in plain words.

To undo a change, `git revert` the commit and push. The page returns to how it was within a minute.

## How Shams wants this handled

- Do the whole job without checking in. Ask first only when the request could be read two ways and the
  difference would be public, such as a price, a date or a phone number.
- Work only in this repository. Do not open, attach, clone or change any of Shams's other GitHub
  repositories, whatever the task.
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
| `docs/assets/fonts/` | The two typefaces, Jost (English) and Vazirmatn (Dari), and their license (`OFL.txt`). They are stored here so the page does not wait on Google Fonts. `site.css` and `404.html` load them. |
| `docs/favicon.ico`, `favicon.svg`, `favicon-192.png`, `apple-touch-icon.png` | The icon in browser tabs, on phone home screens and beside the site in Google results. |
| `docs/img/` | The photos, each in a large and a small size. |
| `docs/404.html` | The page shown for an address that does not exist. Its styles are inside the file. |
| `docs/shop/`, `docs/product-page/` | Addresses from the old website. Each one sends the visitor to the new page. |
| `docs/CNAME`, `docs/.nojekyll` | Files GitHub Pages needs. Do not change, move or delete them. |
| `docs/robots.txt`, `docs/sitemap.xml` | For search engines. |
| `docs/google4219baa0cb6fee68.html` | Proves to Google Search Console that Shams owns the site. Do not change, rename or delete it. |
| `docs/e6b48a8d8394d39b672ce4170b761de1.txt` | The IndexNow key, which lets the site tell Bing about a change. Public on purpose. Do not change, rename or delete it. |
| `tools/indexnow.py` | Tells Bing and the other IndexNow search engines that the page changed. Run it after a wording change is live. |
| `SEO.md` | The rules for search: the searches the store wants, what must match the Google listing, who may change what, and a log. Read it before touching the title, headline, address, phone or the facts for search engines. |
| `tools/check.py` | The check to run before every push. It compares every phone number, address and written time on the page with the facts for search engines, and checks the top photo, the fonts and the files search engines read. |

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

The address and phone on the page must read exactly as on the store's Google listing, character for
character: `3510 Auburn Blvd #2, Sacramento, CA 95821` and `(916) 514-1471`. Change them here only when they
have changed on the Google listing.

The phone number is in `tel:` links, in visible text, in one `data-copy` value, and in `"telephone"` near the top.
The address is in visible text (the big line and the footer), in one `data-copy` value, in the title of the
map, and in the `"address"` block near the top. Change every one; `tools/check.py` reports any that disagree.
The directions links and the map point at the Google listing itself, so they follow the listing. If the store
ever moves, get a new map address from Google Maps (Share, then Embed a map) and new `"geo"` numbers.

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
| `hero` (top of page) | 3:2 | 2000 px wide, plus a 1400 px middle size | 1000 px wide |
| `kitchen` | 3:2 | 1600 px wide | 900 px wide |
| `bakery`, `butcher` | 3:2 | 1400 px wide | 800 px wide |
| `produce`, `groceries`, `clothing` | 4:3 | 1200 px wide | 800 px wide |

Save as JPEG in sRGB, quality about 76, each file under 450 KB. The simplest way is to keep the same file
names. If a name changes, update `src`, `srcset`, `width` and `height` on the `<img>`. Always rewrite the `alt`
text so it describes the new photo. The hero photo is also named in the `preload` line and in the `og:image`
and `"image"` values near the top of the file. The hero comes in three sizes (`hero-1000.jpg`, `hero-1400.jpg`,
`hero-2000.jpg`) because it decides how fast the page appears; the `preload` line must list the same sizes as
the hero `<img>`, which `tools/check.py` checks. Photos the store took itself are worth more to customers and to
Google than stock photos, so swap them in whenever Shams sends some.

### Colors, fonts, spacing

These are named values at the top of `docs/assets/site.css` (for example `--red`, `--black`, `--sans`). The dark
theme overrides some of them in the two blocks just below. Change a value there and it changes everywhere.

## Search (SEO)

`SEO.md` holds the rules. The short version:

- The title, the description, the one `<h1>`, the address, the phone and the facts for search engines were set
  on 2026-10-08 so that the page agrees with the store's Google listing and says what people search for.
  Do not change them, or the words visitors read, for search reasons without asking Shams.
- Most of the store's search traffic comes through its Google Business Profile. Changes to that profile, or to
  Yelp, Zabihah, Apple or Bing listings, are made only with Shams's yes, every time.
- Never invent a fact, a search volume or a ranking. Nothing hidden, nothing written for AI systems, no
  `llms.txt`, no star-rating markup.
- Reviews: ask everyone the same way; never offer anything for one, ask only happy customers, pressure people
  in the store, or ask them to mention something specific. Google's policy forbids all four.
- A new page needs Shams's facts and something of his own (a menu with prices, his photos). No copies of a
  page with a word swapped.
- After a search change, leave it alone for 60 days.
- The site is verified in Google Search Console under Shams's Google account, and the sitemap is submitted.
  Bing hears about changes through IndexNow (`tools/indexnow.py`).

## Hosting and domain

- **Repository:** `shams-amin/shamsmarket.com` on GitHub. It is public because free GitHub Pages needs a public
  repository. Do not put anything private in it.
- **GitHub Pages:** publishes branch `main`, folder `/docs`. Custom domain `www.shamsmarket.com`, set by
  `docs/CNAME`. `shamsmarket.com` without the `www` redirects to `www.shamsmarket.com`.
- **HTTPS:** GitHub issues and renews the certificate by itself, and "Enforce HTTPS" in the repository's Pages
  settings sends `http://` visitors to `https://`. The certificate was first requested on 2026-10-08. If
  `http://www.shamsmarket.com/` ever stops redirecting to `https://`, switch Enforce HTTPS back on there, or
  run `gh api -X PUT repos/shams-amin/shamsmarket.com/pages -F https_enforced=true`.
- **Domain:** `shamsmarket.com` is registered with Squarespace Domains and renews there every autumn.
  `shamsmarket.net` is registered there too and is meant to forward to `shamsmarket.com`. On 2026-10-08 it did so
  only over `http://` (a temporary 302); `https://shamsmarket.net/` showed a Squarespace "Coming Soon" page. The fix
  is in Squarespace (Domains, shamsmarket.net): forward to `https://www.shamsmarket.com`, permanent, with SSL on.
  There is no email on either domain.
- **DNS records:** four `A` records for `shamsmarket.com` (`185.199.108.153`, `185.199.109.153`,
  `185.199.110.153`, `185.199.111.153`) and one `CNAME` record that points `www` to `shams-amin.github.io`.
  These are the addresses GitHub publishes for GitHub Pages. One `TXT` record,
  `_github-pages-challenge-shams-amin` with the value `8f39c52e3e0f77bff7b1f6d844b7de`, proves to GitHub that
  the domain belongs to the `shams-amin` account, so nobody else can publish a GitHub Pages site on it. Keep
  all six records wherever the DNS is managed.
- **Cost:** hosting is free. The only cost is the yearly domain renewal at Squarespace.

If the site is down, check in this order: the latest run under the repository's Actions tab ("pages build and
deployment"), the Pages settings of the repository, and the DNS records (the next section says where they are).

## The move away from Wix: one step left

Until 2026-10-08 this address showed a website built on Wix. The new site went live that day by changing the
DNS records. One step is left: the domain still uses Wix's nameservers (`ns0.wixdns.net` and
`ns1.wixdns.net`), so the DNS records above are kept in Shams's Wix account, under Domains, shamsmarket.com,
Manage DNS Records.

**Until the nameservers have been moved, do not cancel the Wix plan, and do not unassign, remove or transfer
the domain inside Wix.** Any of these can delete the DNS records and take the site down. Wix now shows a
warning that the domain "is set to point away from Wix", with a Try Again button. The warning is expected.
Do not click Try Again: it starts Wix's connection steps again, which can point the domain back at the old
Wix site.

To finish, in Shams's Squarespace account (Domains, shamsmarket.com):

1. Squarespace asks for Shams's Google sign-in again before it allows a DNS change. Only Shams can do that.
   Ask him to open DNS, DNS Settings, click ADD RECORD, then CONTINUE, and pick his Google account.
2. Under DNS Settings, Custom records, add the six records above (host `@` for the `A` records) and four
   `AAAA` records for `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`,
   `2606:50c0:8003::153`.
3. Under DNS, Domain Nameservers, choose USE SQUARESPACE NAMESERVERS. While signed in, also fix the forwarding of
   `shamsmarket.net` (see "Hosting and domain").
4. Run the checks below. Some networks keep using the old nameservers for up to 48 hours, which is why the
   records stay in Wix as well.
5. Two days after step 3, tell Shams that the Wix plan can be cancelled and the domain removed from Wix.
   Cancelling is his decision.
6. Rewrite this section to say that the DNS records are managed at Squarespace, and delete these steps.

## Checking the live site

```
curl -sI https://www.shamsmarket.com/ | head -5        # expect HTTP/2 200
curl -sI https://shamsmarket.com/ | head -5            # expect a 301 to https://www.shamsmarket.com/
dig +short www.shamsmarket.com                         # expect shams-amin.github.io and four 185.199.x.153 addresses
dig +short NS shamsmarket.com                          # the nameservers in use (Wix's until the move is finished)
```
