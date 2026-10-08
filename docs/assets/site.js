(function () {
  'use strict';

  /* ---- Open / closed, worked out in the store's own time zone ---- */
  var TZ = 'America/Los_Angeles';
  var SHORT = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var LONG = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  function toMinutes(hhmm) {
    var p = String(hhmm).split(':');
    return Number(p[0]) * 60 + Number(p[1] || 0);
  }

  /* "09:00-21:00" -> [[540, 1260]]; a day with a midday break is "09:00-13:00,14:00-21:00"; a closed day is "" */
  function parseHours(text) {
    if (!text) return [];
    return String(text).split(',').map(function (part) {
      var ends = part.trim().split('-');
      return [toMinutes(ends[0]), toMinutes(ends[1])];
    }).filter(function (iv) {
      return iv[1] > iv[0];
    }).sort(function (a, b) { return a[0] - b[0]; });
  }

  function clock(mins) {
    var h = Math.floor(mins / 60) % 24, m = mins % 60;
    return (h % 12 || 12) + (m ? ':' + (m < 10 ? '0' : '') + m : '') + (h >= 12 ? ' PM' : ' AM');
  }

  /* hours: {0..6: [[open, close], ...]}; now: {day, mins} */
  function storeStatus(hours, now) {
    var today = hours[now.day] || [];
    for (var i = 0; i < today.length; i++) {
      if (now.mins >= today[i][0] && now.mins < today[i][1]) {
        return { open: true, text: 'Open now, until ' + clock(today[i][1]) };
      }
    }
    for (var j = 0; j < today.length; j++) {
      if (now.mins < today[j][0]) {
        return { open: false, text: 'Closed now, opens at ' + clock(today[j][0]) };
      }
    }
    for (var k = 1; k <= 7; k++) {
      var d = (now.day + k) % 7, next = hours[d] || [];
      if (next.length) {
        return { open: false, text: 'Closed now, opens ' + (k === 1 ? 'tomorrow' : LONG[d]) + ' at ' + clock(next[0][0]) };
      }
    }
    return { open: false, text: 'Closed' };
  }

  function storeNow(date) {
    var parts = new Intl.DateTimeFormat('en-US', {
      timeZone: TZ, weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23'
    }).formatToParts(date);
    var got = {};
    parts.forEach(function (p) { got[p.type] = p.value; });
    return { day: SHORT.indexOf(got.weekday), mins: (Number(got.hour) % 24) * 60 + Number(got.minute) };
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { storeStatus: storeStatus, storeNow: storeNow, clock: clock, parseHours: parseHours };
    return;
  }

  /* The hours list in the page is the single source of truth. */
  var dayItems = Array.prototype.slice.call(document.querySelectorAll('[data-day]'));
  var hours = {};
  dayItems.forEach(function (li) {
    hours[Number(li.getAttribute('data-day'))] = parseHours(li.getAttribute('data-hours'));
  });

  function paint() {
    var now;
    try { now = storeNow(new Date()); } catch (e) { return; }
    if (now.day < 0 || isNaN(now.mins)) return;
    var s = storeStatus(hours, now);
    Array.prototype.forEach.call(document.querySelectorAll('[data-status]'), function (el) {
      el.setAttribute('data-state', s.open ? 'open' : 'closed');
      var t = el.querySelector('[data-status-text]');
      if (t) t.textContent = s.text;
      el.hidden = false;
    });
    dayItems.forEach(function (li) {
      if (Number(li.getAttribute('data-day')) === now.day) li.setAttribute('aria-current', 'date');
      else li.removeAttribute('aria-current');
    });
  }
  paint();
  setInterval(paint, 30000);

  /* ---- Copy buttons ---- */
  Array.prototype.forEach.call(document.querySelectorAll('[data-copy]'), function (btn) {
    var label = btn.querySelector('[data-label]');
    var idle = label.textContent;
    var timer;
    function say(msg) {
      label.textContent = msg;
      clearTimeout(timer);
      timer = setTimeout(function () { label.textContent = idle; }, 2400);
    }
    function selectInstead() {
      var el = document.getElementById(btn.getAttribute('data-target'));
      if (!el) return;
      var range = document.createRange();
      range.selectNodeContents(el);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      say('Selected, ready to copy');
    }
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { say('Copied'); }, selectInstead);
      } else {
        selectInstead();
      }
    });
  });

  /* ---- Phone dock: appears once the hero buttons have scrolled away ---- */
  var dock = document.getElementById('dock');
  var heroActions = document.getElementById('hero-actions');
  if (dock && heroActions && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      dock.classList.toggle('is-on', !entries[0].isIntersecting);
    }).observe(heroActions);
  }
})();
