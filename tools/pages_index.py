# -*- coding: utf-8 -*-
"""Organic-SEO page: index of indoor playgrounds / gimboree centres in Israel,
plus the weekly articles list (tools/articles.json) and one page per article."""
import json, os
from html import escape
from collections import Counter
from gen_lib import PICKUP, PACKAGES, wa, img_tag, SITE
from pages_topics import article
from playgrounds_data import VENUES, REGION, REGION_ORDER, SOURCES, DATA_UPDATED

INDEX_SLUG = "pages/playgrounds-index.html"
HERE = os.path.dirname(os.path.abspath(__file__))
ARTICLES = sorted(json.load(open(os.path.join(HERE, "articles.json"), encoding="utf-8")),
                  key=lambda a: a["date"], reverse=True)

MONTHS = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי", "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]


def he_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} ב{MONTHS[int(m) - 1]} {y}"


def article_slug(a):
    return f"pages/article-{a['slug']}.html"


SLOGANS = [
    ("למה להצטופף במשחקייה עמוסה?", "שכרו ג'ימבורי לבית: הילדים שלכם משחקים בשקט, בקצב שלהם, בלי תורים ובלי רעש."),
    ("כל המשחקייה – רק לילדים שלכם", "סט ג'ימבורי רך עם מזרני הגנה, נקי ובמצב מעולה, בסלון או בחצר. בלי צפיפות ובלי לחכות לתור למגלשה."),
    ("הפעם, המשחקייה באה אליכם הביתה", f"השכרת ג'ימבורי לפעוטות החל מ-300₪ למחיר קבוע, לא לפי ילד. {PICKUP}."),
]


def slogan(i, root, variant=""):
    t, s = SLOGANS[i]
    home = root or "./"
    return f'''<aside class="pgx-slogan{variant}" aria-label="ג'ימבורי לבית">
  <div class="container pgx-slogan-inner">
    <div class="pgx-slogan-icon" aria-hidden="true">🏠</div>
    <div class="pgx-slogan-text"><strong>{t}</strong><span>{s}</span></div>
    <a class="btn btn-primary pgx-slogan-btn" href="{home}">לפרטים על השכרת ג'ימבורי ←</a>
  </div>
</aside>'''


def basic_spotlight(root):
    p = PACKAGES[0]
    lis = "".join(f'<li><span class="check">✓</span> {i}</li>' for i in p["items"])
    msg = f"היי, הגעתי מאינדקס המשחקיות ואשמח לבדוק זמינות ל{p['name']} ({p['price']}₪)"
    return f'''<section class="price-spotlight pgx-spot" aria-labelledby="bs-h">
  <div class="container spotlight-inner">
    <div class="price-card">
      <div class="price-label">🏠 משחקייה פרטית בבית</div>
      <div class="price-amount">{p["price"]}₪</div>
      <div class="price-title" id="bs-h">{p["name"]} – סט ג'ימבורי להשכרה</div>
      <p class="price-desc">מחיר קבוע לכל הסט, לא לפי ילד. כל המתקנים רק לילדים שלכם.</p>
      <ul class="price-features">{lis}</ul>
      <a href="{wa(msg)}" class="btn btn-wa" target="_blank" rel="noopener">בדיקת זמינות בוואטסאפ</a>
      <a href="{root or './'}" class="pgx-spot-link">לכל החבילות והפרטים ←</a>
    </div>
    <figure class="spotlight-image">
      {img_tag("set-gimbori-lehaskara", "סט ג'ימבורי להשכרה – 7 מתקנים רכים לפעוטות", root, eager=True)}
      <figcaption>הסט שמקבלים בחבילה הבסיסית: 7 מתקנים רכים</figcaption>
    </figure>
  </div>
</section>'''


