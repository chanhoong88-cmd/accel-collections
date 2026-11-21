# Curated Experiences page (/experiences/) and its nav + footer links.
# Runs after build8.py. Uses the built Mansion page as the shell, so the header, footer,
# fonts, analytics and Google tag stay identical to the rest of the site.
#
# Photos: drop files into svc/exp/ named evening-1.avif ... evening-4.avif.
# Any slot without a file shows a "Photo to come" placeholder.
import os, re, sys, json, shutil, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
SITE = 'https://collections.accelgroup.asia/'
URL = SITE + 'experiences/'
WA = '601162265257'; WA_D = '+60 11-6226 5257'; EMAIL = 'enquiry@accelgroup.asia'
HERO = 'https://cdn.sanity.io/images/mm0glelj/production/b4deb726b84a95b37a813976ea05d64dcfeab60b-960x1280.jpg'
def e(s): return H.escape(s, quote=True)
from urllib.parse import quote
def q(s): return quote(s, safe='')
def fail(m): print('build9 FAILED: ' + m); sys.exit(1)

TITLE = 'Curated Experiences | An Evening at Dani Hill | Accel Collection'
DESC = ("Hosted evenings at Accel Collection residences. An Evening at Dani Hill: violin from the grand staircase at 5pm, "
        "then a candlelit Chef's Table dinner for twenty at The Mansion, Genting Highlands. RSVP or book it privately.")

RSVP_MSG = "Hello, I'd like to RSVP for An Evening at Dani Hill.\nName:\nNumber of guests:\nPreferred date:"
WA_RSVP = f'https://wa.me/{WA}?text=' + q(RSVP_MSG)
MAIL_RSVP = f'mailto:{EMAIL}?subject=' + q('RSVP: An Evening at Dani Hill') + '&body=' + q(RSVP_MSG)
PRIV_MSG = "Hello, I'd like to arrange a private experience for my group.\nExperience:\nPreferred date:\nNumber of guests:"
WA_PRIV = f'https://wa.me/{WA}?text=' + q(PRIV_MSG)
MAIL_PRIV = f'mailto:{EMAIL}?subject=' + q('Private experience enquiry') + '&body=' + q(PRIV_MSG)
WA_TT = f'https://wa.me/{WA}?text=' + q("Hello, I'd like to RSVP early for Tiles & Tea at The Mansion.\nName:\nNumber of guests:")
WA_NEXT = f'https://wa.me/{WA}?text=' + q("Hello, please let me know when the next Accel Collection experience is announced.")

# ---- photo slots ----
os.makedirs(os.path.join(OUT, 'img', 'exp'), exist_ok=True)
ALTS = ['A violinist on the grand staircase at The Mansion', "Guests seated for dinner in The Mansion's dining hall",
        "Grilled squid with a green chilli sauce, plated for the Chef's Table", "A tartare course with a dried pineapple flower and seeded cracker"]
POS = ['62% 55%', '50% 47%', '40% 55%', '55% 50%']
# Display order: staircase (large), the two dishes side by side, dining hall (wide)
ORDER = [1, 3, 4, 2]
slots = []
for i in ORDER:
    alt = ALTS[i-1]
    src = os.path.join(HERE, 'svc', 'exp', f'evening-{i}.avif')
    cls = 'x-ph x-ph-lead' if i == 1 else 'x-ph'
    if os.path.exists(src):
        shutil.copy(src, os.path.join(OUT, 'img', 'exp', f'evening-{i}.avif'))
        slots.append(f'<figure class="{cls} has-img"><img src="/img/exp/evening-{i}.avif" alt="{e(alt)}" loading="lazy" style="object-position:{POS[i-1]}"></figure>')
    else:
        slots.append(f'<figure class="{cls}" aria-hidden="true"><span>Photo to come</span></figure>')
gallery = '\n          '.join(slots)
shutil.copy(os.path.join(HERE, 'svc', 'exp', 'hero.avif'), os.path.join(OUT, 'img', 'exp', 'hero.avif'))

