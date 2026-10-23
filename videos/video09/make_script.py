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
# ---------- HOOK ----------
sc("""The nose of a Boeing seven forty-seven freighter can swing up like a giant mouth, and a forty foot long pallet can roll straight in. That trick is the reason the pilots of every seven forty-seven, even the passenger ones, sit on top of the airplane, in that famous hump. Cargo planes are full of parts like that, doors in strange places, floors that roll, tails that swing open. Today, ten parts of cargo planes, and why each one exists.""",
   "Boeing 747 freighter nose door open", "WHY DOES THE NOSE OPEN?", cuts=8, chapter="Intro")
sc("""A passenger airplane is built around people. A cargo airplane is built around boxes, engines, helicopters, even other airplanes. Everything has to get in and out fast, stay perfectly still in flight, and never catch fire. That changes the doors, the floor, the walls, and sometimes the whole shape of the machine.""",
   "cargo aircraft loading", "BUILT AROUND BOXES")
sc("""As always, every fact here comes from a named source, manufacturers, accident reports and aviation references, all listed in the description. Let's start with the nose.""",
   "Boeing 747-400F", "WHY DOES THIS EXIST?")

# ---------- 1. NOSE DOOR ----------
part(1, "The nose door", "WHY DOES THIS NOSE OPEN?", "Why Do Cargo Planes Open Their Nose?",
     """Why does the nose of a seven forty-seven freighter open? So long cargo can go straight in, with nothing in the way. In the early nineteen sixties, Boeing designed a huge military transport for a US Air Force competition, and it needed a door at the front. To make room for it, the cockpit was moved up, above the cargo floor. Boeing lost that competition, but the idea moved into the seven forty-seven.""",
     "Boeing 747 nose cargo door")
sc("""At the time, many engineers believed supersonic jets would soon carry most passengers, and the seven forty-seven would end its life as a freighter. So Boeing kept the cockpit up high and made the nose able to open on the freighter versions. Supersonic jets never took over, but the hump became the most famous shape in aviation, and the nose door made the seven forty-seven a cargo legend.""",
   "Boeing 747 hump", "THE HUMP CAME FROM CARGO")
sc("""On the seven forty-seven four hundred freighter, pallets or containers up to forty feet long can be loaded straight through the nose on motor-driven rollers. It can carry around one hundred twenty tonnes of cargo. Things that would never turn the corner of a side door, like oil drilling equipment or parts of other aircraft, simply roll straight in.""",
   "747 freighter loading nose", "40 FEET, STRAIGHT IN")

# ---------- 2. SIDE DOOR ----------
part(2, "The giant side door", "WHY IS THIS DOOR SO BIG?", "Why Do Cargo Planes Have a Giant Side Door?",
     """Why do cargo planes also have a giant door on the side, behind the wing? Because not every airport has the special loaders needed for the nose, and not every freighter has a nose that opens. A large side cargo door lets a standard loader lift pallets up to the main deck from the side. Many freighters converted from passenger jets get one of these doors cut into their fuselage.""",
     "main deck side cargo door")
sc("""Cutting a giant hole in the side of a pressurized fuselage is a serious job. The edges of the hole must be reinforced with new frames and beams, because the fuselage is basically a pressure vessel, and the forces that the old skin carried must now go around the door. The door itself has heavy latches, and the crew gets warnings if it is not fully locked.""",
   "cargo door conversion fuselage", "A HOLE IN A PRESSURE VESSEL")
sc("""Below the main deck, there are smaller doors to the belly holds, for containers up to about sixty-four inches high. That is the same space where your suitcase travels on a passenger flight. In fact, much of the world's air cargo flies in the bellies of passenger airplanes, right under the passengers' feet.""",
   "aircraft belly cargo hold", "UNDER YOUR FEET")

