# Villa Dani photo highlights strip (on /villa-dani/) and the full gallery page (/villa-dani/gallery/).
# Runs after build10.py and mirrors the Mansion strip and gallery. The gallery page uses the built
# Villa Dani page as its shell, so the header, footer, fonts, analytics and Google tag match.
#
# Photos live in svc/villa-dani/ as villa-dani-NNN-s.avif (900px) and villa-dani-NNN-l.avif (1800px max).
# To add or reorder photos, edit PHOTOS and HIGHLIGHTS below.
import os, re, sys, json, shutil, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
SITE = 'https://collections.accelgroup.asia/'
URL = SITE + 'villa-dani/gallery/'
SRC = os.path.join(HERE, 'svc', 'villa-dani')
def e(s): return H.escape(s, quote=True)
def fail(m): print('build11 FAILED: ' + m); sys.exit(1)

# (number, group, caption) — caption doubles as alt text
PHOTOS = [
    ('001', 'house', 'Villa Dani, the white A-frame house'),
    ('002', 'house', 'A bath on the balcony, among the pines'),
    ('003', 'living', 'The lounge at dawn, under the chandelier'),
    ('004', 'living', 'Morning in the lounge'),
    ('005', 'living', 'Tea by the window'),
    ('006', 'living', 'The dining room, set for dinner'),
    ('007', 'living', 'Dinner is set'),
    ('008', 'living', 'The cinema room'),
    ('015', 'living', 'The library corner'),
    ('016', 'living', 'The fireplace'),
    ('020', 'living', 'The kitchen'),
    ('010', 'rooms', 'The master bedroom'),
    ('011', 'rooms', 'The terrace bath off the master bedroom'),
    ('009', 'rooms', 'A twin room with a balcony'),
    ('012', 'rooms', 'A bedroom with botanical wallpaper'),
    ('013', 'rooms', 'A garden-print bedroom'),
    ('014', 'rooms', 'The attic room'),
    ('017', 'rooms', 'The vanity'),
    ('018', 'rooms', 'A patterned bathroom'),
    ('019', 'rooms', 'The gold bathroom'),
]
GROUPS = [('house', 'The house <em>and terraces.</em>'), ('living', 'Living <em>and dining.</em>'), ('rooms', 'Bedrooms <em>and baths.</em>')]
HIGHLIGHTS = ['001', '003', '010', '006', '002', '004', '011', '013', '015', '007', '009', '008']
# focal point for photos cropped into 3:2 tiles (portrait shots)
POS = {'001': '50% 25%', '003': '50% 62%', '004': '50% 50%', '006': '50% 55%', '007': '50% 60%', '008': '50% 45%', '016': '50% 55%', '019': '50% 60%'}

CAP = {n: c for n, _, c in PHOTOS}
ORDER = [n for g, _ in GROUPS for n, gg, _ in PHOTOS if gg == g]  # gallery / lightbox order
for n in CAP:
    for t in 'sl':
        if not os.path.exists(os.path.join(SRC, f'villa-dani-{n}-{t}.avif')): fail(f'missing villa-dani-{n}-{t}.avif')
dst = os.path.join(OUT, 'img', 'villa-dani'); os.makedirs(dst, exist_ok=True)
for f in os.listdir(SRC):
    if f.endswith('.avif'): shutil.copy(os.path.join(SRC, f), os.path.join(dst, f))
def S(n): return f'/img/villa-dani/villa-dani-{n}-s.avif'
def L(n): return f'/img/villa-dani/villa-dani-{n}-l.avif'
TOTAL = len(PHOTOS)
def P(n): return f' style="object-position:{POS[n]}"' if n in POS else ''

ARROW_L = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12.5 4 6.5 10l6 6"/></svg>'
ARROW_R = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M7.5 4l6 6-6 6"/></svg>'

# ================= 1. Highlights strip on /villa-dani/ =================
items = '\n'.join(
    f'        <a class="hl-item" href="/villa-dani/gallery/#p-{n}"><img src="{S(n)}" alt="{e(CAP[n])}" width="900" height="600" loading="lazy" decoding="async"{P(n)}><span>{e(CAP[n])}</span></a>'
    for n in HIGHLIGHTS)