MAIN = f'''<main id="top">
  <section class="r-hero x-hero">
    <div class="hero-bg"><img src="/img/exp/hero.avif" alt="The Mansion at Dani Hill at sunset, Genting Highlands" width="1536" height="1024" fetchpriority="high" decoding="async"></div>
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Accel Collection</a> · <span>Curated Experiences</span></nav>
      <h1>Curated <em>Experiences.</em></h1>
      <div class="r-tag">Hosted evenings at our residences.</div>
      <div class="r-facts"><span>Limited seats</span><span>Hosted by our team</span><span>Private sessions on request</span></div>
      <a class="btn btn-gold" href="#evening">See the first experience</a>
    </div>
  </section>

  <section id="evening" class="x-event">
    <div class="wrap">
      <div class="x-grid">
        <div class="rv">
          <div class="eyebrow">Dani Hill · The Mansion</div>
          <h2>An evening <em>in the house.</em></h2>
          <p>An evening at The Mansion for twenty guests. It begins at 5pm with a violin performance on the grand staircase. At 6pm, dinner is served by candlelight at the Chef&#x27;s Table in the dining hall, with a menu cooked by a guest chef who changes each season.</p>
          <ol class="x-prog">
            <li><span class="x-time">05:00 <small>pm</small></span><span>Violin, <em>on the grand staircase.</em></span></li>
            <li><span class="x-time">06:00 <small>pm</small></span><span>Dinner for twenty, <em>by candlelight.</em></span></li>
            <li><span class="x-time x-season">Each season</span><span>A guest chef, <em>a new menu.</em></span></li>
          </ol>
        </div>
        <div class="rv">
          <dl class="spec">
            <div><dt>Venue</dt><dd>The Mansion, Dani Hill, Genting Highlands</dd></div>
            <div><dt>Time</dt><dd>From 5pm</dd></div>
            <div><dt>Guests</dt><dd>Twenty seats</dd></div>
            <div><dt>Included</dt><dd>Violin performance · Chef&#x27;s Table dinner by a guest chef</dd></div>
            <div><dt>Dates</dt><dd>Check with us for the next available date</dd></div>
          </dl>
          <div class="x-rsvp">
            <div class="eyebrow">RSVP with us</div>
            <p>Send your name, number of guests and preferred date. Your host confirms your seats personally, usually within the day.</p>
            <div class="btn-row"><a class="btn btn-gold" href="{e(WA_RSVP)}" target="_blank" rel="noopener">RSVP on WhatsApp</a><a class="btn btn-line" href="{e(MAIL_RSVP)}">RSVP by email</a></div>
            <small>WhatsApp {WA_D} · {EMAIL}</small>
          </div>
        </div>
      </div>
      <div class="x-gallery rv">
          {gallery}
      </div>
      <p class="x-note">Artist&#x27;s impression. Proposed, subject to final arrangements.</p>
    </div>
  </section>

  <section class="sand x-next">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">Next in the series</div>
          <h2>More evenings, <em>coming soon.</em></h2>
        </div>
        <p>New experiences are added through the year. Each is hosted at an Accel Collection residence, with seats limited to a small group.</p>
      </div>
      <div class="x-soon">
        <div class="who-card rv"><div class="eyebrow">Dani Hill · The Mansion · Details coming soon</div><h3>Tiles &amp; Tea <em>at The Mansion.</em></h3><p>A Cantonese supper club for twenty guests. Chinese tea and dim sum are served in rounds, followed by mahjong late into the evening. Full details coming soon. RSVP early for early-bird perks.</p><a href="{e(WA_TT)}" target="_blank" rel="noopener">RSVP early on WhatsApp →</a></div>
        <div class="who-card rv"><div class="eyebrow">To be announced</div><h3><em>Coming soon.</em></h3><p>Details, venue and dates to be announced.</p><a href="{e(WA_NEXT)}" target="_blank" rel="noopener">Be the first to hear →</a></div>
      </div>
    </div>
  </section>

  <section class="band" id="private">
    <div class="wrap rv">
      <div class="eyebrow">Private sessions</div>
      <h2>Make it yours. <em>Your guests only.</em></h2>
      <p>Any experience can be reserved for your group only. Birthdays, anniversaries, client dinners and team evenings can all be arranged. Share your date and number of guests, and we&#x27;ll plan the programme, menu and transfers with you.</p>
      <div class="btn-row x-center"><a class="btn btn-gold" href="{e(WA_PRIV)}" target="_blank" rel="noopener">Contact us on WhatsApp</a><a class="btn btn-line" style="color:var(--ivory)" href="{e(MAIL_PRIV)}">Email us</a></div>
    </div>
  </section>
</main>'''