# ---------- 3. ROLLER FLOOR ----------
part(3, "The floor that rolls", "WHY IS THIS FLOOR FULL OF ROLLERS?", "Why Is a Cargo Plane Floor Full of Rollers?",
     """Why is the floor of a cargo plane covered in rollers and balls? Because cargo comes in standard pallets and containers that can weigh several tonnes each, and nobody can carry them. Near the door, ball mats let a pallet turn in any direction. Along the length of the airplane, rows of rollers and motor-driven wheels push it toward the back, one position at a time.""",
     "aircraft cargo floor rollers")
sc("""A loadmaster can move a pallet weighing several tonnes with a small joystick. And the containers themselves are clever. Many of them are shaped with a sloped side, so they fit the curve of the fuselage perfectly, wasting as little space as possible. They are called unit load devices, and their shapes are standardized, so the same container can fly on different airplanes.""",
   "unit load device container", "THE BOX FITS THE CURVE")
sc("""Speed is money in cargo. A freighter on the ground is not earning anything. With rollers, motors and standard containers, a big freighter can be unloaded and loaded again in a short turnaround. The floor is not just a floor. It is a conveyor belt that flies.""",
   "cargo pallets airport", "A FLYING CONVEYOR BELT")

# ---------- 4. BARRIER NET ----------
part(4, "The net behind the cockpit", "WHY IS THERE A NET BEHIND THE PILOTS?", "Why Is There a Giant Net Behind Cargo Pilots?",
     """Why is there a strong net or wall right behind the cockpit of a cargo plane? It is the cargo barrier. If the airplane stops suddenly, in a crash landing or a rejected takeoff, tonnes of cargo would keep moving forward. The barrier is there to stop it before it reaches the pilots. Aviation rules require items inside an airplane to be restrained against very high forces, up to nine times their own weight forward.""",
     "cargo barrier net aircraft")
sc("""The cargo itself is also locked to the floor. Pallets are held by locks built into the floor rails, and the load on each pallet is tied down with nets and straps. The loadmaster calculates where every pallet goes, because the weight must be spread along the airplane to keep the center of gravity in a safe range.""",
   "cargo net pallet", "EVERY PALLET LOCKED")
sc("""When that goes wrong, it is deadly. In two thousand thirteen, a cargo Boeing seven forty-seven crashed just after takeoff from Bagram, in Afghanistan. Heavy armored vehicles inside broke free, slid backward, and damaged the airplane's controls. The investigators blamed improper restraint of the cargo. On a cargo plane, a loose load is not a mess. It is an emergency.""",
   "military vehicle loaded aircraft", "A LOOSE LOAD IS AN EMERGENCY")

# ---------- 5. KNEELING GEAR ----------
part(5, "The legs that kneel", "WHY DOES THIS PLANE KNEEL DOWN?", "Why Does This Giant Plane Kneel Down?",
     """Why does the Antonov An-124 kneel down on the ground, like a camel? Its landing gear can lower the nose of the airplane, so the cargo floor becomes a gentle ramp. Then trucks, tanks and heavy machines can be driven or winched straight in through the front door. The An-124 first flew on the twenty-fourth of December nineteen eighty-two, and it is still one of the biggest cargo planes flying.""",
     "Antonov An-124 nose open")
sc("""The An-124 has doors at both ends, so vehicles can drive in one side and out the other. It can carry about one hundred twenty tonnes in its standard version, and up to one hundred fifty in a special version. Inside the cabin, there is an overhead crane that can lift thirty tonnes, plus a winch that can pull loads of up to one hundred twenty tonnes. It does not need much help from the airport.""",
   "Antonov An-124 cargo hold", "A CRANE INSIDE")
sc("""The only airplane that could carry more was its bigger brother, the six engine An-225, built to carry the Soviet Buran space shuttle. It was destroyed at Hostomel, in Ukraine, in two thousand twenty-two. Today, when a huge turbine, a satellite or a power plant part needs to fly, the call often goes to an An-124.""",
   "Antonov An-225", "THE ONLY ONE BIGGER")

