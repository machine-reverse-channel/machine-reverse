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
sc("""To certify a new jet engine, engineers run it at full power and then blow one of its own blades off with a small explosive. They fire birds into it with a cannon. They let gas flow through it that is hotter than the melting point of the metal inside. And it has to survive all of it. Today, eleven parts of a jet engine that almost nobody understands, and why each one exists. Number ten is the reason an engine is designed to fall off the wing.""",
   "jet engine turbofan front view", "11 ENGINE PARTS", cuts=8, chapter="Intro")
sc("""A modern airliner engine is one of the most extreme machines people build. It swallows a huge amount of air every second, squeezes it, sets it on fire, and throws it out the back, for thousands of hours without stopping. Every visible feature on it, and many hidden ones, is the answer to a specific problem, whether that is noise, heat, birds, or the worst case of all, a part breaking loose at full speed.""",
   "GE90 engine Boeing 777", "THE MOST EXTREME MACHINE")
sc("""As always, every number here comes from a named source, the engine makers, NASA, the Federal Aviation Administration rules, or official accident investigations, and all of them are listed in the description. Let's start at the front, with the part you can actually see from your window seat, the giant fan, and the surprising fact about where the engine's push really comes from.""",
   "jet engine fan blades close up", "WHY DOES THIS EXIST?")

# ---------- 1. THE FAN ----------
part(1, "The giant fan", "WHY IS THIS FAN SO HUGE?", "Why Are Jet Engine Fans So Huge?",
     """Why is the fan at the front of a jet engine so enormous? Because the fan makes most of the thrust. In a modern high bypass engine, most of the air pulled in by the fan never goes through the burning core at all. It flows around it, through a duct, and out the back. That bypass air provides up to eighty percent of the total thrust. Moving a lot of air a little faster is more efficient and quieter than moving a little air very fast. That is why fans keep getting bigger.""",
     "GE9X engine fan")
sc("""Look at the GE nine X, the engine of the Boeing seven seven seven X. According to GE Aerospace, its front fan is one hundred thirty-four inches across, and its bypass ratio is about ten to one, meaning roughly ten times more air goes around the core than through it. It holds a world record of one hundred thirty-four thousand three hundred pounds of thrust.""",
   "GE9X engine", "134 INCHES. 10 TO 1.")
sc("""So the jet engine on a modern airliner is really two machines in one. A small, extremely hot gas turbine in the middle, and a giant fan that it drives. The hot core is the heart. But the fan is the muscle. And when engineers want an engine to burn less fuel, one of the main things they do is make the fan larger and let more air bypass the core.""",
   "turbofan engine cutaway", "THE CORE IS THE HEART. THE FAN IS THE MUSCLE.")

# ---------- 2. COMPOSITE BLADES ----------
part(2, "The curved blades", "WHY ARE THESE BLADES CURVED?", "Why Are Jet Engine Blades Curved Like This?",
     """Why are the fan blades of a modern engine so wide and so strangely curved? Because each blade is a wing, and its tip is spinning so fast that it meets the air near or above the speed of sound. The twisted, swept shape keeps the airflow smooth from the root to the tip, and controls shock waves and noise. Many modern fan blades are not even metal. The GE nine X uses carbon fiber composite blades, and only sixteen of them, six fewer than its predecessor, the GE ninety.""",
     "composite fan blades GE engine")
sc("""Fewer, wider, lighter blades mean less weight spinning at the front of the engine, and less weight in the heavy case that surrounds them. Composite blades also tolerate a lot of the vibration and fatigue that metal blades suffer from. According to GE Aerospace, the GE nine X burns up to ten percent less fuel than the GE ninety one fifteen B. Part of that comes from these blades.""",
   "GE90 composite fan blade", "UP TO 10% LESS FUEL")

sc("""There is a catch with composite blades. They have to survive the same brutal tests as metal ones, including birds and blade failures, which we will get to in a moment. Engineers often protect the leading edge, the part that hits the air first, with a metal edge, because that is where rain, hail, sand and birds strike. The blade is a mix of materials, each one placed exactly where its strength is needed most.""",
   "jet engine fan blade leading edge", "METAL WHERE IT HITS")

# ---------- 3. ACOUSTIC LINERS ----------
part(3, "The holes inside the intake", "WHY IS THE INTAKE FULL OF HOLES?", "Why Is the Inside of a Jet Engine Full of Holes?",
     """Why is the inside wall of a jet engine's intake covered in thousands of tiny holes? It is not decoration and not ventilation. It is a sound trap called an acoustic liner. Behind the perforated skin is a honeycomb of small cells, closed at the back. When the noise of the fan hits the holes, the air inside each cell bounces like a spring and absorbs part of the sound energy. It is the same physics that makes a bottle hum when you blow across it, used in reverse to swallow noise instead of making it.""",
     "jet engine intake acoustic liner")
