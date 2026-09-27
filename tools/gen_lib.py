# -*- coding: utf-8 -*-
"""Shared layout pieces for the Gimbory4U static site generator."""
import json, os
from urllib.parse import quote
from html import escape

SITE = "https://gimbory4u.co.il"
PHONE_DISPLAY = "054-9422295"
PHONE_TEL = "+972549422295"
WA_NUMBER = "972549422295"
ADDRESS_STREET = "הזית 14"
ADDRESS_CITY = "קריית עקרון"
PICKUP = "איסוף עצמי מקריית עקרון"
MAPS_URL = "https://maps.google.com/?cid=3609911889483594397"
FACEBOOK_URL = "https://www.facebook.com/Gimbory4u/"
RATING = "4.3"
REVIEW_COUNT = 25
UPDATED = "2026-09-25"
HOURS_TEXT = "א׳–ו׳, 09:00–20:00"

# width/height of generated images (from the image-processing step)
IMG = json.load(open(os.path.join(os.path.dirname(__file__), "img_dims.json"), encoding="utf-8"))

WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.28-.2-.57-.35zM12.05 21.8a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.89 9.88zm8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/></svg>')
PIN_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'


def wa(msg="היי, אשמח לבדוק זמינות להשכרת ג'ימבורי"):
    return f"https://wa.me/{WA_NUMBER}?text={quote(msg)}"


NAV = [
    ("", "דף הבית", "home"),
    ("pages/gimboree-rental-cheap.html", "מחירים", "price"),
    ("pages/gimboree-set-rental.html", "מה כולל הסט", "set"),
    ("pages/gimboree-birthday-home.html", "יום הולדת בבית", "birthday"),
    ("pages/ball-pit-rental.html", "בריכת כדורים", "ballpit"),
    ("pages/service-areas.html", "אזורי שירות", "areas"),
    ("pages/toddler-birthday-checklist.html", "מדריכים", "guides"),
]

PACKAGES = [
    {"name": "חבילה בסיסית", "price": 300, "badge": "",
     "items": ["7 מתקני ג'ימבורי רכים", "מגלשה, מדרגות, קשת, נדנדות וקוביית פעילות", "מתאים לעד 5 ילדים", PICKUP]},
    {"name": "חבילת בטיחות", "price": 450, "badge": "הנבחרת ביותר",
     "items": ["7 מתקני ג'ימבורי רכים", "8 מזרני הגנה עבים", "מתאים לעד 8 ילדים", PICKUP]},
    {"name": "חבילת מסיבה", "price": 550, "badge": "",
     "items": ["7 מתקני ג'ימבורי רכים", "מערכת מזרני הגנה מלאה", "בריכת כדורים גדולה", PICKUP]},
]

REVIEWS = [
    ("shahar david", "שירות מקצועי ואדיב, הדרכה מעולה ועניינית על תפעול הציוד… הילדים מאוד נהנו"),
    ("עוגות דה לה פה", "הכל מקצועי, בטיחותי, חשיבה עד לפרטים הקטנים… שווה כל רגע וכל שקל."),
    ("K Z", "זמין, הוגן מאד, הציוד מצוין"),
    ("יאיר מדר", "מקצוען אמיתי, ציוד איכותי ואחלה מחירים. מומלץ"),
]


def img_tag(name, alt, root, cls="", eager=False, zoom=True):
    w, h, _ = IMG[name]
    classes = " ".join(c for c in [cls, "zoomable" if zoom else ""] if c)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    cls_attr = ' class="' + classes + '"' if classes else ""
    return (f'<img src="{root}images/{name}.webp" alt="{escape(alt)}" width="{w}" height="{h}" '
            f'{load}{cls_attr}>')


