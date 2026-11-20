# Hero search bar: "Check availability" goes straight to the online booking engine
# with the chosen residence, dates and guests already selected.
# Runs after build5.py; injects a small script into the built pages in out/.
# Fails the build if the homepage search bar is not found.
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
BOOK = 'https://accel-booking.vercel.app/book'

SCRIPT = r'''<script id="accel-book-search">(function(){
var BOOK=%r;
var SLUGS=[["estate","dani-hill-estate"],["mansion","the-mansion"],["villa dani","villa-dani"],["rompin","rompin-house"]];
function heroForm(el){var f=el&&el.closest?el.closest("form"):null;if(!f)return null;
 if(f.closest("#reserve"))return null;
 var b=f.querySelector("button,[type=submit]");var t=((f.getAttribute("aria-label")||"")+" "+(b?b.textContent:"")).toLowerCase();
 return t.indexOf("check availability")>-1?f:null;}
function slugOf(sel){if(!sel)return "";var v=(sel.value||"").toLowerCase();
 for(var i=0;i<SLUGS.length;i++){if(v===SLUGS[i][1])return v;}
 var o=sel.options[sel.selectedIndex];var t=((o&&o.text)||v).toLowerCase();
 for(var j=0;j<SLUGS.length;j++){if(t.indexOf(SLUGS[j][0])>-1)return SLUGS[j][1];}return "";}
function go(f){var sels=f.querySelectorAll("select"),res=null,gst=null;
 for(var i=0;i<sels.length;i++){var s=sels[i],txt=(s.getAttribute("aria-label")||s.name||s.id||"")+" "+(s.options[0]?s.options[0].text:"");
  if(/guest/i.test(txt))gst=s;else if(!res)res=s;}
 var d=f.querySelectorAll('input[type=date]');var ci=d[0]?d[0].value:"",co=d[1]?d[1].value:"";
 var p=[],slug=slugOf(res);if(slug)p.push("residence="+slug);
 var re=/^\d{4}-\d{2}-\d{2}$/;
 if(re.test(ci)){p.push("checkin="+ci);if(re.test(co)&&co>ci)p.push("checkout="+co);}
 var g=gst?parseInt(gst.value||(gst.options[gst.selectedIndex]||{}).text,10):NaN;if(g>0)p.push("guests="+g);
 window.location.href=BOOK+(p.length?"?"+p.join("&"):"");}
document.addEventListener("submit",function(e){var f=heroForm(e.target);if(!f)return;e.preventDefault();e.stopImmediatePropagation();go(f);},true);
document.addEventListener("click",function(e){var b=e.target&&e.target.closest?e.target.closest("button,[type=submit]"):null;if(!b)return;
 if(!/check availability/i.test(b.textContent||b.value||""))return;var f=heroForm(b);if(!f)return;e.preventDefault();e.stopImmediatePropagation();go(f);},true);
})();</script>''' % BOOK

done = 0
home_ok = False
for root, _, files in os.walk(OUT):
    for name in files:
        if not name.endswith('.html'):
            continue
        path = os.path.join(root, name)
        html = open(path, encoding='utf-8').read()
        if 'accel-book-search' in html or 'heck availability' not in html or '</body>' not in html:
            continue
        html = html.replace('</body>', SCRIPT + '</body>', 1)
        open(path, 'w', encoding='utf-8').write(html)
        done += 1
        if os.path.normpath(path) == os.path.normpath(os.path.join(OUT, 'index.html')):
            home_ok = True

print('build6: search bar linked to booking engine on %d page(s)' % done)
if not home_ok:
    print('build6: homepage search bar not found', file=sys.stderr)
    sys.exit(1)