sc("""This principle is called Helmholtz resonance. Each cell is tuned by its size and depth to absorb certain frequencies, and some liners stack two layers of honeycomb to catch a wider range. They line both the intake and the bypass duct. The lower panels even have small slots to drain water, so ice cannot form inside them. And the best liners today are made in one seamless piece, because every seam is an area that does not absorb sound.""",
   "engine nacelle inlet", "HELMHOLTZ RESONATORS")

sc("""Why go to all this trouble? Because the fan is the loudest part of a modern engine during approach and landing, when the airplane is low over homes. The core's roar has been tamed by the big bypass stream, which wraps the hot exhaust in a blanket of slower air. What remains is the fan's buzz, and the liners are the main defense against it. Combined with chevrons and careful blade design, they are why airports can sit next to cities.""",
   "airliner landing approach city", "THE FAN IS THE NOISE")

# ---------- 4. BLADE-OFF TEST ----------
part(4, "The containment case", "WHY IS THIS RING SO STRONG?", "Why Do Engineers Blow Up Jet Engines?",
     """Why is the ring around the fan built so incredibly strong? Because of one terrifying test. To certify an engine, regulators require that if a blade breaks off, the engine must contain it. So engineers prepare a blade with a small explosive charge inside, run the engine up, and fire the charge. The blade flies off at full speed and hits the case. No fragment is allowed to punch through the outer casing. The engine can be destroyed. It just cannot throw pieces into the wing, the fuel, or the cabin.""",
     "jet engine fan case")
sc("""The rule is in the US regulations, part thirty-three, section ninety-four, and Europe has the same requirement. There are two ways to stop a flying blade. A hard wall, a heavy metal ring that deflects the debris, or a soft wall, a thick wrap of strong fiber like aramid, which catches the pieces like a net. Composite and hollow blades help here too, because a lighter blade is easier to stop.""",
   "jet engine cross section fan case", "14 CFR 33.94")
sc("""This matters because a blade that escapes can be catastrophic. Engine fragments have punctured fuel tanks, cut hydraulic lines, and broken windows in real accidents. Containment is what turns a frightening engine failure into a story the passengers tell at dinner, about a loud bang and a diversion, instead of a disaster. That is why the explosive test exists, and why every engine has to pass it.""",
   "airliner engine failure damaged", "A BANG, NOT A DISASTER")

# ---------- 5. BIRD STRIKE ----------
part(5, "The bird test", "WHY FIRE BIRDS AT THIS ENGINE?", "Why Do Engineers Fire Birds Into Jet Engines?",
     """Why do engineers fire birds into brand new jet engines with a cannon? Because real birds will hit them. The US rules spell it out. A large engine must survive a single bird of about eight pounds hitting its fan at two hundred knots, and shut down safely without catching fire or breaking loose. Then there is the flock test. Several medium birds are fired in, and the engine must keep running for about twenty minutes afterward, at changing power settings, like it would on a real flight returning to the airport.""",
     "bird strike jet engine test")
sc("""The requirement depends on how big the engine's intake is. The bigger the opening, the bigger and more numerous the birds. For the largest engines, the large single bird test uses a bird of eight point zero three pounds. During the flock test, the engine cannot lose more than twenty-five percent of its thrust and cannot shut down. Engine makers use a compressed air launcher, often called a bird cannon, to fire them at the exact spot on the blades that would do the most damage.""",
   "Canada goose flock", "8.03 POUNDS AT 200 KNOTS")
sc("""Why so strict? Because sometimes the worst happens. In two thousand nine, US Airways flight fifteen forty-nine hit a flock of Canada geese after takeoff from New York, and both engines lost power. Geese can weigh up to around ten pounds, heavier than the biggest certification bird. After that flight, testing for multiple bird ingestion became an even bigger focus. Nature does not read the regulations.""",
   "US Airways Flight 1549 Hudson", "NATURE DOESN'T READ THE RULES")

# ---------- 6. COOLING HOLES ----------
part(6, "The holes in the turbine blades", "WHY ARE THESE BLADES FULL OF HOLES?", "Why Don't Turbine Blades Melt?",
     """Why are the turbine blades deep inside a jet engine covered in tiny holes? Because the gas hitting them is hotter than the melting point of the blades. The gas entering the turbine can reach about sixteen hundred degrees Celsius. The nickel alloy of the blades melts at roughly twelve hundred to fourteen hundred. So the blades are hollow. Cooler air from the compressor flows through channels inside them and comes out of those tiny holes, wrapping the blade in a thin protective film of air. The metal survives because it never actually touches the full heat.""",
     "turbine blade cooling holes")
