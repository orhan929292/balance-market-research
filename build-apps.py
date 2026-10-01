#!/usr/bin/env python3
"""Builds the Apps pages of this site from the Shopify tool snippets.

  apps.html                      list of the five tools
  app-<slug>.html                one page per tool, running the exact snippet

Source snippets live in ../apps/tools/ (the files pasted into Shopify).
Header, menu and brand finder are taken from seo-report.html so every page matches.
Run after editing a tool or the site header:  python3 build-apps.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE.parent / "apps" / "tools"

APPS = [
    ("subscription-planner", "01-subscription-planner.html", "Subscription Planner",
     "Works out how many sachets you need, the best delivery schedule and your yearly saving with Subscribe & Save."),
    ("daily-water-target", "02-daily-water-target.html", "Daily Water Target",
     "Estimates how much fluid to drink today, in litres and Balance Bottles."),
    ("sweat-loss-calculator", "03-sweat-loss-calculator.html", "Sweat Loss Calculator",
     "Shows how much fluid you lose through sweat during training."),
    ("cost-per-serving", "04-cost-per-serving.html", "Cost Per Serving",
     "Shows what Selene costs per serving and how it compares to other drinks."),
    ("caffeine-calculator", "05-daily-caffeine-calculator.html", "Caffeine Calculator",
     "Adds up your daily caffeine and compares it to the recommended limit."),
]

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>')

report = (HERE / "seo-report.html").read_text(encoding="utf-8")
head_links = re.search(r'<link rel="icon".*?<link rel="stylesheet" href="site.css">', report, re.S).group(0)
header = report[report.index('<div class="top">'):report.index("<main>")]
header = header.replace(' aria-current="page"', "")
header = header.replace('<a class="apb" href="apps.html">', '<a class="apb" href="apps.html" aria-current="page">')
script = report[report.rindex("<script>"):report.rindex("</script>") + len("</script>")]
footer = '''<footer class="foot"><div class="wrap">
  <p class="credit" style="margin-top:0">Prepared by O. Gazi Kavak</p>
</div></footer>'''


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def page(title, description, main):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · balance.</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="O. Gazi Kavak">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#000000">
{head_links}
</head>
<body class="ap">
{header}<main>
{main}
</main>
{footer}
{script}
</body>
</html>
'''


# ---- list page ----
cards = "".join(f'''
    <li><a class="appcard" href="app-{slug}.html">
      <span class="n">{i:02d}</span>
      <h2>{esc(name)}</h2>
      <p>{esc(desc)}</p>
      <span class="go">Open {ARROW}</span>
    </a></li>''' for i, (slug, _, name, desc) in enumerate(APPS, 1))
list_main = f'''<header class="hero"><div class="wrap">
  <div class="eyebrow">Apps</div>
  <h1 style="margin-top:18px">Store calculators</h1>
  <p class="lead" style="margin-top:24px">Five calculators built for beinbalance.uk. Open one to try it — each runs entirely in the browser.</p>
</div></header>
<section><div class="wrap">
  <ul class="applist">{cards}
  </ul>
</div></section>'''
(HERE / "apps.html").write_text(
    page("Apps", "Five calculators built for beinbalance.uk: subscription, water, sweat loss, cost per serving and caffeine.", list_main),
    encoding="utf-8")

# ---- one page per tool ----
for i, (slug, file, name, desc) in enumerate(APPS):
    snippet = (SRC / file).read_text(encoding="utf-8")
    prev = APPS[i - 1] if i > 0 else None
    nxt = APPS[i + 1] if i < len(APPS) - 1 else None
    pager = ""
    if prev:
        pager += f'<a href="app-{prev[0]}.html"><small>← Previous</small><span>{esc(prev[2])}</span></a>'
    if nxt:
        pager += f'<a class="nx" href="app-{nxt[0]}.html"><small>Next →</small><span>{esc(nxt[2])}</span></a>'
    main = f'''<header class="hero"><div class="wrap">
  <div class="eyebrow">Apps · {i + 1:02d}</div>
  <h1 style="margin-top:18px">{esc(name)}</h1>
  <p class="lead" style="margin-top:24px">{esc(desc)}</p>
  <div class="appnav"><a class="btn" href="apps.html">{BACK}All apps</a></div>
</div></header>
<section><div class="wrap">
  <div class="apptool">
{snippet}
  </div>
  <nav class="apppager" aria-label="Other apps">{pager}</nav>
</div></section>'''
    (HERE / f"app-{slug}.html").write_text(page(name, desc, main), encoding="utf-8")

print("Wrote apps.html and", len(APPS), "app pages")
