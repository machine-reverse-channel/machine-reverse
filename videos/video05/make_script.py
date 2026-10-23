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
sc("""Some of the most advanced fighter jets in the world are designed to be unstable. Without a computer correcting them many times every second, they would flip out of control. Their tails lean sideways, their doors have teeth, their pilots lie almost on their backs, and some of them have a strange bump right in front of the engine. It all looks wrong. Today, ten fighter jet parts that look wrong, and why every one of them is right.""",
   "fighter jet close up airshow", "10 PARTS THAT LOOK WRONG", cuts=8, chapter="Intro")
sc("""A fighter jet is a compromise between things that fight each other. It has to turn hard, fly faster than sound, hide from radar, carry weapons, and bring the pilot home alive. An airliner is designed to be calm and efficient. A fighter is designed to win. And that is why its shape breaks almost every rule you would expect from an airplane.""",
   "F-16 Fighting Falcon flight", "DESIGNED TO WIN")
sc("""As always, every fact here comes from a named source, the manufacturers, the air forces, and aviation references, all listed in the description. Let's start with the little wings in front of the big wings, and the idea of a plane that wants to fall out of the sky.""",
   "Eurofighter Typhoon canard", "WHY DOES THIS EXIST?")

# ---------- 1. CANARDS ----------
part(1, "The little front wings", "WHY ARE THERE WINGS IN FRONT?", "Why Do Some Fighter Jets Have Wings in Front?",
     """Why do jets like the Eurofighter Typhoon, the Rafale and the Gripen have small wings in front of the main wing? They are called canards, and they are there because these jets are built to be unstable. A stable airplane wants to keep flying straight, and it fights you when you try to turn. An unstable airplane wants to change direction all the time. That makes it much more agile. The canards help control that instability and push the nose around very quickly.""",
     "Eurofighter Typhoon canards")
sc("""The catch is that no human can fly an unstable airplane by hand. So these jets use fly by wire. The pilot's stick does not move the control surfaces directly. It sends a request to flight computers, and the computers move the canards and the other surfaces many times every second to keep the airplane under control. If all the computers failed, the airplane could not be flown. That is why there are several of them, checking each other.""",
   "fighter jet flight control computer cockpit", "A COMPUTER FLIES IT WITH YOU")
sc("""Canards also help on takeoff and landing. Because they lift the nose from the front, the airplane can rotate at lower speeds and land shorter. On a delta wing jet without a tail, they also act as the elevator. Small wings, big job. And they are the first clue that a fighter jet is a different kind of machine.""",
   "Dassault Rafale takeoff", "SMALL WINGS, BIG JOB")

sc("""There is a reason this matters so much. Older fighters were designed to be stable, like airliners, and they paid for it in agility. Fly by wire changed the rules. The F sixteen was the first production fighter intentionally designed to be slightly unstable, and almost every modern fighter since then has followed that path. The canards are simply the most visible sign of it.""",
   "F-16 banking turn", "UNSTABLE ON PURPOSE")

# ---------- 2. LERX ----------
part(2, "The wing extensions", "WHY DOES THE WING STRETCH TO THE NOSE?", "Why Do Fighter Jet Wings Stretch to the Nose?",
     """Why do the wings of jets like the F eighteen Hornet stretch forward almost to the cockpit, in a thin sharp edge? It is called a leading edge extension. At high angles, when the nose points far above the direction of flight, a normal wing stalls. The sharp extension creates a powerful spinning vortex of air that flows over the wing and keeps the air attached to it. That lets the jet keep flying and turning at angles that would make another airplane fall.""",
     "F/A-18 Hornet leading edge extension")
sc("""You can actually see these vortices. On a humid day, at an air show, when a Hornet pulls up hard, white spirals of condensation appear along the top of the wings, starting from those extensions. That is the air being spun into a tornado that holds the jet up. It is one of the reasons the Hornet can point its nose almost anywhere at low speed.""",
   "F/A-18 vortex condensation", "YOU CAN SEE THE TORNADO")