STRIP = f'''  <section class="hl" id="gallery">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">Photo highlights</div>
          <h2>Inside <em>Villa Dani.</em></h2>
        </div>
        <div class="hl-ctl">
          <button class="hl-btn" id="hlPrev" type="button" aria-label="Previous photos">{ARROW_L}</button>
          <button class="hl-btn" id="hlNext" type="button" aria-label="Next photos">{ARROW_R}</button>
          <a class="btn btn-line" href="/villa-dani/gallery/">View all {TOTAL} photos</a>
        </div>
      </div>
    </div>
    <div class="hl-track" id="hlTrack" tabindex="0" aria-label="Villa Dani photo highlights">
{items}
        <a class="hl-item hl-more" href="/villa-dani/gallery/"><span class="hl-more-in"><span class="eyebrow">Gallery</span><strong>View all <em>{TOTAL} photos</em></strong><span class="hl-arrow">→</span></span></a>
    </div>
  </section>

'''
STRIP_CSS = '''<style>
.hl{padding-bottom:clamp(60px,8vw,110px)}
.hl .res-head{margin-bottom:clamp(28px,4vw,44px)}
.hl h2{font-size:clamp(38px,4.6vw,64px);margin-top:14px}
.hl-ctl{display:flex;align-items:center;gap:10px}
.hl-btn{width:48px;height:48px;border:1px solid var(--line);background:transparent;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.25s;border-radius:50%}
.hl-btn:hover{background:var(--ink);color:var(--ivory);border-color:var(--ink)}
.hl-btn:disabled{opacity:.3;pointer-events:none}
.hl-ctl .btn{margin-left:8px}
.hl-track{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;-webkit-overflow-scrolling:touch;scrollbar-width:none;
  padding:0 max(clamp(20px,4vw,48px),calc((100vw - var(--max))/2 + clamp(20px,4vw,48px)));scroll-padding:0 max(clamp(20px,4vw,48px),calc((100vw - var(--max))/2 + clamp(20px,4vw,48px)));outline:none}
.hl-track::-webkit-scrollbar{display:none}
.hl-item{position:relative;flex:0 0 clamp(270px,34vw,520px);aspect-ratio:3/2;overflow:hidden;scroll-snap-align:start;background:var(--sand);cursor:zoom-in}
.hl-item img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s ease}
.hl-item:hover img{transform:scale(1.04)}
.hl-item>span{position:absolute;left:0;right:0;bottom:0;padding:34px 18px 14px;font-size:12px;letter-spacing:.04em;color:#fff;background:linear-gradient(transparent,rgba(20,16,12,.6));opacity:0;transition:opacity .35s}
.hl-item:hover>span,.hl-item:focus-visible>span{opacity:1}
.hl-more{flex-basis:clamp(220px,22vw,320px);background:var(--forest);color:var(--ivory);cursor:pointer;display:flex;align-items:center;justify-content:center;text-align:center}
.hl-more-in{display:flex;flex-direction:column;align-items:center;gap:12px}
.hl-more strong{font-family:var(--serif);font-weight:400;font-size:clamp(28px,2.6vw,36px);line-height:1.1}
.hl-more em{font-style:italic;display:block}
.hl-arrow{font-size:22px;color:var(--gold-soft);transition:transform .3s}
.hl-more:hover .hl-arrow{transform:translateX(6px)}
@media (max-width:700px){.hl-btn{display:none}.hl-ctl .btn{margin-left:0;padding:11px 18px}.hl-item{flex-basis:80vw}.hl-item>span{opacity:1}.hl-more{flex-basis:56vw}}
</style>
'''
STRIP_JS = '''<script>
(function(){var t=document.getElementById('hlTrack');if(!t)return;var p=document.getElementById('hlPrev'),n=document.getElementById('hlNext');
function step(){var i=t.querySelector('.hl-item');return i?(i.getBoundingClientRect().width+14)*Math.max(1,Math.floor(t.clientWidth/(i.getBoundingClientRect().width+14))-0):400}
function upd(){p.disabled=t.scrollLeft<4;n.disabled=t.scrollLeft+t.clientWidth>=t.scrollWidth-4}
p.addEventListener('click',function(){t.scrollBy({left:-step()})});n.addEventListener('click',function(){t.scrollBy({left:step()})});
t.addEventListener('scroll',upd,{passive:true});window.addEventListener('resize',upd);upd();
t.addEventListener('keydown',function(ev){if(ev.key==='ArrowRight'){ev.preventDefault();t.scrollBy({left:step()})}if(ev.key==='ArrowLeft'){ev.preventDefault();t.scrollBy({left:-step()})}});})();
</script>
'''

