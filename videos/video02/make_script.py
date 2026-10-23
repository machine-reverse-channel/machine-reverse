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
sc("""On the second of June, nineteen eighty-three, a burning airliner landed in Cincinnati. The doors opened, fresh air rushed in, and in about ninety seconds the cabin exploded into flames. Twenty-three people died. Almost everything you will see in this video exists because of nights like that one. Ten small things on every airliner, things you walk past without noticing, each one written into the rules by a disaster. And number five burns at more than four hundred degrees.""",
   "airliner cabin interior aisle", "10 THINGS THAT KEEP YOU ALIVE", cuts=8, chapter="Intro")
sc("""The plane in Cincinnati was Air Canada flight seven ninety-seven, a McDonnell Douglas DC nine with forty-six people on board, flying from Dallas toward Toronto and Montreal. A fire started in or around the rear lavatory and spread behind the wall panels, where nobody could see it. By the time the pilots landed, the cabin was filling with smoke. Half the people on board never made it out.""",
   "McDonnell Douglas DC-9 Air Canada", "AIR CANADA 797, 1983")
sc("""What came next changed every airliner in the world. The investigators and the Federal Aviation Administration went after every way that fire had won, the smoke, the darkness, the materials, the time. Every fact in this video comes from the FAA, the National Transportation Safety Board, or a named source listed in the description. So, look around your next cabin, and you will find their work everywhere.""",
   "airliner cabin seats rows", "WRITTEN IN THE RULES")

# ---------- 1. FLOOR LIGHTING ----------
part(1, "The lights on the floor", "WHY ARE THESE LIGHTS ON THE FLOOR?", "Why Do Airplanes Have Lights on the Floor?",
     """Why are there strips of light running along the floor of every airliner? Because smoke rises. In a cabin fire, the ceiling disappears first, and the exit signs above your head can vanish in seconds. But near the floor, where people crouch and crawl, the air stays clearer for longer. These strips lead you along the aisle to the exits, and they change color at the door. After Air Canada flight seven ninety-seven, the whole US fleet was retrofitted by nineteen eighty-six. The FAA estimated a twenty percent faster evacuation when the cabin is full of smoke.""",
     "aircraft floor path lighting emergency")
sc("""Many of these strips no longer need electricity at all. They are made of photoluminescent material, which soaks up the cabin light during the flight and glows on its own in the dark. So even if the airplane loses power, the path still shines. The Flight Safety Foundation says that passengers can lose up to eighty-three percent of their wayfinding ability when smoke or fumes fill a cabin. The floor path is the answer to that number.""",
   "airplane cabin aisle floor", "GLOWS WITHOUT POWER")
sc("""This is also why the crew dims the cabin lights for takeoff and landing at night. Airline pilot Patrick Smith explains that pre-adjusting your eyes means you will not be suddenly blinded while dashing for the doors in darkness or smoke. And with dim lights inside, the crew can also see fire or debris outside the windows. The dark cabin is not about mood. It is about the first ninety seconds of an emergency.""",
   "airplane cabin night dim lights", "WHY THE LIGHTS GO DOWN")

# ---------- 2. SMOKE DETECTOR ----------
part(2, "The smoke detector in the lavatory", "WHY IS THIS DETECTOR HERE?", "Why Every Airplane Bathroom Has This",
     """Why is there a smoke detector on the ceiling of every airplane bathroom? Because a lavatory is a small closed room where nobody is watching. On Air Canada flight seven ninety-seven, the fire started in or around the rear lavatory, and it was spreading behind the panels before anyone understood how bad it was. Minutes matter in a fire at thirty thousand feet, because there is nowhere to go. After that flight, lavatory smoke detectors became mandatory. The FAA required them in nineteen eighty-six, and gave airlines eighteen months to install them.""",
     "aircraft lavatory smoke detector")
sc("""The detector does two jobs. It warns the crew early, while the fire is still small enough to fight with a handheld extinguisher. And it stops a lot of fires before they start, because it catches people who try to smoke in secret. Tampering with it is a serious federal offense in the United States, and the warning sign on the door tells you so. That little dome is watching on behalf of everyone on board.""",
   "airplane lavatory interior", "EARLY WARNING")
sc("""In the same period, the FAA also added Halon fire extinguishers to every commercial airliner in nineteen eighty-six, with two required per aircraft in addition to the other extinguishers. Halon smothers a fire chemically, without the mess of powder, which matters in a sealed cabin full of people. Detection, then suppression. That is the playbook that came out of Cincinnati.""",
   "Halon fire extinguisher aircraft", "THEN: HALON")

