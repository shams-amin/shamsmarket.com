# Search (SEO) for shamsmarket.com

Read this before changing the page title, the headline, the address or phone, the facts for search engines,
or before adding a page. It follows the order of Nicholas Dulait's 2026 guide to SEO with Claude (pick the
searches that bring customers, make the page deserve to rank, get named by others, then repeat slowly),
corrected where Google's own rules or better evidence say otherwise. The sources are listed at the end.

Shams Market is a local business, so most of its search visibility comes from its Google Business Profile
(the listing with the map, hours and reviews), not from this website. Google ranks local results on
"relevance, distance, and popularity" (Google, n.d.-c). The website's job is to agree with that listing exactly,
to say plainly what the store sells, in the words customers use, and to load fast.

## What moves search for this store

Ranked by the strength of the evidence, as of October 2026.

1. **The Google Business Profile.** The categories chosen affect local ranking (Google, n.d.-b), and the
   primary category is the factor local search specialists rank highest (Shaw, 2025). Being open at the time
   of the search lifts a listing (Hawkins, 2023). The number of reviews and their ratings count (Google, n.d.-c),
   and a steady flow of new ones appears to count more than the total (Hawkins, 2025). Services chosen from
   Google's own list help for matching searches (Hawkins, 2026).
2. **The rating customers see.** 68% of consumers will only use a business rated four stars or more
   (Murphy, 2026). The store is at 3.8 from 1,136 reviews (2026-10-08). Only real reviews, asked for the
   right way (rule 12), move this.
3. **The same name, address, phone and hours everywhere:** the Google listing, this site, Yelp, Zabihah,
   Apple Maps, Bing Places. Google may change a listing when other sources disagree with it (Google, n.d.-a).
4. **A page that fully answers the search, in the customers' words.** Google's own engineers described
   anchors (links), body text and user clicks as the basic relevance signals, and Google keeps 13 months of
   click data by query and place (United States v. Google LLC, 2024). Searchers who come back to the
   results unsatisfied count against a page.
5. **Being named by others:** local press, community pages, food guides, directories people use. None of the
   independent Sacramento food pages found on 2026-10-08 names Shams Market.
6. **Speed on phones.** Google's "good" marks: largest image or text shown within 2.5 s, response to a tap
   within 200 ms, layout shift under 0.1 (Google, 2025b). They count, but relevance comes first.

AI answers draw on the same places. Google's AI Overviews and AI Mode need nothing extra on the page: no
special files, no special markup, no rewriting for AI (Google, 2026a). Gemini uses Google Search and Maps;
Microsoft Copilot uses Bing and Bing Places; ChatGPT uses several search providers and, since July 2026,
Yelp's listings and reviews (Mills, 2026); Perplexity has its own index and has used Yelp and Tripadvisor.
With an AI summary on the results page, people clicked a result in 8% of visits, against 15% without one
(Chapekis & Lieb, 2025), so being named inside the answer matters more each year.

## The searches the store wants to be found for

| Search | Where the page answers it | Monthly searches |
| --- | --- | --- |
| afghan grocery store sacramento, afghan market sacramento | title, "Inside the market" | not measured |
| halal meat sacramento, halal butcher sacramento | title, "Halal butcher" card | not measured |
| afghan bakery sacramento, afghan naan | headline, "Bakery" card | not measured |
| afghan restaurant sacramento, kabob sacramento | "From our kitchen" (the Google listing has no restaurant category yet) | not measured |
| halal market that accepts EBT | the four facts under the photo, "Groceries" card | not measured |
| shams market menu, shams kabob menu | "From our kitchen" (four dishes; Google suggested both searches on 2026-10-08, so a full menu would be used) | not measured |
| shams market hours, address, phone | "Find us on Auburn Blvd" | not measured |

"Not measured" means nobody has pulled the number from Google Search Console or a keyword tool. Never put a
guessed number in this table. A blank is better than a plausible number.

## Rules

