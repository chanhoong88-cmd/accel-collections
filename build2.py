import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, 'build.py')
s = open(p).read()
R = [
 ('Raised herb beds with labelled lemongrass, mint and other tea herbs at Rompin House', 'Raised herb beds labelled basil, rosemary, thyme, sage, oregano, dill and parsley in the Rompin House garden'),
 ('("tea-garden","Journaling & drawing"', '("journaling","Journaling & drawing"'),
 ('A quiet workshop in the garden with notebooks, pencils and watercolours. No experience needed, just time to look closely.', 'A quiet workshop with notebooks, fine-liner pens and pressed leaves and flowers from the garden. No experience needed, just time to look closely.'),
 ('Glass jars of dried flower tea beside a teapot, set out for an afternoon in the garden', 'Open journal with handwriting, sketches, pressed ferns and flowers, beside fine-liner pens and a cup of coffee'),
 ('.exp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(18px,2.4vw,32px);margin-top:clamp(28px,4vw,48px)}',
  '.exp-sec .wrap{max-width:860px}.exp-grid{display:grid;grid-template-columns:repeat(3,minmax(0,240px));justify-content:center;column-gap:clamp(16px,3vw,40px);row-gap:clamp(28px,3.5vw,44px);margin-top:clamp(28px,4vw,44px)}'),
 ('.exp-n{position:absolute;left:16px;bottom:12px;z-index:1;font-family:var(--serif);font-size:30px', '.exp-n{position:absolute;left:12px;bottom:8px;z-index:1;font-family:var(--serif);font-size:22px'),
 ('.exp figcaption{padding:18px 2px 0}', '.exp figcaption{padding:14px 2px 0}'),
 ('font-size:clamp(22px,2vw,26px);line-height:1.2;margin:0 0 8px}', 'font-size:20px;line-height:1.2;margin:0 0 6px}'),
 ('.exp p{color:rgba(246,241,232,.78);font-size:15px;margin:0}', '.exp p{color:rgba(246,241,232,.78);font-size:13.5px;line-height:1.6;margin:0}.exp figcaption .eyebrow{font-size:10px}'),
 ('@media (max-width:1020px){.exp-grid{grid-template-columns:1fr 1fr}}', '@media (max-width:720px){.exp-grid{grid-template-columns:repeat(2,minmax(0,240px))}}'),
 ('@media (max-width:560px){.exp-grid{grid-template-columns:1fr}.exp-img{aspect-ratio:5/4}}', '@media (max-width:560px){.exp-grid{column-gap:14px}.exp h3{font-size:18px}}'),
]
for a, b in R:
    assert a in s, a
    s = s.replace(a, b)
import re
s = re.sub(r"(\\n|\n)V = '\d+'", lambda m: m.group(1) + "V = '5'", s, count=1)
b = os.path.join(HERE, 'build_base.py')
bs = open(b).read()
bs2 = re.sub(r"^V = '\d+'", "V = '5'", bs, count=1, flags=re.M)
assert bs2 != bs, 'V not found'
open(b, 'w').write(bs2)
exec(compile(s, p, 'exec'), {'__file__': p, '__name__': '__main__'})