# ---------- 3. TRASH BIN EXTINGUISHER ----------
part(3, "The extinguisher in the trash bin", "WHY IS THIS TRASH BIN SPECIAL?", "The Secret Inside Airplane Trash Bins",
     """Why does the trash bin in an airplane bathroom have its own fire extinguisher? Because it is the most likely place for a fire to start. It is full of paper towels, and it is exactly where someone might throw a cigarette they were not supposed to light. So hidden above the bin is a small automatic extinguisher. When the heat rises, it fires by itself, and floods the bin. No crew member has to notice. The FAA made these automatic bin extinguishers mandatory in nineteen eighty-seven, with a two-year deadline.""",
     "aircraft lavatory waste bin")
sc("""The flap on top of the bin is part of the same idea. It springs closed after you push something through, so a fire inside starves of air and stays contained. And this is the same reason the bathroom still has an ashtray, even though smoking is banned. The rules assume that someone, someday, will break the rules, and they give that person a safe place to put out the cigarette, instead of the trash.""",
   "airplane lavatory door ashtray", "BUILT FOR RULE BREAKERS")

sc("""Think about why automatic matters here. A lavatory fire often starts when the door is closed and nobody is inside, or when the only person inside is the one who started it. A crew member might not walk past for many minutes. The bin extinguisher does not need anyone to notice, decide, or act. It turns the most dangerous corner of the cabin into one that defends itself.""",
   "aircraft galley lavatory", "NO HUMAN NEEDED")

# ---------- 4. SEAT CUSHIONS ----------
part(4, "The seat cushions", "WHY IS THIS SEAT SO SPECIAL?", "Your Airplane Seat Is Fireproof. Here's Why.",
     """Why is the cushion of your airplane seat so special? Because it is fire blocked. Ordinary foam burns fast and releases thick toxic smoke, and in a cabin fire, the seats are the biggest fuel load in the room. In October nineteen eighty-four, the FAA set a tough new test for seat cushions, using a kerosene burner. The airlines replaced six hundred fifty thousand cushions across the US fleet. In tests, the new cushions gave passengers forty to sixty seconds of extra time to escape. In a fire, forty seconds can be the whole difference.""",
     "airplane seats cabin economy")
sc("""The walls and ceiling got the same treatment. A nineteen eighty-five standard targeted the big panels, the ceilings, the walls, the galleys and the overhead bins, to delay what firefighters call flashover, the moment when a whole room ignites at once. Airplanes built after August nineteen ninety had to meet the final, lower heat release level. That is the exact thing that killed so many people in Cincinnati.""",
   "airplane cabin overhead bins ceiling", "DELAYING THE FLASHOVER")
sc("""Notice the pattern. Nobody could promise that a fire would never happen. So engineers attacked time. Lights that show the way out. Detectors that warn early. Extinguishers that fire by themselves. Materials that burn slower. Each one adds seconds, and together they turn an unsurvivable cabin into one where people can walk out. Which brings us to the most famous object in the safety briefing.""",
   "aircraft cabin evacuation drill", "THE WAR AGAINST TIME")

# ---------- 5. OXYGEN MASK ----------
part(5, "The oxygen mask", "WHERE DOES THIS OXYGEN COME FROM?", "Where Does Airplane Mask Oxygen Come From?",
     """Where does the oxygen in the drop down mask actually come from? There is no oxygen tank above your seat. There is a chemical generator. When you pull the mask, a spring fires a small cap that ignites a core of sodium chlorate mixed with iron, and as it burns, it releases almost pure oxygen. Once it starts, it cannot be stopped. It runs for about twelve to twenty minutes, enough for the pilots to dive down to around ten thousand feet, where you can breathe on your own. And the bag may not inflate even when the oxygen is flowing.""",
     "aircraft oxygen masks deployed cabin")
sc("""Why the hurry? Because at forty thousand feet, the FAA estimates the time of useful consciousness at less than ten seconds. That is why the briefing tells you to put your own mask on first. And the generator gets hot. Its case typically reaches four hundred fifty to five hundred degrees Fahrenheit, and passengers often notice a burning smell. That smell is normal. It is the chemistry doing its job.""",
   "oxygen mask airplane", "UNDER 10 SECONDS AT 40,000 FT")
sc("""That heat has a dark side. On the eleventh of May, nineteen ninety-six, ValuJet flight five ninety-two crashed into the Florida Everglades, killing all one hundred ten people on board. Expired oxygen generators, wrongly labeled as empty and missing their safety caps, had been loaded in the cargo hold. They ignited, and because they make their own oxygen, the fire fed itself. After that, these generators were banned as cargo on passenger airplanes.""",
   "Florida Everglades aerial", "VALUJET 592: THE OTHER SIDE")

