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
sc("""Drive across a big bridge and at some point your car goes over a row of steel teeth, locked together like the fingers of two hands. Thump, thump. Most people never look down. But those teeth are there because the bridge is moving, right now, under your wheels. Today, eleven parts of a bridge, and why each one exists, starting with those metal teeth.""",
   "finger expansion joint", "THE BRIDGE IS MOVING", cuts=8, chapter="Intro")
sc("""A bridge looks like the most solid thing a city owns. It is not. It grows and shrinks with the temperature, it bends under trucks, it sways in the wind, and the river under it is slowly trying to wash it away. Every part you are about to see exists to let the bridge move safely, or to stop something from destroying it.""",
   "bridge expansion joint", "NOTHING IS STILL")
sc("""As always, every fact comes from a named source, highway agencies, bridge engineers, and official accident reports, all listed in the description. Let's start with the teeth.""",
   "finger expansion joint", "WHY DOES THIS EXIST?")

# ---------- 1. FINGER JOINT ----------
part(1, "The metal teeth", "WHY DOES THIS BRIDGE HAVE METAL TEETH?", "Why Do Bridges Have Metal Teeth?",
     """Why do bridges have rows of metal teeth across the road? Because the bridge changes length with the weather. Steel and concrete expand when they get warm and shrink when they get cold. A steel deck a hundred meters long grows by about one point two centimeters for every ten degrees of warming. Between a winter night and a summer afternoon, a long bridge can change length by tens of centimeters.""",
     "finger expansion joint")
sc("""If the deck were fixed solidly at both ends, that movement would have nowhere to go. In summer, the deck would push against its supports with enormous force, and in winter it would pull on them. So the bridge is cut into sections with gaps, called expansion joints. The teeth, or fingers, bridge the gap, sliding in and out of each other so tires can roll over smoothly.""",
   "bridge expansion joint", "A GAP THAT BREATHES")
sc("""Look closely on a hot day and the fingers are pushed deep together. On a cold morning, they pull apart. The bridge is breathing with the seasons. Under the fingers, there is usually a trough that catches rainwater and dirt, so they do not fall onto the supports below.""",
   "finger expansion joint", "BREATHING WITH THE SEASONS")

# ---------- 2. MODULAR JOINT ----------
part(2, "The joint with many beams", "WHY DOES THIS JOINT HAVE SO MANY BEAMS?", "Why Do Big Bridges Have Joints With Many Steel Beams?",
     """Why do the biggest bridges have joints made of many steel beams side by side, instead of fingers? Because their movements are too large for teeth. On a very long bridge, the deck can move by more than a meter between extremes. A single gap that wide would swallow a motorcycle wheel. So a modular joint splits the movement into many small gaps.""",
     "modular expansion joint")
sc("""Each steel beam sits on its own supports, with rubber seals between them. A control system of springs or linkages keeps the gaps equal, so each one only opens a few centimeters. Ten small gaps can add up to a huge total movement, while each one stays narrow enough to drive over safely.""",
   "modular expansion joint", "MANY SMALL GAPS")
sc("""That rhythmic thump thump you hear when you drive onto a long bridge often comes from these joints. They take a beating from every truck, and they are among the parts of a bridge that wear out and need to be replaced most often, sometimes while traffic keeps flowing on the other lanes.""",
   "bridge expansion joint", "THUMP THUMP")

# ---------- 3. ELASTOMERIC BEARING ----------
part(3, "The rubber pads under the deck", "WHY DOES THIS BRIDGE SIT ON RUBBER?", "Why Do Bridges Sit on Rubber Pads?",
     """Why does a heavy concrete bridge sit on blocks of rubber? Because the deck must be allowed to move and tilt on top of its supports. These bearings are made of layers of rubber with thin steel plates inside. The steel stops the rubber from bulging out under the weight, so it can carry hundreds of tonnes. But the rubber can still lean sideways, letting the deck slide as it grows and shrinks.""",
     "elastomeric bearing")
sc("""The pads also let the deck rotate a little at the ends, as it bends under heavy trucks. Without them, the corners of the concrete would crack. They are simple, cheap and need almost no maintenance, which is why you can find them under thousands of highway bridges.""",
   "bridge bearing", "LETTING IT LEAN")
sc("""For bigger loads and movements, engineers use other bearings. Pot bearings hold a rubber disc inside a steel pot. Sliding bearings use plates of very slippery plastic against polished steel. Some bearings in earthquake zones are even designed to isolate the bridge, so the ground can shake while the deck moves much less.""",
   "bridge pot bearing", "ISOLATING EARTHQUAKES")

