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
sc("""A fighter jet lands at around two hundred and forty kilometres per hour. On a normal airport, it needs a runway more than a kilometre long to stop. On an aircraft carrier, it has about one hundred metres. So the ship catches it, with a steel cable, and stops it in around two seconds. Today, ten parts of an aircraft carrier, and why each one exists.""",
   "aircraft carrier landing", "CAUGHT BY A CABLE", cuts=8, chapter="Intro")
sc("""An aircraft carrier is a floating airport, squeezed onto a deck about three hundred metres long, moving, rolling and pitching in the sea. Almost every part of it exists because there is not enough space. Planes must launch without a long runway, land without a long runway, and be parked where there is no room.""",
   "aircraft carrier flight deck", "NOT ENOUGH SPACE")
sc("""As always, every fact here comes from a named source, navies and naval references, all listed in the description. Let's start with the cables.""",
   "aircraft carrier at sea", "WHY DOES THIS EXIST?")

# ---------- 1. ARRESTING WIRES ----------
part(1, "The arresting wires", "WHY ARE THERE CABLES ACROSS THE DECK?", "Why Do Aircraft Carriers Catch Jets With Cables?",
     """Why are there steel cables stretched across the deck of an aircraft carrier? They are arresting wires. A landing jet catches one of them with a hook, and the cable pulls out, slowing the plane down. Below deck, each wire is connected to a large machine that absorbs the energy of the landing.""",
     "aircraft carrier arresting wire")
sc("""The machine is the clever part. It controls how hard the cable pulls, depending on the weight and speed of each aircraft. Too soft, and the plane rolls off the end of the deck. Too hard, and the hook or the plane could be torn apart. The settings are changed for every single landing.""",
   "arresting gear", "SET FOR EVERY LANDING")
sc("""American carriers have three or four wires. On carriers with four wires, pilots aim for the third, because it gives the safest margin. Every landing is graded, and pilots are ranked by how well they land. Stopping a jet in about two seconds pushes the pilot hard into the straps, and most say it never feels normal.""",
   "F/A-18 arrested landing", "AIM FOR THE THIRD WIRE")

# ---------- 2. TAILHOOK ----------
part(2, "The tailhook", "WHY DOES THIS JET HAVE A HOOK?", "Why Do Navy Jets Have a Hook on the Tail?",
     """Why do navy jets have a hook under the tail? It is the tailhook, the other half of the arresting system. Before landing, the pilot lowers the hook. It hangs behind the plane and drags along the deck, ready to snag one of the cables. Air force versions of the same jets often have a much smaller hook, or none at all.""",
     "tailhook")
sc("""The hook has to take enormous forces in a fraction of a second. So it is built into a strong part of the plane's structure, and navy jets have stronger frames and landing gear overall. That extra strength adds weight, which is one reason carrier aircraft are heavier than their land based versions.""",
   "F-35C tailhook", "BUILT FOR THE PULL")
sc("""Navy pilots do not flare and float onto the deck like airline pilots. They fly straight into the deck at a steady angle, in what looks like a controlled crash. The landing gear is built to absorb that impact, and the hook is placed so it is sure to drag across the wires.""",
   "carrier landing", "A CONTROLLED CRASH")

# ---------- 3. FULL THROTTLE ----------
part(3, "The full throttle landing", "WHY DO PILOTS SPEED UP WHEN THEY LAND?", "Why Do Navy Pilots Go Full Throttle When Landing?",
     """Why do navy pilots push the throttle to full power the moment they touch the deck? In case the hook misses the wires. If the hook bounces over every cable, the plane is running out of deck very fast. With the engines already at full power, it can take off again immediately.""",
     "jet landing on carrier")
sc("""A missed landing like this is called a bolter. The jet roars off the end of the angled deck, climbs, circles, and tries again. If the engines were idle, they would need several seconds to spool up, and the plane would fall into the sea. Full power on landing turns a disaster into a second try.""",
   "carrier bolter", "A SECOND TRY")
sc("""If the hook does catch a wire, the cable is strong enough to hold the jet even at full power. Only when the plane has stopped does the pilot pull the throttle back. It is one of the strangest rules in aviation. To land safely, you must be ready to take off.""",
   "F/A-18 Super Hornet carrier", "READY TO TAKE OFF")