def home_vs_playground(root):
    rows = [
        ("צפיפות", "הרבה ילדים בגילים שונים על אותם מתקנים", "רק הילדים שהזמנתם"),
        ("מחיר", "לפי ילד, ועולה עם כל אורח", "מחיר קבוע לסט, החל מ-300₪"),
        ("שעות", "לפי שעות הפתיחה של המקום", "לפי שנת הצהריים של הילד"),
        ("רעש ושקט", "מוזיקה, צעקות ועומס בשישי ובחגים", "סביבה מוכרת ורגועה בבית"),
        ("ההורים", "מחפשים מקום ישיבה ומשגיחים מרחוק", "יושבים קרוב, בסלון או בחצר"),
    ]
    trs = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td><td class=\"pgx-win\">✓ {c}</td></tr>" for a, b, c in rows)
    return f'''<section class="section pgx-consider" aria-labelledby="cn-h">
  <div class="container">
    <div class="pgx-consider-box">
      <div class="pgx-consider-head">
        <span class="pgx-consider-badge">💡 שווה לשקול</span>
        <h2 id="cn-h">לפני שיוצאים למשחקייה – אולי עדיף ג'ימבורי בבית?</h2>
        <p>משחקייה היא בילוי נחמד, אבל לפעוטות קטנים היא לא תמיד המקום הכי נוח. השוואה קצרה:</p>
      </div>
      <div class="table-wrap"><table>
        <thead><tr><th scope="col"></th><th scope="col">משחקייה ציבורית</th><th scope="col">ג'ימבורי בבית</th></tr></thead>
        <tbody>{trs}</tbody></table></div>
      <div class="pgx-consider-cta">
        <a href="{root or './'}" class="btn btn-primary btn-lg">לפרטים על השכרת ג'ימבורי לבית</a>
        <span>{PICKUP} · נקי ובמצב מעולה</span>
      </div>
    </div>
  </div>
</section>'''


def _bars():
    per_region = Counter(REGION[v[1]] for v in VENUES)
    top = max(per_region.values())
    rows = []
    for r in REGION_ORDER:
        n = per_region.get(r, 0)
        pct = round(n / top * 100)
        rows.append(f'''<button type="button" class="pgx-bar" data-region="{r}" aria-label="סינון לפי אזור {r}: {n} מתחמים">
        <span class="pgx-bar-label">{r}</span>
        <span class="pgx-bar-track"><span class="pgx-bar-fill" style="width:{pct}%"></span></span>
        <span class="pgx-bar-val">{n}</span></button>''')
    return "".join(rows)


def _city_bars():
    per_city = Counter(v[1] for v in VENUES).most_common(8)
    top = per_city[0][1]
    return "".join(
        f'''<button type="button" class="pgx-bar pgx-bar-city" data-city="{c}" aria-label="הצגת המתחמים ב{c}: {n}">
        <span class="pgx-bar-label">{c}</span>
        <span class="pgx-bar-track"><span class="pgx-bar-fill" style="width:{round(n / top * 100)}%"></span></span>
        <span class="pgx-bar-val">{n}</span></button>''' for c, n in per_city)


TYPE_LABEL = {"רשת": "סניף רשת", "עצמאי": "משחקייה עצמאית", "מרכז הורים": "מרכז הורים ופעוטות", "מוזיאון": "מוזיאון ילדים"}
SRC_LABEL = {"pealton": "אתר הרשת", "dapei": "דפי זהב", "karamel": "קרמל"}


def _cards():
    by_region = {r: [] for r in REGION_ORDER}
    for v in VENUES:
        by_region[REGION[v[1]]].append(v)
    out = []
    for r in REGION_ORDER:
        items = sorted(by_region[r], key=lambda v: (v[1], v[0]))
        cards = []
        for name, city, loc, typ, src in items:
            addr = f'<p class="pgx-card-addr">📍 {escape(loc)}, {city}</p>' if loc and loc not in name else f'<p class="pgx-card-addr">📍 {city}</p>'
            cards.append(f'''<li class="pgx-card" data-city="{city}" data-region="{r}" data-name="{escape(name)}">
          <h4 class="pgx-card-name">{escape(name)}</h4>
          {addr}
          <div class="pgx-card-tags"><span class="pgx-tag pgx-tag-{ 'chain' if typ == 'רשת' else 'ind' }">{TYPE_LABEL[typ]}</span><span class="pgx-tag pgx-tag-src">מקור: {SRC_LABEL[src]}</span></div>
        </li>''')
        out.append(f'''<section class="pgx-region" data-region="{r}" aria-labelledby="rg-{REGION_ORDER.index(r)}">
      <h3 class="pgx-region-title" id="rg-{REGION_ORDER.index(r)}">{r} <span class="pgx-region-count">{len(items)} מתחמים</span></h3>
      <ul class="pgx-grid">{"".join(cards)}</ul>
    </section>''')
    return "".join(out)