def business_schema():
    return {
        "@type": "LocalBusiness",
        "@id": f"{SITE}/#business",
        "name": "Gimbory4U",
        "alternateName": ["גימבורי4יו", "Gimbory4U – ג'ימבורי להשכרה לפעוטות"],
        "description": "השכרת ג'ימבורי לפעוטות לימי הולדת ואירועים בבית. איסוף עצמי מקריית עקרון, החל מ-300₪.",
        "url": f"{SITE}/",
        "telephone": PHONE_TEL,
        "image": f"{SITE}/images/haskarat-gimbori-lepeotot.webp",
        "priceRange": "₪300–₪550",
        "currenciesAccepted": "ILS",
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS_STREET,
                    "addressLocality": ADDRESS_CITY, "addressCountry": "IL"},
        "geo": {"@type": "GeoCoordinates", "latitude": 31.8585, "longitude": 34.8225},
        "hasMap": MAPS_URL,
        "areaServed": {"@type": "GeoCircle",
                       "geoMidpoint": {"@type": "GeoCoordinates", "latitude": 31.8585, "longitude": 34.8225},
                       "geoRadius": 30000},
        "sameAs": [MAPS_URL, FACEBOOK_URL],
        "makesOffer": [
            {"@type": "Offer", "name": f"השכרת ג'ימבורי – {p['name']}", "price": str(p["price"]),
             "priceCurrency": "ILS", "availability": "https://schema.org/InStock"} for p in PACKAGES
        ],
    }


