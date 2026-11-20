import json, re, os, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
SITE = 'https://collections.accelgroup.asia/'
V = '3'  # asset version for cache busting
def IMG(k, w): return f"https://cdn.sanity.io/images/mm0glelj/production/{k}?w={w}&q=80&auto=format"
K = {'m': 'b4deb726b84a95b37a813976ea05d64dcfeab60b-960x1280.jpg', 'v': '68bdb15f93bd9e776fe46eef40f3db4da9060f4f-1537x1023.png', 'r': '117c55f41d9bea80b3a7d85c5d1ca0cbe5e0c8c9-1400x934.jpg'}
WA = '601162265257'; WA_D = '+60 11-6226 5257'; EMAIL = 'enquiry@accelgroup.asia'

ESTATE_AMEN = ["A day of golf at Awana Genting golf course", "Recovery and rejuvenation sessions with our skilled masseur", "Daily activity workshops hosted on request", "Meeting TV, whiteboard and PA system", "Breakout areas for small groups", "Activity room with automatic mahjong table, karaoke, pool, darts and foosball", "Board games, cards and movie nights", "Charcoal BBQ pit"]

RES = [
 dict(slug='the-mansion', k=K['m'], name='The Mansion', place='Dani Hill', loc='Genting Highlands, Pahang', locality='Genting Highlands',
  title="The Mansion at Dani Hill | Luxury Heritage Residence, Genting Highlands",
  meta="Book The Mansion at Dani Hill, a restored heritage residence in Genting Highlands, 45 minutes from KL. Sleeps 15, with a personal host, housekeeping, chauffeur and a private Chef's Table.",
  alt='The Mansion at Dani Hill, a restored heritage residence in Genting Highlands',
  tagline='Gather above the clouds.',
  short="A restored heritage mansion on a private highland estate, with gardens, mist and a grand house made for gatherings. Evenings close around a private Chef's Table inside the Mansion.",
  intro=["The Mansion is the heart of the Dani Hill estate: a heritage house, restored in 2026 and set in gardens in the cool air of Genting Highlands. It sleeps up to 15 guests and is hosted from the moment you arrive.",
         "Evenings gather around the Chef's Table, a private dinner served inside the Mansion. By day there is room to work, to walk the gardens, or to do very little at all."],
  type='Heritage residence', signature="Chef's Table in the Mansion", services='Personal host · Housekeeping · Chauffeur', occ='Sleeps up to 15', occmax=15, access='45 min from Kuala Lumpur',
  who=[("For the business traveller", "A meeting TV, whiteboard and PA system on the estate, breakout space and a host who keeps the day on time. Close the day with a round at Awana Genting or a recovery session."),
       ("For couples", "A heritage house in the hills, a private Chef's Table set for two and nobody else's schedule. Arrive, switch off and let the house run around you."),
       ("For families and teams", "Up to 15 guests, or 30 with Villa Dani next door. Chinese tea ceremonies can be held in the Mansion for family occasions.")],
  getting="Dani Hill is about 45 minutes from Kuala Lumpur. Your chauffeur can collect you from the city, and for larger groups 40-seater coaches can reach the estate.",
  amen=ESTATE_AMEN,
  faq=[("How many guests can stay at The Mansion?", "The Mansion sleeps up to 15 guests. Reserve it together with Villa Dani and the Dani Hill estate hosts up to 30."),
       ("How far is The Mansion from Kuala Lumpur?", "The Dani Hill estate in Genting Highlands is about 45 minutes from Kuala Lumpur, and a private chauffeur can be arranged."),
       ("Is private dining available?", "Yes. The signature experience is the Chef's Table, a private dinner served inside the Mansion. Your host arranges it when you book."),
       ("Can we hold a meeting or celebration at The Mansion?", "Yes. The estate has a meeting TV, whiteboard and PA system for groups of up to 30. For weddings and larger events, see danihill.my."),
       ("Can we play golf during our stay?", "Yes. The Awana Genting golf course is at Dani Hill, so guests who love golf can spend a day on the course. Your host can help arrange it."),
       ("What else can be arranged?", "Recovery and rejuvenation sessions with our skilled masseur, and daily activity workshops hosted on request by your host.")]),
 dict(slug='villa-dani', k=K['v'], name='Villa Dani', place='Dani Hill', loc='Genting Highlands, Pahang', locality='Genting Highlands',
  title="Villa Dani at Dani Hill | Hosted Private Residence with Golf Views, Genting Highlands",
  meta="Book Villa Dani, a hosted private residence on the Dani Hill estate in Genting Highlands, overlooking the golf course. Sleeps 15, 45 minutes from KL, with host, housekeeping and chauffeur.",
  alt='Villa Dani at Dani Hill, a private residence overlooking the golf course in Genting Highlands',
  tagline='Cool air, open views, an easy pace.',
  short="The second residence on the Dani Hill estate, looking out over the Awana Genting golf course. Relaxed, sociable rooms for families and small teams, with the Mansion a short walk across the gardens.",
  intro=["Villa Dani is the second residence on the Dani Hill estate, looking out across the Awana Genting golf course. Relaxed, sociable rooms suit families, friends and small teams, with the Mansion a short walk across the gardens.",
         "Like every Accel Collection residence, it is hosted: the rooms are ready before you arrive, housekeeping is quietly taken care of, and your chauffeur can collect you from Kuala Lumpur."],
  type='Private residence', signature='Awana Genting golf course view', services='Personal host · Housekeeping · Chauffeur', occ='Sleeps up to 15', occmax=15, access='45 min from Kuala Lumpur',
  who=[("For the business traveller", "A quieter base for a small team, with the estate's meeting TV, whiteboard and breakout areas close by when you need them."),
       ("For couples", "Golf course views, cool highland air and an easy pace. Spend a day on the Awana Genting course, then a recovery session before dinner."),
       ("For families and teams", "Sleeps up to 15. Add the Mansion for gatherings of up to 30 across the estate.")],
  getting="Dani Hill is about 45 minutes from Kuala Lumpur. Your chauffeur can collect you from the city, and for larger groups 40-seater coaches can reach the estate.",
  amen=ESTATE_AMEN,
  faq=[("How many guests can stay at Villa Dani?", "Villa Dani sleeps up to 15 guests. Reserve it together with The Mansion and the Dani Hill estate hosts up to 30."),
       ("What is the difference between Villa Dani and The Mansion?", "The Mansion is the estate's heritage house and home of the Chef's Table. Villa Dani is the more relaxed residence overlooking the golf course. Many groups reserve both."),
       ("How far is Villa Dani from Kuala Lumpur?", "The Dani Hill estate in Genting Highlands is about 45 minutes from Kuala Lumpur, and a private chauffeur can be arranged."),
       ("Is Villa Dani suitable for a work retreat?", "Yes. It is a quiet base for small teams, with the estate's meeting TV, whiteboard, PA system and breakout areas close by."),
       ("Can we play golf during our stay?", "Yes. Villa Dani overlooks the Awana Genting golf course at Dani Hill, so guests who love golf can spend a day on the course. Your host can help arrange it.")]),
 dict(slug='rompin-house', k=K['r'], name='Rompin House', place="Fraser's Hill", loc="Fraser's Hill, Pahang", locality="Fraser's Hill",
  title="Rompin House, Fraser's Hill | Hosted 1930s Colonial Bungalow Retreat",
  meta="Book Rompin House, a hosted 1930s colonial bungalow at Fraser's Hill, 1,300 metres up. English garden, garden kitchen and a quiet retreat for couples, families and small teams. Sleeps 10 (15 with extra beds).",
  alt="Rompin House, a 1930s colonial bungalow with an English garden at Fraser's Hill",
  tagline='A slower rhythm in the hills.',
  short="A 1930s colonial bungalow at 1,300 metres, with an English garden, a working kitchen and long, unhurried afternoons. Meals follow the garden, cooked to order by the house kitchen.",
  intro=["Rompin House is a 1930s colonial bungalow at Fraser's Hill, 1,300 metres above sea level. An English garden, a working kitchen and long, unhurried afternoons set the pace.",
         "Meals follow the garden, cooked to order by the house kitchen. The house sleeps 10 guests, or up to 15 with extra beds, and your host runs it throughout your stay."],
  type='Colonial bungalow, c. 1930s', signature='The Garden Kitchen', services='Personal host · Housekeeping · Chauffeur on request', occ='Sleeps 10 (15 with extra beds)', occmax=15, access='1,300 m above sea level',
  who=[("For the business traveller", "Fraser's Hill is quiet by nature. Bring a small team for thinking time well away from the city."),
       ("For couples", "Cool mornings in the garden, slow lunches from the kitchen, and nowhere you need to be."),
       ("For families and teams", "Sleeps 10, or 15 with extra beds: room for three generations under one roof.")],
  getting="Rompin House is at Fraser's Hill in Pahang, in the hills north of Kuala Lumpur. A private chauffeur from the city can be arranged on request.",
  amen=["English garden", "Working house kitchen, cooking to order", "Garden-to-table meals", "Recovery and rejuvenation sessions with our skilled masseur", "Daily activity workshops hosted on request", "Cool hill-station climate at 1,300 metres", "Extra beds for up to 15 guests", "Chauffeur on request"],
  faq=[("How many guests can stay at Rompin House?", "Rompin House sleeps 10 guests, or up to 15 with extra beds."),
       ("What is the Garden Kitchen?", "It is the house's signature experience: meals that follow the English garden, cooked to order by the house kitchen during your stay."),
       ("Is a chauffeur included?", "A private chauffeur from Kuala Lumpur can be arranged on request. Your host will confirm the details when you book."),
       ("What is the weather like at Fraser's Hill?", "At 1,300 metres, Fraser's Hill is noticeably cooler than Kuala Lumpur, so bring a light layer for the evenings."),
       ("What can we do during our stay?", "Recovery and rejuvenation sessions with our skilled masseur, and daily activity workshops hosted on request by your host, alongside long garden lunches from the kitchen.")]),
]
BY = {r['slug']: r for r in RES}