# ---------- 4. CATAPULT ----------
part(4, "The catapult", "WHY DOES THIS DECK HAVE A SLOT?", "Why Do Aircraft Carriers Launch Jets With Catapults?",
     """Why does the deck of an aircraft carrier have a long slot running to the front? It is the catapult. A heavy jet cannot reach take off speed in less than a hundred metres on its own. The catapult grabs the nose wheel and throws the plane forward, from zero to around two hundred and sixty kilometres per hour in about two seconds.""",
     "aircraft carrier catapult")
sc("""For decades, catapults were powered by steam from the ship's boilers or reactors, pushing pistons along a cylinder under the deck. The steam catapult was a British invention of the nineteen fifties. You can still see the clouds of steam rising from the slot after each launch.""",
   "steam catapult", "POWERED BY STEAM")
sc("""The newest American carrier, the Gerald R Ford, uses an electromagnetic catapult instead, a linear electric motor that pushes the plane with magnetic force. It can be adjusted more precisely for light and heavy aircraft, and it puts less stress on the planes. The idea is old, but the power behind it keeps changing.""",
   "USS Gerald R. Ford", "ELECTRIC CATAPULT")

# ---------- 5. JET BLAST DEFLECTOR ----------
part(5, "The blast deflector", "WHY DOES THIS WALL RISE FROM THE DECK?", "Why Does a Wall Rise Behind Jets on a Carrier?",
     """Why does a metal wall rise from the deck behind a jet before it launches? It is the jet blast deflector. When the jet goes to full power on the catapult, its engines blast hot gas straight backwards. Without the wall, that blast would hit the planes and people waiting behind it.""",
     "jet blast deflector")
sc("""The deflector tilts up from the deck and sends the hot exhaust upwards, away from the crew. Because the blast is so hot, the panels are cooled by sea water running through pipes inside them. Without cooling, they would warp after a few launches.""",
   "jet blast deflector carrier", "COOLED BY SEA WATER")
sc("""The deflector lets the carrier launch planes one after another, with the next jet waiting just behind. On a busy flight deck, every metre counts. A simple wall makes it possible to line up aircraft behind each other, instead of spreading them out across the deck.""",
   "carrier flight deck operations", "EVERY METRE COUNTS")

# ---------- 6. ANGLED DECK ----------
part(6, "The angled deck", "WHY IS THE LANDING DECK CROOKED?", "Why Is an Aircraft Carrier's Landing Deck Angled?",
     """Why is the landing area of an aircraft carrier set at an angle to the ship? On early carriers, planes landed straight down the length of the deck. If a plane missed the wires, it crashed into the planes parked at the front. Barriers were used to stop them, and many aircraft were destroyed.""",
     "aircraft carrier angled deck")
sc("""In the early nineteen fifties, British officers came up with a simple idea. Angle the landing area to the left, so it points off the side of the ship. A plane that misses the wires simply flies off the end of the angled deck and goes around. The front of the ship stays clear for parking and catapult launches.""",
   "angled flight deck", "A BRITISH IDEA")
sc("""The angled deck changed carrier design forever. It allowed landings and launches at the same time, and made bolters safe. Almost every large carrier built since has one. A few degrees of paint on the deck turned the most dangerous part of naval aviation into a routine.""",
   "Nimitz class aircraft carrier", "A FEW DEGREES OF PAINT")

# ---------- 7. MEATBALL ----------
part(7, "The landing lights", "WHY DOES THIS LIGHT HELP PILOTS LAND?", "Why Do Carrier Pilots Follow a Ball of Light?",
     """Why do carrier pilots follow a ball of light? On the side of the deck there is a system of lights, called the optical landing system. Pilots call the central light the meatball, or just the ball. Its position, compared with a row of green reference lights, tells the pilot whether the plane is too high, too low or exactly on the glide path.""",
     "Fresnel lens optical landing system")
sc("""The system uses special lenses that only show the ball at the right height to a pilot at the right angle. If the plane is too high, the ball appears above the green lights. Too low, and it drops below them, and turns red if it is dangerously low. The pilot keeps the ball in the middle all the way down.""",
   "carrier landing lights", "KEEP THE BALL CENTRED")
