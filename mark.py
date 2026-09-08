CHAR="#2A2B2E"; RUST="#C9512A"; BONE="#F2EDE4"
def mirror(pts):
    return " ".join(f"{100-float(p.split(',')[0]):g},{p.split(',')[1]}" for p in pts.split())
LWING = "44,24 4,5 2,11 9,31 15,50 20,39 27,52 32,42 40,56 44,58"
BODY  = "50,12 56,24 57,58 50,64 43,58 44,24"
TAIL  = "44,56 56,56 66,82 50,78 34,82"
BAND  = "34.4,82 50,78 65.6,82 68,91 50,86 32,91"
def mark(fill=CHAR, accent=RUST, x=0, y=0, s=1.0, mono=False):
    acc = fill if mono else accent
    g = f'<g transform="translate({x},{y}) scale({s})">'
    for p in (LWING, mirror(LWING), BODY, TAIL):
        g += f'<polygon points="{p}" fill="{fill}"/>'
    g += f'<polygon points="{BAND}" fill="{acc}"/></g>'
    return g
if __name__=="__main__":
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="400" height="400"><rect width="100" height="100" fill="{BONE}"/>{mark()}</svg>'
    open("mark_test.svg","w").write(svg)
    import cairosvg; cairosvg.svg2png(bytestring=svg.encode(), write_to="mark_test.png")
