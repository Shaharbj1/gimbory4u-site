# -*- coding: utf-8 -*-
import os, shutil
from gen_lib import render, SITE, UPDATED, INDEXNOW_KEY
from pages_topics import TOPICS
from pages_cities import CITY_PAGES, AREAS, ACCESS
from pages_index import INDEX_PAGES, INDEX, ARTICLE_PAGES

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
PAGES = TOPICS + [AREAS] + CITY_PAGES + INDEX_PAGES + [ACCESS]
BY_SLUG = {p["slug"]: p for p in PAGES}

# sanity: every related link must exist
for p in PAGES:
    for r in p.get("related", []):
        assert r in BY_SLUG, (p["slug"], r)

CITIES_FOOTER = [(p["slug"], p["crumb"].replace("השכרת ג'ימבורי ", "")) for p in CITY_PAGES]
GUIDES_FOOTER = [
    ("pages/gimboree-set-rental.html", "סט ג'ימבורי להשכרה"),
    ("pages/gimboree-rental-cheap.html", "השכרת ג'ימבורי בזול"),
    ("pages/gimboree-birthday-home.html", "ג'ימבורי ליום הולדת בבית"),
    ("pages/birthday-one-year.html", "יום הולדת שנה"),
    ("pages/birthday-two-years.html", "יום הולדת שנתיים"),
    ("pages/birthday-three-years.html", "יום הולדת 3"),
    ("pages/ball-pit-rental.html", "השכרת בריכת כדורים"),
    ("pages/gimboree-for-babies.html", "ג'ימבורי לתינוקות"),
    ("pages/gimboree-kindergarten.html", "ג'ימבורי לגן ולמעון"),
    ("pages/gimboree-vs-inflatable.html", "ג'ימבורי או מתנפח"),
    ("pages/toddler-birthday-checklist.html", "צ'קליסט יום הולדת"),
    ("pages/playgrounds-index.html", "אינדקס משחקיות לילדים"),
]

# footer city links: "השכרת ג'ימבורי <city>" – strip preposition form
from pages_cities import CITIES
CITIES_FOOTER = [(f"pages/gimboree-rental-{c[0]}.html", c[2]) for c in CITIES]

os.makedirs(f"{OUT}/pages", exist_ok=True)
for p in PAGES:
    html = render(p, BY_SLUG, CITIES_FOOTER, GUIDES_FOOTER)
    with open(f"{OUT}/{p['slug']}", "w", encoding="utf-8") as f:
        f.write(html)