# ---------- 6. REAR RAMP ----------
part(6, "The ramp at the back", "WHY DOES THE TAIL OPEN LIKE A RAMP?", "Why Do Military Cargo Planes Open at the Back?",
     """Why do military cargo planes open their tail like a ramp? Because the cargo often has wheels. With a ramp at the back, jeeps, trucks and helicopters can be driven or pushed straight in, without special airport equipment. That is why military transports like the C-130 Hercules and the C-17 have a high wing, a tail lifted up out of the way, and a fuselage that sits close to the ground.""",
     "C-130 Hercules rear ramp open")
sc("""The ramp can also open in flight. That is how paratroopers jump and how cargo is dropped by parachute. Pallets slide out of the back, pulled by a small parachute, and a big one opens to bring them down. In some low level drops, the airplane flies just above the ground, and the cargo is pulled out by parachute and lands on its skids.""",
   "C-17 airdrop cargo", "IT OPENS IN FLIGHT")
sc("""All of this changes the shape of the airplane. The wing is on top, so it does not block the cabin. The landing gear is in bulges on the sides, so the floor stays low. And the engines are high, away from rocks and dust on rough runways. Look at any military transport, and you are looking at a machine designed around its back door.""",
   "C-130 Hercules landing", "DESIGNED AROUND THE BACK DOOR")

# ---------- 7. SWING TAIL ----------
part(7, "The tail that swings open", "WHY DOES THIS TAIL SWING OPEN?", "Why Does the Dreamlifter's Tail Swing Open?",
     """Why does the tail of this strange seven forty-seven swing open sideways? This is the Dreamlifter, a seven forty-seven heavily modified by Boeing to carry the giant parts of the seven eight seven, like wings and fuselage sections, between factories in different countries. The parts are too big for any normal door, so the entire back of the airplane swings open on hinges.""",
     "Boeing Dreamlifter tail open")
sc("""The Dreamlifter's fuselage was enlarged into a huge bulging shape, with far more volume than a normal seven forty-seven freighter. Its cargo is big but not very heavy, so volume matters more than weight. Only four were built, and they are a key part of how the seven eight seven is built, as the parts come from suppliers spread around the world.""",
   "Boeing 747 Dreamlifter", "VOLUME OVER WEIGHT")
sc("""Opening the tail needs a special vehicle on the ground, a loader that drives up to the back and pulls the parts out. It is a big process, but the alternative was shipping giant fuselage sections by sea and by road, which takes weeks. With the Dreamlifter, a wing can cross an ocean in a day.""",
   "Dreamlifter loading", "AN OCEAN IN A DAY")

# ---------- 8. BELUGA ----------
part(8, "The bubble on top", "WHY DOES THIS PLANE HAVE A BUBBLE?", "Why Does the Airbus Beluga Look Like a Whale?",
     """Why does the Airbus Beluga have that giant bubble on top? Because Airbus builds its airliners in pieces across Europe, wings in Britain, fuselage sections in France, Germany and Spain, and those pieces must fly to the final assembly lines. The Beluga's cockpit was lowered, and a huge cargo bay was built above it, opening through a door at the front, above the cockpit.""",
     "Airbus Beluga")
sc("""The newer BelugaXL is based on the A three thirty and first flew in July two thousand eighteen. It can carry two A three fifty wings at the same time. Its designers even painted a smiling face on the nose, with eyes and a mouth, after a public vote. It is one of the few aircraft built to look friendly on purpose.""",
   "Airbus BelugaXL", "TWO WINGS AT ONCE")
sc("""The Beluga and the Dreamlifter solve the same problem in different ways. Both turn big airliners into flying warehouses for their own factories. Without them, building a modern airliner would mean trucks, ships and many weeks of transport for every single airplane.""",
   "Airbus factory wings", "A FLYING WAREHOUSE")

# ---------- 9. CARGO LINER ----------
part(9, "The walls of the cargo hold", "WHY ARE THESE WALLS FIREPROOF?", "Why Are Cargo Plane Walls Fireproof?",
     """Why are the walls of a cargo hold covered in special fire-resistant panels? They are called cargo liners, and their job is to hold a fire inside the cargo compartment long enough for the crew to land. Behind those walls run the cables and control systems that fly the airplane. If a fire burns through, the pilots can lose control.""",
     "aircraft cargo hold liner")