sc("""The same idea shows up on many modern fighters, sometimes as small strakes on the nose or body. The Su twenty-seven family, the F sixteen and the F eighteen all use sharp extensions where the wing meets the body. Engineers learned that a carefully shaped vortex is like a free extra wing at high angles. It weighs almost nothing and adds lift exactly when the jet needs it most, in a tight, slow turn.""",
   "Su-27 fighter wing root", "A FREE EXTRA WING")

# ---------- 3. CANTED TAILS ----------
part(3, "The tails that lean", "WHY DO THESE TAILS LEAN SIDEWAYS?", "Why Do Stealth Jets Have Tilted Tails?",
     """Why do the twin tails on jets like the F twenty-two and the F thirty-five lean outward instead of standing straight up? One big reason is radar. A vertical tail meeting a flat wing or body makes a ninety degree corner. Corners like that bounce radar waves straight back to where they came from, like a mirror. Tilting the tails breaks that corner, so the radar energy is reflected away into the sky instead of back to the enemy.""",
     "F-22 Raptor tails")
sc("""Two tails also help at high angles of attack. When the nose is pointed very high, a single tail in the middle can be hidden behind the body, in turbulent air, and lose its grip. Two tails placed farther apart stay in cleaner air. So the same feature makes the jet harder to see and easier to control, two goals that usually fight each other.""",
   "F-35 Lightning tails", "HARDER TO SEE, EASIER TO FLY")
sc("""Stealth designers think of every surface as a mirror. The trick is not to make the airplane invisible, but to make sure that the radar energy that hits it goes almost anywhere except back to the radar. So the edges, angles and surfaces of a stealth jet are aligned with each other, in a few chosen directions. That idea explains the next strange part too.""",
   "stealth fighter angles", "EVERY SURFACE IS A MIRROR")

# ---------- 4. SAWTOOTH ----------
part(4, "The teeth on the doors", "WHY DO THESE DOORS HAVE TEETH?", "Why Do Stealth Jet Doors Have Teeth?",
     """Why do the doors and panels on stealth jets have zigzag edges, like teeth? Because every edge on an airplane reflects radar, especially an edge that faces the radar straight on. A straight door edge would create a bright flash. The zigzag edges are angled to match the main edges of the wings and tail. That way, all the edges send their reflections in the same few directions, instead of lighting up in every direction.""",
     "F-22 sawtooth panel edges")
sc("""You can see the teeth on landing gear doors, weapon bay doors, and access panels. Even small gaps and screws matter. On stealth aircraft, maintenance crews treat panel edges and seams carefully, because a badly sealed gap can make the jet more visible to radar. A fighter can be stealthy in the factory and noticeably less stealthy after careless maintenance.""",
   "F-35 weapons bay door", "EVEN A GAP CAN BETRAY IT")

sc("""Stealth also changes how a jet carries weapons. Missiles and bombs hanging under the wings are full of edges and corners, so stealth jets carry them inside, in weapon bays with those same toothed doors. The doors snap open, the weapon drops out, and the doors close again in a moment. For that short time, the jet is a little easier to see. Then it disappears again.""",
   "F-35 internal weapons bay open", "WEAPONS HIDDEN INSIDE")

# ---------- 5. GOLD CANOPY ----------
part(5, "The gold canopy", "WHY IS THIS CANOPY GOLD?", "Why Do Some Fighter Jets Have Gold Canopies?",
     """Why do some fighter jets, like the F sixteen and the F twenty-two, have a canopy with a golden tint? Because the cockpit is one of the brightest things on a fighter on radar. Radar waves go straight through clear glass and bounce around inside the cockpit, off the helmet, the seat and the instruments. A very thin metallic coating on the canopy, often based on indium tin oxide, reflects radar away while still letting the pilot see out.""",
     "F-22 gold canopy")
sc("""The coating also blocks some heat and light from the sun, which helps the pilot in a cockpit that sits under a big bubble of glass. And the bubble itself is a design choice. The F sixteen's frameless bubble canopy gives the pilot a view almost all the way around, including behind. In a dogfight, seeing the enemy first can matter more than any weapon.""",
   "F-16 bubble canopy", "SEE FIRST, WIN FIRST")

