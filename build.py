import os, math, cairosvg
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from PIL import Image
from mark import mark, CHAR, RUST, BONE

OUT="/home/claude/kit/out"
for d in ("logo/svg","logo/png","icons/svg","icons/png","banners","preview"):
    os.makedirs(f"{OUT}/{d}", exist_ok=True)
FONTS="/mnt/skills/examples/canvas-design/canvas-fonts/"
SLATE="#5C5F66"; ASH="#A9ABB0"; INK="#151618"

# ---------- text -> paths ----------
_fc={}
def font(name):
    if name not in _fc: _fc[name]=TTFont(FONTS+name)
    return _fc[name]
def text_path(txt, fname, size, x, y, fill, tracking=0.0, anchor="start"):
    f=font(fname); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    sc=size/upm; parts=[]; adv=0
    glyphs=[cmap.get(ord(c),'.notdef') for c in txt]
    width=sum(gs[g].width for g in glyphs)*sc + tracking*size*(len(txt)-1)
    x0 = x if anchor=="start" else (x-width/2 if anchor=="middle" else x-width)
    for c,g in zip(txt,glyphs):
        pen=SVGPathPen(gs); gs[g].draw(pen); d=pen.getCommands()
        if d and c!=' ':
            parts.append(f'<path transform="translate({x0+adv:.2f},{y:.2f}) scale({sc:.5f},{-sc:.5f})" d="{d}" fill="{fill}"/>')
        adv += gs[g].width*sc + tracking*size
    return "".join(parts), width
TEK="Tektur-Medium.ttf"; MONO="GeistMono-Regular.ttf"

def svg(w,h,body,bg=None):
    r=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{r}{body}</svg>'
def save(name,s,png_scale=None,png_name=None):
    p=f"{OUT}/{name}"; open(p,"w").write(s)
    if png_scale:
        cairosvg.svg2png(bytestring=s.encode(), write_to=png_name or p.replace("/svg/","/png/").replace(".svg",".png"), scale=png_scale)

# ---------- wordmark ----------
def wordmark(x,y,size,fill,accent,anchor="start"):
    # "KESTREL" heavy, "LABS" spaced, accent dot between
    a,w1=text_path("KESTREL",TEK,size,x,y,fill,0.06,anchor)
    return a,w1
def lockup_h(fill,accent,bg=None,h=160):
    pad=24; ms=1.12
    m=mark(fill,accent,x=pad,y=(h-100*ms)/2,s=ms, mono=(accent==fill))
    tx=pad+100*ms+30
    t1,w1=text_path("KESTREL",TEK,62,tx,h/2+22,fill,0.05)
    t2,w2=text_path("LABS",TEK,62,tx+w1+16,h/2+22,accent,0.05)
    w=round(tx+w1+16+w2+pad)
    return svg(w,h,m+t1+t2,bg)
def lockup_s(fill,accent,bg=None,w=360,h=360):
    m=mark(fill,accent,x=100,y=30,s=1.6, mono=(accent==fill))
    t1,w1=text_path("KESTREL",TEK,44,180,262,fill,0.06,"middle")
    t2,w2=text_path("LABS",MONO,22,180,306,accent,0.42,"middle")
    return svg(w,h,m+t1+t2,bg)

# mark variants
for nm,fill,acc,bg in [("kestrel-mark",CHAR,RUST,None),("kestrel-mark-reversed",BONE,RUST,None),
                       ("kestrel-mark-rust",RUST,RUST,None),("kestrel-mark-mono-black","#000000","#000000",None),
                       ("kestrel-mark-mono-white","#FFFFFF","#FFFFFF",None)]:
    save(f"logo/svg/{nm}.svg", svg(100,100,mark(fill,acc,mono=(fill==acc)),bg), png_scale=8)
save("logo/svg/kestrel-mark-on-charcoal.svg", svg(120,120,mark(BONE,RUST,10,10),CHAR), png_scale=6)
save("logo/svg/kestrel-mark-on-bone.svg",     svg(120,120,mark(CHAR,RUST,10,10),BONE), png_scale=6)
# lockups
save("logo/svg/kestrel-labs-horizontal.svg",          lockup_h(CHAR,RUST), png_scale=4)
save("logo/svg/kestrel-labs-horizontal-reversed.svg", lockup_h(BONE,RUST), png_scale=4)
save("logo/svg/kestrel-labs-horizontal-mono.svg",     lockup_h(CHAR,CHAR), png_scale=4)
save("logo/svg/kestrel-labs-horizontal-on-charcoal.svg", lockup_h(BONE,RUST,CHAR), png_scale=4)
save("logo/svg/kestrel-labs-stacked.svg",             lockup_s(CHAR,RUST), png_scale=4)
save("logo/svg/kestrel-labs-stacked-reversed.svg",    lockup_s(BONE,RUST), png_scale=4)
save("logo/svg/kestrel-labs-stacked-on-charcoal.svg", lockup_s(BONE,RUST,CHAR), png_scale=4)

