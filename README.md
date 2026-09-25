# Gimbory4U – gimbory4u.co.il

אתר סטטי להשכרת ג'ימבורי לפעוטות (איסוף עצמי מקריית עקרון).
מתארח ב-Cloudflare Workers (Static Assets) ומתפרסם אוטומטית בכל push לענף `main`.

## מבנה
| תיקייה / קובץ | תפקיד |
|---|---|
| `public/` | מה שמתפרסם באתר: HTML, CSS, JS, תמונות, `_redirects`, `_headers`, `404.html` |
| `tools/` | מחולל העמודים (Python). התוכן של כל עמוד נמצא ב-`pages_topics.py` וב-`pages_cities.py` |
| `wrangler.jsonc` | הגדרות Cloudflare |

## עדכון תוכן
1. עורכים את הטקסטים ב-`tools/pages_topics.py` / `tools/pages_cities.py` (או את העיצוב ב-`tools/static/css/style.css`).
2. מריצים: `python3 tools/build.py` – העמודים ב-`public/` נבנים מחדש.
3. אם שיניתם CSS/JS – מעלים את `ASSET_V` ב-`tools/gen_lib.py` כדי לעקוף מטמון.
4. commit + push ל-`main` → Cloudflare מפרסם תוך כדקה.

## תמונות
קבצי WebP ב-`public/images/`, בשמות לפי מילת החיפוש של העמוד. המידות שלהן רשומות ב-`tools/img_dims.json`.
