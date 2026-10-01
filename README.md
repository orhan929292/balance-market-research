# balance. — Market Research

Brand Radar: 19 UK electrolyte & calm brands: product and price, packaging, website and tech stack, typography, technical SEO, Instagram and Meta ads.

Prepared by O. Gazi Kavak.

## Structure

```
index.html                 # Brand Radar (single-page, hash-routed: #/brands, #/seo, …)
seo-report.html            # SEO & competitive report for beinbalance.uk ("What is next" button)
site.css                   # shared styles for all pages (Poppins, black/white, 7px buttons)
apps.html                  # "Apps" button: list of the five store calculators
app-*.html                 # one page per calculator (generated)
build-apps.py              # regenerates apps.html + app-*.html from ../apps/tools/
competitor-atlas-assets/   # Instagram and Meta Ad Library screenshots
vercel.json                # static hosting config (noindex, asset caching)
```

No build step, no dependencies.

## Run locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy to Vercel via GitHub

1. Push this folder to a new GitHub repository.
2. In Vercel: **Add New → Project → Import** the repository.
3. Framework preset: **Other**. Leave Build Command and Output Directory empty (root is served as-is).
4. Deploy. Every push to `main` redeploys automatically.

The site sends `noindex` (meta tag and `X-Robots-Tag` header) so it stays out of search results. Remove both if it should be public.

## Updating the apps

The calculator code lives in `../apps/tools/` (the snippets pasted into Shopify). After editing one, run:

```bash
python3 build-apps.py
```

and commit the regenerated `apps.html` / `app-*.html`. The script also copies the header from `seo-report.html`.
