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
sc("""Look at almost any modern wind turbine on Earth and you will count the same number of blades. Three. Not two, not four, not twenty like an old farm windmill. Three. Engineers tried everything else, one blade, two blades, many blades, and almost all of them lost. Today, eleven parts of a wind turbine, and why each one exists, starting with that magic number.""",
   "wind turbine", "WHY ALWAYS THREE?", cuts=8, chapter="Intro")
sc("""Modern wind turbines are some of the biggest machines ever built. The tallest ones reach more than two hundred meters to the tip of the blade, taller than most skyscrapers in Europe. A single blade can be longer than a football field, and one turbine can power thousands of homes.""",
   "offshore wind turbine", "LONGER THAN A FOOTBALL FIELD")
sc("""As always, every fact comes from a named source, turbine makers, energy laboratories, and engineering references, all listed in the description. Let's start with the question in the title.""",
   "wind turbine blade", "WHY DOES THIS EXIST?")

# ---------- 1. THREE BLADES ----------
part(1, "The three blades", "WHY DOES IT HAVE ONLY 3 BLADES?", "Why Do Wind Turbines Have Only 3 Blades?",
     """Why do wind turbines have three blades, and not more? Because more blades do not catch much more energy. A rotor can never take all the energy from the wind, there is a physical limit called the Betz limit, about fifty nine percent. Three slim blades spinning fast already get close to what is practical. A fourth blade would add a lot of cost and weight for only a tiny gain.""",
     "Nacelle of Wind Turbine")
sc("""So why not two, which would be even cheaper? Because two blades wobble. When the turbine turns to face the wind, a two bladed rotor is unbalanced. When its blades are vertical, it resists turning, and when they are horizontal, it does not. That flips twice every rotation, shaking the whole machine. With three blades, the forces stay smooth in every position.""",
   "two-bladed wind turbine", "TWO BLADES WOBBLE")
sc("""Two bladed turbines also have to spin faster, which makes them louder and harder on the eye. Three blades turn at a calm, steady pace that people find easier to live next to. Some designers still build two bladed turbines for special cases, like floating offshore platforms, but on land, three won the race.""",
   "wind turbine", "THREE WON THE RACE")

# ---------- 2. ROOT BOLTS ----------
part(2, "The ring of bolts at the root", "WHY ARE THERE SO MANY BOLTS HERE?", "Why Is a Wind Turbine Blade Held by a Ring of Bolts?",
     """Why is the end of a wind turbine blade covered in a ring of steel bolts? Because this is where the whole blade hangs on the turbine. Every rotation, the blade is pulled by gravity one way, then the other, and pushed by the wind. All of that force passes through this ring. Large blades are fixed with around a hundred or more bolts, each tightened to a precise force.""",
     "Shaft end of Wind turbine blades")
sc("""A blade turns maybe fifteen times a minute, which means millions of load cycles over its life. Bolts that are loose or tightened unevenly can crack from fatigue. So technicians check and re-tighten them during maintenance, often with hydraulic tools, because a human arm cannot reach that force.""",
   "wind turbine blade", "MILLIONS OF CYCLES")
sc("""When a blade does break off, the result is spectacular and dangerous. Pieces can be thrown hundreds of meters. That is why turbines are built away from houses and roads, and why the root of the blade, where the bolts sit, is one of the most carefully designed parts of the whole machine.""",
   "wind turbine blade", "THROWN HUNDREDS OF METERS")

# ---------- 3. PITCH ----------
part(3, "The hub that turns the blades", "WHY CAN THESE BLADES TWIST?", "Why Can Wind Turbine Blades Twist?",
     """Why can each wind turbine blade rotate around its own length? Because that is how the turbine controls its power. Inside the hub, motors or hydraulic cylinders turn every blade a few degrees at a time. This is called pitch. In light wind, the blades face the wind to catch as much as possible. In strong wind, they turn away to spill the extra energy.""",
     "wind turbine hub")
