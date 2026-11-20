# Vercel Web Analytics: inject the tracking script into every built page in out/.
# Static-site equivalent of `npm i @vercel/analytics` + <Analytics />.
# Runs after build6.py. Fails the build if index.html can't be patched.
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
SNIPPET = ('<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>\n'
           '<script defer src="/_vercel/insights/script.js"></script>\n')
MARK = '/_vercel/insights/script.js'

total = 0; index_done = False
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8').read()
        if MARK in t:
            done = True
        else:
            i = t.lower().rfind('</head>')
            if i == -1:
                continue
            t = t[:i] + SNIPPET + t[i:]
            open(p, 'w', encoding='utf-8').write(t)
            total += 1
            done = True
        if os.path.relpath(p, OUT) == 'index.html':
            index_done = done
print(f'vercel analytics added to {total} page(s)')
if not index_done:
    print('ANALYTICS PATCH FAILED: </head> not found in index.html'); sys.exit(1)