# ---------- 4. ROCKER ----------
part(4, "The old rocker bearing", "WHY DOES THIS OLD BRIDGE STAND ON ROCKERS?", "Why Do Old Bridges Stand on Rockers?",
     """Why do many old steel bridges stand on curved steel pieces that look like the bottom of a rocking chair? Because before modern rubber bearings, that was how a bridge was allowed to move. As the deck grew longer in summer, the rocker tilted one way. In winter, it tilted back. The bridge rocked gently through the seasons.""",
     "bridge rocker bearing")
sc("""Inspectors use them like a thermometer. They know which way a rocker should lean on a hot or cold day. If a rocker is tilted too far, or stuck, it means something is wrong. Dirt and rust can freeze a rocker in place, and then the bridge pushes on its supports instead of moving freely.""",
   "bridge rocker bearing", "A STEEL THERMOMETER")
sc("""Rockers can also tip over in an earthquake. In several earthquakes, decks slid off their bearings and fell. So many old bridges have been retrofitted with steel cables or blocks that tie the deck to its supports, so it can move, but not fall off.""",
   "bridge bearing", "TIED SO IT CANNOT FALL")

# ---------- 5. DRAINS ----------
part(5, "The holes in the deck", "WHY ARE THERE HOLES IN THIS BRIDGE?", "Why Do Bridges Have Holes in the Deck?",
     """Why are there small holes along the edge of a bridge deck? They are drains, and they protect the bridge from its worst enemy, water. Rain on a bridge has nowhere to soak in. If it stays on the deck, it makes the road slippery and freezes in winter. If it runs down the sides, it carries salt and dirt onto the steel and concrete below.""",
     "bridge deck drain")
sc("""Road salt is especially destructive. It soaks into the concrete and reaches the steel bars inside, which start to rust. Rust takes up more space than steel, so it cracks the concrete from the inside, and pieces fall off. Much of the damage on older bridges starts with water that drained in the wrong place.""",
   "bridge deck drain", "SALT AND RUST")
sc("""So bridge drains are carefully placed, piped away from the supports, and inspected. A blocked drain can quietly destroy a bridge over decades. On a bridge, keeping water moving is as important as holding up the weight.""",
   "bridge pier", "KEEP THE WATER MOVING")

# ---------- 6. SCOUR ----------
part(6, "The riverbed around the pier", "WHY IS THE RIVER THE BRIDGE'S ENEMY?", "Why Do Rivers Knock Down Bridges?",
     """Why is the riverbed around a bridge pier so dangerous? Because the water is digging it away. When a river flows around a pier, the water speeds up and forms swirls at the front and the sides. Those swirls lift sand and gravel and carry them off, leaving a hole around the base of the pier. This is called scour, and in a flood, it can happen fast.""",
     "bridge pier")
sc("""In April nineteen eighty seven, in New York State, the Schoharie Creek bridge on the Thruway collapsed during a flood. Scour had removed the soil under one of its piers, and the pier dropped. Cars and a truck fell into the river, and ten people were killed. Scour is one of the leading causes of bridge failure in the United States.""",
   "Schoharie Creek bridge collapse", "SCHOHARIE CREEK, 1987")
sc("""So piers are now built deeper, on piles driven far below the riverbed, and protected with heavy rock placed around them. Divers and sonar inspect the riverbed around bridges, especially after floods. The most dangerous part of a bridge may be the part you can never see.""",
   "bridge pier", "THE PART YOU NEVER SEE")

# ---------- 7. STAY CABLES ----------
part(7, "The spiral on the cables", "WHY DO THESE CABLES HAVE A SPIRAL?", "Why Do Bridge Cables Have a Spiral on Them?",
     """Why do the cables of many cable stayed bridges have a thin spiral wrapped around them? Because of rain and wind. When rain runs down a smooth cable in the wind, the water forms little rivers on its surface. Those rivers change the shape of the cable in the airflow, and the cable can start to swing, sometimes by more than a meter.""",
     "cable stayed bridge")
sc("""This is called rain wind induced vibration, and it was discovered on real bridges in the nineteen eighties. The spiral ridge, or the dimpled surface on some cables, breaks up those rivers of water so they cannot form. Dampers near the bottom of the cables also absorb any shaking that still starts.""",
   "stay cable damper", "RAIN AND WIND")
sc("""A swinging cable is not just scary to watch. Over years, the bending at the anchors can tire the steel. So a cable stayed bridge is tested in wind tunnels before it is built, and its cables are designed to stay calm in a storm.""",
   "cable stayed bridge", "CALM IN A STORM")

# ---------- 8. DRY AIR ----------
part(8, "The main cable that breathes dry air", "WHY IS DRY AIR PUMPED INTO THIS CABLE?", "Why Do Suspension Bridges Pump Dry Air Into Their Cables?",
     """Why do some suspension bridges pump dry air into their main cables? Because the cables rust from the inside. A main cable is made of thousands of thin steel wires packed together. Moisture gets trapped between them, and the wires slowly corrode where nobody can see. On some older bridges, inspectors opened the cables and found broken and rusted wires.""",
     "suspension bridge cable")