sc("""The idea started with a British mirror landing aid in the nineteen fifties, using a mirror and a light. Next to it stands a landing signal officer, an experienced pilot who watches every approach and talks to the pilot by radio. Lights and a human eye work together on every landing.""",
   "landing signal officer", "LIGHTS AND A HUMAN EYE")

# ---------- 8. ISLAND ----------
part(8, "The island", "WHY IS THE TOWER ALWAYS ON THE RIGHT?", "Why Is an Aircraft Carrier's Tower Always on the Right?",
     """Why is the control tower of an aircraft carrier almost always on the right side? The tower is called the island, and it holds the bridge, the flight control and radars. Putting it on one edge leaves the rest of the deck free. The choice of the right side is partly about the angled landing deck, which points to the left.""",
     "aircraft carrier island")
sc("""There is also a historical reason that is often given. Early propeller planes tended to pull to the left when they went to full power, and pilots usually turned left if they had to abort a landing. An island on the right was out of the way. Once that layout became standard, the rest of the deck was designed around it.""",
   "aircraft carrier tower", "OUT OF THE WAY")
sc("""A few carriers have been built with the island on the left, but they were rare and were not repeated. The British Queen Elizabeth class carriers have two islands, one for steering the ship and one for controlling flight operations. Even the tower of a carrier is a careful compromise.""",
   "HMS Queen Elizabeth", "TWO ISLANDS")

# ---------- 9. FOLDING WINGS ----------
part(9, "The folding wings", "WHY DO THESE WINGS FOLD UP?", "Why Do Navy Jets Have Folding Wings?",
     """Why do the wings of navy aircraft fold up? To save space. A carrier may carry dozens of aircraft, and they all have to fit on the deck and in the hangar below. Folding the wings can reduce a plane's width a lot, so more planes fit in the same space, and they can be moved around more easily.""",
     "folding wings aircraft carrier")
sc("""The fold adds hinges, locks and hydraulic systems, which add weight and complexity. A wing that fails to lock properly before take off is a serious danger, so the system has multiple checks. Navy versions of aircraft like the F thirty-five C have folding wings, while the air force versions do not need them.""",
   "F-35C folded wings", "HINGES AND LOCKS")
sc("""The aircraft elevators on the side of the ship lift planes between the hangar and the flight deck, and they are sized for folded aircraft. Helicopters fold their rotor blades for the same reason. On a carrier, every aircraft is designed to shrink when it is not flying.""",
   "aircraft carrier elevator", "DESIGNED TO SHRINK")

# ---------- 10. COLOURED SHIRTS ----------
part(10, "The coloured shirts", "WHY DOES THE DECK CREW WEAR COLOURS?", "Why Do Aircraft Carrier Crews Wear Different Colors?",
     """Why do the crew on an aircraft carrier deck wear different coloured shirts? So everyone can see instantly who does what. On a deck full of noise, with jet engines screaming, people cannot easily talk. A colour tells a pilot or another sailor someone's job from far away.""",
     "aircraft carrier deck crew")
sc("""Yellow shirts direct the aircraft, guiding pilots with hand signals. Green shirts run the catapults and arresting gear. Red shirts handle weapons and fire fighting. Purple shirts handle fuel, and they are nicknamed grapes. White shirts are often safety and medical staff. Each colour is a job.""",
   "flight deck crew signals", "EACH COLOUR IS A JOB")
sc("""Hand signals replace words. A yellow shirt can guide a jet onto the catapult using only arm movements, at night with lighted wands. It is a language built for the most dangerous deck in the world, where a single mistake can cost lives, and everyone has to understand each other at a glance.""",
   "aircraft carrier night operations", "A LANGUAGE OF COLOURS")

# ---------- VERDICT ----------
sc("""So here are the ten. Cables that stop a jet in two seconds. A hook built to take the pull. Full throttle on landing, in case of a miss. A catapult that throws planes into the air. A wall that deflects the blast. A crooked deck for safe go arounds. A ball of light that guides every landing. A tower on the right. Wings that fold. And colours that speak when no one can hear.""",
   "aircraft carrier", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""An aircraft carrier is an airport that had to fit on a ship. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which part of the carrier surprised you most.""",
   "aircraft carrier sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video36", "title": "Why Do Aircraft Carriers Catch Jets With Cables?",
           "length_scale": 1.6, "scenes": S}, open("videos/video36/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
