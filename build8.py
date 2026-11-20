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

# Make the booking-engine mention in the FAQ answer a clickable link (visible HTML only, not JSON-LD).
A = '<p>Book directly on our booking engine at booknow.accelgroup.asia/book:'
B = '<p>Book directly on our booking engine at <a href="https://booknow.accelgroup.asia/book">booknow.accelgroup.asia/book</a>:'
for root, _, files in os.walk(OUT):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            t = open(p, encoding='utf-8').read()
            if A in t:
                open(p, 'w', encoding='utf-8').write(t.replace(A, B))