sc("""This trick is called film cooling. The cooling air itself is around seven hundred to eight hundred degrees Celsius, which sounds hot, but compared with the gas outside the blade, it is cold. The internal channels are formed during casting, using ceramic cores inside the mold, and the holes are drilled afterward with incredible precision. Each blade is a tiny piece of plumbing, built to survive in a place where its own material should be liquid.""",
   "jet engine turbine blades", "1,600°C GAS. 1,300°C METAL.")

sc("""Some of the most advanced turbine blades take this even further. They are cast as a single crystal of metal, with no grain boundaries, the tiny weak lines between crystals where cracks like to start at high temperature. Rolls-Royce has cast blades this way in Derby, England, since the nineteen eighties, about three hundred thousand blades a year. The metal is poured at around fifteen hundred degrees Celsius, and the mold is slowly pulled into a cold chamber so the metal freezes as one crystal.""",
   "single crystal turbine blade", "ONE CRYSTAL. ONE BLADE.")

# ---------- 7. CERAMICS ----------
part(7, "The ceramic armor", "WHY IS THIS METAL COATED IN CERAMIC?", "Why Do Jet Engines Wear Ceramic Armor?",
     """Why are the hottest parts of a jet engine coated in ceramic? Because ceramic is a terrible conductor of heat, and that is exactly what you want. A thermal barrier coating about a quarter of a millimeter thick is sprayed onto the turbine blades. That thin layer keeps the metal underneath roughly a hundred degrees cooler than its surface. A hundred degrees may not sound like much, but at these temperatures, it can be the difference between a blade that lasts for years and one that fails.""",
     "thermal barrier coating turbine blade")
sc("""The newest engines go further. According to GE Aerospace, the GE nine X has more than one hundred parts made from ceramic matrix composites, materials that can handle more heat than metal while weighing much less. Hotter running engines are more efficient, so every material that tolerates more heat lets engineers squeeze more power from less fuel. The history of the jet engine is, in large part, a history of fighting heat.""",
   "GE9X engine core", "100+ CERAMIC PARTS")

# ---------- 8. THRUST REVERSERS ----------
part(8, "The thrust reversers", "WHY DOES THE ENGINE OPEN UP ON LANDING?", "Why Do Jet Engines Open Up When They Land?",
     """Why does the back of a jet engine slide open right after landing? That is the thrust reverser. On most modern engines, a sleeve slides back, blocker doors close the normal exit, and the fan air is forced out through angled vanes called cascades, pointing forward. The engine is still blowing backward through its core, but most of its push now goes the other way, helping to slow the airplane. According to Pilot Institute, reverse thrust can shorten the landing distance by up to twenty percent. And it saves the brakes.""",
     "thrust reverser deployed landing")
sc("""But many landing distance calculations do not count on reversers at all, because an engine might be out, so the brakes alone must be enough. And reversers have to stay locked in flight. In nineteen ninety-one, on Lauda Air flight zero zero four, a Boeing seven sixty-seven's left thrust reverser deployed in flight while the engine was at high power during the climb from Bangkok. The airplane went out of control, and everyone on board died. Boeing then added a mechanical lock to the system.""",
   "Boeing 767 engine", "LAUDA AIR 004, 1991")

# ---------- 9. BLEED AIR ----------
part(9, "The air you breathe", "WHERE DOES THE CABIN AIR COME FROM?", "Why Does Cabin Air Come From the Engines?",
     """Where does the air you breathe on most airliners come from? From the engines. Since the nineteen fifties, jets have taken compressed air from the compressor stages of their engines, called bleed air. It is already squeezed and hot, so after cooling in the air conditioning packs, it pressurizes the cabin. The same hot air also heats the wings to stop ice and powers other systems. It is clean air from outside. It is pulled in at the front, before any fuel is burned.""",
     "airliner engine pylon wing")
sc("""But bleed air is not free. Every bit of air taken out of the compressor is air that is not making thrust. So the Boeing seven eighty-seven took a different path. It uses electric compressors to pressurize the cabin, and electric heating mats to de-ice its wings. Boeing claimed about a three percent improvement in fuel burn from this no bleed design. To make that possible, each engine drives two big generators.""",
   "Boeing 787 Dreamliner", "THE 787: NO BLEED AIR")

sc("""There is a quiet engineering trade-off hidden here. The engine's compressor is designed to make thrust, and every system that borrows its air makes it work a little harder. Moving to electric systems means bigger generators and more wiring, but it lets the engine do one job very well. Newer airliners are moving in this direction, step by step, toward what engineers call the more electric aircraft.""",
   "Boeing 787 engine nacelle", "THE MORE ELECTRIC AIRCRAFT")