mp = os.path.join(OUT, 'villa-dani', 'index.html')
shell = open(mp, encoding='utf-8').read()  # unmodified Villa Dani page = shell for the gallery
anchor = '  <section class="sand" id="retreats">'
if anchor not in shell: fail('retreats section not found on Villa Dani page')
page = shell.replace(anchor, STRIP + anchor, 1)
i = page.lower().rfind('</head>'); page = page[:i] + STRIP_CSS + page[i:]
i = page.lower().rfind('</body>'); page = page[:i] + STRIP_JS + page[i:]
open(mp, 'w', encoding='utf-8').write(page)

# ================= 2. Gallery page /villa-dani/gallery/ =================
IDX = {n: k for k, n in enumerate(ORDER)}
blocks = []
for g, title in GROUPS:
    figs = '\n'.join(
        f'          <a class="g-item" id="p-{n}" href="{L(n)}" data-i="{IDX[n]}"><img src="{S(n)}" alt="{e(CAP[n])}" width="900" height="600" loading="lazy" decoding="async"{P(n)}></a>'
        for n, gg, _ in PHOTOS if gg == g)
    count = sum(1 for _, gg, _ in PHOTOS if gg == g)
    blocks.append(f'''      <div class="g-group rv">
        <div class="g-head"><h2>{title}</h2><span class="eyebrow">{count} photos</span></div>
        <div class="g-grid">
{figs}
        </div>
      </div>''')
DATA = json.dumps([{'s': L(n), 'c': CAP[n]} for n in ORDER], ensure_ascii=False)

MAIN = f'''<main id="top">
  <section class="g-top">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Accel Collection</a> · <a href="/villa-dani/">Villa Dani</a> · <span>Gallery</span></nav>
      <div class="g-intro">
        <div>
          <div class="eyebrow">Dani Hill · Genting Highlands</div>
          <h1>Villa Dani, <em>in pictures.</em></h1>
        </div>
        <div class="g-intro-r">
          <p>{TOTAL} photographs of the house, its lounge, dining room and bedrooms, and the terraces. Select any photo to view it full size.</p>
          <div class="btn-row"><a class="btn btn-gold" href="/villa-dani/#reserve">Check availability</a><a class="btn btn-line" href="/villa-dani/">Back to Villa Dani</a></div>
        </div>
      </div>
    </div>
  </section>
  <section class="g-body">
    <div class="wrap">
{chr(10).join(blocks)}
    </div>
  </section>
</main>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button class="lb-x" id="lbX" type="button" aria-label="Close">×</button>
  <button class="lb-nav lb-p" id="lbP" type="button" aria-label="Previous photo">{ARROW_L}</button>
  <figure class="lb-fig"><img id="lbImg" alt=""><figcaption><span id="lbCap"></span><span id="lbNum"></span></figcaption></figure>
  <button class="lb-nav lb-n" id="lbN" type="button" aria-label="Next photo">{ARROW_R}</button>
</div>'''

