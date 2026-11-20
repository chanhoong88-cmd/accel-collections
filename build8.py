# Point every booking link at the branded domain booknow.accelgroup.asia.
# Runs last; rewrites built files in out/.
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
OLD = 'https://accel-booking.vercel.app'
NEW = 'https://booknow.accelgroup.asia'
n = 0
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith(('.html', '.js', '.json', '.xml', '.txt')):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8').read()
        except Exception:
            continue
        if OLD in t:
            open(p, 'w', encoding='utf-8').write(t.replace(OLD, NEW))
            n += 1
print(f'booking links rewritten in {n} file(s)')