CSS = '''<style>
.x-hero h1 em{font-style:italic}
.x-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(40px,6vw,96px);align-items:start}
.x-grid h2{font-size:clamp(38px,4.6vw,64px);margin:14px 0 22px}
.x-grid p{max-width:52ch}
.x-prog{list-style:none;padding:0;margin:36px 0 0;border-top:1px solid var(--line)}
.x-prog li{display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:baseline;padding:20px 0;border-bottom:1px solid var(--line);font-family:var(--serif);font-size:clamp(20px,1.8vw,24px)}
.x-time{font-size:clamp(30px,3vw,40px);line-height:1;color:var(--ink)}
.x-time small{font-family:var(--sans);font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.x-season{font-size:clamp(22px,2vw,26px);font-style:italic;color:var(--gold)}
.x-rsvp{margin-top:34px;padding:30px;background:var(--sand)}
.x-rsvp p{margin:10px 0 22px}
.x-rsvp small{display:block;margin-top:16px;color:var(--muted);font-size:12px}
.btn-row{display:flex;gap:12px;flex-wrap:wrap}
.x-center{justify-content:center;margin-top:34px}
.x-gallery{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:repeat(2,minmax(180px,22vw));gap:14px;margin-top:clamp(56px,7vw,96px)}
.x-ph{margin:0;background:var(--sand);border:1px dashed var(--stone);display:flex;align-items:center;justify-content:center;overflow:hidden}
.x-ph span{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.x-ph-lead{grid-row:span 2}
.x-ph:nth-child(4){grid-column:span 2}
.x-ph.has-img{border:0}
.x-ph img{display:block;width:100%;height:100%;object-fit:cover}
.x-note{margin-top:14px;font-size:11px;letter-spacing:.06em;color:var(--muted)}
.x-next{padding-top:clamp(64px,8vw,110px)}
.x-soon{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.x-soon .who-card{display:flex;flex-direction:column}
.x-soon .who-card h3{font-size:clamp(28px,2.6vw,36px);margin:12px 0 8px}
.x-soon .who-card h3 em{font-style:italic}
.x-soon .who-card a{margin-top:auto;padding-top:18px;align-self:flex-start}
@media (max-width:900px){
.x-grid,.x-soon{grid-template-columns:1fr}
.x-prog li{grid-template-columns:110px 1fr}
.x-gallery{grid-template-columns:1fr 1fr;grid-template-rows:none;grid-auto-rows:44vw}
.x-ph-lead{grid-column:span 2;grid-row:auto}
.x-ph:nth-child(4){grid-column:span 2}
}
</style>
</head>'''

LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "Organization", "@id": SITE + "#org", "name": "Accel Collection", "url": SITE},
    {"@type": "Event", "name": "An Evening at Dani Hill", "url": URL + "#evening",
     "description": "Violin from the grand staircase at 5pm, then a candlelit Chef's Table dinner for twenty at The Mansion, Dani Hill. A guest chef cooks the menu each season.",
     "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
     "location": {"@type": "Place", "name": "The Mansion, Dani Hill",
                  "address": {"@type": "PostalAddress", "addressLocality": "Genting Highlands", "addressRegion": "Pahang", "addressCountry": "MY"}},
     "maximumAttendeeCapacity": 20, "organizer": {"@id": SITE + "#org"}, "image": [HERO + "?w=1600&q=80&auto=format"]},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accel Collection", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Curated Experiences", "item": URL}]}]}
