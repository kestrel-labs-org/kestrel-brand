import cairosvg
from build import text_path, mark, svg, TEK, MONO, CHAR, RUST, BONE, ASH, SLATE, INK, OUT, lockup_h, lockup_s
W,H=1600,1000
b=[]
b.append(f'<rect width="{W}" height="{H}" fill="{BONE}"/>')
b.append(f'<rect x="0" y="0" width="{W}" height="520" fill="{CHAR}"/>')
b.append(mark(BONE,RUST,x=110,y=110,s=2.8))
t,w1=text_path("KESTREL",TEK,120,470,300,BONE,0.05); b.append(t)
t,_=text_path("LABS",TEK,120,470+w1+34,300,RUST,0.05); b.append(t)
t,_=text_path("OPEN SOURCE TOOLS FOR LINUX  ·  kestrellabs.org",MONO,26,470,362,ASH,0.2); b.append(t)
t,_=text_path("BRAND KIT  v1.0  ·  2026",MONO,20,W-90,470,ASH,0.15,"end"); b.append(t)
# palette
sw=[("CHARCOAL",CHAR,"#2A2B2E"),("RUST",RUST,"#C9512A"),("BONE",BONE,"#F2EDE4"),("SLATE",SLATE,"#5C5F66"),("ASH",ASH,"#A9ABB0"),("INK",INK,"#151618")]
x=110
for n,c,hx in sw:
    stroke = f' stroke="{ASH}" stroke-width="1"' if c==BONE else ''
    b.append(f'<rect x="{x}" y="590" width="180" height="120" fill="{c}"{stroke}/>')
    t,_=text_path(n,TEK,20,x,745,CHAR,0.08); b.append(t)
    t,_=text_path(hx,MONO,17,x,772,SLATE,0.05); b.append(t)
    x+=215
# small lockups row
b.append(f'<rect x="110" y="830" width="560" height="120" fill="{CHAR}"/>')
b.append(mark(BONE,RUST,x=140,y=840,s=1.0))
t,w1=text_path("KESTREL",TEK,52,270,908,BONE,0.05); b.append(t); t,_=text_path("LABS",TEK,52,270+w1+14,908,RUST,0.05); b.append(t)
b.append(mark(CHAR,RUST,x=720,y=840,s=1.0))
t,w1=text_path("KESTREL",TEK,52,850,908,CHAR,0.05); b.append(t); t,_=text_path("LABS",TEK,52,850+w1+14,908,RUST,0.05); b.append(t)
# icon tiles
for i,(bg,f,a) in enumerate([(CHAR,BONE,RUST),(RUST,BONE,CHAR),(BONE,CHAR,RUST)]):
    x=1320+i*80
    b.append(f'<rect x="{x}" y="850" width="64" height="64" rx="14" fill="{bg}" stroke="{ASH if bg==BONE else bg}"/>')
    b.append(mark(f,a,x=x+10,y=860,s=0.44,mono=(f==a)))
t,_=text_path("Tektur  ·  Geist Mono",MONO,17,1320,935,SLATE,0.05); b.append(t)
s=svg(W,H,"".join(b))
open(f"{OUT}/preview/brand-sheet.svg","w").write(s)
cairosvg.svg2png(bytestring=s.encode(), write_to=f"{OUT}/preview/brand-sheet.png")