HOME_FAQ = [
 ("How do I book an Accel Collection residence?", "Book directly on our booking engine at booknow.accelgroup.asia/book: choose a residence, your dates and the number of guests. Or use the booking panel to send a request on WhatsApp or by email, and your host replies personally to confirm availability. Nothing is charged when you send a request."),
 ("What is included with every stay?", "Every residence is hosted. Stays come with a personal host and private housekeeping, and a private chauffeur from Kuala Lumpur can be arranged (on request at Rompin House). Private dining, such as the Chef's Table at The Mansion, can be arranged with your host."),
 ("Is Accel Collection like an Airbnb?", "You stay in a private residence rather than a hotel room, as you would with a holiday rental. The difference is that every Accel Collection residence is hosted and serviced, so the house is prepared before you arrive and run for you throughout your stay."),
 ("What can we do during our stay?", "Guests who love golf can spend a day at the Awana Genting golf course at Dani Hill. Across the Collection we arrange recovery and rejuvenation sessions with our skilled masseur, and your host can run daily activity workshops on request."),
 ("Is it suitable for a couple's retreat?", "Yes. Every residence can be reserved for two. Couples come for the quiet, the cool highland air, private dining and a house run around their own pace."),
 ("Can I work or hold meetings during my stay?", "Yes. The residences suit business travellers who need a quiet base. At Dani Hill there is a meeting TV, whiteboard and PA system for team meetings of up to 30 people, alongside breakout areas."),
 ("How many guests can stay?", "The Mansion and Villa Dani each sleep up to 15 guests, and the whole Dani Hill estate can be reserved for up to 30. Rompin House sleeps 10, or up to 15 with extra beds."),
 ("Where are the residences?", "The Mansion and Villa Dani are on the Dani Hill estate in Genting Highlands, about 45 minutes from Kuala Lumpur. Rompin House is a colonial bungalow at Fraser's Hill, Pahang, at 1,300 metres."),
 ("Can I host an event or wedding?", "Weddings, celebrations and corporate events are held at Dani Hill. See danihill.my for events, or add a note to your booking request and our team will advise."),
]

def e(s): return H.escape(s, quote=True)