# ---------- 6. 16G SEATS ----------
part(6, "The seat frame", "WHY IS THIS SEAT BUILT LIKE A TANK?", "Airplane Seats Are Crash Tested Like Cars",
     """Why is a thin airplane seat built to survive sixteen times the force of gravity? Because most airplane accidents are survivable, if your seat stays attached to the floor. For decades, seats were only approved to a static standard of nine G, with no test of what happened to the person sitting in them. In nineteen eighty-eight, the FAA required newly designed airliners to use sixteen G seats, tested dynamically with a crash test dummy, like a car. And airplanes built after October twenty-seventh, two thousand nine, had to meet the sixteen G standard too.""",
     "aircraft seats crash test")
sc("""The difference is huge. A static test just pulls on a seat slowly. A dynamic test fires it down a sled at high speed and stops it violently, and measures what the dummy's head, spine and legs experience. A seat that tears loose turns into a projectile, and it also blocks the aisle that everyone else needs to escape. A seat that holds keeps you in place, and keeps the path open.""",
   "airplane seat row aisle", "9G STATIC VS 16G DYNAMIC")

sc("""And it is not only the seat. The same logic reaches the flight attendants' jump seats, the seat belts, and the way overhead bins are latched, because anything that comes loose in a crash becomes something that hurts people. The goal is simple to say and hard to build. When the airplane stops, the cabin should still look like a cabin, with every seat in place and every aisle open, so that everyone can stand up and walk out.""",
   "airplane cabin seats overhead bins", "KEEP THE CABIN INTACT")

# ---------- 7. ESCAPE SLIDE ----------
part(7, "The escape slide", "WHY IS THIS DOOR SO HEAVY?", "The Hidden Slide in Every Airplane Door",
     """Why is the bottom of every airplane door so thick and heavy? Because there is an inflatable slide packed inside it. Open the door in an emergency, and the slide inflates in about six seconds, using stored gas. It has to, because of one of the toughest rules in aviation. To be certified, an airliner must prove that everyone on board can be evacuated in ninety seconds, using only half the exits, with a realistic mix of passengers. Ninety seconds is roughly how long the cabin of Air Canada seven ninety-seven had after the doors opened.""",
     "airplane evacuation slide inflated")
sc("""On airplanes that fly over water, many of those slides are slide rafts. After everyone is out, the crew can detach them, and they float as life rafts holding thirty to seventy people. So the same object that gets you down to the runway in a few seconds can also keep you alive in the ocean. It is one of the most cleverly packed pieces of equipment in aviation.""",
   "aircraft slide raft water", "SLIDE BY LAND, RAFT AT SEA")

sc("""The ninety second test is brutal. Manufacturers fill a cabin with volunteers, block half of the exits, turn off the normal lights, and start the clock. Only the floor lighting and the emergency lights help people find the way. Everything in this video meets in that test. The lights, the seats that stayed in place, the slides that inflate in seconds, and the crew who knows exactly what to shout. If the airplane cannot empty in time, it cannot be certified.""",
   "aircraft evacuation test", "THE 90 SECOND TEST")

# ---------- 8. ARMED DOORS ----------
part(8, "Arm the doors and cross check", "WHAT DOES ARM THE DOORS MEAN?", "What 'Arm the Doors and Cross Check' Really Means",
     """What does it mean when the crew says arm the doors and cross check? Arming a door connects the packed slide to the floor of the airplane. If an armed door is opened, the slide blasts out and inflates automatically, with no extra steps, because in an emergency, there is no time for extra steps. Cross check means a second flight attendant confirms it was done. Before the jet bridge comes back at the gate, the doors are disarmed, so the slide does not explode onto the ground crew. It is a tiny ritual hiding a powerful machine.""",
     "airplane door slide armed lever")
sc("""That is also why the crew watches that door so carefully. A slide deployed by accident at the gate is not just embarrassing. It can injure someone, it takes the airplane out of service until the slide is repacked or replaced, and it costs the airline real money. So the arming lever is designed to be deliberate, colored, and checked twice. The cross check exists because one person can make a mistake, and two rarely make the same one.""",
   "flight attendant aircraft door", "TWO PEOPLE. ONE DOOR.")

# ---------- 9. LIFE VEST ----------
part(9, "The life vest", "WHY NOT INFLATE IT INSIDE?", "Why You Never Inflate a Life Vest Inside the Plane",
     """Why does the safety briefing tell you not to inflate your life vest until you are outside the airplane? Because it can trap you. On the twenty-third of November, nineteen ninety-six, a hijacked Ethiopian Airlines Boeing seven sixty-seven ran out of fuel and ditched in the ocean near the Comoros Islands. Some passengers survived the impact, but had already inflated their vests inside the cabin. As water rushed in, the vests lifted them toward the ceiling, and they could not swim down to the exits. They drowned inside the airplane. The instruction exists because of them.""",
     "aircraft life vest under seat")
