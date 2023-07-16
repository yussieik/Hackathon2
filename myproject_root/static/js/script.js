fetch('https://www.hebcal.com/shabbat?cfg=i2&geonameid=294117&b=18&M=on&lg=fr&tgt=_top')
  .then(response => response.text())
  .then(data => document.getElementById('hebcal-shabbat').innerHTML = data);

  document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
          left: 'title',
          right: 'prev,next today',
        },
        events: {
            url: "https://www.hebcal.com/hebcal?cfg=fc&v=1&i=off&maj=on&min=on&nx=on&mf=on&ss=on&mod=on&lg=s&s=on&c=on&geonameid=294117",
            cache: true
        }
    });
    calendar.render();
    // optional: bind keyboard left/right arrow keys
    // to move calendar forward/backward by a month
    document.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft' && !e.metaKey) {
        calendar.prev();
      } else if (e.key === 'ArrowRight' && !e.metaKey) {
        calendar.next();
      }
    });
  });