# ---------------- shared CSS ----------------
css = open(os.path.join(HERE,'src','base.css')).read()
css += '''
/* Residence pages */
body.page header{background:rgba(246,241,232,.96);border-color:var(--line)}
body.page header .brand{opacity:1;pointer-events:auto}
body.page header .navlinks a{color:var(--ink)}
body.page header .navlinks a.btn{color:#fff}
body.page header .menu-btn{color:var(--ink)}
.r-hero{position:relative;min-height:78svh;display:flex;align-items:flex-end;color:#fff;padding:140px 0 72px}
.r-hero .hero-bg::after{background:linear-gradient(180deg,rgba(20,16,12,.25) 0%,rgba(20,16,12,.2) 45%,rgba(20,16,12,.72) 100%)}
.r-hero .wrap{position:relative;width:100%}
.r-hero .eyebrow{color:var(--gold-soft)}
.r-hero h1{font-size:clamp(52px,8vw,112px);margin:14px 0 8px}
.r-hero .r-tag{font-family:var(--serif);font-style:italic;font-size:clamp(22px,2.4vw,30px);opacity:.92}
.r-hero .r-facts{display:flex;gap:26px;flex-wrap:wrap;margin:26px 0 30px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-soft)}
.crumbs{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.75)}
.crumbs a:hover{color:#fff}
.r-overview{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(40px,7vw,110px);align-items:start}
.r-overview h2{font-size:clamp(36px,4.4vw,58px);margin:14px 0 22px}
.r-overview p{color:var(--ink-2);font-size:17px;margin-bottom:16px;max-width:56ch}
.amen{columns:2;column-gap:32px;margin-top:8px}
.amen li{list-style:none;break-inside:avoid;padding:12px 0 12px 22px;border-bottom:1px solid var(--line);position:relative;color:var(--ink-2)}
.amen li::before{content:"";position:absolute;left:0;top:21px;width:8px;height:8px;border:1px solid var(--gold);transform:rotate(45deg)}
.sand{background:var(--sand)}
.others{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,3vw,36px)}
.other{display:block;background:var(--ivory)}
.other img{width:100%;aspect-ratio:3/2;object-fit:cover}
.other div{padding:22px 24px 26px}
.other h3{font-size:32px;margin:8px 0 6px}
.other p{color:var(--ink-2);font-size:15px}
.other:hover h3{color:var(--gold)}
@media (max-width:1020px){.r-overview,.others{grid-template-columns:1fr}.amen{columns:1}}
'''

