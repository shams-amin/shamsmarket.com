# shamsmarket.com

The website of Shams Market, an Afghan bakery, halal butcher, grocery and kitchen at 3510 Auburn Blvd #2,
Sacramento, CA. Live at https://www.shamsmarket.com.

## Changing the site

Ask Claude. In any Claude chat that can work with GitHub, say what you want, for example:

> On shamsmarket.com, change the hours to 8 AM to 10 PM.

> Add a notice to shamsmarket.com that we are closed this Thursday.

> Add mantu to the kitchen menu on shamsmarket.com.

Claude edits the files here, checks them, and publishes. The change is live about a minute later. The
instructions Claude follows are in [`CLAUDE.md`](CLAUDE.md).

You can also edit by hand: change a file under `docs/`, commit to `main`, and it is published.

## How it works

- The whole site is the `docs/` folder. It is plain HTML, CSS and JavaScript with no build step.
- GitHub Pages serves that folder for free at `www.shamsmarket.com`.
- The domain is registered with Squarespace Domains, and its DNS records point to GitHub Pages.
- `python3 tools/check.py` checks the files before a change is published.
- `SEO.md` has the rules for how the site shows up in search, and a log of what was changed for search.

## Photos

The photos are stock photos from Unsplash, used under the Unsplash License, which allows business use.
None of them shows the store itself.

| File | Shows | Photographer | Source |
| --- | --- | --- | --- |
| `hero` | Afghan naan with nigella and sesame seeds | Syed F Hashemi | https://unsplash.com/photos/brown-bread-on-black-surface-ht8LS00RUWA |
| `bakery` | Long sheets of Afghan naan | Syed F Hashemi | https://unsplash.com/photos/brown-and-white-abstract-painting-ZsHn_qLRNMo |
| `butcher` | Beef cuts on a butcher's block | Kyle Mackie | https://unsplash.com/photos/sliced-meat-beside-silver-knife-Xedxbjx7MFg |
| `produce` | Bell peppers, eggplants, tomatoes, dill | Nadine Primeau | https://unsplash.com/photos/bunch-of-vegetables-wpoKpJqOsKE |
| `groceries` | Whole and ground spices | Anju Ravindranath | https://unsplash.com/photos/a-table-topped-with-different-types-of-spices-Nihdo084Yos |
| `clothing` | Scarves in many colors | Andreas Fickl | https://unsplash.com/photos/assorted-color-cloth-lot-4elcA2EcuFo |
| `kitchen` | Kabob skewers over charcoal | litoon dev | https://unsplash.com/photos/meat-skewers-cooking-over-glowing-hot-coals-zk2lkQZEkGc |

The logo was redrawn as a vector from the store's window decal and storefront sign.