def _articles_list(root):
    items = "".join(f'''<li class="pgx-art">
      <a href="{root}{article_slug(a)}">
        <time datetime="{a["date"]}">{he_date(a["date"])}</time>
        <h3>{escape(a["title"])}</h3>
        <p>{escape(a["desc"])}</p>
        <span class="pgx-art-more">לקריאת המאמר ←</span>
      </a></li>''' for a in ARTICLES)
    return f'''<section class="section pgx-articles" aria-labelledby="ar-h">
  <div class="container">
    <h2 class="section-title" id="ar-h">מאמרים להורים לפעוטות</h2>
    <p class="section-subtitle">מדריכים קצרים על משחקיות, משחקי תנועה וימי הולדת לגיל הרך. מאמר חדש מתווסף בכל שבוע.</p>
    <ul class="pgx-art-list">{items}</ul>
  </div>
</section>'''


def index_body(root):
    cities = sorted({v[1] for v in VENUES})
    opts = "".join(f'<option value="{c}"></option>' for c in cities)
    chips = '<button type="button" class="pgx-chip is-active" data-region="">כל הארץ</button>' + "".join(
        f'<button type="button" class="pgx-chip" data-region="{r}">{r}</button>' for r in REGION_ORDER)
    n_chain = sum(1 for v in VENUES if v[3] == "רשת")
    src_links = " · ".join(f'<a href="{u}" target="_blank" rel="noopener nofollow">{t}</a>' for t, u in SOURCES)
    return f'''{basic_spotlight(root)}
{slogan(0, root)}
<section class="section pgx-search-sec" aria-labelledby="sr-h">
  <div class="container">
    <h2 class="section-title" id="sr-h">חיפוש משחקייה לפי עיר</h2>
    <p class="section-subtitle">הקלידו שם עיר או בחרו אזור, והרשימה תתעדכן מיד.</p>
    <div class="pgx-search" role="search">
      <label for="pgx-q" class="pgx-sr">חיפוש לפי עיר</label>
      <input id="pgx-q" type="search" list="pgx-cities" placeholder="לדוגמה: רחובות, חיפה, באר שבע…" autocomplete="off">
      <datalist id="pgx-cities">{opts}</datalist>
      <button type="button" class="pgx-clear" id="pgx-clear" aria-label="ניקוי החיפוש">✕</button>
    </div>
    <div class="pgx-chips" role="group" aria-label="סינון לפי אזור">{chips}</div>
    <p class="pgx-status" id="pgx-status" aria-live="polite"></p>
  </div>
</section>

<section class="pgx-stats-sec" aria-labelledby="stt-h">
  <div class="container">
    <h2 class="pgx-sr" id="stt-h">המספרים בקצרה</h2>
    <div class="pgx-stats">
      <div class="pgx-stat"><span class="pgx-stat-num">{len(VENUES)}</span><span class="pgx-stat-lbl">משחקיות ומתחמים</span></div>
      <div class="pgx-stat"><span class="pgx-stat-num">{len(cities)}</span><span class="pgx-stat-lbl">ערים ויישובים</span></div>
      <div class="pgx-stat"><span class="pgx-stat-num">{len(REGION_ORDER)}</span><span class="pgx-stat-lbl">אזורים בארץ</span></div>
      <div class="pgx-stat"><span class="pgx-stat-num">{round(n_chain / len(VENUES) * 100)}%</span><span class="pgx-stat-lbl">סניפים של רשתות</span></div>
    </div>
    <div class="pgx-charts">
      <figure class="pgx-chart"><figcaption>מספר המתחמים לפי אזור</figcaption>{_bars()}</figure>
      <figure class="pgx-chart"><figcaption>הערים עם הכי הרבה משחקיות</figcaption>{_city_bars()}</figure>
    </div>
    <p class="pgx-chart-hint">לחיצה על עמודה מסננת את הרשימה.</p>
  </div>
</section>

{slogan(1, root, " pgx-slogan-mid")}

{home_vs_playground(root)}

<section class="section pgx-results-sec" aria-labelledby="rs-h">
  <div class="container">
    <h2 class="section-title" id="rs-h">רשימת המשחקיות ומתחמי הג'ימבורי</h2>
    <div id="pgx-results">{_cards()}</div>
    <p class="pgx-empty" id="pgx-empty" hidden>לא מצאנו משחקייה בעיר הזו ברשימה שלנו. אולי זו הזדמנות לחגוג בבית? <a href="{root or './'}">ג'ימבורי להשכרה לפעוטות</a></p>
    <div class="pgx-note" role="note">
      <strong>ℹ️ על הנתונים:</strong> המידע בעמוד מבוסס על נתונים שנאספו מהאינטרנט ממקורות פומביים, ועודכן לאחרונה ב-{he_date(DATA_UPDATED)}.
      ייתכן ששעות, כתובות או סניפים השתנו, ולכן מומלץ לבדוק מול המקום לפני ההגעה. Gimbory4U אינה קשורה למקומות המופיעים ברשימה.
      <span class="pgx-note-src">מקורות: {src_links}</span>
    </div>
  </div>
</section>

{_articles_list(root)}

{slogan(2, root, " pgx-slogan-end")}

<script>
(function(){{
  var q=document.getElementById('pgx-q'),clr=document.getElementById('pgx-clear'),
      st=document.getElementById('pgx-status'),empty=document.getElementById('pgx-empty'),
      cards=[].slice.call(document.querySelectorAll('.pgx-card')),
      regions=[].slice.call(document.querySelectorAll('.pgx-region')),
      chips=[].slice.call(document.querySelectorAll('.pgx-chip')),region='';
  function norm(s){{return (s||'').replace(/["'״׳\\-–\\s]/g,'').replace(/קרית/g,'קריית');}}
  function apply(){{
    var t=norm(q.value),n=0;
    cards.forEach(function(c){{
      var ok=(!region||c.dataset.region===region)&&(!t||norm(c.dataset.city).indexOf(t)>-1||norm(c.dataset.name).indexOf(t)>-1);
      c.hidden=!ok; if(ok)n++;
    }});
    regions.forEach(function(r){{r.hidden=!r.querySelector('.pgx-card:not([hidden])');}});
    chips.forEach(function(c){{c.classList.toggle('is-active',c.dataset.region===region);}});
    clr.style.visibility=q.value?'visible':'hidden';
    empty.hidden=n>0;
    st.textContent=(t||region)?('נמצאו '+n+' מתחמים'+(q.value?' עבור "'+q.value+'"':'')+(region?' באזור '+region:'')):'';
  }}
  q.addEventListener('input',apply);
  clr.addEventListener('click',function(){{q.value='';q.focus();apply();}});
  chips.forEach(function(c){{c.addEventListener('click',function(){{region=c.dataset.region;apply();}});}});
  [].slice.call(document.querySelectorAll('.pgx-bar')).forEach(function(b){{
    b.addEventListener('click',function(){{
      if(b.dataset.region){{region=b.dataset.region;q.value='';}} else {{q.value=b.dataset.city;region='';}}
      apply(); document.getElementById('rs-h').scrollIntoView({{behavior:'smooth'}});
    }});
  }});
  var p=new URLSearchParams(location.search).get('city'); if(p){{q.value=p;}}
  apply();
}})();
</script>'''