sc("""So engineers wrap the cable in an airtight cover and blow dry air through it, from machines on the towers and anchorages. The dry air pushes the moisture out and keeps the humidity low. Japan used this method on the Akashi Kaikyo Bridge, and many bridges in Europe and the United States have added it since.""",
   "Akashi Kaikyo Bridge", "BLOWING THE WATER OUT")
sc("""Replacing a main cable on a suspension bridge is almost impossible without closing the bridge for years. So it is much better to keep the original cables healthy. A few fans and dehumidifiers protect a structure worth billions.""",
   "suspension bridge cable", "CABLES YOU CANNOT REPLACE")

# ---------- 9. WIND ----------
part(9, "The shape of the deck", "WHY IS THIS BRIDGE DECK SHAPED LIKE A WING?", "Why Are Bridge Decks Shaped Like Wings?",
     """Why are the decks of modern long bridges shaped like a flat airplane wing? Because of one famous disaster. In November nineteen forty, the Tacoma Narrows Bridge in Washington State twisted itself apart in a wind of only about sixty kilometers an hour. Its deck was thin and had solid sides, and the wind made it twist more and more until it broke.""",
     "Tacoma Narrows Bridge 1940")
sc("""Nobody died except a dog left in a car, but engineers learned a huge lesson. Wind does not only push a bridge. It can make it twist and oscillate. Since then, long bridges are tested as models in wind tunnels, and many have streamlined box decks that let the air slide past smoothly.""",
   "suspension bridge", "THE WIND TUNNEL")
sc("""Some bridges use open grids, slots in the middle of the deck, or stiff trusses to stop the twisting. The Tacoma Narrows collapse was filmed, and that film is still shown to engineering students around the world. A bridge does not just have to be strong. It has to be calm.""",
   "suspension bridge", "STRONG IS NOT ENOUGH")

# ---------- 10. ICE ----------
part(10, "The bridge that freezes first", "WHY DOES THE BRIDGE FREEZE FIRST?", "Why Do Bridges Freeze Before the Road?",
     """Why do bridges freeze before the road around them? Because a bridge has air on both sides. A normal road sits on the ground, which stores heat from the day and keeps the surface a little warmer at night. A bridge deck has cold air above it and cold air below it, so it loses heat from both sides and cools down much faster.""",
     "bridge ices before road")
sc("""That is why you see signs warning that the bridge ices before the road. A driver can come off a wet but safe road onto a bridge covered in thin, invisible ice. Some bridges even have sensors and automatic sprayers that spread anti icing liquid on the deck when the temperature drops.""",
   "bridge ices before road", "INVISIBLE ICE")
sc("""It is a simple bit of physics with deadly results. Every winter, accidents happen on bridges while the roads nearby are fine. If you remember one thing from this video, let it be this one. Slow down on bridges in the cold.""",
   "bridge", "SLOW DOWN IN THE COLD")

# ---------- 11. PAINT ----------
part(11, "The paint that never ends", "WHY IS THIS BRIDGE ALWAYS BEING PAINTED?", "Why Is This Bridge Always Being Painted?",
     """Why does it seem that some steel bridges are always being painted? Because paint is the main armor of a steel bridge against rust. On Scotland's Forth Bridge, painting the bridge became a famous saying for a job that never ends, because by the time the painters reached one end, the other end needed painting again.""",
     "Forth Bridge")
sc("""In two thousand eleven, the Forth Bridge got a new kind of coating, a system first developed for offshore oil platforms, expected to last at least twenty five years. The painters removed the old layers down to bare steel and applied new ones in a big project that lasted about ten years.""",
   "Forth Bridge", "25 YEARS OF PROTECTION")
sc("""Every steel bridge has a maintenance plan like this. Inspectors climb, hang from ropes, or use drones to check every joint, bolt and weld. A bridge is not built once. It is kept alive, year after year, by people most drivers never notice.""",
   "bridge inspection", "KEPT ALIVE")

# ---------- VERDICT ----------
sc("""So here are the eleven. Metal teeth that let the bridge breathe, and joints with many beams for the biggest movements. Rubber pads and old rockers, holes in the deck to drain the water, and a riverbed that tries to wash the piers away. Spiral cables against rain and wind, dry air inside the main cables, a deck shaped like a wing, a surface that freezes first, and paint that never ends.""",
   "bridge", "11 PARTS. 1 MOVING BRIDGE.", chapter="The verdict", cuts=6)
sc("""Next time you feel that thump thump on a bridge, look down. The bridge is moving, exactly as it was designed to. If you want more machines and structures explained part by part, subscribe to Machine Reverse. And tell us in the comments what you want us to take apart next.""",
   "bridge expansion joint", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video55", "title": "Why Do Bridges Have Metal Teeth?",
           "length_scale": 1.6, "scenes": S}, open("videos/video55/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
