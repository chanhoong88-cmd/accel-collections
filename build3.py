# Post-build copy patches for collections.accelgroup.asia
import os, sys, re, glob, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
r = subprocess.run([sys.executable, os.path.join(HERE, 'build2.py')], cwd=HERE)
if r.returncode != 0:
    sys.exit(r.returncode)
OUT = os.path.join(HERE, 'out')
PATCHES = [
 ('index.html',
  '<p>Every residence in the Collection is hosted. Before you arrive, the rooms are prepared, the kitchen is stocked and your host knows how your days should run.</p>\n          <p>Private residences with your own host, chef and chauffeur. Work when you must. Restore in between.</p>',
  '<p>Private hosted residences. Each stay includes a dedicated host, with a personal chef or chauffeur available. Your house is prepared and the kitchen stocked before you arrive. Meals, transfers and housekeeping are arranged for you, with room to work and room to rest. Leave the details to us.</p>'),
 ('index.html',
  '<h2>A house to yourself. <em>A team quietly taking care of the details.</em></h2>',
  '<h2>A private residence. <em>Ready when you arrive.</em></h2>'),
]
for f, old, new in PATCHES:
    p = os.path.join(OUT, f)
    t = open(p, encoding='utf-8').read()
    if old not in t:
        print('COPY PATCH NOT FOUND in', f, ':', old[:60]); sys.exit(1)
    open(p, 'w', encoding='utf-8').write(t.replace(old, new))
    print('copy patch applied:', f, ':', old[:40])
# Regex heading patches applied across all pages: (pattern, replacement)
RX = [
 (r'(<h2[^>]*>)\s*Made for the ones[\s\S]*?(</h2>)', r'\1Cooler air. <em>A slower pace.</em>\2'),
 (r'(<h2[^>]*>)\s*Three houses,?(?:\s|<[^>]*>)*two highlands[\s\S]*?(</h2>)', r'\1Cool mornings. <em>Misty evenings.</em>\2'),
]
for pat, rep in RX:
    total = 0
    for p in glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True):
        t = open(p, encoding='utf-8').read()
        t2, n = re.subn(pat, rep, t, flags=re.I)
        if n:
            open(p, 'w', encoding='utf-8').write(t2)
            print('regex patch applied:', os.path.relpath(p, OUT), n)
            total += n
    if total == 0:
        print('REGEX PATCH NOT FOUND:', pat)
        for p in glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True):
            t = open(p, encoding='utf-8').read()
            for m in re.finditer('Three houses', t, re.I):
                print('CTX', os.path.relpath(p, OUT), repr(t[max(0,m.start()-200):m.end()+200]))
        sys.exit(1)