INDEX = {
    "slug": INDEX_SLUG, "nav": "pgindex", "crumb": "אינדקס משחקיות",
    "title": "אינדקס מתחמי גימבורי ומשחקיות לילדים בכל הארץ – חיפוש לפי עיר | Gimbory4U",
    "desc": f"אינדקס מתחמי ג'ימבורי ומשחקיות לילדים ופעוטות ברחבי הארץ: {len(VENUES)} מקומות ב-{len({v[1] for v in VENUES})} ערים, עם חיפוש לפי עיר ואזור. ולמי שמעדיף בלי צפיפות – ג'ימבורי להשכרה לבית.",
    "eyebrow": "אינדקס משחקיות",
    "h1": "אינדקס מתחמי גימבורי ומשחקיות לילדים",
    "lead": "כל המשחקיות ומתחמי הג'ימבורי לפעוטות ברחבי הארץ במקום אחד, עם חיפוש לפי עיר. ואם בא לכם לוותר על הצפיפות – הג'ימבורי יכול להגיע גם לסלון שלכם.",
    "img": "haskarat-gimbori-lepeotot", "alt": "אינדקס משחקיות ומתחמי ג'ימבורי לילדים בישראל",
    "card": "אינדקס משחקיות לילדים", "card_sub": "חיפוש לפי עיר",
    "body": index_body,
    "updated": DATA_UPDATED,
    "schema_extra": [{
        "@type": "ItemList", "name": "משחקיות ומתחמי ג'ימבורי לילדים בישראל",
        "numberOfItems": len(VENUES),
        "itemListElement": [{"@type": "ListItem", "position": i + 1,
                             "item": {"@type": "Place", "name": v[0],
                                      "address": {"@type": "PostalAddress", "addressLocality": v[1],
                                                  **({"streetAddress": v[2]} if v[2] and v[2] not in v[0] else {}),
                                                  "addressCountry": "IL"}}}
                            for i, v in enumerate(VENUES)],
    }],
    "show_packages": False, "show_steps": False, "show_reviews": False, "show_cta": True,
    "cta_title": "רוצים משחקייה פרטית בבית? בואו נדבר",
    "wa": "היי, הגעתי מאינדקס המשחקיות ואשמח לבדוק זמינות להשכרת ג'ימבורי",
    "faq": [
        ("איך מחפשים משחקייה בעיר מסוימת?", "מקלידים את שם העיר בתיבת החיפוש, או בוחרים אזור. הרשימה מתעדכנת מיד ומציגה רק את המתחמים המתאימים."),
        ("האם המידע על המשחקיות מעודכן?", f"המידע נאסף ממקורות פומביים באינטרנט ועודכן לאחרונה ב-{he_date(DATA_UPDATED)}. כתובות ושעות פתיחה משתנים, ולכן כדאי לבדוק מול המקום לפני שמגיעים."),
        ("מה ההבדל בין משחקייה לבין ג'ימבורי להשכרה?", "משחקייה היא מקום ציבורי שמשלמים בו לפי ילד או לפי שעה, ולעיתים הוא עמוס. ג'ימבורי להשכרה הוא סט מתקנים רכים שלוקחים הביתה, למחיר קבוע, כך שרק הילדים שהזמנתם משחקים בו."),
    ],
    "related": ["index.html", "pages/gimboree-birthday-home.html", "pages/gimboree-vs-inflatable.html", "pages/service-areas.html"],
    "related_title": "אולי במקום משחקייה – ג'ימבורי בבית",
}