sc("""The pilot's helmet is part of the system too. On the F thirty-five, the helmet displays flight data and images from cameras around the jet, so the pilot can look down and see through the floor of the airplane. The canopy, the helmet and the sensors work together. The cockpit is not just a seat with a view. It is a sensor station built around one person.""",
   "F-35 pilot helmet", "SEE THROUGH THE FLOOR")

# ---------- 6. DSI ----------
part(6, "The bump in front of the engine", "WHY IS THERE A BUMP HERE?", "Why Do New Fighter Jets Have a Bump by the Engine?",
     """Why do jets like the F thirty-five have a strange bump right in front of the engine intake? It is called a diverterless supersonic inlet. Air flowing along the body of the jet forms a slow, messy layer close to the skin, and engines hate that air. Older jets used a gap and a separate plate to push it away. The bump does the same job with no moving parts. Its shape pushes the slow air to the sides, so only clean air enters the engine.""",
     "F-35 diverterless supersonic inlet")
sc("""Lockheed Martin developed it in the early nineteen nineties and first flew it on December eleventh, nineteen ninety-six, on a modified F sixteen, which still reached Mach two. In the Joint Strike Fighter studies, the bump design was about thirty percent lighter than the traditional inlet, and it removed the gaps and plates that reflected radar. Today it appears on several new fighters around the world.""",
   "F-16 diverterless inlet test", "30 PERCENT LIGHTER")
sc("""The bump also helps hide the engine. The front of a jet engine, with its spinning fan, is one of the brightest radar targets on an airplane. Curved intake ducts and shapes like the bump help keep the fan out of direct view. Stealth is not one trick. It is hundreds of small decisions, and this is one of the most visible.""",
   "fighter jet intake close up", "HIDE THE FAN")

# ---------- 7. THRUST VECTORING ----------
part(7, "The nozzles that move", "WHY DO THESE NOZZLES MOVE?", "Why Do Some Fighter Jet Nozzles Move?",
     """Why can the exhaust nozzles of the F twenty-two move up and down? It is called thrust vectoring. Normally an airplane turns by pushing air with its control surfaces, and at low speed there is not much air to push. The F twenty-two's engines can point their thrust as much as twenty degrees up or down. So even at very low speed, the jet can use the power of its engines to swing its nose around.""",
     "F-22 thrust vectoring nozzle")
sc("""The nozzles are flat, not round, which also helps reduce the heat and radar signature from behind. The movement is managed automatically by the flight computers, together with the control surfaces. The pilot does not steer the nozzles. He or she just pulls the stick, and the computers decide how much to use the tail and how much to use the engines.""",
   "F-22 Raptor rear view", "FLAT FOR STEALTH")
sc("""Russian fighters like the Sukhoi Su thirty-five use round nozzles that can move in more directions, and they are famous for slow, impossible looking maneuvers at air shows. Whether those moves matter in real combat is debated. But at low speed, with the nose pointed where a normal jet cannot point it, thrust vectoring gives the pilot one more way to aim.""",
   "Sukhoi Su-35 airshow", "ONE MORE WAY TO AIM")

# ---------- 8. SEAT ----------
part(8, "The seat that leans back", "WHY IS THIS PILOT LYING DOWN?", "Why Do F-16 Pilots Sit Almost Lying Down?",
     """Why does the F sixteen pilot sit leaning so far back? The seat is reclined at thirty degrees, about twice as much as in most fighters. The reason is g force. In a hard turn, blood is pulled from the head toward the feet, and the pilot can black out. Leaning back reduces the height between the heart and the eyes, so the heart has an easier job pushing blood up to the brain. It increases the pilot's tolerance to high g.""",
     "F-16 cockpit seat")
