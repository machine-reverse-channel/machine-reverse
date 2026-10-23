import json
S = []


def sc(text, query, caption, **kw):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption, **kw})


def part(n, name, question, short, text, query, file=None, arrow=True, local=None):
    """The "Why does this exist?" scene. It must work alone as a Short: question, answer, punchline.
    file = exact Commons photo of the part, arrow = {"x", "y"} position of the part in the 16:9 frame."""
    extra = {"arrow": arrow, "chapter": f"{n}. {name}", "short": short, "cuts": 3}
    if file:
        extra["file"] = file
    if local:
        extra["local"] = local
    sc(text, query, question, **extra)
# ---------- HOOK ----------
sc("""Most people imagine an icebreaker smashing through ice like a hammer, or cutting it like a knife. It does neither. An icebreaker drives up onto the ice, and then crushes it with its own weight, again and again, thousands of times a day. Today, ten parts of an icebreaker, and why each one exists.""",
   "icebreaker", "IT CLIMBS ON THE ICE", cuts=8, chapter="Intro")
sc("""Sea ice can be more than a metre thick, and it can trap a normal ship for weeks, or even crush its hull. In places like the Arctic and the Baltic Sea, icebreakers keep ports and shipping lanes open through the winter. They are some of the toughest ships ever built, and almost every part of them is designed for ice.""",
   "icebreaker Arctic", "THE TOUGHEST SHIPS")
sc("""As always, every fact here comes from a named source, ice class rules, shipbuilders and naval references, all listed in the description. Let's start with the bow.""",
   "icebreaker bow", "WHY DOES THIS EXIST?")

# ---------- 1. SLOPED BOW ----------
part(1, "The sloped bow", "WHY IS THIS BOW SO SLOPED?", "Why Do Icebreakers Climb On Top of the Ice?",
     """Why does an icebreaker have a long, sloped bow, like a spoon? So it can climb on top of the ice. A normal ship's bow is steep, and it would hit thick ice head on and stop. An icebreaker's bow is shallow and angled, so when it meets the ice, the ship slides up onto it.""",
     "icebreaker bow")
sc("""Once the bow is on top, the weight of thousands of tonnes of ship presses down. Ice is strong when you push it from the side, but weak when you bend it from above. The ice sheet cracks under the weight, and the broken pieces are pushed down and aside, under the hull.""",
   "icebreaker breaking ice", "BENDING, NOT CUTTING")
sc("""If the ice is too thick to break in one go, the icebreaker backs up and rams it, sliding further up each time. This is called ramming, and it can take many attempts to get through a ridge of piled up ice. It is slow, noisy and violent work, but it opens a path for other ships.""",
   "icebreaker ramming", "BACK UP AND RAM")

# ---------- 2. ICE BELT ----------
part(2, "The ice belt", "WHY IS THE HULL THICKER HERE?", "Why Is an Icebreaker's Hull Thicker at the Waterline?",
     """Why is the hull of an icebreaker much thicker in a band around the waterline? That band is called the ice belt. It is the part of the hull that hits the ice, scrapes along it and gets squeezed by it. On a large icebreaker, the steel there can be several centimetres thick, much thicker than on a normal ship.""",
     "icebreaker hull")
sc("""Inside, the ice belt is also supported by extra frames placed close together, like the ribs of a strong animal. Ice does not push evenly. It hits in sharp, concentrated points, which can dent normal steel. The thick plates and dense frames spread those forces out.""",
   "ship hull frames", "CLOSE TOGETHER LIKE RIBS")
sc("""The steel itself is special. Normal steel becomes brittle in extreme cold, and can crack like glass. Icebreakers use steel that stays tough at very low temperatures, often far below minus thirty degrees. In the Arctic, even the choice of metal is a matter of survival.""",
   "Arctic ship ice", "STEEL THAT STAYS TOUGH")

# ---------- 3. ROUND HULL ----------
part(3, "The round hull", "WHY IS THIS HULL SO ROUNDED?", "Why Are Icebreaker Hulls So Rounded?",
     """Why are icebreaker hulls rounded at the sides, instead of straight? So that ice pushes the ship up, instead of crushing it. When floating ice is pressed together by wind and currents, it can close in on a ship from both sides. A straight sided hull takes the full squeeze, like a nut in a nutcracker.""",
     "icebreaker hull shape")
sc("""A rounded hull turns that sideways squeeze partly into an upward push. The ice slides down along the curve and lifts the ship, instead of crushing it. The famous polar ship Fram, built for the explorer Fridtjof Nansen in the eighteen nineties, used this idea. It was frozen into the Arctic ice on purpose and survived.""",
   "Fram ship", "LIFTED, NOT CRUSHED")
