# balance. — Market Research

Brand Radar: 19 UK electrolyte & calm brands: product and price, packaging, website and tech stack, typography, technical SEO, Instagram and Meta ads.

Prepared by O. Gazi Kavak · October 2026.

## Structure

```
index.html                 # Brand Radar (single-page, hash-routed: #/brands, #/seo, …)
seo-report.html            # SEO & competitive report for beinbalance.uk ("What is next" button)
site.css                   # shared styles for both pages (Poppins, black/white, 7px buttons)
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