1. **Match the Google listing character for character.** The address is `3510 Auburn Blvd #2, Sacramento, CA 95821`
   and the phone is `(916) 514-1471`, exactly as on the Google Business Profile. If Shams changes either one on
   Google, change it here the same day, everywhere (`tools/check.py` checks every copy).
2. **Title:** what people search for first, then the city, then the name. Google sets no length limit, but it cuts
   long titles off on phones, so keep it to 60 characters. **Description:** 155 characters at most. Its job is to
   earn the click: what you get, that EBT is accepted, the hours. `og:title` and `og:description` repeat them.
3. **One `<h1>`,** and it names Sacramento.
4. **The facts for search engines** are two `application/ld+json` blocks: the store (with its hours, address,
   map position and listings) and the website (which sets the site name Google shows). They describe only what
   the page shows. No star ratings: Google shows no stars for a business's markup of reviews about itself
   (Google, 2026b). No FAQ markup: Google stopped showing FAQ results on 2026-05-07.
5. **Never invent a fact.** No made-up prices, awards, years in business, search volumes or rankings. If
   something is not known, ask Shams or leave it out.
6. **Nothing hidden from visitors.** No keyword lists, no text in the page's colors, no sentences written for
   AI systems and no instructions to them; Google's spam policy now covers attempts to manipulate AI answers
   (Google, 2026c). Text read aloud only by screen readers to help blind visitors is allowed (Google, 2026c),
   which covers the store's name in the headline and the full weekday names in the hours.
7. **A new page needs two things from Shams first:** the facts (for a menu page, the dishes and prices) and
   something a visitor cannot get from the other results, such as his own photos. One search, one page. Never
   copy a page and swap a town or a word: Google calls that doorway abuse (Google, 2026c). At most one new page
   a week.
8. **When a page is added:** link to it from a sentence on the home page, add it to `docs/sitemap.xml`, ask
   Google to index it in Search Console (URL inspection, then Request indexing), and run `python3 tools/indexnow.py`
   with its path for Bing.
9. **Before publishing a rewrite, list what the old version had that the new one does not:** sections, links,
   buttons, the map, the facts blocks. Nothing is dropped silently.
10. **After a search change, wait.** Do not judge it or undo it for 60 days. A dip in the first weeks is normal.
11. **Do not** delete a page or one of the old-address folders, change `robots.txt` or the canonical link, buy
    links, trade links in bulk, or email other websites. No `llms.txt` or other special file is needed: Google
    says a site needs nothing extra to appear in its AI answers (Google, 2026a), and no AI company has said it
    reads that file.
12. **Reviews.** Ask every customer the same way: the "Review us on Google" link on the page, or the QR code
    Google makes in the Business Profile. Google forbids offering anything for a review, asking only happy
    customers, pressuring people to write one while they are in the store, and asking them to include specific
    words or items (Google, n.d.-d). The US rule on fake reviews also bans paying for reviews that must say
    something good (or bad) and suppressing bad ones (Federal Trade Commission, 2024). Reply to reviews
    personally, within a week.
13. **Speed.** The top photo loads first: its `preload` line has `fetchpriority="high"` and the same list of sizes
    as the photo (`tools/check.py` compares them). Every photo has a width and a height. Nothing from another
    server holds up the first screen: the typefaces are stored in `docs/assets/fonts`. After a layout change,
    run PageSpeed Insights on the phone setting and keep the largest paint under 2.5 s.

## Who may do what

- **Claude may, without asking:** read Search Console, Bing and search results, fix anything `tools/check.py`
  reports, keep the address, phone and hours in step with the Google listing, make the page faster without
  changing what it shows, run `tools/indexnow.py`, and add an entry to the log below.
- **Ask Shams first:** changing words visitors read, changing the title or headline, adding a page, and every
  change to the Google Business Profile or any other listing. (A change Shams asks for himself is made without
  asking again.)