sc("""Of the one hundred seventy-five people on board that flight, one hundred twenty-five died, including the three hijackers, and fifty survived. The pilots managed to put the airplane down in shallow water off a beach, which is part of why anyone lived at all. So when you hear that line in the briefing, do not inflate the vest inside the aircraft, remember that it is not a formality. It is a lesson.""",
   "Grande Comore beach", "ETHIOPIAN 961: 50 SURVIVED")
sc("""The vest has other small details with big reasons. A light that switches on in water, so rescuers can find you at night. A whistle, because a voice gets tired and a whistle carries. And manual tubes to top up the air if the gas cartridge fails. Every part of that yellow vest assumes you are cold, in the dark, and waiting for someone to find you.""",
   "life jacket whistle light aviation", "THE LIGHT AND THE WHISTLE")

# ---------- 10. COCKPIT DOOR ----------
part(10, "The cockpit door", "WHY IS THIS DOOR BULLETPROOF?", "Why the Cockpit Door Is Bulletproof",
     """Why is the cockpit door on a passenger jet bulletproof? Before two thousand one, cockpit doors were light and easy to open. After the September eleventh attacks, airlines first reinforced their doors with metal bars, and then, by April two thousand three, every large commercial airplane in the United States had a bulletproof cockpit door. It stays locked during flight. The pilots control who comes in. It is the one door on the airplane designed to keep people out, not to let them escape.""",
     "aircraft cockpit door")
sc("""But a locked door creates new problems, and engineers and crews have had to manage them. Pilots still need to leave for the restroom or swap crews on long flights. As one pilot put it in two thousand three, it's a barrier when it's closed, it's an entry when it's open. That is why you will often see a cart or a flight attendant blocking the aisle while the door is open. Every safety device has a weak moment, and the procedures exist to cover it.""",
   "airliner cockpit pilots", "THE WEAK MOMENT")

sc("""There is a lesson here that goes beyond the door itself. Safety on an airplane is a balance between getting people out fast and keeping the wrong people out. Every exit, every lock, and every rule is a compromise between those two goals. The cockpit door is the clearest example, because it was built for a threat that the people who designed the original cabin never imagined.""",
   "airliner cockpit door cabin", "A BALANCE OF TWO FEARS")

# ---------- VERDICT ----------
sc("""So here are the ten. Lights on the floor that glow without power. A detector that watches the bathroom, and an extinguisher hidden in the trash. Cushions that buy forty seconds, a mask that burns to give you air, and a seat built for sixteen G. A slide that inflates in six seconds, a door ritual that keeps it under control, a vest you must not inflate inside, and a door that keeps people out. Most of them were paid for by a tragedy.""",
   "airliner cabin evacuation", "10 THINGS. 10 LESSONS.", chapter="The verdict", cuts=6)
sc("""The next time you board, look for them. Count the floor lights, find the thick bulge at the bottom of the door where the slide is packed, and read the sign on the bathroom detector. Then remember that flying is as safe as it is because people refused to accept the same accident twice. Subscribe to Machine Reverse for more machines explained part by part, and tell us which safety feature you want explained next.""",
   "airliner boarding passengers", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Economy Plus seat on a 737 Max.jpg', 0.5, 0.88),
    2: ('File:Econamy class lavatory.jpg', 0.6, 0.08),
    3: ('File:Trash bin signage in aircraft.jpg', 0.22, 0.4),
    4: ('File:JP 沖繩 Okinawa 亞洲航空 AirAsia flying to HKG flight aircraft economy class interior seats February 2026 N13P 01.jpg', 0.3, 0.52),
    5: ('File:PECO Passenger Service Unit.jpg', 0.15, 0.72),
    6: ('File:Controlled impact demonstration dummies.jpg', 0.42, 0.85),
    7: ('File:SP-LPC LO16 Flight escape slide.png', 0.38, 0.3),
    8: ('File:Deflated evacuation slide on an Airbus A320.jpg', 0.45, 0.4),
    9: ('File:Infant Life Vest 婴儿救生衣.jpg', 0.5, 0.5),
    10: ('File:Cockpit door Airbus A319-100 D-AKNM Germanwings.jpg', 0.25, 0.5),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video02", "title": "Why Are There Lights on the Floor of Every Airplane?",
           "length_scale": 1.6, "scenes": S}, open("videos/video02/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