# ---------------- shared JS ----------------
js = r'''/* BOOKING ENGINE CONFIG — the only thing to change when an engine is chosen.
   provider: null (request form) | 'iframe' (embeds urls[residence]) | 'link' (opens urls[residence]) | 'script' (loads scriptSrc, calls window.mountBookingEngine(el, ctx))
   URL placeholders {checkin} {checkout} {guests} are filled automatically. */
const BOOKING_ENGINE = {
  provider: null,
  urls: { 'the-mansion':'', 'villa-dani':'', 'rompin-house':'', 'dani-hill-estate':'' },
  scriptSrc: ''
};
const ENQUIRY_EMAIL = 'enquiry@accelgroup.asia';
const BOOKING_WHATSAPP = '601162265257';
const IMG = k => 'https://cdn.sanity.io/images/mm0glelj/production/'+k+'?w=200&q=80&auto=format';
const RES = [
  { id:'the-mansion', name:'The Mansion', place:'Dani Hill', sleeps:15, img:IMG('b4deb726b84a95b37a813976ea05d64dcfeab60b-960x1280.jpg') },
  { id:'villa-dani', name:'Villa Dani', place:'Dani Hill', sleeps:15, img:IMG('68bdb15f93bd9e776fe46eef40f3db4da9060f4f-1537x1023.png') },
  { id:'rompin-house', name:'Rompin House', place:"Fraser's Hill", sleeps:10, extra:15, img:IMG('117c55f41d9bea80b3a7d85c5d1ca0cbe5e0c8c9-1400x934.jpg') }
];
const ESTATE = { id:'dani-hill-estate', name:'Dani Hill Estate', place:'The Mansion + Villa Dani', sleeps:30, img:RES[0].img };
const ALL = [...RES, ESTATE];
const byId = id => ALL.find(r => r.id === id) || RES[0];
const cap = r => r.extra || r.sleeps;
const $id = id => document.getElementById(id);
const state = { res: document.body.dataset.res || 'the-mansion', checkin:'', checkout:'', guests:2 };

const iso = d => d.toISOString().slice(0,10);
const addDays = (s,n) => { const d = new Date(s+'T00:00:00'); d.setDate(d.getDate()+n); return iso(d); };
const today = iso(new Date());
const nights = () => state.checkin && state.checkout ? Math.round((new Date(state.checkout)-new Date(state.checkin))/864e5) : 0;
const fmt = s => s ? new Date(s+'T00:00:00').toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'}) : '—';
function fillGuests(sel, r, val, short){ const max = cap(r); sel.innerHTML = Array.from({length:max},(_,i)=>`<option value="${i+1}">${i+1} ${i?'guests':'guest'}${i+1>r.sleeps?(short?' +bed':' (extra bed)'):''}</option>`).join(''); sel.value = Math.min(val,max); }
function fillUrl(u){ return u.replace('{checkin}',state.checkin).replace('{checkout}',state.checkout).replace('{guests}',state.guests); }
const goReserve = () => { const r = $id('reserve'); if (r) r.scrollIntoView({behavior:'smooth'}); };

/* ---------- Quick bar (home page only) ---------- */
const qbRes = $id('qb-res'), qbIn = $id('qb-in'), qbOut = $id('qb-out'), qbG = $id('qb-guests');
if (qbRes) {
  qbRes.innerHTML = ALL.map(r => `<option value="${r.id}">${r.name}${r.id==='dani-hill-estate'?' (both houses)':' · '+r.place}</option>`).join('');
  qbIn.min = today; qbOut.min = addDays(today,1);
  qbRes.onchange = () => { state.res = qbRes.value; state.guests = Math.min(state.guests, cap(byId(state.res))); syncAll(); };
  qbIn.onchange = () => { state.checkin = qbIn.value; if (!state.checkout || state.checkout <= state.checkin) state.checkout = addDays(state.checkin,2); syncAll(); };
  qbOut.onchange = () => { state.checkout = qbOut.value; syncAll(); };
  qbG.onchange = () => { state.guests = +qbG.value; syncAll(); };
  $id('quickbar').onsubmit = e => {
    e.preventDefault();
    if (BOOKING_ENGINE.provider === 'link' && BOOKING_ENGINE.urls[state.res]) { window.open(fillUrl(BOOKING_ENGINE.urls[state.res]), '_blank', 'noopener'); return; }
    goReserve();
  };
}
function syncBar(){ if (!qbRes) return; qbRes.value = state.res; fillGuests(qbG, byId(state.res), state.guests, true); qbIn.value = state.checkin; qbOut.value = state.checkout; qbOut.min = state.checkin ? addDays(state.checkin,1) : addDays(today,1); }

/* ---------- Booking tab ---------- */
const TABS = [
  { id:'the-mansion', label:'The Mansion', sub:'Dani Hill' },
  { id:'villa-dani', label:'Villa Dani', sub:'Dani Hill' },
  { id:'rompin-house', label:'Rompin House', sub:"Fraser's Hill" }
];
const tabsEl = $id('tabs'), eng = $id('booking-engine');
function renderTabs(){
  if (!tabsEl) return;
  const active = state.res === 'dani-hill-estate' ? 'the-mansion' : state.res;
  tabsEl.innerHTML = TABS.map(t => `<button class="tab" role="tab" aria-selected="${t.id===active}" data-tab="${t.id}"><b>${t.label}</b><small>${t.sub}</small></button>`).join('');
  tabsEl.querySelectorAll('.tab').forEach(b => b.onclick = () => { state.res = b.dataset.tab; state.guests = Math.min(state.guests, cap(byId(state.res))); syncAll(); });
}
function renderEngine(){
  if (!eng) return;
  const r = byId(state.res);
  const url = BOOKING_ENGINE.urls[state.res];
  if (BOOKING_ENGINE.provider === 'iframe' && url) { eng.innerHTML = `<iframe title="Book ${r.name}" src="${fillUrl(url)}" loading="lazy"></iframe>`; return; }
  if (BOOKING_ENGINE.provider === 'script' && BOOKING_ENGINE.scriptSrc) {
    eng.innerHTML = '';
    const go = () => window.mountBookingEngine && window.mountBookingEngine(eng, {...state, residence:r});
    if (!window.__beLoaded) { const s = document.createElement('script'); s.src = BOOKING_ENGINE.scriptSrc; s.onload = () => { window.__beLoaded = true; go(); }; document.head.appendChild(s); } else go();
    return;
  }
  const n = nights();
  eng.innerHTML = `
    <div class="engine-sum"><img src="${r.img}" alt="${r.name}" width="84" height="84"><div><h4>${r.name}</h4><p>${r.place} · sleeps ${r.sleeps}${r.extra?` (up to ${r.extra} with extra beds)`:''}</p></div></div>
    <form id="reqForm" novalidate>
      <div class="fgrid">
        <div class="f full"><label for="f-res">Residence</label><select id="f-res">${ALL.map(x=>`<option value="${x.id}" ${x.id===state.res?'selected':''}>${x.name}${x.id==='dani-hill-estate'?' (The Mansion + Villa Dani)':' · '+x.place}</option>`).join('')}</select></div>
        <div class="f"><label for="f-in">Arrive</label><input type="date" id="f-in" min="${today}" value="${state.checkin}" required></div>
        <div class="f"><label for="f-out">Depart</label><input type="date" id="f-out" min="${state.checkin?addDays(state.checkin,1):addDays(today,1)}" value="${state.checkout}" required></div>
        <div class="f"><label for="f-g">Guests</label><select id="f-g"></select></div>
        <div class="f"><label for="f-p">Purpose of stay</label><select id="f-p"><option>Couple's retreat</option><option>Business / work stay</option><option>Family stay</option><option>Celebration</option><option>Team retreat / offsite</option><option>Day escape (no overnight)</option><option>Other</option></select></div>
        <div class="stay-line"><span>${fmt(state.checkin)} → ${fmt(state.checkout)}</span><b>${n>0?n+(n>1?' nights':' night'):'Select dates'}</b></div>
        <div class="f"><label for="f-name">Full name</label><input id="f-name" autocomplete="name" required></div>
        <div class="f"><label for="f-phone">Mobile / WhatsApp</label><input id="f-phone" type="tel" autocomplete="tel" required></div>
        <div class="f full"><label for="f-email">Email</label><input id="f-email" type="email" autocomplete="email" required></div>
        <div class="f full"><label for="f-notes">Anything your host should know</label><textarea id="f-notes" placeholder="Golf day, recovery session, workshop, private dining, chauffeur from KL…"></textarea></div>
      </div>
      <div class="err" id="err" role="alert"></div>
      <div class="engine-foot"><small>Your host confirms availability personally, usually within the day. Nothing is charged at this stage.</small><div class="btn-row"><button class="btn btn-gold" type="submit" data-via="wa">Request on WhatsApp</button><button class="btn btn-line" type="submit" data-via="email">Request by email</button></div></div>
    </form>`;
  fillGuests($id('f-g'), r, state.guests);
  $id('f-res').onchange = e => { state.res = e.target.value; state.guests = Math.min(state.guests, cap(byId(state.res))); keepFormAndSync(); };
  $id('f-in').onchange = e => { state.checkin = e.target.value; if (!state.checkout || state.checkout <= state.checkin) state.checkout = addDays(state.checkin,2); keepFormAndSync(); };
  $id('f-out').onchange = e => { state.checkout = e.target.value; keepFormAndSync(); };
  $id('f-g').onchange = e => { state.guests = +e.target.value; syncBar(); };
  $id('reqForm').onsubmit = submitRequest;
}
let draft = {};
function keepFormAndSync(){
  ['f-p','f-name','f-phone','f-email','f-notes'].forEach(id => { const el = $id(id); if (el) draft[id] = el.value; });
  syncAll();
  Object.entries(draft).forEach(([id,v]) => { const el = $id(id); if (el) el.value = v; });
}
function submitRequest(e){
  e.preventDefault();
  const v = id => $id(id).value.trim();
  const err = $id('err');
  if (!state.checkin || !state.checkout) return err.textContent = 'Please choose your arrival and departure dates.';
  if (state.checkout <= state.checkin) return err.textContent = 'Departure must be after arrival.';
  if (!v('f-name') || !v('f-phone') || !/^\S+@\S+\.\S+$/.test(v('f-email'))) return err.textContent = 'Please add your name, mobile number and a valid email.';
  const r = byId(state.res), n = nights();
  const body = [
    `Residence: ${r.name} (${r.place})`, `Arrive: ${fmt(state.checkin)}`, `Depart: ${fmt(state.checkout)} (${n} night${n>1?'s':''})`,
    `Guests: ${state.guests}`, `Purpose: ${v('f-p')}`, '', `Name: ${v('f-name')}`, `Mobile: ${v('f-phone')}`, `Email: ${v('f-email')}`, '', `Notes: ${v('f-notes') || '—'}`,
    '', 'Sent from '+location.host+location.pathname
  ].join('\n');
  const via = (e.submitter && e.submitter.dataset.via) || 'wa';
  if (via === 'wa') window.open(`https://wa.me/${BOOKING_WHATSAPP}?text=${encodeURIComponent('Hello, I would like to reserve '+r.name+'.\n\n'+body)}`, '_blank', 'noopener');
  else window.location.href = `mailto:${ENQUIRY_EMAIL}?subject=${encodeURIComponent('Reservation request: '+r.name+' · '+fmt(state.checkin))}&body=${encodeURIComponent(body)}`;
  eng.innerHTML = `<div class="done"><div class="eyebrow">Request prepared</div><h4>Thank you.</h4><p>Your request for ${r.name} is ready in ${via==='wa'?'WhatsApp':'your email app'}. Send it and your host will be in touch to confirm. If nothing opened, message <a href="https://wa.me/${BOOKING_WHATSAPP}" style="text-decoration:underline">+60 11-6226 5257</a> or write to <a href="mailto:${ENQUIRY_EMAIL}" style="text-decoration:underline">${ENQUIRY_EMAIL}</a>.</p><button class="btn btn-line" id="again">Plan another stay</button></div>`;
  $id('again').onclick = () => { draft = {}; renderEngine(); };
}
function syncAll(){ syncBar(); renderTabs(); renderEngine(); }

(function initFromUrl(){
  const p = new URLSearchParams(location.search);
  if (p.get('residence') && ALL.some(r => r.id === p.get('residence'))) state.res = p.get('residence');
  if (p.get('checkin') >= today) state.checkin = p.get('checkin');
  if (state.checkin && p.get('checkout') > state.checkin) state.checkout = p.get('checkout');
  if (+p.get('guests')) state.guests = Math.min(+p.get('guests'), cap(byId(state.res)));
})();
syncAll();
if (location.hash.startsWith('#reserve') && $id('reserve')) $id('reserve').scrollIntoView();

document.addEventListener('click', e => {
  const a = e.target.closest('[data-pick]'); if (!a || !$id('reserve')) return;
  e.preventDefault(); goReserve(); history.replaceState(null,'','?residence='+a.dataset.pick+'#reserve');
  state.res = a.dataset.pick; state.guests = Math.min(state.guests, cap(byId(state.res))); syncAll();
});

/* ---------- Chrome ---------- */
const hdr = $id('hdr'), sticky = $id('sticky');
const onScroll = () => {
  hdr.classList.toggle('solid', scrollY > 60);
  const rv = $id('reserve'); if (!sticky || !rv) return;
  const b = rv.getBoundingClientRect();
  sticky.classList.toggle('hide', scrollY < 400 || (b.top < innerHeight && b.bottom > 0));
};
addEventListener('scroll', onScroll, {passive:true}); onScroll();
const menuBtn = $id('menuBtn'), links = $id('navlinks');
menuBtn.onclick = () => { const o = links.classList.toggle('open'); menuBtn.setAttribute('aria-expanded', o); hdr.classList.add('solid'); };
links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting){ x.target.classList.add('in'); io.unobserve(x.target); } }), {threshold:.12});
document.querySelectorAll('.rv').forEach(el => io.observe(el));
$id('yr').textContent = new Date().getFullYear();
'''

