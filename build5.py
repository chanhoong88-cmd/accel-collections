# Header button: "Reserve" (jumps to the enquiry form) -> "Book now" (online booking engine).
# Runs after build4.py; edits the built pages in out/. Fails the build if the button is not found,
# so the live site is never left half-changed.
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
URL = 'https://accel-booking.vercel.app/book'
anchor = re.compile(r'<a\b([^>]*?)\bhref="[^"]*#reserve"([^>]*)>(\s*)Reserve(\s*)</a>', re.I)
total = 0; index_done = False
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8').read()
        m = re.search(r'<header\b.*?</header>', t, re.S | re.I)
        if not m:
            continue
        head = m.group(0)
        new_head, n = anchor.subn(lambda a: f'<a{a.group(1)}href="{URL}"{a.group(2)}>{a.group(3)}Book now{a.group(4)}</a>', head, count=1)
        if n:
            open(p, 'w', encoding='utf-8').write(t[:m.start()] + new_head + t[m.end():])
            total += n
            if os.path.relpath(p, OUT) == 'index.html':
                index_done = True
print(f'header button updated on {total} page(s)')
if not index_done:
    print('BOOK NOW PATCH FAILED: header Reserve button not found on index.html'); sys.exit(1)