sc("""In a storm, the blades turn almost fully edge-on to the wind, like a feather. They stop catching wind, and the rotor slows down. That is the main brake of a modern turbine. Most turbines shut down this way when the wind goes above around twenty five meters per second, about ninety kilometers an hour.""",
   "wind turbine", "THE FEATHER BRAKE")
sc("""Because this brake is so important, each blade has its own pitch system and its own backup power, batteries or pressure tanks. If the grid fails and the turbine loses power, the blades still feather by themselves. One working blade is enough to slow the rotor down.""",
   "wind turbine hub", "BACKUP FOR EACH BLADE")

# ---------- 4. VORTEX GENERATORS ----------
part(4, "The little fins on the blade", "WHY ARE THERE LITTLE FINS ON THIS BLADE?", "Why Do Wind Turbine Blades Have Little Fins?",
     """Why do some wind turbine blades have rows of small fins near their base? They are called vortex generators. Each fin creates a tiny swirl of air, which mixes fast moving air into the thin layer right next to the blade. That keeps the airflow stuck to the surface, instead of separating from it.""",
     "wind turbine vortex generators")
sc("""Near the root, the blade is thick and turns slowly, and air tends to break away from it. When the flow separates, the blade stalls, like an airplane wing at a steep angle, and loses lift. The little fins delay that stall, so the inner part of the blade produces more power.""",
   "wind turbine blade", "DELAYING THE STALL")
sc("""The same trick is used on airplane wings, where you can sometimes see a row of tiny tabs from your window seat. On turbines, the fins can even be glued onto older blades years later, and makers report gains of a few percent in energy. For a turbine running for twenty years, that adds up.""",
   "wind turbine blade", "A FEW PERCENT MORE")

# ---------- 5. LIGHTNING ----------
part(5, "The blade tip that catches lightning", "WHY DOES THIS BLADE TIP CATCH LIGHTNING?", "Why Do Wind Turbine Blades Catch Lightning on Purpose?",
     """Why do wind turbine blades have metal points built into their tips? Because a turbine is often the tallest thing for kilometers, and lightning loves it. The blade itself is made of fiberglass or carbon, which cannot carry the current. So metal receptors on the blade surface catch the strike, and a thick cable inside the blade carries it down to the hub, the tower and into the ground.""",
     "wind turbine blade tip")
sc("""Without that path, lightning would find its own way through the blade. The current heats the air and moisture inside to explosive temperatures, which can crack the blade open or blow off its tip. Lightning is one of the leading causes of blade damage worldwide.""",
   "wind turbine blade", "EXPLOSIVE HEAT")
sc("""Turbines in places with lots of storms can be hit many times a year. After a strike, sensors can record it, and drones or technicians inspect the receptors. A turbine is not just catching wind. It is also catching lightning, safely, again and again.""",
   "wind turbine", "HIT MANY TIMES A YEAR")

# ---------- 6. ROPE ACCESS ----------
part(6, "The workers hanging on the blade", "WHY ARE PEOPLE HANGING ON THIS BLADE?", "Why Do People Hang From Wind Turbine Blades?",
     """Why do technicians hang from ropes on wind turbine blades, a hundred meters in the air? Because the blades wear out, especially at the front edge. The tip of a big blade moves at around three hundred kilometers an hour. At that speed, raindrops, hail, sand and insects hit the edge like tiny bullets and slowly eat away the surface. This is called leading edge erosion.""",
     "Vortex Generator Installation")
sc("""A rough edge disturbs the airflow and steals power, and if it gets deep enough, water can enter the blade. So rope access technicians, trained climbers, abseil down the blade to sand, fill and coat the damaged edge. Some blades now get protective tapes or shields on the front edge, like a stone guard on a car.""",
   "wind turbine blade", "RAINDROPS LIKE BULLETS")
