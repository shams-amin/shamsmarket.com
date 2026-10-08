# Search (SEO) for shamsmarket.com

Read this before changing the page title, the headline, the address or phone, the facts for search engines,
or before adding a page. It follows the order of Nicholas Dulait's 2026 guide to SEO with Claude: pick the
searches that bring customers, make the page deserve to rank, get named by others, then repeat slowly.

Shams Market is a local business, so most of its search visibility comes from its Google Business Profile
(the listing with the map, hours and reviews), not from this website. The website's job is to agree with
that listing exactly and to say plainly what the store sells.

## The searches the store wants to be found for

| Search | Where the page answers it | Monthly searches |
| --- | --- | --- |
| afghan grocery store sacramento, afghan market sacramento | title, "Inside the market" | not measured |
| halal meat sacramento, halal butcher sacramento | title, "Halal butcher" card | not measured |
| afghan bakery sacramento, afghan naan | headline, "Bakery" card | not measured |
| afghan restaurant sacramento, kabob sacramento | "From our kitchen" | not measured |
| halal market that accepts EBT | the four facts under the photo, "Groceries" card | not measured |
| shams market menu | "From our kitchen" (four dishes; the full menu is not on the site yet) | not measured |
| shams market hours, address, phone | "Find us on Auburn Blvd" | not measured |

"Not measured" means nobody has pulled the number from Google Search Console or a keyword tool. Never put a
guessed number in this table. A blank is better than a plausible number.

## Rules

1. **Match the Google listing character for character.** The address is `3510 Auburn Blvd #2, Sacramento, CA 95821`
   and the phone is `(916) 514-1471`, exactly as on the Google Business Profile. If Shams changes either one on
   Google, change it here the same day, everywhere (`tools/check.py` checks the address in four places).
2. **Title:** what people search for first, then the city, then the name. 60 characters at most.
   **Description:** 155 characters at most. Its job is to earn the click, so it says what you get, that EBT is
   accepted, and the hours. `og:title` and `og:description` repeat them.
3. **One `<h1>`,** and it names Sacramento.
4. **The facts for search engines** (the `application/ld+json` block) describe only what the page shows. No
   star ratings there: Google does not show review stars for a business's markup of reviews about itself.
5. **Never invent a fact.** No made-up prices, awards, years in business, search volumes or rankings. If
   something is not known, ask Shams or leave it out.
6. **Nothing hidden.** No text that visitors cannot see, no lists of keywords, no sentences written for AI
   systems to read.
7. **A new page needs two things from Shams first:** the facts (for a menu page, the dishes and prices) and
   something a visitor cannot get from the other results, such as his own photos. One search, one page. Never
   copy a page and swap a town or a word. At most one new page a week.
8. **When a page is added:** link to it from a sentence on the home page, add it to `docs/sitemap.xml`, and ask
   Google to index it in Search Console (URL inspection, then Request indexing).
9. **Before publishing a rewrite, list what the old version had that the new one does not:** sections, links,
   buttons, the map, the facts block. Nothing is dropped silently.
10. **After a search change, wait.** Do not judge it or undo it for 60 days. A dip in the first weeks is normal.
11. **Do not** delete a page or one of the old-address folders, change `robots.txt` or the canonical link, buy
    links, trade links in bulk, or email other websites. No `llms.txt` or other special file is needed:
    Google says a site needs nothing extra to appear in its AI answers.

## Who may do what

- **Claude may, without asking:** read Search Console and search results, fix anything `tools/check.py`
  reports, keep the address, phone and hours in step with the Google listing, and add an entry to the log below.
- **Ask Shams first:** changing words visitors read, changing the title or headline, adding a page.
  (A change Shams asks for himself is published without asking again.)
- **Never:** delete pages, edit `robots.txt` or the canonical link, send email outside, buy anything, post or
  answer reviews, or touch any repository other than this one.

## Google tools

- **Search Console:** the site is verified as `https://www.shamsmarket.com/` in Shams's Google account, through the
  file `docs/google4219baa0cb6fee68.html`. Do not delete or rename that file. The sitemap was submitted on
  2026-10-08.
- **Checks:** Google's Rich Results Test should show one valid "Local businesses" item for the home page.

## The monthly review

Once a month, not more often:

1. In Search Console, compare the last 28 days with the 28 before: which searches bring visits, which searches
   show the page without a click, and whether Google reports any page problem.
2. Look up the searches in the table above in a private window and note who is in the map results and
   whether Shams Market is. One look proves little; the direction over months is what counts.
3. Check that the Google listing, Yelp and Zabihah show the same name, address, phone and hours as the site.
4. Give Shams at most five actions, ordered by what brings customers, and add a dated line to the log.

## Log

- 2026-10-08: New site launched on GitHub Pages, replacing the Wix site.
- 2026-10-08: Search pass. Title and description rewritten around "Afghan grocery" and "halal butcher" in
  Sacramento. Headline now names Sacramento. Address changed to `3510 Auburn Blvd #2` to match the Google listing.
  Added the Google map of the store and a "Review us on Google" link. Facts for search engines: added the map
  position, the bakery, EBT, and the Yelp and Zabihah listings. Verified in Search Console, submitted the
  sitemap, requested indexing. Leave these alone until 2026-12-08.