def page_schema(page, root_url):
    graph = [business_schema()]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "דף הבית", "item": f"{SITE}/"}]
    if page["slug"] != "index.html":
        for i, (name, href) in enumerate(page.get("crumbs", []), start=2):
            crumbs.append({"@type": "ListItem", "position": i, "name": name, "item": f"{SITE}/{href}"})
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": page["crumb"], "item": root_url})
    graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    graph.append({
        "@type": "WebPage", "@id": root_url + "#webpage", "url": root_url, "name": page["title"],
        "description": page["desc"], "inLanguage": "he-IL", "dateModified": UPDATED,
        "about": {"@id": f"{SITE}/#business"},
        "primaryImageOfPage": f"{SITE}/images/{page['img']}.webp",
    })
    if page.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in page["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)




# ============================================================
#  LAYOUT (v4) — restores the original Gimbory4U look:
#  centered hero, price spotlight, 3 package cards, icon steps,
#  white article card, blue CTA band, dark footer.
#  One keyword-named image per page (home: + small gallery).
# ============================================================
ASSET_V = "20260927a"   # bump to bust Hostinger CDN cache

PACKAGES = [
    {"name": "חבילה בסיסית", "price": 300, "featured": False, "key": "basic",
     "items": ["7 מתקני ג'ימבורי פרימיום", "מגלשה, מדרגות, קשת ונדנדות", "נקי ובמצב מעולה", "איסוף עצמי מקריית עקרון"]},
    {"name": "חבילת בטיחות", "price": 450, "featured": True, "key": "safety",
     "items": ["7 מתקני ג'ימבורי פרימיום", "8 מזרני הגנה עבים", "בטיחות מקסימלית לגיל הרך", "נקי ובמצב מעולה"]},
    {"name": "חבילת מסיבה מושלמת", "price": 550, "featured": False, "key": "party",
     "items": ["7 מתקני ג'ימבורי פרימיום", "מערכת מזרני הגנה מלאה", "בריכת כדורים מפנקת וגדולה", "מתאים למסיבות ולגיל שנה"]},
]


def header(page, root):
    home = root or "./"
    items = []
    for href, label, key in NAV:
        link = (root + href) or "./"
        cur = ' aria-current="page"' if page.get("nav") == key else ""
        items.append(f'<li><a href="{link}"{cur}>{label}</a></li>')
    return f'''<a class="skip-link" href="#main">דילוג לתוכן הראשי</a>
<header class="site-header">
  <div class="container">
    <div class="header-inner">
      <a href="{home}" class="logo" aria-label="Gimbory4U – דף הבית">
        <span class="logo-icon" aria-hidden="true">🎪</span>
        <span>
          <span class="logo-text-main">GIMBORY4U</span>
          <span class="logo-sub">ג'ימבורי להשכרה לפעוטות</span>
        </span>
      </a>
      <a class="header-rating" href="{MAPS_URL}" target="_blank" rel="noopener" aria-label="דירוג {RATING} מתוך 5 בגוגל, {REVIEW_COUNT} ביקורות">
        <span class="header-rating-stars" aria-hidden="true">★</span>
        <span class="header-rating-score">{RATING}</span>
        <span class="header-rating-count">{REVIEW_COUNT} ביקורות בגוגל</span>
      </a>
      <div class="header-actions">
        <a class="header-phone" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
        <a href="{wa(page.get('wa', "היי, אשמח לבדוק זמינות להשכרת ג'ימבורי"))}" class="btn btn-wa header-cta" target="_blank" rel="noopener" aria-label="צרו קשר בוואטסאפ">{WA_SVG}<span>צרו קשר עכשיו</span></a>
      </div>
    </div>
  </div>
  <nav class="site-nav" aria-label="ניווט ראשי">
    <div class="container"><ul class="nav-list">{"".join(items)}</ul></div>
  </nav>
</header>'''


def breadcrumb(page, root):
    if page["slug"] == "index.html":
        return ""
    home = root or "./"
    parts = [f'<li><a href="{home}">דף הבית</a></li>']
    for name, href in page.get("crumbs", []):
        parts.append(f'<li><a href="{root}{href}">{name}</a></li>')
    parts.append(f'<li aria-current="page">{page["crumb"]}</li>')
    return f'<nav class="breadcrumb" aria-label="פירורי לחם"><div class="container"><ol>{"".join(parts)}</ol></div></nav>'


def hero(page, root):
    msg = page.get("wa", "היי, אשמח לבדוק זמינות להשכרת ג'ימבורי")
    return f'''<section class="hero">
  <div class="container">
    <div class="hero-badge">{page["eyebrow"]}</div>
    <h1>{page["h1"]}</h1>
    <p class="hero-subtitle">{page["lead"]}</p>
    <div class="hero-tags">
      <span class="tag tag-green">✓ לגילאי 8 חודשים – 4 שנים</span>
      <span class="tag tag-green">✓ עובר ניקוי ובמצב מעולה</span>
      <span class="tag tag-blue">📍 {PICKUP}</span>
    </div>
    <div class="hero-cta">
      <a href="{wa(msg)}" class="btn btn-wa btn-lg" target="_blank" rel="noopener">{WA_SVG}בדיקת זמינות בוואטסאפ</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline btn-lg">חיוג {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>'''


def spotlight(page, root):
    """Featured package card + the page's single keyword image."""
    p = PACKAGES[1]
    lis = "".join(f'<li><span class="check">✓</span> {i}</li>' for i in [p["items"][0], p["items"][1], PICKUP])
    msg = page.get("wa", "היי, אשמח לבדוק זמינות לחבילת הבטיחות (450₪)")
    return f'''<section class="price-spotlight">
  <div class="container spotlight-inner">
    <div class="price-card">
      <div class="price-label">⭐ החבילה הפופולרית</div>
      <div class="price-amount">450₪</div>
      <div class="price-title">חבילת בטיחות — המומלצת</div>
      <p class="price-desc">7 מתקנים + 8 מזרני הגנה עבים — הבחירה הנפוצה ביותר</p>
      <ul class="price-features">{lis}</ul>
      <a href="{wa(msg)}" class="btn btn-wa" target="_blank" rel="noopener">בדיקת זמינות</a>
    </div>
    <figure class="spotlight-image">
      {img_tag(page["img"], page["alt"], root, eager=True)}
      <figcaption>{page["alt"]}</figcaption>
    </figure>
  </div>
</section>'''


def steps():
    return f'''<section class="section how-it-works" aria-labelledby="st-h">
  <div class="container">
    <h2 class="section-title" id="st-h">איך זה עובד?</h2>
    <p class="section-subtitle">תהליך פשוט ומהיר — מההזמנה ועד החגיגה</p>
    <div class="steps-grid">
      <div class="step-card"><div class="step-icon" aria-hidden="true">💬</div><div class="step-number">1</div>
        <h3>בוחרים וסוגרים</h3><p>שולחים הודעת וואטסאפ עם תאריך, גיל הילד ומספר הילדים. אנחנו מאשרים זמינות, בדרך כלל תוך שעה.</p></div>
      <div class="step-card"><div class="step-icon" aria-hidden="true">🚗</div><div class="step-number">2</div>
        <h3>איסוף עצמי מקריית עקרון</h3><p>מגיעים ל{ADDRESS_STREET}, {ADDRESS_CITY}. הציוד מחכה נקי וארוז, ואנחנו מסבירים איך מרכיבים. כ-10 דקות.</p></div>
      <div class="step-card"><div class="step-icon" aria-hidden="true">🎉</div><div class="step-number">3</div>
        <h3>חוגגים ונהנים</h3><p>פורסים מזרנים, מקימים את הג'ימבורי ב-5 דקות, ואחרי האירוע מחזירים. את הניקוי אנחנו עושים.</p></div>
    </div>
  </div>
</section>'''


def packages(root):
    cards = []
    for p in PACKAGES:
        feat = " featured" if p["featured"] else ""
        badge = '<div class="featured-badge">⭐ הכי פופולרי</div>' if p["featured"] else ""
        lis = "".join(f'<li><span class="check">✓</span> {i}</li>' for i in p["items"])
        msg = f"היי, אשמח לבדוק זמינות ל{p['name']} ({p['price']}₪)"
        cls = "btn-wa" if p["featured"] else "btn-outline"
        cards.append(f'''<div class="package-card{feat}">{badge}
        <h3 class="pkg-name">{p["name"]}</h3>
        <div class="pkg-price">{p["price"]}₪</div>
        <ul class="pkg-features">{lis}</ul>
        <a href="{wa(msg)}" class="btn {cls}" target="_blank" rel="noopener">צרו עימנו קשר עכשיו</a>
      </div>''')
    return f'''<section class="section packages" id="packages" aria-labelledby="pk-h">
  <div class="container">
    <h2 class="section-title" id="pk-h">החבילות והמחירים שלנו</h2>
    <p class="section-subtitle">כל החבילות ב{PICKUP}. המחיר זהה לכל הערים, בלי דמי משלוח.</p>
    <div class="packages-grid">{"".join(cards)}</div>
  </div>
</section>'''


def gallery(page, root):
    items = page.get("gallery")
    if not items:
        return ""
    figs = "".join(f'<figure class="gallery-item">{img_tag(n, a, root)}</figure>' for n, a in items)
    return f'''<section class="section gallery" aria-labelledby="gl-h">
  <div class="container">
    <h2 class="section-title" id="gl-h">רגעים מהאירועים שלנו</h2>
    <p class="section-subtitle">הסט, בריכת הכדורים והמתקנים לתינוקות.</p>
    <div class="gallery-grid">{figs}</div>
  </div>
</section>'''


def reviews():
    cards = "".join(
        f'<figure class="testimonial-card"><div class="review-source">ביקורת Google</div>'
        f'<blockquote class="testimonial-text">״{t}״</blockquote>'
        f'<figcaption class="testimonial-author"><strong>{n}</strong> — ביקורת בגוגל</figcaption></figure>'
        for n, t in REVIEWS[:3])
    return f'''<section class="section testimonials" aria-labelledby="rv-h">
  <div class="container">
    <h2 class="section-title" id="rv-h">מה כתבו עלינו בגוגל</h2>
    <p class="section-subtitle">דירוג {RATING} מתוך 5 · {REVIEW_COUNT} ביקורות · <a href="{MAPS_URL}" target="_blank" rel="noopener">לכל הביקורות</a></p>
    <div class="testimonials-grid">{cards}</div>
  </div>
</section>'''


def faq_block(page):
    if not page.get("faq"):
        return ""
    items = "".join(
        f'<details class="faq-item"><summary class="faq-question"><span class="faq-q-text">{q}</span><span class="faq-arrow" aria-hidden="true">▼</span></summary><div class="faq-answer">{a}</div></details>'
        for q, a in page["faq"])
    return f'''<section class="section faq" aria-labelledby="fq-h">
  <div class="container">
    <h2 class="section-title" id="fq-h">{page.get("faq_title", "שאלות נפוצות")}</h2>
    <div class="faq-list">{items}</div>
  </div>
</section>'''


def related(page, root, pages_by_slug):
    rel = page.get("related", [])
    if not rel:
        return ""
    links = "".join(f'<li><a href="{root}{s}">{pages_by_slug[s]["card"]}</a></li>' for s in rel)
    return f'''<nav class="related" aria-labelledby="rl-h">
  <div class="container">
    <h2 id="rl-h">{page.get("related_title", "עוד באתר")}</h2>
    <ul class="chips">{links}</ul>
  </div>
</nav>'''


def cta(page):
    msg = page.get("wa", "היי, אשמח לבדוק זמינות להשכרת ג'ימבורי")
    return f'''<section class="final-cta">
  <div class="container">
    <h2>{page.get("cta_title", "חוגגים יום הולדת? בואו נתכנן רגע קסום לקטנטנים!")}</h2>
    <p>שלחו הודעה עם התאריך ומספר הילדים, ונחזור אליכם עם זמינות. {PICKUP}.</p>
    <a href="{wa(msg)}" class="btn-wa-white" target="_blank" rel="noopener">צרו עימנו קשר עכשיו</a>
  </div>
</section>'''


def footer(root, cities, guides):
    city_links = "".join(f'<a href="{root}{s}">{n}</a>' for s, n in cities)
    guide_links = "".join(f'<a href="{root}{s}">{n}</a>' for s, n in guides)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="footer-logo">🎪 GIMBORY4U</div>
        <p class="footer-tagline">ג'ימבורי להשכרה לפעוטות — נקי, בטיחותי ומשתלם לאירועים בבית.<br>{PICKUP}.</p>
        <address>
          <p class="footer-contact-line">📍 {ADDRESS_STREET}, {ADDRESS_CITY}</p>
          <p class="footer-contact-line">📞 <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
          <p class="footer-contact-line">💬 <a href="{wa()}" target="_blank" rel="noopener">וואטסאפ</a> · {HOURS_TEXT}</p>
          <p class="footer-contact-line"><a href="{MAPS_URL}" target="_blank" rel="noopener">Google</a> · <a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Facebook</a></p>
        </address>
      </div>
      <div class="footer-col"><h2>שירותים ומדריכים</h2><nav aria-label="שירותים">{guide_links}</nav></div>
      <div class="footer-col"><h2>השכרת ג'ימבורי לפי עיר</h2><nav class="footer-cities" aria-label="ערים">{city_links}</nav></div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Gimbory4U · <a href="{root}pages/service-areas.html">אזורי שירות</a> · <a href="{root}pages/accessibility-statement.html">הצהרת נגישות</a></p>
    </div>
  </div>
</footer>
<a href="{wa()}" class="wa-float" target="_blank" rel="noopener" aria-label="שליחת הודעה בוואטסאפ">{WA_SVG}</a>
<div class="sticky-cta">
  <a href="{wa()}" class="btn btn-wa" target="_blank" rel="noopener">צרו קשר בוואטסאפ</a>
  <a href="tel:{PHONE_TEL}" class="btn btn-outline">חיוג</a>
</div>'''


def render(page, pages_by_slug, cities, guides):
    root = "../" if page["slug"].startswith("pages/") else ""
    url = f"{SITE}/" if page["slug"] == "index.html" else f"{SITE}/{page['slug']}"
    og_img = f"{SITE}/images/{page['img']}.webp"
    body_html = page["body"](root) if callable(page["body"]) else page["body"]
    sales = page.get("show_packages", True)
    parts = [
        breadcrumb(page, root),
        hero(page, root),
        spotlight(page, root) if sales else "",
        steps() if page.get("show_steps", True) else "",
        packages(root) if sales else "",
        gallery(page, root),
        body_html,
        reviews() if page.get("show_reviews", True) else "",
        faq_block(page),
        related(page, root, pages_by_slug),
        cta(page) if page.get("show_cta", True) else "",
    ]
    return f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{escape(page["desc"])}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large")}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="he_IL">
<meta property="og:site_name" content="Gimbory4U">
<meta property="og:title" content="{escape(page["title"])}">
<meta property="og:description" content="{escape(page["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0062C4">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="{root}css/style.css?v={ASSET_V}">
<script type="application/ld+json">
{page_schema(page, url)}
</script>
</head>
<body data-root="{root}">
{header(page, root)}
<main id="main">
{"".join(parts)}
</main>
{footer(root, cities, guides)}
<script src="{root}js/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