sc("""The turbine is stopped and locked before anyone goes on a blade. Then the work is done from ropes or platforms hanging from the nacelle, often in cold wind. Drones now help find the damage first, so the climbers only go where they are needed.""",
   "wind turbine", "LOCKED BEFORE THE CLIMB")

# ---------- 7. ICE ----------
part(7, "The ice on the blade", "WHY IS ICE ON A BLADE DANGEROUS?", "Why Is Ice on a Wind Turbine Blade So Dangerous?",
     """Why do wind turbines in cold places worry so much about ice? Because ice on a blade changes its shape. It ruins the airfoil, and the turbine loses power. Ice also adds weight unevenly, so the rotor becomes unbalanced and shakes. And when chunks break off a spinning blade, they can be thrown a long way.""",
     "Ice-at-rotor-blade-of-wind-turbine")
sc("""So turbines in cold regions carry sensors that detect icing, and many stop automatically when ice builds up. Warning signs around them tell walkers to keep away in winter. In places like Scandinavia and Canada, some blades are fitted with heating systems, warm air blown through the inside or heating mats under the surface.""",
   "wind turbine", "HEATED BLADES")
sc("""Heating costs some energy, but a stopped turbine makes none at all. In cold climates, a turbine that can de-ice itself may produce far more power over a winter. It is the same problem airplanes face, solved on a machine that never leaves the ground.""",
   "wind turbine", "LIKE AN AIRPLANE WING")

# ---------- 8. NACELLE ----------
part(8, "The machine room on top", "WHY IS THERE A ROOM UP HERE?", "Why Is There a Whole Room on Top of a Wind Turbine?",
     """Why does a wind turbine have a box the size of a bus on top of its tower? Because that is the power plant. The nacelle holds the main shaft, the bearings, the generator, and on many turbines, a gearbox. The rotor turns slowly, maybe ten to fifteen times a minute, but a normal generator wants to spin much faster. The gearbox speeds it up about a hundred times.""",
     "Inside the nacelle")
sc("""Gearboxes are one of the parts that fail most often, and replacing one at a hundred meters height needs a giant crane. So some makers removed it. Direct drive turbines use a very large generator, several meters across, that turns at the same slow speed as the rotor. Fewer moving parts, but a heavier and more expensive generator.""",
   "wind turbine nacelle", "NO GEARBOX")
sc("""The nacelle also turns to face the wind. A wind vane and an anemometer on its roof measure the wind direction and speed, and yaw motors rotate the whole nacelle on a big bearing at the top of the tower. On the biggest offshore turbines, everything up there can weigh hundreds of tonnes.""",
   "wind turbine nacelle", "IT TURNS TO THE WIND")

# ---------- 9. TOWER ----------
part(9, "The ladder inside the tower", "WHY IS THERE A LADDER IN HERE?", "Why Do Wind Turbine Technicians Climb a 100 Meter Ladder?",
     """Why is there a ladder inside a wind turbine tower? Because that is how technicians get to work. The tower is a hollow steel tube, sometimes more than a hundred meters tall. Inside, a ladder runs all the way up, with rest platforms on the way. Many modern turbines also have a small service lift, but the ladder is always there as a backup.""",
     "Looking Up The Wind Turbine Tower")
sc("""Climbing it is like climbing a thirty story building. Technicians wear harnesses clipped to a safety rail, so a slip cannot become a fall. They carry tools and spare parts in bags, or use a small crane in the nacelle to lift heavy pieces from the ground.""",
   "wind turbine", "THIRTY STORIES")
sc("""The tower also hides the power cables, the control cabinets and the transformer on some designs. It is tapered, wider at the bottom where the bending force is strongest, and built in sections that are bolted together on site.""",
   "wind turbine", "WIDER AT THE BOTTOM")

# ---------- 10. TRANSPORT ----------
part(10, "The blade on the road", "WHY IS THIS BLADE ON A TRUCK?", "Why Are Wind Turbine Blades So Hard to Move?",
     """Why does moving a single wind turbine blade need a police escort? Because the blade is made in one piece, and it is longer than almost anything else on the road. On land, blades of sixty to eighty meters are common. They cannot bend, and they cannot be cut in two without making them weaker. So they travel whole, on special extending trailers.""",
     "Wind turbine blade coming south of Selkirk on A7")