G_CSS = '''<style>
header{background:rgba(246,241,232,.96);backdrop-filter:blur(8px);border-color:var(--line)}
header .brand{opacity:1;pointer-events:auto;color:var(--ink)} header .navlinks a{color:var(--ink)}
.g-top{padding:clamp(130px,14vw,180px) 0 clamp(30px,4vw,50px)}
.g-top .crumbs{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:28px}
.g-top .crumbs a{color:var(--ink-2)}
.g-intro{display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(30px,6vw,90px);align-items:end}
.g-intro h1{font-size:clamp(46px,6.4vw,92px);margin-top:14px}
.g-intro-r p{max-width:44ch;margin-bottom:24px;color:var(--ink-2)}
.btn-row{display:flex;gap:12px;flex-wrap:wrap}
.g-body{padding-top:clamp(20px,3vw,40px)}
.g-group+.g-group{margin-top:clamp(56px,7vw,96px)}
.g-head{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:22px}
.g-head h2{font-size:clamp(30px,3.2vw,44px)}
.g-head .eyebrow{color:var(--muted)}
.g-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.g-item{display:block;aspect-ratio:3/2;overflow:hidden;background:var(--sand);cursor:zoom-in;scroll-margin-top:120px}
.g-item:first-child{grid-column:span 2;grid-row:span 2;aspect-ratio:auto}
.g-item{position:relative}
.g-item:first-child img{position:absolute;inset:0}
.g-item img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s ease}
.g-item:hover img{transform:scale(1.04)}
.lb{position:fixed;inset:0;z-index:200;background:rgba(18,15,12,.96);display:flex;align-items:center;justify-content:center}
.lb[hidden]{display:none}
.lb-fig{margin:0;max-width:min(92vw,1800px);display:flex;flex-direction:column;align-items:center}
.lb-fig img{max-width:100%;max-height:82vh;object-fit:contain;user-select:none}
.lb-fig figcaption{display:flex;justify-content:space-between;gap:30px;width:100%;margin-top:14px;color:#e9e1d3;font-size:13px;letter-spacing:.03em}
#lbNum{color:var(--gold-soft);font-size:11px;letter-spacing:.2em;white-space:nowrap}
.lb-x{position:absolute;top:18px;right:24px;background:none;border:0;color:#fff;font-size:40px;line-height:1;cursor:pointer;opacity:.8}
.lb-x:hover{opacity:1}
.lb-nav{position:absolute;top:50%;transform:translateY(-50%);width:54px;height:54px;border-radius:50%;border:1px solid rgba(255,255,255,.3);background:transparent;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.25s}
.lb-nav:hover{background:rgba(255,255,255,.12)}
.lb-p{left:24px}.lb-n{right:24px}
body.lb-open{overflow:hidden}
@media (max-width:900px){.g-intro{grid-template-columns:1fr}.g-grid{grid-template-columns:1fr 1fr;gap:10px}.lb-nav{display:none}}
@media (max-width:560px){.g-grid{grid-template-columns:1fr}.g-item:first-child{grid-column:auto;grid-row:auto;aspect-ratio:3/2}}
</style>
'''
G_JS = '''<script>
(function(){var P=__DATA__,lb=document.getElementById('lb'),im=document.getElementById('lbImg'),cap=document.getElementById('lbCap'),num=document.getElementById('lbNum'),k=0,last=null;
function show(i){k=(i+P.length)%P.length;im.src=P[k].s;im.alt=P[k].c;cap.textContent=P[k].c;num.textContent=(k+1)+' / '+P.length;
 var a=new Image();a.src=P[(k+1)%P.length].s;}
function open(i){last=document.activeElement;show(i);lb.hidden=false;document.body.classList.add('lb-open');document.getElementById('lbX').focus();}
function close(){lb.hidden=true;document.body.classList.remove('lb-open');if(location.hash)history.replaceState(null,'',location.pathname);if(last)last.focus();}
document.querySelectorAll('.g-item').forEach(function(a){a.addEventListener('click',function(ev){ev.preventDefault();open(+a.dataset.i);});});
document.getElementById('lbX').onclick=close;document.getElementById('lbP').onclick=function(){show(k-1)};document.getElementById('lbN').onclick=function(){show(k+1)};
lb.addEventListener('click',function(ev){if(ev.target===lb)close();});
document.addEventListener('keydown',function(ev){if(lb.hidden)return;if(ev.key==='Escape')close();if(ev.key==='ArrowRight')show(k+1);if(ev.key==='ArrowLeft')show(k-1);});
var x0=null;lb.addEventListener('touchstart',function(ev){x0=ev.touches[0].clientX},{passive:true});
lb.addEventListener('touchend',function(ev){if(x0===null)return;var d=ev.changedTouches[0].clientX-x0;if(Math.abs(d)>40)show(d<0?k+1:k-1);x0=null;});
var h=location.hash.match(/^#p-(\\d+)$/);if(h){var el=document.getElementById('p-'+h[1]);if(el)open(+el.dataset.i);}})();
</script>
'''.replace('__DATA__', DATA)