# Event schema requires a startDate; leave it out of the graph until a date is set.
LD["@graph"] = [g for g in LD["@graph"] if g["@type"] != "Event"]

# ---- build the page from the Mansion shell ----
shell = open(os.path.join(OUT, 'the-mansion', 'index.html'), encoding='utf-8').read()
m = re.search(r'<main id="top">.*?</main>', shell, re.S)
if not m: fail('main not found in shell')
page = shell[:m.start()] + MAIN + shell[m.end():]
page = re.sub(r'<title>.*?</title>', '<title>' + e(TITLE) + '</title>', page, count=1, flags=re.S)
page = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda x: x.group(1) + e(DESC), page)
page = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda x: x.group(1) + e(TITLE), page)
page = re.sub(r'(<meta property="og:image:alt" content=")[^"]*', lambda x: x.group(1) + 'The Mansion at Dani Hill, Genting Highlands', page)
page = page.replace(SITE + 'the-mansion/', URL)
page = re.sub(r'<script type="application/ld\+json">.*?</script>',
              lambda x: '<script type="application/ld+json">' + json.dumps(LD, ensure_ascii=False, separators=(',', ':')) + '</script>', page, count=1, flags=re.S)
page = page.replace('data-res="the-mansion"', 'data-res="experiences"')
page = page.replace('?residence=the-mansion', '')
page = re.sub(r'<a class="btn btn-gold sticky-cta" id="sticky" href="[^"]*">[^<]*</a>',
              '<a class="btn btn-gold sticky-cta" id="sticky" href="#evening">RSVP for the evening</a>', page)
if 'RSVP for the evening' not in page: fail('sticky button not found')
page = re.sub(r'<link rel="preload"[^>]*>\s*', '', page)
i = page.lower().rfind('</head>')
page = page[:i] + CSS + page[i + len('</head>'):]
os.makedirs(os.path.join(OUT, 'experiences'), exist_ok=True)
open(os.path.join(OUT, 'experiences', 'index.html'), 'w', encoding='utf-8').write(page)

# ---- nav + footer links on every page ----
NAV_OLD = re.compile(r'(<a href="/?#retreats">Retreats</a>)')
FOOT_OLD = '<li><a href="/#faq">FAQ</a></li></ul>'
FOOT_NEW = '<li><a href="/experiences/">Curated Experiences</a></li><li><a href="/#faq">FAQ</a></li></ul>'
navs = 0
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8').read()
        if 'href="/experiences/">Experiences' not in t:
            t, n = NAV_OLD.subn(lambda x: x.group(1) + '\n      <a href="/experiences/">Experiences</a>', t, count=1)
            navs += n
        if 'Curated Experiences</a></li>' not in t:
            t = t.replace(FOOT_OLD, FOOT_NEW, 1)
        open(p, 'w', encoding='utf-8').write(t)
# The homepage "Your days" section points to the new page too.
idx = os.path.join(OUT, 'index.html')
t = open(idx, encoding='utf-8').read()
old = '<p>Arranged by your host, around your schedule.</p>'
if old in t:
    t = t.replace(old, '<p>Arranged by your host, around your schedule. <a href="/experiences/" style="text-decoration:underline;text-underline-offset:3px">See our curated evenings →</a></p>', 1)
    open(idx, 'w', encoding='utf-8').write(t)

# ---- sitemap ----
sm = os.path.join(OUT, 'sitemap.xml')
s = open(sm, encoding='utf-8').read()
if URL not in s:
    s = s.replace('</urlset>', f'  <url><loc>{URL}</loc><lastmod>2026-11-21</lastmod></url>\n</urlset>')
    open(sm, 'w', encoding='utf-8').write(s)

if navs < 2: fail('Experiences nav link not added')
print(f'build9: /experiences/ built; nav link added to {navs} page(s)')