- **Never:** delete pages, edit `robots.txt` or the canonical link, send email outside, buy anything, post or
  answer reviews in his name, or touch any repository other than this one.

## Google, Bing and the AI tools

- **Google Search Console:** verified as `https://www.shamsmarket.com/` in Shams's Google account through the
  file `docs/google4219baa0cb6fee68.html` (do not delete or rename it). Sitemap submitted 2026-10-08. The
  Generative AI performance report (open to every site since 2026-08-31) shows how often the site appears in
  AI Overviews and AI Mode. Settings, "Search generative AI control" must stay on "Include".
- **Bing:** the IndexNow key is `docs/e6b48a8d8394d39b672ce4170b761de1.txt`; `tools/indexnow.py` uses it. Bing
  Webmaster Tools is not set up yet: Shams signs in at bing.com/webmasters and imports the site from Google
  Search Console. Its AI Performance report counts citations in Copilot (Microsoft, 2026).
- **Checks:** Google's Rich Results Test should show one valid "Local businesses" item. PageSpeed Insights on
  2026-10-08, before the speed work: phone 90 (largest paint 2.7 s), desktop 99.
- **AI crawlers:** `robots.txt` allows every crawler, including OAI-SearchBot (ChatGPT search), PerplexityBot,
  Claude-SearchBot and Bingbot. Keep it that way; blocking them keeps the store out of their answers.

## Listings that must match the site

| Where | State on 2026-10-08 | Who fixes it |
| --- | --- | --- |
| Google Business Profile ("Shams Market and Restaurant") | Matches. Categories: Grocery store (primary), Bakery, Butcher shop, Produce market; no restaurant category. Services and menu empty. Description about 330 of 750 characters. | Shams, or Claude with his yes |
| Yelp (yelp.com/biz/shams-market-sacramento) | Shows 9 AM to 8 PM; the site says 9 PM | Shams (Yelp for Business) |
| Zabihah | 8:30 AM to 9 PM, a Tuesday error, no `#2`, no phone, no website | Shams |
| MapQuest | Shows 9 AM to 8 PM | Updates from data providers |
| Apple Maps (Apple Business Connect) | Not checked; feeds Maps and Siri | Shams |
| Bing Places | Not checked; feeds Bing and Copilot | Shams |

## The monthly review

Once a month, not more often:

1. **Search Console:** compare the last 28 days with the 28 before: which searches bring visits, which show the
   page without a click, any page problem, and the Generative AI report.
2. **Google Business Profile, Performance:** the searches that found the listing, calls, direction requests,
   website clicks, and the reviews that came in (count, average, replies within a week).
3. **The searches in the table above,** in a private window: who is in the map results, whether Shams Market is,
   and what the AI Overview names. Then ask ChatGPT, Gemini, Perplexity and Copilot, logged out, "best Afghan
   grocery store in Sacramento", "where to buy halal meat in Sacramento" and "best Afghan restaurant in
   Sacramento", and note whether the store is named and which sources are cited. Answers change from month to
   month; the direction over several months is what counts.
4. **The listings table:** do Google, Yelp, Zabihah, Apple and Bing show the same name, address, phone and hours?
5. Give Shams at most five actions, ordered by what brings customers, and add a dated line to the log.

## Log

- 2026-10-08: New site launched on GitHub Pages, replacing the Wix site.
- 2026-10-08: Search pass. Title and description rewritten around "Afghan grocery" and "halal butcher" in
  Sacramento. Headline now names Sacramento. Address changed to `3510 Auburn Blvd #2` to match the Google listing.
  Added the Google map of the store and a "Review us on Google" link. Facts for search engines: added the map
  position, the bakery, EBT, and the Yelp and Zabihah listings. Verified in Search Console, submitted the
  sitemap, requested indexing. Leave these alone until 2026-12-08.