# ---------------- logo sprite ----------------
sym = open(os.path.join(HERE,'src','logo-path.txt')).read()
path_d = sym.strip()
logo_svg = f'<svg xmlns="http://www.w3.org/2000/svg"><symbol id="acl-logo" viewBox="0 0 800 254"><path fill="#BB9A60" fill-rule="evenodd" d="{path_d}"/></symbol></svg>\n'
LOGO_USE = lambda cls: f'<svg class="{cls}" viewBox="0 0 800 254" role="img" aria-label="Accel Collection"><use href="/assets/logo.svg?v={V}#acl-logo"/></svg>'

# ---------------- page parts ----------------
def head(title, desc, canonical, og_img, og_alt, ld, preload=None):
    pre = ''
    if preload:
        k = preload
        pre = f'<link rel="preload" as="image" href="{IMG(k,1600)}" imagesrcset="{IMG(k,800)} 800w, {IMG(k,1600)} 1600w, {IMG(k,2400)} 2400w" imagesizes="100vw" fetchpriority="high">\n'
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Accel Collection">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{IMG(og_img,1200)}">
<meta property="og:image:alt" content="{e(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f1b17">
{pre}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.sanity.io">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={V}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',',':'))}</script>
</head>
'''

def header(home):
    pre = '' if home else '/'
    return f'''<header id="hdr">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Accel Collection home">{LOGO_USE('logo')}</a>
    <nav class="navlinks" id="navlinks">
      <a href="{pre}#residences">Residences</a>
      <a href="{pre}#retreats">Retreats</a>
      <a href="#faq">FAQ</a>
      <a href="https://accelgroup.asia">Accel Group</a>
      <a class="btn btn-gold" href="#reserve">Reserve</a>
    </nav>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false">
      <svg width="26" height="26" viewBox="0 0 26 26" stroke="currentColor" stroke-width="1.4"><path d="M3 8h20M3 13h20M3 18h20"/></svg>
    </button>
  </div>
</header>
'''

def reserve_section(lede):
    return f'''  <section class="reserve" id="reserve">
    <div class="wrap reserve-grid">
      <div class="aside rv">
        <div class="eyebrow">Reserve</div>
        <h2>Plan your <em>stay.</em></h2>
        <p>{lede}</p>
        <p>For golf days, recovery sessions, workshops, private dining and events at Dani Hill, add a note and we'll arrange it.</p>
        <div class="contact-lines">
          <a href="https://wa.me/{WA}" target="_blank" rel="noopener"><span>WhatsApp</span>{WA_D}</a>
          <a href="mailto:{EMAIL}"><span>Email</span>{EMAIL}</a>
          <a href="https://www.danihill.my" target="_blank" rel="noopener"><span>Events at Dani Hill</span>danihill.my</a>
        </div>
      </div>
      <!-- BOOKING ENGINE SLOT: configured in /assets/app.js -->
      <div class="engine rv" id="engine">
        <div class="tabs" role="tablist" id="tabs"></div>
        <div id="booking-engine" role="tabpanel"><noscript><p style="padding:32px">To reserve, message your host on WhatsApp at <a href="https://wa.me/{WA}">{WA_D}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></noscript></div>
      </div>
    </div>
  </section>