# ── sitemap ──
prio = {"index.html": "1.0"}
urls = []
for p in PAGES:
    loc = f"{SITE}/" if p["slug"] == "index.html" else f"{SITE}/{p['slug']}"
    img = f"{SITE}/images/{p['img']}.webp"
    urls.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{p.get("updated", UPDATED)}</lastmod>
    <image:image><image:loc>{img}</image:loc></image:image>
  </url>""")
open(f"{OUT}/sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n")

# ── llms.txt ──
lines = ["# Gimbory4U – השכרת ג'ימבורי לפעוטות", "",
         "> השכרת סטים של ג'ימבורי רך לפעוטות (8 חודשים עד 4 שנים) לימי הולדת ואירועים בבית. "
         "איסוף עצמי בלבד מקריית עקרון (הזית 14), ליד רחובות. חבילות: 300₪ (7 מתקנים), 450₪ (עם 8 מזרני הגנה), "
         "550₪ (עם מזרנים ובריכת כדורים). מחיר זהה לכל הערים. טלפון/וואטסאפ: 054-9422295.", "",
         "> English: Gimbory4U is a small equipment rental business in Israel. Parents rent soft-play gym sets, "
         "safety mats and ball pits for toddler birthday parties at home, with self-pickup from Kiryat Ekron. "
         "Category: equipment / party rental (not games).", "",
         "## עמודים עיקריים"]
for p in TOPICS + [AREAS, INDEX]:
    loc = f"{SITE}/" if p["slug"] == "index.html" else f"{SITE}/{p['slug']}"
    lines.append(f"- [{p['h1']}]({loc}): {p['desc']}")
lines += ["", "## מאמרים להורים לפעוטות"]
for p in ARTICLE_PAGES:
    lines.append(f"- [{p['h1']}]({SITE}/{p['slug']}): {p['desc']}")
lines += ["", "## ערים (עד 30 ק\"מ מקריית עקרון)"]
for p in CITY_PAGES:
    lines.append(f"- [{p['h1']}]({SITE}/{p['slug']})")
open(f"{OUT}/llms.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")

print(len(PAGES), "pages built")

# ── static assets (css/js) ──
HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ("css", "js"):
    shutil.copytree(os.path.join(HERE, "static", sub), os.path.join(OUT, sub), dirs_exist_ok=True)

# ── robots.txt ──
AI_BOTS = ["Googlebot", "Bingbot", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User",
           "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Applebot-Extended"]
open(f"{OUT}/robots.txt", "w", encoding="utf-8").write(
    "".join(f"User-agent: {b}\n" for b in AI_BOTS) + "Allow: /\n\n"
    "User-agent: *\nAllow: /\n\n"
    "Sitemap: https://gimbory4u.co.il/sitemap.xml\n")
# Google Search Console verification file (account gimbory4u@gmail.com) - keep it, or verification is lost
open(f"{OUT}/googleb9345453808673e2.html", "w", encoding="utf-8").write(
    "google-site-verification: googleb9345453808673e2.html")
# IndexNow key file (Bing, Yandex and other IndexNow engines)
open(f"{OUT}/{INDEXNOW_KEY}.txt", "w", encoding="utf-8").write(INDEXNOW_KEY)

# ── _redirects (Cloudflare Workers static assets) ──
from urllib.parse import quote
OLD = [
    ("/השכרת-גימבורי-רחובות-2", "/pages/gimboree-rental-rehovot.html"),
    ("/השכרת-גימבורי-רחובות", "/pages/gimboree-rental-rehovot.html"),
    ("/השכרת-גימבורי-ראשון-לציון", "/pages/gimboree-rental-rishon.html"),
    ("/השכרת-גימבורי-חולון", "/pages/gimboree-rental-holon.html"),
    ("/השכרת-גימבורי-לאירועים/השכרת_גימבורי_אשדוד", "/pages/gimboree-rental-ashdod.html"),
    ("/השכרת-גימבורי-לאירועים/גימבורי_להשכרה", "/"),
    ("/השכרת-גימבורי-לאירועים", "/"),
    ("/השכרת-בריכת-כדורים", "/pages/ball-pit-rental.html"),
    ("/יום_הולדת_שנה", "/pages/birthday-one-year.html"),
    ("/השכרת_מתנפחים_קרית_עקרון", "/pages/gimboree-rental-kiryat-ekron.html"),
    ("/השכרת_מתנפחים_קטנים", "/pages/gimboree-vs-inflatable.html"),
    ("/השכרת_מגלשת_מים", "/"),
    ("/השכרת_מתנפח_מים", "/"),
    ("/אטרקציות_לבת_מצווה", "/"),
]
MERGED = [
    ("/pages/gimboree-rental.html", "/"),
    ("/pages/gimboree-for-rent.html", "/"),
    ("/pages/gimboree-equipment-rental.html", "/pages/gimboree-set-rental.html"),
    ("/pages/gimboree-rental-toddlers.html", "/"),
    ("/pages/gimboree-rental-nes-ziona-2.html", "/pages/gimboree-rental-nes-ziona.html"),
    ("/admin", "/"), ("/admin/", "/"),
]
lines = ["# Gimbory4U – 301 redirects (generated by tools/build.py)", "", "# merged / removed pages"]
lines += [f"{s} {d} 301" for s, d in MERGED]
lines += ["", "# URLs from the old site that are still indexed by Google"]
seen = set()
for src, dst in OLD:
    for variant in (src, src + "/"):
        for form in (quote(variant, safe="/_-"),):
            if form not in seen:
                seen.add(form)
                lines.append(f"{form} {dst} 301")
lines += ["", "# anything else under the old events folder", f"{quote('/השכרת-גימבורי-לאירועים/', safe='/_-')}* / 301"]
open(f"{OUT}/_redirects", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# ── _headers ──
open(f"{OUT}/_headers", "w", encoding="utf-8").write("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN

/css/*
  Cache-Control: public, max-age=2592000

/js/*
  Cache-Control: public, max-age=2592000

/images/*
  Cache-Control: public, max-age=15552000
""")

# ── 404 page (absolute paths, served at any depth) ──
NF = dict(ACCESS)
NF.update({
    "slug": "404.html", "nav": "", "crumb": "העמוד לא נמצא",
    "title": "העמוד לא נמצא | Gimbory4U", "desc": "העמוד שחיפשתם לא נמצא.",
    "eyebrow": "שגיאה 404", "h1": "העמוד שחיפשתם לא נמצא",
    "lead": "ייתכן שהכתובת השתנתה. אפשר לחזור לדף הבית או לבחור עיר מהרשימה למטה.",
    "robots": "noindex, follow", "faq": [], "related": [],
    "body": lambda root: "", "show_packages": True, "show_steps": False, "show_reviews": False, "show_cta": True,
})
html = render(NF, BY_SLUG, CITIES_FOOTER, GUIDES_FOOTER)
for a in ('href="', 'src="'):
    for p in ("css/", "js/", "images/", "pages/"):
        html = html.replace(f'{a}{p}', f'{a}/{p}')
html = html.replace('href="./"', 'href="/"').replace('data-root=""', 'data-root="/"')
open(f"{OUT}/404.html", "w", encoding="utf-8").write(html)
print("extras written")