TITLE = 'Villa Dani Gallery | Photos of Villa Dani at Dani Hill, Genting Highlands'
DESC = (f'{TOTAL} photos of Villa Dani at Dani Hill, a private A-frame residence in Genting Highlands: '
        'the lounge, dining room, cinema room, library corner, bedrooms, bathrooms and balcony bath.')
LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "ImageGallery", "@id": URL + "#gallery", "name": "Villa Dani at Dani Hill: photo gallery", "url": URL,
     "about": {"@id": SITE + "villa-dani/#lodging"},
     "image": [{"@type": "ImageObject", "contentUrl": SITE.rstrip('/') + L(n), "caption": CAP[n]} for n in ORDER]},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accel Collection", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Villa Dani", "item": SITE + "villa-dani/"},
        {"@type": "ListItem", "position": 3, "name": "Gallery", "item": URL}]}]}

m = re.search(r'<main id="top">.*?</main>', shell, re.S)
if not m: fail('main not found in shell')
g = shell[:m.start()] + MAIN + shell[m.end():]
g = re.sub(r'<title>.*?</title>', '<title>' + e(TITLE) + '</title>', g, count=1, flags=re.S)
g = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda x: x.group(1) + e(DESC), g)
g = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda x: x.group(1) + e(TITLE), g)
g = re.sub(r'(<meta property="og:image" content=")[^"]*', lambda x: x.group(1) + SITE.rstrip('/') + L('001'), g)
g = re.sub(r'(<meta property="og:image:alt" content=")[^"]*', lambda x: x.group(1) + e(CAP['001']), g)
g = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda x: x.group(1) + URL, g)
g = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda x: x.group(1) + URL, g)
g = re.sub(r'<script type="application/ld\+json">.*?</script>',
           lambda x: '<script type="application/ld+json">' + json.dumps(LD, ensure_ascii=False, separators=(',', ':')) + '</script>', g, count=1, flags=re.S)
g = re.sub(r'<link rel="preload"[^>]*>\s*', '', g)
g = g.replace('href="#reserve"', 'href="/villa-dani/#reserve"').replace('href="#faq"', 'href="/villa-dani/#faq"')
i = g.lower().rfind('</head>'); g = g[:i] + G_CSS + g[i:]
i = g.lower().rfind('</body>'); g = g[:i] + G_JS + g[i:]
os.makedirs(os.path.join(OUT, 'villa-dani', 'gallery'), exist_ok=True)
open(os.path.join(OUT, 'villa-dani', 'gallery', 'index.html'), 'w', encoding='utf-8').write(g)

# ---- sitemap ----
sm = os.path.join(OUT, 'sitemap.xml')
s = open(sm, encoding='utf-8').read()
if URL not in s:
    imgs = ''.join(f'<image:image><image:loc>{SITE.rstrip("/")}{L(n)}</image:loc><image:title>{e(CAP[n])}</image:title></image:image>' for n in ORDER)
    s = s.replace('</urlset>', f'  <url><loc>{URL}</loc><lastmod>2026-11-24</lastmod>{imgs}</url>\n</urlset>')
    open(sm, 'w', encoding='utf-8').write(s)

print(f'build11: highlights strip ({len(HIGHLIGHTS)} photos) on /villa-dani/; /villa-dani/gallery/ built with {TOTAL} photos')