def _article_page(a):
    def body(root):
        others = [o for o in ARTICLES if o["slug"] != a["slug"]][:3]
        more = "".join(f'<li><a href="{root}{article_slug(o)}">{escape(o["title"])}</a></li>' for o in others)
        return (slogan(0, root) + article(f'''
<p class="pgx-art-date"><time datetime="{a["date"]}">{he_date(a["date"])}</time></p>
{a["body"]}
<div class="article-cta"><a class="btn btn-primary" href="{root}{INDEX_SLUG}">לאינדקס המשחקיות לפי עיר</a></div>
<h2>עוד מאמרים</h2><ul>{more}</ul>''') + slogan(2, root, " pgx-slogan-end"))
    return {
        "slug": article_slug(a), "nav": "", "crumb": a["title"],
        "crumbs": [("אינדקס משחקיות", INDEX_SLUG)],
        "title": f'{a["title"]} | Gimbory4U', "desc": a["desc"],
        "eyebrow": "מאמרים להורים", "h1": a["title"], "lead": a["desc"],
        "img": "haskarat-gimbori-lepeotot", "alt": a["title"], "card": a["title"], "card_sub": "",
        "body": body, "show_packages": False, "show_steps": False, "show_reviews": False, "show_cta": True,
        "related": [], "faq": [], "updated": a["date"],
        "schema_extra": [{
            "@type": "BlogPosting", "headline": a["title"], "description": a["desc"],
            "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "he-IL",
            "mainEntityOfPage": f"{SITE}/{article_slug(a)}",
            "image": f"{SITE}/images/haskarat-gimbori-lepeotot.webp",
            "author": {"@type": "Organization", "name": "Gimbory4U", "url": f"{SITE}/"},
            "publisher": {"@id": f"{SITE}/#business"},
        }],
    }


ARTICLE_PAGES = [_article_page(a) for a in ARTICLES]
INDEX_PAGES = [INDEX] + ARTICLE_PAGES
