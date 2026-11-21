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

# The sticky "Reserve a residence" button goes straight to the booking engine,
# opening on the residence of the page it sits on.
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8').read()
        slug = os.path.basename(root) if root != OUT else ''
        url = f'{NEW}/book' + (f'?residence={slug}' if slug in ('the-mansion', 'villa-dani', 'rompin-house') else '')
        old = 'id="sticky" href="#reserve"'
        if old in t:
            open(p, 'w', encoding='utf-8').write(t.replace(old, f'id="sticky" href="{url}"'))

# Member "Sign in" link beside the header "Book now" button.
BOOK_BTN = '<a class="btn btn-gold" href="https://booknow.accelgroup.asia/book">Book now</a>'
SIGN_IN = '<a href="https://booknow.accelgroup.asia/account" data-member-link>Sign in</a>'

# Google tag. G = GA4 property for accelgroup.asia (564468279); AW = Accel Collections Google Ads account (107-266-8744).
# The cookie is shared across *.accelgroup.asia, so a booking paid on booknow.accelgroup.asia
# is credited to the ad click that landed here. This tag records visits only, never conversions.
TAG_IDS = ['G-XQ0707P9BD', 'AW-18573607023']
GTAG = ('<script async src="https://www.googletagmanager.com/gtag/js?id=' + TAG_IDS[0] + '"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());"
        + ''.join("gtag('config','" + i + "',{cookie_domain:'accelgroup.asia',linker:{domains:['collections.accelgroup.asia','booknow.accelgroup.asia','accelgroup.asia']}});" for i in TAG_IDS)
        + "</script>\n")

navs = tags = 0
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding='utf-8').read()
        u = t
        if BOOK_BTN in u and 'data-member-link' not in u:
            u = u.replace(BOOK_BTN, SIGN_IN + '\n      ' + BOOK_BTN, 1); navs += 1
        if 'googletagmanager.com/gtag/js' not in u:
            i = u.lower().find('</head>')
            if i != -1:
                u = u[:i] + GTAG + u[i:]; tags += 1
        if u != t:
            open(p, 'w', encoding='utf-8').write(u)
print(f'sign-in link added to {navs} page(s); Google tag added to {tags} page(s)')