- 2026-10-08: Second pass, from deeper research. Speed: the top photo loads first and phones get a 1,400 px
  version instead of 2,000 px; wide screens get smaller card photos; the typefaces are stored on the site instead
  of Google Fonts. Added a 192 px icon, the WebSite facts block (site name), the IndexNow key and
  `tools/indexnow.py`, and "Also known as kabuli pulao" under qabuli palaw. `tools/check.py` now checks every
  phone number and written time, the map title, the top photo and the search files. Rules 4, 6, 8, 11, 12 and 13
  and the monthly review updated. Leave the title, headline and description alone until 2026-12-08.

## Sources

Chapekis, A., & Lieb, A. (2025, July 22). *Google users are less likely to click on links when an AI summary
appears in the results*. Pew Research Center. https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/

Dulait, N. (2026, October 8). *How to use Claude Opus 5.5 for SEO so well it feels illegal* [Article]. X.
https://x.com/NicholasDulait/status/2108212094214529135

Federal Trade Commission. (2024). Trade regulation rule on the use of consumer reviews and testimonials, 16 C.F.R.
pt. 465. *Federal Register, 89*(163), 68034–68079. https://www.govinfo.gov/content/pkg/FR-2024-08-22/pdf/2024-18519.pdf

Google. (n.d.-a). *Understand Google updates on your Business Profile*. Google Business Profile Help.
Retrieved October 8, 2026, from https://support.google.com/business/answer/3480441

Google. (n.d.-b). *Manage your business category*. Google Business Profile Help. Retrieved October 8, 2026, from
https://support.google.com/business/answer/7249669

Google. (n.d.-c). *Tips to improve your local ranking on Google*. Google Business Profile Help. Retrieved
October 8, 2026, from https://support.google.com/business/answer/7091

Google. (n.d.-d). *Prohibited & restricted content*. Maps User Generated Content Policy Help. Retrieved
October 8, 2026, from https://support.google.com/contributionpolicy/answer/7400114

Google. (2025a). *AI features and your website*. Google Search Central. https://developers.google.com/search/docs/appearance/ai-features

Google. (2025b). *Understanding Core Web Vitals and Google search results*. Google Search Central.
https://developers.google.com/search/docs/appearance/core-web-vitals

Google. (2026a). *Optimizing your website for generative AI features on Google Search*. Google Search Central.
https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

Google. (2026b). *Review snippet (Review, AggregateRating) structured data*. Google Search Central.
https://developers.google.com/search/docs/appearance/structured-data/review-snippet

Google. (2026c). *Spam policies for Google web search*. Google Search Central.
https://developers.google.com/search/docs/essentials/spam-policies

Hawkins, J. (2023, December 7). *Google just added business hours as a new local pack ranking factor*. Sterling Sky.
https://www.sterlingsky.ca/google-added-a-new-ranking-factor/

Hawkins, J. (2025, July 28). *Review recency: Does it impact ranking?* [Case study]. Sterling Sky.
https://www.sterlingsky.ca/google-review-recency-ranking/

Hawkins, J. (2026, September 22). *GBP services: Do services in Google Business Profiles impact ranking?* Sterling Sky.
https://www.sterlingsky.ca/services-in-google-business-profile-impact-ranking/

Microsoft. (2026, February 10). *Introducing AI Performance in Bing Webmaster Tools public preview*. Bing Webmaster Blog.
https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview

Mills, M. (2026, July 23). Exclusive: Yelp partners with ChatGPT to surface reviews. *Axios*.
https://www.axios.com/2026/07/23/yelp-reviews-chatgpt-geo-partnership

Murphy, R. (2026, February 11). *Local consumer review survey 2026*. BrightLocal.
https://www.brightlocal.com/research/local-consumer-review-survey/

Shaw, D. (2025, November 6). *Local search ranking factors 2026*. Whitespark. https://whitespark.ca/local-search-ranking-factors/

United States v. Google LLC, No. 1:20-cv-03010-APM (D.D.C. Aug. 5, 2024) (memorandum opinion).
https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1033.0_2.pdf