'''

def faq_section(faq, title='Before you <em>book.</em>'):
    items = '\n'.join(f'        <details{" open" if i==0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i,(q,a) in enumerate(faq))
    return f'''  <section class="faq" id="faq">
    <div class="wrap faq-grid">
      <div class="rv">
        <div class="eyebrow">Questions</div>
        <h2>{title}</h2>
        <p class="faq-lede">Anything else, ask your host on WhatsApp at <a href="https://wa.me/{WA}">{WA_D}</a>.</p>
      </div>
      <div class="faq-list rv">
{items}
      </div>
    </div>
  </section>
'''

def footer():
    return f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand" href="/">{LOGO_USE('logo logo-foot')}</a>
        <p style="margin-top:18px;max-width:34ch">Curated places. Exceptional stays. Hosted private residences by Accel Hospitality.</p>
      </div>
      <div>
        <h5>Residences</h5>
        <ul><li><a href="/the-mansion/">The Mansion · Dani Hill</a></li><li><a href="/villa-dani/">Villa Dani · Dani Hill</a></li><li><a href="/rompin-house/">Rompin House · Fraser's Hill</a></li><li><a href="/#faq">FAQ</a></li></ul>
      </div>
      <div>
        <h5>Accel Group</h5>
        <ul><li><a href="https://accelgroup.asia">accelgroup.asia</a></li><li><a href="https://accelgroup.asia/collection">The full Collection</a></li><li><a href="https://www.danihill.my">Dani Hill events</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
      </div>
    </div>
    <div class="legal"><span>© <span id="yr"></span> Accel Hospitality Management Sdn. Bhd. (202601033619 (1695714-U))</span><span>Accel Collection is part of Accel Group.</span></div>
  </div>
</footer>

<a class="btn btn-gold sticky-cta" id="sticky" href="#reserve">Reserve a residence</a>
<script src="/assets/app.js?v={V}" defer></script>
</body>
</html>
'''

ORG = {"@type":"Organization","@id":SITE+"#org","name":"Accel Collection","url":SITE,"logo":SITE+"favicon.svg","email":EMAIL,"telephone":WA_D,
       "parentOrganization":{"@type":"Organization","name":"Accel Hospitality Management Sdn. Bhd.","url":"https://accelgroup.asia"}}
def lodging(r):
    url = SITE + r['slug'] + '/'
    return {"@type":"LodgingBusiness","@id":url+"#residence","name":f"{r['name']} — {r['place']}","description":r['short'],"url":url,
      "image":[IMG(r['k'],1600)],"brand":{"@id":SITE+"#org"},"telephone":WA_D,"email":EMAIL,
      "address":{"@type":"PostalAddress","addressLocality":r['locality'],"addressRegion":"Pahang","addressCountry":"MY"},
      "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in r['amen']],
      "containsPlace":{"@type":"Accommodation","name":r['name'],"occupancy":{"@type":"QuantitativeValue","maxValue":r['occmax'],"unitText":"guests"}},
      "potentialAction":{"@type":"ReserveAction","target":{"@type":"EntryPoint","urlTemplate":url+"#reserve","actionPlatform":["http://schema.org/DesktopWebPlatform","http://schema.org/MobileWebPlatform"]},"result":{"@type":"LodgingReservation","name":"Reservation request: "+r['name']}}}
def faq_ld(faq, url): return {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}

