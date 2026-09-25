/* ============================================================
   Gimbory4U — main.js (v3)
   כל התוכן, הקישורים והתמונות כתובים ישירות ב-HTML.
   הקובץ הזה מוסיף רק שיפורי ממשק:
   1. צל לכותרת בזמן גלילה
   2. הגדלת תמונה בלחיצה (Lightbox)
   3. תפריט נגישות (ת"י 5568 / WCAG 2.1 AA)
   ============================================================ */

(function () {
  'use strict';

  /* ── 1. Header shadow on scroll ── */
  function initHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var update = function () { header.classList.toggle('scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ── 2. Lightbox for images marked .zoomable ── */
  function initLightbox() {
    var images = document.querySelectorAll('img.zoomable');
    if (!images.length) return;

    var box = document.createElement('div');
    box.className = 'lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'תצוגת תמונה מוגדלת');
    box.innerHTML = '<button type="button" aria-label="סגירת התמונה">✕</button><img alt="">';
    document.body.appendChild(box);

    var big = box.querySelector('img');
    var closeBtn = box.querySelector('button');
    var lastFocus = null;

    function open(img) {
      lastFocus = img;
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      box.classList.add('open');
      closeBtn.focus();
    }
    function close() {
      box.classList.remove('open');
      if (lastFocus) lastFocus.focus();
    }

    images.forEach(function (img) {
      img.setAttribute('tabindex', '0');
      img.addEventListener('click', function () { open(img); });
      img.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(img); }
      });
    });
    closeBtn.addEventListener('click', close);
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && box.classList.contains('open')) close();
    });
  }

  /* ── 3. Accessibility widget ── */
  function initAccessibility() {
    var STORE = 'g4u_access_v3';
    var MODES = [
      ['acc-hi', 'ניגודיות גבוהה'],
      ['acc-gray', 'גווני אפור'],
      ['acc-links', 'הדגשת קישורים'],
      ['acc-noanim', 'עצירת אנימציות'],
      ['acc-rfont', 'גופן קריא'],
      ['acc-spacing', 'ריווח מוגבר']
    ];
    var FONTS = ['', 'acc-f1', 'acc-f2', 'acc-f3'];
    var root = document.documentElement;

    var state = { font: 0, modes: {} };
    try {
      var saved = JSON.parse(localStorage.getItem(STORE) || 'null');
      if (saved) state = { font: saved.font || 0, modes: saved.modes || {} };
    } catch (e) { /* storage unavailable */ }

    function apply() {
      FONTS.forEach(function (c) { if (c) root.classList.remove(c); });
      if (state.font) root.classList.add(FONTS[state.font]);
      MODES.forEach(function (m) { root.classList.toggle(m[0], !!state.modes[m[0]]); });
      try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (e) { /* ignore */ }
    }
    apply();

    var fontButtons = ['A', 'A+', 'A++', 'A+++'].map(function (label, i) {
      return '<button type="button" class="acc-font" data-font="' + i + '" aria-pressed="' + (state.font === i) + '">' + label + '</button>';
    }).join('');
    var modeButtons = MODES.map(function (m) {
      return '<button type="button" class="acc-btn" data-mode="' + m[0] + '" aria-pressed="' + !!state.modes[m[0]] + '">' + m[1] + '</button>';
    }).join('');

    var widget = document.createElement('div');
    widget.id = 'acc-widget';
    widget.innerHTML =
      '<button type="button" id="acc-toggle" aria-expanded="false" aria-controls="acc-panel">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="4" r="2"/><path d="M12 6v6l3 3M5 8h14M9 21l-2-6 3-3 2 3 2-3 3 3-2 6"/></svg>' +
        'נגישות</button>' +
      '<div id="acc-panel" role="dialog" aria-label="הגדרות נגישות">' +
        '<div class="acc-head">הגדרות נגישות<button type="button" data-close aria-label="סגירת תפריט הנגישות">✕</button></div>' +
        '<div class="acc-fonts"><span>גודל טקסט</span>' + fontButtons + '</div>' +
        '<div class="acc-grid">' + modeButtons + '</div>' +
        '<div class="acc-foot"><button type="button" data-reset>איפוס</button>' +
        '<a href="' + (document.body.dataset.root || '') + 'pages/accessibility-statement.html">הצהרת נגישות</a></div>' +
      '</div>';
    document.body.appendChild(widget);

    var toggle = widget.querySelector('#acc-toggle');
    var panel = widget.querySelector('#acc-panel');

    function setOpen(isOpen) {
      panel.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
      (isOpen ? panel.querySelector('[data-close]') : toggle).focus();
    }
    function refreshPressed() {
      widget.querySelectorAll('.acc-font').forEach(function (b) {
        b.setAttribute('aria-pressed', String(Number(b.dataset.font) === state.font));
      });
      widget.querySelectorAll('.acc-btn').forEach(function (b) {
        b.setAttribute('aria-pressed', String(!!state.modes[b.dataset.mode]));
      });
    }

    toggle.addEventListener('click', function () { setOpen(!panel.classList.contains('open')); });
    panel.querySelector('[data-close]').addEventListener('click', function () { setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('open')) setOpen(false);
    });
    panel.addEventListener('click', function (e) {
      var btn = e.target.closest('button');
      if (!btn) return;
      if (btn.dataset.font) state.font = Number(btn.dataset.font);
      else if (btn.dataset.mode) state.modes[btn.dataset.mode] = !state.modes[btn.dataset.mode];
      else if (btn.hasAttribute('data-reset')) state = { font: 0, modes: {} };
      else return;
      apply();
      refreshPressed();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initHeader();
    initLightbox();
    initAccessibility();
  });
})();