sc("""The same jet moved the control stick from the middle of the cockpit to the right side, on the armrest. A side stick lets the pilot rest the arm while pulling high g, and make precise inputs with the wrist. Because the F sixteen uses fly by wire, the stick barely moves. It mostly senses how hard the pilot is pushing. In a long, hard turn, those small details are the difference between staying in control and getting tired.""",
   "F-16 side stick", "THE STICK BARELY MOVES")

sc("""Even with the seat and the stick, pilots fight g force with their own bodies. They wear a g suit, trousers with air bladders that inflate automatically and squeeze the legs and belly, to keep blood from pooling in the lower body. And they use a breathing and straining technique, tensing the muscles to keep blood in the head. Pulling nine g is hard physical work.""",
   "fighter pilot g suit", "NINE G IS HARD WORK")

# ---------- 9. EJECTION SEAT ----------
part(9, "The yellow handle", "WHY IS THERE A YELLOW HANDLE HERE?", "Why Is There a Yellow Handle Between a Pilot's Legs?",
     """Why is there a yellow and black striped handle in front of the pilot's seat? That is the ejection handle. Pull it, and in less than a second the canopy is blown away or shattered, a rocket fires the seat out of the jet, a parachute opens, and the seat falls away from the pilot. The yellow and black stripes are the universal warning. On the ground, the seat is made safe with pins and red remove before flight flags, so nobody can fire it by accident.""",
     "ejection seat handle")
sc("""Modern seats are zero zero seats. That means they can save the pilot even at zero altitude and zero speed, sitting still on the runway. The seat is fired high enough for the parachute to open before reaching the ground. According to Martin-Baker, the British company that makes many of them, its seats had saved seven thousand eight hundred twenty-seven lives as of August twenty twenty-six.""",
   "Martin-Baker ejection seat", "7,827 LIVES")
sc("""Ejecting is violent. The acceleration can injure the spine, which is one reason pilots are trained to sit in a precise position before pulling the handle. But compared to staying in a doomed jet, it is the best option there is. Every one of those thousands of saved lives began with someone pulling a striped handle.""",
   "pilot parachute descent", "THE BEST BAD OPTION")

# ---------- 10. TAILHOOK ----------
part(10, "The hook on the tail", "WHY IS THERE A HOOK ON THIS JET?", "Why Do Navy Jets Have a Hook on the Tail?",
     """Why do navy fighters have a big hook under the tail? Because an aircraft carrier deck is far too short to land on normally. As the jet touches down, the hook catches one of several steel cables stretched across the deck, called arresting wires. The wires are connected to hydraulic engines below the deck that absorb the energy and stop a jet going around one hundred fifty miles an hour in about two seconds.""",
     "F/A-18 tailhook arresting wire")
sc("""Here is the part that looks crazy. When a navy jet touches down on a carrier, the pilot pushes the throttles to full power instead of pulling them back. If the hook misses all the wires, which is called a bolter, the jet needs enough power to fly off the end of the deck and try again. If the hook catches, the wire stops the jet anyway. Full power on landing is the safe choice.""",
   "aircraft carrier landing full power", "FULL POWER TO LAND")
sc("""Navy jets also have stronger landing gear, because carrier landings are hard, controlled crashes onto the deck without a flare. Many have folding wings, so more jets fit on a crowded ship. A navy fighter is basically a land fighter rebuilt to survive the harshest airport in the world.""",
   "carrier fighter folded wings", "THE HARSHEST AIRPORT")

# ---------- VERDICT ----------
sc("""So here are the ten. Little wings in front for an unstable jet that only computers can fly. Wing extensions that make tornadoes. Tails that lean away from radar, doors with teeth, and a golden canopy. A bump that replaces moving parts, nozzles that steer with thrust, a seat that leans back against g force, a striped handle that has saved thousands of lives, and a hook for the shortest runway on earth.""",
   "fighter jet formation flight", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Fighter jets look strange because every part is the answer to a fight, against physics, against radar, or against an enemy. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "fighter jet afterburner takeoff", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video05", "title": "Why Do Fighter Jets Look So Weird?",
           "length_scale": 1.6, "scenes": S}, open("videos/video05/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