# ---------------- residence page ----------------
def res_page(r):
    url = SITE + r['slug'] + '/'
    ld = {"@context":"https://schema.org","@graph":[ORG, lodging(r),
          {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accel Collection","item":SITE},{"@type":"ListItem","position":2,"name":r['name'],"item":url}]},
          faq_ld(r['faq'], url)]}
    others = [o for o in RES if o['slug'] != r['slug']]
    amen = '\n'.join(f'            <li>{e(a)}</li>' for a in r['amen'])
    who = '\n'.join(f'        <div class="who-card rv"><div class="num">0{i+1}</div><h3>{e(t)}</h3><p>{e(p)}</p><a href="#reserve">Check availability →</a></div>' for i,(t,p) in enumerate(r['who']))
    oth = '\n'.join(f'''        <a class="other rv" href="/{o['slug']}/"><img src="{IMG(o['k'],900)}" alt="{e(o['alt'])}" width="900" height="600" loading="lazy" decoding="async"><div><div class="eyebrow">{e(o['place'])}</div><h3>{e(o['name'])}</h3><p>{e(o['tagline'])} {e(o['occ'])}.</p></div></a>''' for o in others)
    k = r['k']
    intro = ''.join(f'<p>{e(p)}</p>' for p in r['intro'])
    body = f'''<body class="page" data-res="{r['slug']}">
{header(False)}
<main id="top">
  <section class="r-hero">
    <div class="hero-bg"><img src="{IMG(k,1600)}" srcset="{IMG(k,800)} 800w, {IMG(k,1600)} 1600w, {IMG(k,2400)} 2400w" sizes="100vw" alt="{e(r['alt'])}" width="1600" height="1067" fetchpriority="high" decoding="async"></div>
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Accel Collection</a> · <span>{e(r['place'])}</span></nav>
      <h1>{e(r['name'])}</h1>
      <div class="r-tag">{e(r['tagline'])}</div>
      <div class="r-facts"><span>{e(r['loc'])}</span><span>{e(r['occ'])}</span><span>{e(r['access'])}</span></div>
      <a class="btn btn-gold" href="#reserve">Check availability</a>
    </div>
  </section>

  <section id="overview">
    <div class="wrap r-overview">
      <div class="rv">
        <div class="eyebrow">Hosted private residence · {e(r['place'])}</div>
        <h2>{e(r['name'])}, <em>{e(r['locality'])}.</em></h2>
        {intro}
      </div>
      <div class="rv">
        <dl class="spec">
          <div><dt>Property type</dt><dd>{e(r['type'])}</dd></div>
          <div><dt>Location</dt><dd>{e(r['loc'])}</dd></div>
          <div><dt>Signature experience</dt><dd>{e(r['signature'])}</dd></div>
          <div><dt>Hosted services</dt><dd>{e(r['services'])}</dd></div>
          <div><dt>Guests</dt><dd>{e(r['occ'])}</dd></div>
          <div><dt>Getting there</dt><dd>{e(r['access'])}</dd></div>
        </dl>
        <a class="btn btn-gold" href="#reserve">Book {e(r['name'])}</a>
      </div>
    </div>
  </section>

  <section class="sand" id="retreats">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">A quiet retreat</div>
          <h2>Who {e(r['name'])} <em>is made for.</em></h2>
        </div>
        <p>Every stay comes with a personal host and private housekeeping, so the house runs around you.</p>
      </div>
      <div class="who-grid">
{who}
      </div>
    </div>
  </section>

  <section id="amenities">
    <div class="wrap r-overview">
      <div class="rv">
        <div class="eyebrow">{'On the estate' if r['place']=='Dani Hill' else 'At the house'}</div>
        <h2>What's <em>here.</em></h2>
        <ul class="amen">
{amen}
        </ul>
      </div>
      <div class="rv">
        <div class="eyebrow">Getting there</div>
        <h2>Arriving at <em>{e(r['place'])}.</em></h2>
        <p>{e(r['getting'])}</p>
      </div>
    </div>
  </section>

{reserve_section(f"Choose your dates for {e(r['name'])}. Your host replies personally to confirm availability and shape the stay around your group.")}
{faq_section(r['faq'], f"{e(r['name'])}, <em>answered.</em>")}
  <section id="residences">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">Also in the Collection</div>
          <h2>More hosted <em>residences.</em></h2>
        </div>
        <p><a href="/" style="text-decoration:underline;text-underline-offset:3px">See all Accel Collection residences</a></p>
      </div>
      <div class="others">
{oth}
      </div>
    </div>
  </section>
</main>

'''
    return head(r['title'], r['meta'], url, k, r['alt'], ld, preload=k) + body + footer()

# ---------------- home page ----------------
def card(r, i):
    return f'''        <article class="res {'flip' if i%2 else ''}" id="{r['slug']}">
          <a class="res-img rv" href="/{r['slug']}/"><img src="{IMG(r['k'],1200)}" srcset="{IMG(r['k'],700)} 700w, {IMG(r['k'],1200)} 1200w, {IMG(r['k'],1600)} 1600w" sizes="(max-width:1020px) 100vw, 55vw" alt="{e(r['alt'])}" width="1200" height="1500" loading="lazy" decoding="async"><span class="tag">{e(r['place'])}</span></a>
          <div class="res-body rv">
            <div class="crumb">Accel Collection <b>→</b> {e(r['name'])}</div>
            <h3><a href="/{r['slug']}/">{e(r['name'])}</a></h3>
            <div class="tagline">{e(r['tagline'])}</div>
            <p class="desc">{e(r['short'])}</p>
            <dl class="spec">
              <div><dt>Property type</dt><dd>{e(r['type'])}</dd></div>
              <div><dt>Location</dt><dd>{e(r['loc'])}</dd></div>
              <div><dt>Signature experience</dt><dd>{e(r['signature'])}</dd></div>
              <div><dt>Hosted services</dt><dd>{e(r['services'])}</dd></div>
              <div><dt>Guests</dt><dd>{e(r['occ'])}</dd></div>
              <div><dt>Ideal for</dt><dd>Couples, business stays, families</dd></div>
            </dl>
            <div class="res-actions">
              <a class="btn btn-gold" href="?residence={r['slug']}#reserve" data-pick="{r['slug']}">Book {e(r['name'])}</a>
              <a class="btn btn-line" href="/{r['slug']}/">View {e(r['name'])}</a>
            </div>
          </div>
        </article>'''

def home_page():
    ld = {"@context":"https://schema.org","@graph":[ORG,
      {"@type":"WebSite","@id":SITE+"#website","name":"Accel Collection","url":SITE,"publisher":{"@id":SITE+"#org"},"inLanguage":"en-GB"},
      {"@type":"ItemList","name":"Accel Collection residences","itemListElement":[{"@type":"ListItem","position":i+1,"url":SITE+r['slug']+'/',"name":r['name']} for i,r in enumerate(RES)]},
      *[lodging(r) for r in RES], faq_ld(HOME_FAQ, SITE)]}
    k = K['v']
    cards = '\n'.join(card(r,i) for i,r in enumerate(RES))
    body = f'''<body data-res="the-mansion">
{header(True)}
<main id="top">
  <section class="hero" style="padding-top:0">
    <div class="hero-bg"><img src="{IMG(k,1600)}" srcset="{IMG(k,800)} 800w, {IMG(k,1600)} 1600w, {IMG(k,2400)} 2400w" sizes="100vw" alt="Villa Dani at Dani Hill, Genting Highlands, lit up at dusk" width="1537" height="1023" fetchpriority="high" decoding="async"></div>
    <div class="wrap hero-mark">
      <h1 class="hero-line">Accel Collection · Hosted Private Residences</h1>
    </div>
  </section>

  <div class="wrap bookbar-shell">
    <form class="bookbar" id="quickbar" aria-label="Check availability">
      <div class="field"><label for="qb-res">Residence</label><select id="qb-res"></select></div>
      <div class="field"><label for="qb-in">Arrive</label><input type="date" id="qb-in" required></div>
      <div class="field"><label for="qb-out">Depart</label><input type="date" id="qb-out" required></div>
      <div class="field"><label for="qb-guests">Guests</label><select id="qb-guests"></select></div>
      <button class="btn btn-gold" type="submit">Check availability</button>
    </form>
    <div class="bookbar-note"><span>Each stay is confirmed personally by the residence host.</span><a href="#reserve" style="text-decoration:underline;text-underline-offset:3px">Day escapes and private events</a></div>
  </div>

  <section id="standard">
    <div class="wrap">
      <div class="intro">
        <div class="rv">
          <div class="eyebrow">The Accel Collection</div>
          <h2>A house to yourself. <em>A team quietly taking care of the details.</em></h2>
        </div>
        <div class="rv">
          <p>Every residence in the Collection is hosted. Before you arrive, the rooms are prepared, the kitchen is stocked and your host knows how your days should run.</p>
          <p>Private residences with your own host, chef and chauffeur. Work when you must. Restore in between.</p>
        </div>
      </div>
      <div class="pillars">
        <div class="pillar rv"><div class="num">01</div><h3>Personal Host</h3><p>One person who runs the residence for you, from arrival to the last coffee.</p></div>
        <div class="pillar rv"><div class="num">02</div><h3>Private Housekeeping</h3><p>Rooms kept quietly in order throughout your stay, never in the way.</p></div>
        <div class="pillar rv"><div class="num">03</div><h3>Private Chauffeur</h3><p>Door-to-door from Kuala Lumpur, so the journey becomes part of the stay.</p></div>
      </div>
    </div>
  </section>

  <section class="who" id="retreats">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">A quiet retreat</div>
          <h2>Made for the ones <em>who need the quiet.</em></h2>
        </div>
        <p>Luxury hosted residences in the Malaysian highlands, close enough to Kuala Lumpur to arrive the same afternoon.</p>
      </div>
      <div class="who-grid">
        <div class="who-card rv"><div class="num">01</div><h3>For the business traveller</h3><p>A calm base for work that needs focus. Your host looks after meals and your chauffeur handles the drive, so the day stays yours. Dani Hill is meeting-ready for teams of up to 30, with golf at Awana Genting next door.</p><a href="/the-mansion/">Plan a work retreat →</a></div>
        <div class="who-card rv"><div class="num">02</div><h3>For couples</h3><p>A retreat for two. Cool highland air, a private Chef's Table and nobody else's schedule. Arrive, switch off and let the house run around you.</p><a href="/rompin-house/">Plan a couple's retreat →</a></div>
        <div class="who-card rv"><div class="num">03</div><h3>For families and teams</h3><p>Room for everyone under one roof, with space to gather and space to be alone. Reserve both Dani Hill houses for up to 30 guests.</p><a href="?residence=dani-hill-estate#reserve" data-pick="dani-hill-estate">Plan a group stay →</a></div>
      </div>
    </div>
  </section>

  <section class="sand" id="experiences">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">Your days</div>
          <h2>Golf, recovery <em>and time well spent.</em></h2>
        </div>
        <p>Arranged by your host, around your schedule.</p>
      </div>
      <div class="who-grid">
        <div class="who-card rv"><div class="num">01</div><h3>A day of golf</h3><p>The Awana Genting golf course is at Dani Hill. Guests who love the game can spend a day on the course and be back for dinner at the house.</p><a href="/villa-dani/">Stay at Dani Hill →</a></div>
        <div class="who-card rv"><div class="num">02</div><h3>Recovery sessions</h3><p>Sessions with our highly skilled masseur, focused on recovery and rejuvenation. Book one after a round of golf, a long drive or a long week.</p><a href="#reserve">Add to your stay →</a></div>
        <div class="who-card rv"><div class="num">03</div><h3>Daily workshops</h3><p>Activity workshops hosted on request by your skilled host, for families, couples and teams who want something to do together.</p><a href="#reserve">Ask your host →</a></div>
      </div>
    </div>
  </section>

  <section class="residences" id="residences">
    <div class="wrap">
      <div class="res-head rv">
        <div>
          <div class="eyebrow">The Residences</div>
          <h2>Three houses, <em>two highlands.</em></h2>
        </div>
        <p>Two residences on the Dani Hill estate in Genting Highlands, and a 1930s colonial bungalow at Fraser's Hill.</p>
      </div>
      <div id="res-list">
{cards}
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap rv">
      <div class="eyebrow">Dani Hill · Genting Highlands</div>
      <h2>Take the whole estate. <em>Both houses, one gathering.</em></h2>
      <p>The Mansion and Villa Dani can be reserved together for up to 30 overnight guests: family celebrations, leadership retreats and team offsites, 45 minutes from Kuala Lumpur.</p>
      <div style="margin-top:34px"><a class="btn btn-line" style="color:var(--ivory)" href="?residence=dani-hill-estate#reserve" data-pick="dani-hill-estate">Reserve the estate</a></div>
    </div>
  </section>

{reserve_section("Choose a residence and your dates. Your host replies personally to confirm availability and shape the stay around your group.")}
{faq_section(HOME_FAQ)}
</main>

'''
    return head("Accel Collection | Luxury Hosted Private Residences & Quiet Retreats near KL",
                "Book a luxury hosted private residence in Genting Highlands or Fraser's Hill. The Mansion, Villa Dani and Rompin House come with a personal host, housekeeping and chauffeur. A quiet retreat for couples and business travellers.",
                SITE, k, "Villa Dani at Dani Hill, Genting Highlands, at dusk", ld, preload=k) + body + footer()

css += '.res-body h3 a:hover{color:var(--gold)}\n'

# ---------------- sitemap ----------------
def sitemap():
    urls = [(SITE, [(K['v'],'Villa Dani, Dani Hill, Genting Highlands'),(K['m'],'The Mansion, Dani Hill'),(K['r'],"Rompin House, Fraser's Hill")])] + \
           [(SITE+r['slug']+'/', [(r['k'], f"{r['name']}, {r['locality']}")]) for r in RES]
    out = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for u, imgs in urls:
        out.append(f'  <url><loc>{u}</loc><lastmod>2026-11-13</lastmod>' + ''.join(f'<image:image><image:loc>{e(IMG(k,1600))}</image:loc><image:title>{e(t)}</image:title></image:image>' for k,t in imgs) + '</url>')
    out.append('</urlset>')
    return '\n'.join(out) + '\n'

files = {
 'assets/site.css': css, 'assets/app.js': js, 'assets/logo.svg': logo_svg,
 'index.html': home_page(), 'sitemap.xml': sitemap(),
 'robots.txt': 'User-agent: *\nAllow: /\n\nSitemap: https://collections.accelgroup.asia/sitemap.xml\n',
}
for r in RES: files[f"{r['slug']}/index.html"] = res_page(r)
for f, c in files.items():
    p = os.path.join(OUT, f); os.makedirs(os.path.dirname(p), exist_ok=True); open(p,'w').write(c)
subs=re.findall(r'M[^M]*',path_d)
mark=''.join(x for x in subs if max(float(n) for n in re.findall(r'(-?\d+\.?\d*) ',x+' ')[0::2])<245)
open(OUT+'/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 254 254"><rect width="254" height="254" rx="40" fill="#1F1B17"/><svg x="14" y="14" width="226" height="226" viewBox="0 0 240 254"><path fill="#BB9A60" fill-rule="evenodd" d="{mark}"/></svg></svg>\n')
for f in sorted(files): print(f, len(files[f]))