sc("""That is what happened to UPS flight six on the third of September two thousand ten. Shortly after takeoff from Dubai, a pallet carrying more than eighty-one thousand lithium batteries caught fire by itself. The fire burned through the liner, damaged the flight controls, and smoke filled the cockpit. Both pilots died, about twenty-seven minutes after the first fire warning.""",
   "UPS Boeing 747 freighter", "27 MINUTES")
sc("""After that crash, the rules changed. Bulk lithium battery shipments on passenger planes were restricted, Boeing changed its fire checklists to keep air flowing to the flight deck, and the investigators called for automatic fire suppression in cargo holds. Today, cargo airlines use fire containment covers and special containers. Every new safety part was paid for by that flight.""",
   "cargo container fire containment", "PAID FOR BY ONE FLIGHT")

# ---------- 10. LOADMASTER STATION ----------
part(10, "The seat for the loadmaster", "WHY IS THERE A SEAT IN THE CARGO HOLD?", "Why Is There a Seat Inside a Cargo Plane?",
     """Why is there a seat and a control panel inside the cargo hold of a military transport? It is the loadmaster's station. The loadmaster is the crew member who plans where all the cargo goes, checks that every pallet and vehicle is locked down, operates the ramp, and in flight watches the cargo and runs airdrops. On a cargo plane, the cargo has its own crew member.""",
     "loadmaster C-17")
sc("""The loadmaster's numbers decide whether the airplane can fly at all. If the weight is too far forward or too far back, the airplane can become impossible to control on takeoff. That is why every piece of cargo is weighed and its position recorded, and why the loadmaster signs off before the airplane moves.""",
   "loadmaster cargo aircraft", "THE NUMBERS DECIDE")
sc("""So cargo planes are not just passenger planes with the seats removed. Their doors, floors, walls, tails and even their crews are designed around one simple goal, get anything, of any shape, from one side of the world to the other, safely and fast.""",
   "cargo plane takeoff", "ANYTHING, ANY SHAPE")

# ---------- VERDICT ----------
sc("""So here are the ten. A nose that opens and a hump that came from it. A giant side door, a floor that rolls, and a net that protects the pilots. Legs that kneel, a ramp at the back, a tail that swings open, a bubble for airplane parts, fireproof walls, and a seat for the person who makes sure it all stays in place.""",
   "Antonov An-124 landing", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see a cargo plane, look at the doors. They tell you exactly what it was built to carry. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "cargo plane sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Big mouth (50162261181).jpg", 0.3, 0.45),
    2: ("File:B-16462 B747-45E (SCD) Eva Air BKK 31MAR06 (6539733803).jpg", 0.62, 0.55),
    3: ("File:USCG Lockheed HC-130H 1704 cargo bay pallet rollers.JPG", 0.5, 0.5),
    4: ("File:N414FE cargo hold.jpg", 0.5, 0.4),
    5: ("File:Antonov An-124 (445770991).jpg", 0.6, 0.6),
    6: ("File:C-130 Air Drop 110411-F-RH591-224.jpg", 0.5, 0.55),
    7: ("File:Boeing 747-400LCF Dreamlifter.jpg", 0.75, 0.45),
    8: ("File:Airbus Beluga, ILA 2024, Schoenefeld (ILA43968).jpg", 0.6, 0.3),
    9: ("File:CARGO HOLD OF BOEING 747-230 D-ABYM ON DISPLAY AT THE TECHNIK MUSEUM SPEYER GERMANY APRIL 2013 (9377073884).jpg", 0.3, 0.4),
    10: ("File:JASDF C-2(78-1205) loadmaster station at Komaki Air Base March 3, 2018.jpg", 0.5, 0.5),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video09", "title": "Why Do Cargo Planes Open Their Nose?",
           "length_scale": 1.6, "scenes": S}, open("videos/video09/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