sc("""Many ships trapped in ice in the past, with straight sides, were crushed and sank. The rounded shape makes the ship roll more in open water, which is uncomfortable for the crew. But in the ice, comfort is less important than survival.""",
   "ship trapped in ice", "SURVIVAL FIRST")

# ---------- 4. HEELING TANKS ----------
part(4, "The heeling tanks", "WHY DOES THIS SHIP ROCK ITSELF?", "Why Do Icebreakers Rock Themselves From Side to Side?",
     """Why does an icebreaker rock itself from side to side on purpose? To avoid getting stuck. Ice can grip the sides of a ship with huge friction. Large tanks on both sides of the hull pump water quickly from one side to the other, making the ship roll a few degrees back and forth.""",
     "icebreaker heeling system")
sc("""That rolling motion breaks the grip of the ice on the hull, like wiggling a stuck key in a lock. It also helps the ship turn in thick ice and break free when it is pinned. Some icebreakers can also pump water forward and backward to tilt the bow up or down.""",
   "icebreaker in ice", "WIGGLING A STUCK KEY")
sc("""The heeling system is powerful. Hundreds of tonnes of water can be moved in under a minute. Finnish icebreaker designers were among the pioneers of the idea, because the Baltic Sea freezes every winter, and keeping its ports open is vital for the country's trade.""",
   "Finnish icebreaker", "BORN IN THE BALTIC")

# ---------- 5. AIR BUBBLES ----------
part(5, "The air bubbling system", "WHY DOES THIS SHIP BLOW BUBBLES?", "Why Do Some Icebreakers Blow Bubbles?",
     """Why do some icebreakers blow air bubbles out of their hull? To reduce friction. Holes along the lower hull release a stream of compressed air. The bubbles rise along the sides of the ship, carrying water with them, and form a slippery layer between the hull and the ice.""",
     "icebreaker air bubbling system")
sc("""Ice and snow piled against a hull can act like glue, especially wet snow on top of ice. The bubbling water washes it away and makes the ice slide more easily. The ship needs less power to move, and is less likely to get stuck in heavy ice.""",
   "ship in snow ice", "A SLIPPERY LAYER")
sc("""Some icebreakers use a very smooth, hard coating on the hull instead, which also reduces friction and protects the steel. Both ideas aim at the same problem. Breaking the ice is only half the battle. The other half is sliding through the broken pieces without being held back.""",
   "icebreaker hull coating", "SLIDING THROUGH")

# ---------- 6. DIESEL ELECTRIC ----------
part(6, "The electric drive", "WHY DO ICEBREAKERS USE ELECTRIC MOTORS?", "Why Do Icebreakers Use Electric Motors?",
     """Why do most icebreakers turn their propellers with electric motors? Because the propellers keep hitting ice. A block of ice can suddenly jam a propeller and almost stop it. A diesel engine connected directly to the propeller could stall or be damaged by that shock.""",
     "icebreaker propeller")
sc("""In a diesel electric icebreaker, the diesel engines run generators, and the generators power electric motors that turn the propellers. An electric motor can produce full force even at very low speed, so when ice slows the propeller, the motor keeps pushing hard and chews through it.""",
   "diesel-electric ship", "FULL FORCE AT LOW SPEED")
sc("""The propellers themselves are made of very strong steel, with thick blades, and they are often designed so a damaged blade can be replaced. Some icebreakers have propellers at the bow too, to wash broken ice away from the hull. Every part of the drive is built to survive ice.""",
   "icebreaker propeller dry dock", "BUILT TO SURVIVE ICE")

# ---------- 7. NUCLEAR ----------
part(7, "The nuclear reactor", "WHY DOES THIS ICEBREAKER HAVE A REACTOR?", "Why Does Russia Have Nuclear Icebreakers?",
     """Why does Russia operate icebreakers powered by nuclear reactors? Because of distance and power. The Arctic route along the north of Russia is very long, far from ports where a ship could refuel. Breaking thick ice also needs enormous power for long periods.""",
     "nuclear icebreaker")
sc("""A nuclear reactor provides that power without refuelling for years. The Soviet Union launched the Lenin in nineteen fifty-seven, the world's first nuclear powered surface ship. In nineteen seventy-seven, the nuclear icebreaker Arktika became the first surface ship to reach the North Pole.""",
   "icebreaker Arktika", "FIRST TO THE NORTH POLE")
sc("""Russia still builds new nuclear icebreakers, among the most powerful ever made, to keep the Northern Sea Route open. Nuclear power is expensive and complex, and only makes sense for the toughest jobs. In the Arctic, where the ice never stops and fuel is far away, it is the toughest job of all.""",
   "Russian nuclear icebreaker", "THE TOUGHEST JOB")