sc("""Every route is planned in advance. Corners, bridges, trees and road signs are checked, and some are removed for a night. In mountains, special trailers can tilt the blade up into the air, so it can pass tight curves with its tip pointing at the sky.""",
   "wind turbine blade transport", "TIP TO THE SKY")
sc("""This limit on transport is one reason the biggest turbines are built offshore. Blades of more than a hundred meters can be loaded onto ships right at the factory on the coast, and taken to sea without ever touching a road.""",
   "wind turbine blade transport", "OFFSHORE FOR THE GIANTS")

# ---------- 11. FOUNDATION ----------
part(11, "The legs under the sea", "WHY DO OFFSHORE TURBINES STAND ON THESE?", "Why Do Offshore Wind Turbines Stand on Steel Legs?",
     """Why do some offshore wind turbines stand on these steel towers with legs, called jackets? Because the sea gets deep. In shallow water, a turbine usually stands on a monopile, a single giant steel tube hammered into the seabed. But the deeper the water, the thicker and heavier that tube must be. A lattice jacket with four legs spreads the load and uses less steel.""",
     "Offshore Wind Farm Foundation")
sc("""The foundation must survive waves, currents, and the huge bending force from the rotor above. Engineers design it for the worst storm expected in fifty years, and for decades of waves hitting it every few seconds. Below the waterline, it is protected from corrosion with coatings and metal anodes that corrode instead of the steel.""",
   "offshore wind turbine foundation", "THE 50 YEAR STORM")
sc("""Where the sea is too deep for any fixed foundation, turbines can now float, held in place by anchors and chains, like oil platforms. It is the same old problem, keeping a tall machine standing in the wind, solved one more way.""",
   "offshore wind turbine", "TURBINES THAT FLOAT")

# ---------- VERDICT ----------
sc("""So here are the eleven. Three blades, because two wobble and four cost too much. A ring of bolts at the root, a hub that twists the blades, little fins that delay the stall, and tips that catch lightning on purpose. Workers on ropes fixing the edges, ice that turns a blade into a danger, a machine room on top, a ladder inside, a blade too long for the road, and steel legs under the sea.""",
   "wind turbine", "11 PARTS. 3 BLADES.", chapter="The verdict", cuts=6)
sc("""Next time you see a wind farm turning slowly on a hill, count the blades, and remember that every number on that machine was a choice. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "wind turbine", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Nacelle of Wind Turbine 01.jpg", 0.62, 0.32),
    2: ("File:Shaft end of Wind turbine blades.jpg", 0.27, 0.5),
    3: ("File:Wind turbine construction, Pougny, Enercon E-103 hub (1).jpg", 0.5, 0.45),
    4: ("File:Wind turbine blades in laydown yard Pasco 2009 fins - detail.jpg", 0.55, 0.5),
    5: ("File:N117 Vortexgenerator.jpg", 0.85, 0.6),
    6: ("File:Vortex Generator Installation.jpg", 0.52, 0.65),
    7: ("File:Ice-at-rotor-blade-of-wind-turbine.jpg", 0.5, 0.45),
    8: ("File:Inside the nacelle.jpg", 0.6, 0.55),
    9: ("File:Looking Up The Wind Turbine Tower, Byron, Wisconsin, 2007-05-05.jpg", 0.5, 0.45),
    10: ("File:Wind turbine blade coming south of Selkirk on A7.jpg", 0.6, 0.35),
    11: ("File:Offshore Wind Farm Foundation, Nigg Energy Park (geograph 6656608).jpg", 0.42, 0.35),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video53", "title": "Why Do Wind Turbines Have Only 3 Blades?",
           "length_scale": 1.6, "scenes": S}, open("videos/video53/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