# ---------- icons ----------
def tile(bg,fill,acc,r=22,size=100):
    return (f'<rect width="{size}" height="{size}" rx="{r}" fill="{bg}"/>' + mark(fill,acc,x=15,y=15,s=0.70, mono=(fill==acc)))
icon_charcoal = svg(100,100,tile(CHAR,BONE,RUST))
icon_rust     = svg(100,100,tile(RUST,BONE,CHAR))
icon_bone     = svg(100,100,tile(BONE,CHAR,RUST))
save("icons/svg/app-icon.svg",icon_charcoal); save("icons/svg/app-icon-rust.svg",icon_rust); save("icons/svg/app-icon-light.svg",icon_bone)
# symbolic (Linux panel/tray) — single-colour, tiny-size friendly: no band detail
save("icons/svg/kestrel-symbolic.svg", svg(16,16,mark("#000000","#000000",x=0.5,y=0.5,s=0.15,mono=True)))
sizes=[16,22,24,32,48,64,128,256,512,1024]
for s in sizes:
    cairosvg.svg2png(bytestring=icon_charcoal.encode(), write_to=f"{OUT}/icons/png/app-icon-{s}.png", output_width=s, output_height=s)
# favicon.ico bundle
ims=[Image.open(f"{OUT}/icons/png/app-icon-{s}.png") for s in (16,32,48)]
ims[0].save(f"{OUT}/icons/favicon.ico", sizes=[(16,16),(32,32),(48,48)], append_images=ims[1:])
os.system(f"cp {OUT}/icons/svg/app-icon.svg {OUT}/icons/favicon.svg")

# ---------- banners ----------
def grid(w,h,step=40,color="#3A3C40",op=0.5):
    g=[f'<g stroke="{color}" stroke-opacity="{op}" stroke-width="1">']
    for x in range(0,w+1,step): g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
    for y in range(0,h+1,step): g.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
    return "".join(g)+"</g>"
def hover_field(w,h,cx,cy,acc=RUST):
    # concentric hairline rings — a "hovering" thermal/wind-field motif
    r=[]; 
    for i in range(1,14):
        rad=i*46
        r.append(f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="{acc}" stroke-opacity="{max(0.02,0.16-i*0.011):.3f}" stroke-width="1"/>')
    return "".join(r)
def banner(w,h,name,tagline=True,url=True):
    b=[grid(w,h,step=48)]
    # ghost mark: large, low-contrast, bleeding off the right/bottom edge
    gs=h*0.0125
    # left content block
    pad=w*0.075
    ms=h*0.0032
    _,wk=text_path("KESTREL",TEK,1,0,0,BONE,0.05); _,wl=text_path("LABS",TEK,1,0,0,BONE,0.05)
    avail=w-pad-(pad+100*ms+h*0.09)
    fs=min(h*0.165, avail/(wk+wl+0.28))
    tx=pad+100*ms+h*0.09
    cy=h*0.47 if tagline else h*0.5
    b.append(hover_field(w,h,pad+50*ms,cy))
    b.append(mark(BONE,RUST,x=pad,y=cy-50*ms,s=ms))
    t1,w1=text_path("KESTREL",TEK,fs,tx,cy+fs*0.36,BONE,0.05)
    t2,_ =text_path("LABS",TEK,fs,tx+w1+fs*0.28,cy+fs*0.36,RUST,0.05)
    b+=[t1,t2]
    if tagline:
        tg,_=text_path("OPEN SOURCE TOOLS FOR LINUX",MONO,fs*0.26,tx,cy+fs*0.36+fs*0.62,ASH,0.26)
        b.append(tg)
    if url:
        u,uw=text_path("kestrellabs.org",MONO,h*0.042,w-pad,h-h*0.10,ASH,0.05,"end")
        b.append(u)
        b.append(f'<rect x="{pad}" y="{h-h*0.10-h*0.015}" width="{h*0.15}" height="{h*0.012}" fill="{RUST}"/>')
    s=svg(w,h,"".join(b),CHAR)
    open(f"{OUT}/banners/{name}.svg","w").write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=f"{OUT}/banners/{name}.png")
banner(1280,640,"github-social-preview-1280x640")
banner(1200,300,"readme-banner-1200x300")
banner(1500,500,"social-header-1500x500")
banner(1920,600,"website-hero-1920x600")
print("built")