# ---------- 10. FUSE PINS ----------
part(10, "The pins that are meant to break", "WHY IS THIS ENGINE DESIGNED TO FALL OFF?", "Why Are Jet Engines Designed to Fall Off?",
     """Why is a jet engine attached to the wing with pins that are designed to break? They are called fuse pins, and like an electrical fuse, they fail on purpose. If an engine suffers a huge overload, for example in a crash landing or a violent seizure, the pins snap, and the engine breaks away cleanly. The idea is to protect the wing, and especially the fuel tank inside it, from being torn open. Losing an engine is bad. Losing the wing and its fuel is much worse.""",
     "engine pylon airliner wing")
sc("""But a fuse must break only when it should. On the fourth of October, nineteen ninety-two, an El Al Boeing seven forty-seven freighter took off from Amsterdam. Fuse pins on the number three engine had developed fatigue cracks. The engine broke off, struck the outer engine, and tore it away too. The airplane crashed into apartment buildings in the Bijlmermeer district. Four people on board and at least forty-three on the ground died.""",
   "Boeing 747 freighter El Al", "EL AL 1862, AMSTERDAM 1992")
sc("""The Dutch investigation found that the pylon's design and certification were inadequate, and that inspections had failed to catch the cracks. Boeing ordered the engines and pylons removed from seven forty-sevens so the pins could be inspected, and cracked pins were replaced. The idea of a part that breaks on purpose survived. But the lesson was that it must be strong enough for every normal flight, for decades.""",
   "Boeing 747 engines wing", "BREAK ONLY WHEN IT SHOULD")

# ---------- 11. GENERATORS ----------
part(11, "The generators", "WHY DOES A JET ENGINE MAKE ELECTRICITY?", "Why Does a Jet Engine Make Electricity?",
     """Why does a jet engine also make electricity? Because the airplane needs a power plant in the sky. Underneath the engine is a gearbox, driven by the engine's shaft, that spins pumps and generators. They power the lights, the screens, the galleys, the flight computers, and on modern jets, much more. On the Boeing seven eighty-seven, each engine drives two generators of two hundred fifty kilovolt amperes each. That is one thousand kilovolt amperes from the two engines, far more than older jets needed.""",
     "jet engine accessory gearbox generator")
sc("""On the ground, before the engines start, the auxiliary power unit in the tail takes over that job, with its own generators. In the air, if every engine stops, the ram air turbine we saw in our last airplane video drops out to keep the essentials alive. Electricity on an airliner has several layers of backup, because almost everything on a modern jet, from the flight controls to the fuel pumps, depends on it.""",
   "airliner tail APU exhaust", "LAYERS OF BACKUP")

# ---------- VERDICT ----------
sc("""So here are the eleven. A fan that makes most of the thrust, with curved composite blades. Holes in the intake that swallow sound. A ring that catches its own exploding blade, and a test that fires birds into it. Blades with holes that survive above their melting point, and ceramic armor on top. Doors that push backward on landing, air for your lungs, pins designed to break, and generators that make it a flying power plant.""",
   "jet engine test run", "11 PARTS. 11 REASONS.", chapter="The verdict", cuts=6)
sc("""A jet engine looks like a simple tube with a fan. It is really dozens of solutions to dozens of problems, stacked inside each other. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next. Rockets are coming soon.""",
   "airliner takeoff engines", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Engine of Jet Airways Boeing 777-300ER.jpg', 0.38, 0.3),
    2: ('File:GE90 dsc04644.jpg', 0.72, 0.25),
    3: ("File:Fan & nacelle Airbus A300's CF-6.JPG", 0.7, 0.75),
    4: ('File:PW4077 Fan.jpg', 0.84, 0.5),
    5: ('File:JT8D Engine after Bird Strike.jpg', 0.3, 0.6),
    6: ('File:Repair process for a V2500 high-pressure turbine guide vane (9).jpg', 0.55, 0.45),
    7: ('File:Stator Blade with Thermal Barrier Testing on Hot Gas Rig (GRC-1975-C-01372).jpg', 0.2, 0.5),
    8: ('File:Thrust reversers arp, G-EZIO, Airbus A319 of EasyJet at Bristol International Airport, 2006.jpg', 0.46, 0.56),
    9: ('File:Detail of GEnx turbofan engine core.jpg', 0.3, 0.3),
    10: ('File:JASDF C-2(78-1205) engine pylon left side view at Komaki Air Base March 3, 2018.jpg', 0.55, 0.4),
    11: ('File:Pratt & Whitney Canada JT15D-5F turbofan engine accessory gearbox left front view at JASDF Hamamatsu Air Base October 23, 2022.jpg', 0.45, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video03", "title": "Why Do Engineers Blow Up Jet Engines on Purpose?",
           "length_scale": 1.6, "scenes": S}, open("videos/video03/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
