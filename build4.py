import os, re, sys, glob, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.check_call([sys.executable, os.path.join(HERE, 'build3.py')], cwd=HERE)
OUT = os.path.join(HERE, 'out')

# 1. Remove 01 / 02 / 03 numbering on every page
for path in glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True):
    s = open(path, encoding='utf-8').read()
    s2 = re.sub(r'<div class="num">\d+</div>', '', s)
    if s2 != s:
        open(path, 'w', encoding='utf-8').write(s2)

# 2. Homepage: Accel Hosted Experience title + five services
idx = os.path.join(OUT, 'index.html')
s = open(idx, encoding='utf-8').read()

def rep(old, new):
    global s
    if s.count(old) != 1:
        raise SystemExit('Patch target not found exactly once: ' + old[:80])
    s = s.replace(old, new)

rep('<div class="pillars">',
    '<h3 class="pillars-title rv">Accel Hosted Experience</h3>\n      <div class="pillars pillars-5">')

rep('<h3>Private Chauffeur</h3><p>Door-to-door from Kuala Lumpur, so the journey becomes part of the stay.</p></div>',
    '<h3>Private Chauffeur</h3><p>Door-to-door from Kuala Lumpur, so the journey becomes part of the stay.</p></div>\n'
    '        <div class="pillar rv"><h3>Private Dining Chef</h3><p>A personal chef cooks in the house, from breakfast to a private Chef&#x27;s Table dinner.</p></div>\n'
    '        <div class="pillar rv"><h3>Curated Experiences</h3><p>Golf, recovery sessions and workshops, arranged by your host around your stay.</p></div>')

# 3. Photo under each hosted service
SAN = 'https://cdn.sanity.io/images/mm0glelj/production/'
import shutil
os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
for n in ('host', 'housekeeping', 'chauffeur', 'experiences'):
    shutil.copy(os.path.join(HERE, 'svc', n + '.avif'), os.path.join(OUT, 'img', 'svc-' + n + '.avif'))
PHOTOS = {
 'Personal Host': ('/img/svc-host.avif', 'A smiling host welcoming a guest at the reception desk'),
 'Private Housekeeping': ('/img/svc-housekeeping.avif', 'Housekeeping smoothing a quilted throw on a freshly made bed'),
 'Private Chauffeur': ('/img/svc-chauffeur.avif', 'A chauffeur holding the car door open for a guest'),
 'Private Dining Chef': (SAN+'5cf56df07a951d4bfe08faaa91353bf18411e2ca-720x1280.jpg?w=640&h=640&fit=crop&crop=bottom&q=80&auto=format', 'The dining hall at The Mansion, laid for a private dinner'),
 'Curated Experiences': ('/img/svc-experiences.avif', 'Guests at a hosted herb and botanicals workshop'),
}
for title, (src, alt) in PHOTOS.items():
    pat = re.compile(r'(<h3>' + re.escape(title) + r'</h3><p>.*?</p>)(</div>)')
    s, n = pat.subn(lambda m: m.group(1) + '<img class="pillar-img" src="' + src + '" alt="' + alt.replace("'", '&#x27;') + '" loading="lazy" width="640" height="640">' + m.group(2), s, count=1)
    if n != 1:
        raise SystemExit('Photo patch failed for ' + title)

# 4. Quiet retreat cards: equal-length copy, links aligned
CARDS = {
 'For the business traveller': 'A quiet base for focused work. Your host handles meals and your chauffeur the drive. Dani Hill hosts teams of up to 30, with meeting equipment on site and the Awana Genting golf course next door.',
 'For couples': 'A retreat for two in the cool highland air. A private chef can cook breakfast and a Chef&#x27;s Table dinner in the house. The whole residence is yours, and the day runs to your own schedule.',
 'For families and teams': 'Room for everyone under one roof, with space to gather and space to be alone. Each house sleeps up to 15, and both Dani Hill houses can be reserved together for up to 30 overnight guests.',
}
for title, text in CARDS.items():
    pat = re.compile(r'(<h3>' + re.escape(title) + r'</h3><p>).*?(</p>)')
    s, n = pat.subn(lambda m: m.group(1) + text + m.group(2), s, count=1)
    if n != 1:
        raise SystemExit('Card patch failed for ' + title)

# 5. Wide Genting Highlands photo under the quiet retreat cards
shutil.copy(os.path.join(HERE, 'svc', 'genting.avif'), os.path.join(OUT, 'img', 'genting-mist-2.avif'))
i = s.index('id="retreats"'); j = s.index('</section>', i); k = s.rindex('</div>', i, j)
s = s[:k] + '<figure class="mist rv"><img src="/img/genting-mist-2.avif" alt="Morning mist over the forest and houses at Dani Hill, Genting Highlands" loading="lazy" width="1200" height="514"><figcaption>Morning mist at Dani Hill, Genting Highlands</figcaption></figure>\n    ' + s[k:]

css = '''<style>
.pillars-title{font-family:var(--serif);font-weight:400;font-size:clamp(30px,3.2vw,40px);line-height:1.1;margin:clamp(56px,7vw,90px) 0 0}
.pillars.pillars-5{grid-template-columns:repeat(5,1fr);margin-top:26px}
.pillars-5 .pillar h3{font-size:22px;margin:0 0 8px}
.pillars.pillars-5{column-gap:36px}
.pillars-5 .pillar,.pillars-5 .pillar+.pillar{padding:34px 0 0;border-left:0;position:relative}
.pillars-5 .pillar+.pillar::before{content:"";position:absolute;left:-18px;top:0;bottom:0;border-left:1px solid var(--line)}
@media (min-width:1021px) and (max-width:1279px){.pillars-5 .pillar h3{min-height:2.2em}}
@media (max-width:1020px){
.pillars.pillars-5{grid-template-columns:1fr}
.pillars-5 .pillar,.pillars-5 .pillar+.pillar{padding:24px 0;border-left:0;border-bottom:1px solid var(--line)}
.pillars-5 .pillar+.pillar::before{display:none}
}
.who-card h3{margin-top:0}
#standard{padding-bottom:0}
#retreats .who-card,#experiences .who-card{display:flex;flex-direction:column}
#retreats .who-card a,#experiences .who-card a{margin-top:auto;align-self:flex-start}
#experiences{padding-bottom:0}
#residences{padding-top:clamp(48px,5vw,72px)}
figure.mist{margin:clamp(48px,6vw,80px) 0 0}
figure.mist img{display:block;width:100%;height:auto;aspect-ratio:1200/514;object-fit:cover}
figure.mist figcaption{margin-top:12px;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
@media (max-width:760px){figure.mist img{aspect-ratio:4/3}}
#retreats{padding-top:clamp(48px,5vw,72px)}
.pillars-5 .pillar{display:flex;flex-direction:column}
.pillar-img{display:block;width:100%;height:auto;flex:none;aspect-ratio:1/1;object-fit:cover;margin-top:auto;padding-top:24px;box-sizing:content-box}
@media (max-width:1020px){.pillar-img{aspect-ratio:3/2;padding-top:18px}}
</style>
</head>'''
rep('</head>', css)

open(idx, 'w', encoding='utf-8').write(s)
print('build4: hosted experience patch applied')
