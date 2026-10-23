import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F="/usr/share/fonts/opentype/inter/"
BG=(10,14,22); GRID=(22,34,52); GRID2=(30,48,74); LINE=(120,160,205); WHITE=(240,244,250); ORANGE=(255,122,0); MUTED=(140,155,175)

def grid(d,w,h,s,step):
    for x in range(0,w,step*s): d.line([(x,0),(x,h)],fill=GRID,width=max(1,s))
    for y in range(0,h,step*s): d.line([(0,y),(w,y)],fill=GRID,width=max(1,s))
    for x in range(0,w,step*5*s): d.line([(x,0),(x,h)],fill=GRID2,width=2*s)
    for y in range(0,h,step*5*s): d.line([(0,y),(w,y)],fill=GRID2,width=2*s)

def gear_pts(cx,cy,r_out,r_in,teeth,rot=0):
    pts=[]; per=2*math.pi/teeth
    for t in range(teeth):
        a=rot+t*per
        for frac,r in [(0.0,r_in),(0.12,r_out),(0.42,r_out),(0.54,r_in)]:
            pts.append((cx+r*math.cos(a+frac*per),cy+r*math.sin(a+frac*per)))
    return pts

def gear(d,cx,cy,r,teeth,color,width,fill=None,rot=0,hole=0.38,spokes=True):
    d.polygon(gear_pts(cx,cy,r,r*0.82,teeth,rot),outline=color,fill=fill,width=width)
    hr=r*hole
    d.ellipse([cx-hr,cy-hr,cx+hr,cy+hr],outline=color,width=width,fill=BG if fill else None)
    sr=r*0.6
    d.ellipse([cx-sr,cy-sr,cx+sr,cy+sr],outline=color,width=max(1,width//2))

def arrow(d,tip,tail,color,width,head):
    (tx,ty),(sx,sy)=tip,tail
    ang=math.atan2(ty-sy,tx-sx)
    bx,by=tx-head*math.cos(ang),ty-head*math.sin(ang)
    d.line([(sx,sy),(bx,by)],fill=color,width=width)
    p=ang+math.pi/2; hw=head*0.62
    d.polygon([(tx,ty),(bx+hw*math.cos(p),by+hw*math.sin(p)),(bx-hw*math.cos(p),by-hw*math.sin(p))],fill=color)

# ---------- PROFILE 800x800 ----------
S=4; W=800*S
im=Image.new("RGB",(W,W),BG); d=ImageDraw.Draw(im)
grid(d,W,W,S,40)
cx,cy=W*0.45,W*0.57
r=W*0.29
gear(d,cx,cy,r,9,WHITE,int(W*0.03),fill=(26,34,48),rot=0.15)
# dimension ring tick to look technical
# arrow pointing at tooth upper-right
ta=-0.70
tip=(cx+(r+W*0.015)*math.cos(ta),cy+(r+W*0.015)*math.sin(ta))
arrow(d,tip,(W*0.84,W*0.16),ORANGE,int(W*0.06),W*0.17)
# "?" in hub
fq=ImageFont.truetype(F+"Inter-ExtraBold.otf",int(W*0.22))
d.text((cx,cy),"?",font=fq,fill=ORANGE,anchor="mm")
im.resize((800,800),Image.LANCZOS).save("profile-800.png")

# ---------- BANNER 2560x1440 ----------
S=2; W,H=2560*S,1440*S
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
grid(d,W,H,S,32)
# vignette-ish darker center band behind text
ov=Image.new("L",(W,H),0); od=ImageDraw.Draw(ov)
od.rectangle([W*0.2,H*0.33,W*0.8,H*0.67],fill=170)
ov=ov.filter(ImageFilter.GaussianBlur(120*S))
im=Image.composite(Image.new("RGB",(W,H),BG),im,ov); d=ImageDraw.Draw(im)
# decorative blueprint gears outside safe area (left/right)
gear(d,W*0.12,H*0.62,H*0.30,14,LINE,3*S,rot=0.1)
gear(d,W*0.12+H*0.05,H*0.62-H*0.47,H*0.17,9,LINE,3*S,rot=0.3)
gear(d,W*0.90,H*0.40,H*0.26,12,LINE,3*S,rot=0.2)
gear(d,W*0.90-H*0.02,H*0.40+H*0.43,H*0.14,8,LINE,3*S,rot=0.0)
# center lines / crosshair on gears
for gx,gy,gr in [(W*0.12,H*0.62,H*0.30),(W*0.90,H*0.40,H*0.26)]:
    d.line([(gx-gr*1.25,gy),(gx+gr*1.25,gy)],fill=LINE,width=S)
    d.line([(gx,gy-gr*1.25),(gx,gy+gr*1.25)],fill=LINE,width=S)
# safe area center
cx,cy=W/2,H/2
f1=ImageFont.truetype(F+"Inter-ExtraBold.otf",int(150*S))
f2=ImageFont.truetype(F+"Inter-Bold.otf",int(52*S))
f3=ImageFont.truetype(F+"Inter-Medium.otf",int(30*S))
title="MACHINE REVERSE"
d.text((cx,cy-28*S),title,font=f1,fill=WHITE,anchor="mm")
bb=d.textbbox((cx,cy-28*S),title,font=f1,anchor="mm")
# orange underline accent under REVERSE
rv=d.textbbox((0,0),"REVERSE",font=f1); rw=rv[2]-rv[0]
d.rectangle([bb[2]-rw,bb[3]+14*S,bb[2],bb[3]+24*S],fill=ORANGE)
# tagline with arrow
tag="WHY DOES THIS EXIST?"
ty=bb[3]+80*S
tb=d.textbbox((0,0),tag,font=f2); tw=tb[2]-tb[0]
aw=150*S; gap=28*S
start=cx-(tw+aw+gap)/2
arrow(d,(start+aw,ty),(start,ty),ORANGE,12*S,46*S)
d.text((start+aw+gap,ty),tag,font=f2,fill=ORANGE,anchor="lm")
# small overline above title
d.text((cx,bb[1]-50*S),"ENGINEERING  ·  HIDDEN DETAILS  ·  NEW VIDEOS WEEKLY",font=f3,fill=MUTED,anchor="mm")
im=im.resize((2560,1440),Image.LANCZOS); im.save("banner-2560x1440.png")
# preview with safe-area guides
p=im.copy(); pd=ImageDraw.Draw(p)
for (w,h,c) in [(1546,423,(0,255,0)),(2560,423,(255,0,255)),(1855,423,(0,200,255))]:
    pd.rectangle([(2560-w)/2,(1440-h)/2,(2560+w)/2,(1440+h)/2],outline=c,width=3)
p.resize((1280,720)).save("banner-preview-guides.png")
# circle preview of profile
pr=Image.open("profile-800.png").resize((240,240),Image.LANCZOS)
m=Image.new("L",(240,240),0); ImageDraw.Draw(m).ellipse([0,0,239,239],fill=255)
c=Image.new("RGB",(560,260),(255,255,255)); c.paste(pr,(10,10),m)
for i,s in enumerate([88,48,24]):
    q=pr.resize((s,s),Image.LANCZOS); mm=Image.new("L",(s,s),0); ImageDraw.Draw(mm).ellipse([0,0,s-1,s-1],fill=255)
    c.paste(q,(280+sum([88,48,24][:i])+i*20,130-s//2),mm)
c.save("profile-preview.png")