# ---------- 8. DOUBLE ACTING ----------
part(8, "The backward ship", "WHY DOES THIS SHIP SAIL BACKWARDS?", "Why Do Some Ships Sail Backwards Through Ice?",
     """Why do some ships sail backwards through ice on purpose? They are called double acting ships. The bow is shaped for open water, so the ship is efficient in normal seas. The stern is shaped like an icebreaker, and it has rotating propeller pods that can break and mill the ice.""",
     "double acting ship")
sc("""In heavy ice, the ship turns around and goes stern first. The propellers chew up the ice in front of them and wash it away along the hull, which turns out to be very effective, especially in thick, packed ice. In open water, the ship turns around again and sails normally.""",
   "ship in ice stern first", "STERN FIRST")
sc("""This idea was developed in Finland, and it allowed some cargo ships and tankers to sail in ice without needing an icebreaker escort. It is a perfect example of engineering thinking. When one end of the ship cannot be good at two jobs, give each end a different job.""",
   "Arctic tanker", "EACH END HAS A JOB")

# ---------- 9. TOWING NOTCH ----------
part(9, "The towing notch", "WHY IS THERE A NOTCH IN THE BACK?", "Why Do Icebreakers Have a Notch in the Stern?",
     """Why do some icebreakers have a curved notch cut into the back of the hull? It is a towing notch. When a cargo ship gets stuck in heavy ice, the icebreaker can pull it very close, until the cargo ship's bow sits right inside the notch.""",
     "icebreaker towing notch")
sc("""Then the two ships move together as one. The icebreaker breaks the ice, and the cargo ship pushes from behind, with no gap where the ice could close in between them. In thick ice, a channel can freeze shut quickly, so keeping the ships tightly together is essential.""",
   "icebreaker escort ship", "MOVING AS ONE")
sc("""The notch is padded with heavy rubber fenders to protect both ships. It is a simple solution that looks strange in a photo, like a bite taken out of the stern. But in the Arctic, it can be the difference between a cargo ship reaching port and spending the winter trapped.""",
   "icebreaker stern", "A BITE IN THE STERN")

# ---------- 10. OBLIQUE ----------
part(10, "The sideways icebreaker", "WHY DOES THIS ICEBREAKER GO SIDEWAYS?", "Why Does This Icebreaker Sail Sideways?",
     """Why does one icebreaker sail sideways through the ice? It is the Baltika, an oblique icebreaker built for Russia. Its hull is asymmetric, not the same on both sides. It can move forward or backward like a normal icebreaker, but it can also move at an angle, pushing its long side against the ice.""",
     "oblique icebreaker Baltika")
sc("""Moving sideways, the small ship opens a channel much wider than itself, wide enough for a big tanker to follow. Normally, that would need a much larger icebreaker. Its propeller pods can rotate in any direction, letting it slide diagonally through the ice.""",
   "Baltika icebreaker", "A WIDER CHANNEL")
sc("""It was designed by Finnish engineers and entered service in the twenty tens. It shows that, even after more than a century of icebreakers, there are still new ways to break ice. Sometimes the best way forward is to go sideways.""",
   "icebreaker channel", "SOMETIMES, GO SIDEWAYS")

# ---------- VERDICT ----------
sc("""So here are the ten. A sloped bow that climbs onto the ice. A thick ice belt with ribs close together. A rounded hull that gets lifted, not crushed. Tanks that rock the ship free. Bubbles that make the ice slippery. Electric motors that chew through ice. Reactors for the longest routes. Ships that sail backwards on purpose. A notch for close towing. And an icebreaker that goes sideways.""",
   "icebreaker", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""An icebreaker does not fight the ice with sharpness, but with weight, shape and patience. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments, would you sail through the Arctic on an icebreaker?""",
   "icebreaker night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Icebreaker Stephan Jantzen in Stadthafen Rostock 2010-12-28.jpg', 0.17, 0.58),
    2: ('File:Aurora Australis drydock Woolloomooloo.jpg', 0.45, 0.68),
    3: ('File:USCGC Polar Star (WAGB 10) stern.jpg', 0.5, 0.4),
    4: ('File:Finnish icebreaker Polaris (24 March 2017).jpg', 0.5, 0.65),
    5: ('File:Ship, ice breaking, winter, river, shore Fortepan 75138.jpg', 0.5, 0.55),
    6: ('File:Jääkarhu propellers by P Smit.jpg', 0.5, 0.5),
    7: ('File:Russian Nuclear Icebreaker Arktika.jpg', 0.6, 0.45),
    8: ('File:Polaris bollardpull 2016-04-26.jpg', 0.65, 0.6),
    9: ('File:Icebreaker SHIRASE - しらせ- the stern of shirase.jpg', 0.5, 0.6),
    10: ('File:Oblique icebreaker Baltika (29 March 2015).jpg', 0.55, 0.63),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video40", "title": "Why Do Icebreakers Climb On Top of the Ice?",
           "length_scale": 1.6, "scenes": S}, open("videos/video40/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
