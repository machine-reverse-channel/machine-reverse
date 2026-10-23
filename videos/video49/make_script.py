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
sc("""In Japan, a train has carried people at six hundred three kilometers an hour, faster than the takeoff speed of an airliner. And it did it without touching the ground. Maglev trains have no wheels on the rails at full speed. They float, held up by magnets, a few millimeters or a few centimeters above the track. Today, eleven parts of a floating train, and why each one exists.""",
   "L0 series maglev", "A TRAIN THAT FLOATS", cuts=8, chapter="Intro")
sc("""The idea is more than a hundred years old. Inventors in the early nineteen hundreds dreamed of trains lifted by magnets, and in the nineteen sixties and seventies, Germany and Japan started building real ones. The promise was simple. No wheels means no rolling friction, no wear on rails, and almost no vibration. The only thing slowing the train down is the air.""",
   "Transrapid", "NO WHEELS, NO WEAR")
sc("""As always, every fact comes from a named source, railway operators, engineering references, and official accident reports, all listed in the description. Let's start with the most commercial maglev on Earth, the one in Shanghai.""",
   "Shanghai Maglev", "WHY DOES THIS EXIST?")

# ---------- 1. WRAP ----------
part(1, "The arms that hug the track", "WHY DOES THIS TRAIN HUG THE TRACK?", "Why Does a Maglev Train Wrap Around Its Track?",
     """Why does this maglev train wrap around its track like a hand around a bar? Because it does not push itself up. It pulls. On the German Transrapid design, used in Shanghai, the train has arms that reach around and under the edges of the guideway. Electromagnets on those arms sit under a steel rail on the underside of the track, and they attract it. The magnets pull upward toward the rail, lifting the whole train.""",
     "Transrapid")
sc("""This is called electromagnetic suspension. It works even when the train is standing still, so the train floats at the station too. And because the arms wrap around the guideway, the train physically cannot jump off. Other magnets on the sides keep it centered, so it does not rub against the guideway in curves or in wind.""",
   "Transrapid guideway", "IT CANNOT JUMP OFF")
sc("""The Shanghai Maglev opened for commercial service in two thousand four, linking the city to Pudong airport, about thirty kilometers away. For years, it ran at up to four hundred thirty-one kilometers an hour in daily service, covering the trip in around eight minutes. It is still the most famous floating train that ordinary passengers can ride.""",
   "Shanghai Maglev", "AIRPORT IN 8 MINUTES")

# ---------- 2. GAP ----------
part(2, "The 10 millimeter gap", "WHY IS THIS GAP ONLY 10 MILLIMETERS?", "Why Does This Train Float Only 1 Centimeter Up?",
     """Why does the Transrapid float only about a centimeter above its track? Because magnetic attraction is unstable. If the magnet gets a little closer to the steel rail, the pull gets much stronger, and it snaps against it. If it moves a little away, the pull gets weaker, and the train drops. There is no natural balance point. So the gap must be controlled actively, all the time.""",
     "Transrapid 07")
sc("""Sensors measure the gap continuously, and a computer adjusts the current in the electromagnets thousands of times per second, holding the gap at around ten millimeters. It is like balancing a broom on your hand, but done by electronics, so fast that passengers never notice. If the power fails, the train settles down onto skids, which act as emergency landing gear.""",
   "maglev guideway", "BALANCING A BROOM")
sc("""Because the gap is so small, the guideway has to be built with extreme precision, often to within a few millimeters along its whole length. That is one of the reasons maglev lines are so expensive. A normal railway can be adjusted with stones. A maglev guideway must be nearly perfect from the start.""",
   "Emsland test facility", "NEARLY PERFECT")

# ---------- 3. LINEAR MOTOR ----------
part(3, "The motor in the track", "WHY IS THE MOTOR IN THE TRACK?", "Why Is a Maglev's Motor Built Into the Track?",
     """Why doesn't a maglev train have an engine? Because the motor is in the track. Imagine a normal electric motor, with its round stator and spinning rotor, cut open and unrolled into a long flat line. That is a linear motor. Coils along the guideway create a magnetic wave that travels along the track, and the train's magnets are dragged along by it, like a surfer on a wave.""",
     "The Rail of Linimo")
sc("""To go faster, the control center makes the wave travel faster. To brake, it reverses the wave. The train is pushed and stopped by the track itself, with no gears, no wheels, and no friction. That is also why maglev trains can climb steeper slopes and accelerate harder than many normal trains.""",
   "Linimo", "A SURFER ON A WAVE")
sc("""On some designs, the guideway is powered only in the section where the train is. As the train moves, the power moves with it, section by section. It saves energy, and it means two trains cannot easily drive into each other, because the track decides where each train can go. The guideway is not just a road. It is the engine.""",
   "maglev train guideway", "THE TRACK IS THE ENGINE")

# ---------- 4. SUPERCONDUCTING MAGNETS ----------
part(4, "The frozen magnets", "WHY ARE THESE MAGNETS COLDER THAN SPACE?", "Why Are Japan's Maglev Magnets Colder Than Space?",
     """Why does Japan's maglev carry magnets colder than outer space? The Japanese system, called SCMaglev, uses superconducting magnets. When certain materials are cooled to extreme cold, close to absolute zero, their electrical resistance disappears. A current can flow in them almost forever without losing energy, creating a magnetic field far stronger than a normal electromagnet of the same size.""",
     "JR Maglev-Model-truck")
sc("""The magnets on the train's bogies are cooled with liquid helium, around minus two hundred sixty-nine degrees Celsius, and kept inside insulated containers like super thermos flasks. Japan has also tested magnets that use other superconducting materials at less extreme temperatures, to make the system simpler and cheaper.""",
   "liquid helium", "MINUS 269 DEGREES")
sc("""These strong magnets allow a much bigger gap than the German system, around ten centimeters. That gives a large safety margin in earthquakes, a big concern in Japan. On April twenty-first, twenty fifteen, a seven-car L zero series train reached six hundred three kilometers an hour on the Yamanashi test line, the world record for a train.""",
   "L0 series", "603 KM/H")

# ---------- 5. WHEELS ----------
part(5, "The wheels it still needs", "WHY DOES A FLOATING TRAIN HAVE WHEELS?", "Why Does a Floating Train Still Have Wheels?",
     """Why does Japan's floating train still have rubber wheels? Because it can only float when it is moving fast. SCMaglev uses electrodynamic suspension. The train's magnets passing by coils in the guideway walls induce currents in those coils, and those currents create magnetic fields that push the train up. No motion, no current, no lift. The faster it goes, the stronger the lift.""",
     "L0 series maglev")
sc("""So at low speed, the train runs on rubber tyres, like an airplane taxiing. When it passes about one hundred fifty kilometers an hour, the magnetic lift becomes strong enough, and the wheels retract, just like landing gear. When it slows down, the wheels come out again before it settles. Passengers feel a small change, like a plane leaving the runway.""",
   "SC Maglev Test Ride", "LIKE LANDING GEAR")
sc("""This is the big difference between the two main maglev families. The German system pulls itself up with controlled electromagnets and floats even when stopped. The Japanese system is pushed up by induced currents and needs speed. Both float. They just do it in opposite ways.""",
   "Transrapid 09", "PULL VS PUSH")

# ---------- 6. FIGURE 8 COILS ----------
part(6, "The figure 8 coils", "WHY ARE THESE COILS SHAPED LIKE AN 8?", "Why Do Maglev Tracks Have Figure 8 Coils?",
     """Why does the Japanese maglev guideway have coils shaped like the number eight? They are called null flux coils, and they are a clever trick. Each coil has an upper loop and a lower loop wound in opposite directions. When the train's magnet passes exactly in the middle, the two loops cancel out and no current flows. No current, no drag.""",
     "JR Maglev-Guide")
sc("""But if the train drops a little, the magnet sits more in front of the lower loop, the balance breaks, current flows, and the coil pushes the train back up and pulls it toward the center. The coils also connect across the guideway, so if the train drifts to one side, it is pushed back. The train is held in the middle automatically, without any computer.""",
   "Yamanashi maglev test line", "SELF CENTERING")
sc("""That is the beauty of the design. A heavy train is lifted and steered by coils that do nothing at all while everything is perfect, and push back only when something goes wrong. Physics does the control work, without sensors, without software, thousands of times per second.""",
   "maglev guideway coils", "PHYSICS DOES THE WORK")

# ---------- 7. SWITCH ----------
part(7, "The track that bends", "WHY DOES THIS WHOLE TRACK BEND?", "Why Does a Maglev Track Bend to Switch?",
     """How does a maglev train change tracks? A normal railway switch moves thin rails a few centimeters. But a maglev wraps around a thick guideway beam, so there are no thin rails to move. The answer is a switch that bends the whole beam. On the Transrapid, a steel section of guideway, up to around one hundred fifty meters long, is pushed sideways by motors, flexing gently into a curve that leads to the other track.""",
     "Transrapid01wissel")
sc("""Bending steel that big takes time, often several seconds, and the switch must lock perfectly in place before a train can pass. For high speed straight through, the beam is straight. For the branch, it bends. It is one of the strangest sights in railway engineering, a massive track that moves like a snake.""",
   "Transrapid02beweegbaar", "A TRACK LIKE A SNAKE")
sc("""Switches are one of the reasons maglev is hard to build into networks. Normal railways can branch, merge and cross easily, and trains can use old lines to reach city centers. Maglev needs its own guideway all the way, with no connection to the existing railway. Every station, depot and branch must be built new.""",
   "maglev viaduct", "ITS OWN WORLD")

# ---------- 8. GUIDEWAY ----------
part(8, "The guideway in the air", "WHY IS THIS TRACK UP IN THE AIR?", "Why Are Maglev Tracks Built Up in the Air?",
     """Why are many maglev tracks built high up on concrete pillars? Partly for safety. A train going four hundred kilometers an hour cannot share space with cars, people or animals. An elevated guideway separates the train from everything below. It also keeps the precise guideway away from flooding and ground movement, and takes less land than an embankment.""",
     "1999 Transrapid Test Facility Emsland")
sc("""In Germany, the Transrapid test line in Emsland was built mostly on pillars, with cows grazing in the fields below. Engineers tested trains there for decades, at speeds above four hundred kilometers an hour, and Germany hoped to sell the system to the world. But apart from Shanghai, almost nobody bought it.""",
   "Emsland Transrapid", "COWS BELOW, 400 KM/H ABOVE")
sc("""The reason was cost. A maglev line costs much more per kilometer than a high speed railway, and it cannot use any existing track. High speed trains on steel wheels kept getting faster, reaching three hundred twenty kilometers an hour in service. For most routes, the extra speed of maglev was not worth the extra price.""",
   "ICE high speed train", "NOT WORTH THE PRICE")

# ---------- 9. TUNNELS ----------
part(9, "The line under the mountains", "WHY IS THIS TRAIN BUILT MOSTLY UNDERGROUND?", "Why Will Japan's Maglev Run Mostly Underground?",
     """Why will Japan's new maglev line run mostly underground? The Chuo Shinkansen is planned to link Tokyo and Nagoya, and later Osaka, cutting the Tokyo to Nagoya trip to around forty minutes. To go that fast, it needs a nearly straight path. And between Tokyo and Nagoya are the Japanese Alps. So the line will run through the mountains, in tunnels, for most of its length, including deep under Tokyo.""",
     "Chuo Shinkansen construction")
sc("""Building it has been difficult. Tunnels under the Southern Alps are among the hardest in the world, and in Shizuoka Prefecture, local concerns about water flowing out of the river Oi through the tunnels delayed the work for years. The original opening target of twenty twenty-seven was abandoned, and the line is now expected to open years later.""",
   "Japanese Alps", "THROUGH THE ALPS")
sc("""Even with the delays, Japan continues to build it, partly as a backup for the old Tokaido Shinkansen, which is busy and exposed to earthquakes along the coast. A second line through the mountains, built for six hundred kilometers an hour, would give Japan two independent arteries between its biggest cities.""",
   "Tokaido Shinkansen", "A SECOND ARTERY")

# ---------- 10. LATHEN ----------
part(10, "The lesson of Lathen", "WHY DID THIS TEST TRACK CLOSE?", "Why Did Germany's Maglev Dream End?",
     """Why did Germany's own maglev test track close? On September twenty-second, two thousand six, a Transrapid train on the Emsland test track near Lathen hit a maintenance vehicle that had been left on the guideway. The train was traveling at around one hundred seventy kilometers an hour. Twenty-three people died. It was the first fatal accident in the history of the Transrapid.""",
     "Transrapid 07 in Lathen")
sc("""Investigators found that the system had no automatic way to detect that the maintenance vehicle was still on the track. The train was allowed to start based on human procedures, and those procedures failed. A floating, computer-controlled train was stopped by a simple question. Is the track clear?""",
   "maglev viaduct Emsland", "IS THE TRACK CLEAR?")
sc("""The test track closed a few years later, and Germany's dream of exporting the Transrapid faded. The lesson applies to every advanced machine. The most futuristic technology still depends on the most basic safety rules. Today, other countries, especially China, continue to develop new maglev trains, and the race to float is not over.""",
   "Shanghai Maglev 2", "THE RACE IS NOT OVER")

# ---------- 11. SHIELDING ----------
part(11, "The shielded cabin", "WHY IS THIS CABIN SHIELDED FROM MAGNETS?", "Why Are Maglev Passengers Shielded From the Magnets?",
     """Why do Japan's maglev cars need magnetic shielding? Because the superconducting magnets are extremely strong, and they sit on the bogies, right under the ends of the cars. Strong magnetic fields can affect things like pacemakers, credit cards and electronics. So the cars are designed with shielding, and the seats are placed so that passengers are kept away from the strongest fields.""",
     "SC Maglev Test Ride")
sc("""JR Central says the magnetic field inside the passenger area stays below international guidelines for public exposure. The bogies are placed between the cars, not under the seats, which keeps the magnets as far from people as possible. The boarding bridges at stations are also designed so passengers never walk close to the magnets.""",
   "maglev train interior", "BELOW THE GUIDELINES")
sc("""It is a reminder that a new technology brings new questions. A normal train never had to think about the magnetic field in its cabin. A maglev does, for every seat, every door and every station. Floating is not just about lifting a train. It is about making that train safe to sit in.""",
   "L0 series maglev station", "SAFE TO SIT IN")

# ---------- VERDICT ----------
sc("""So here are the eleven. Arms that hug the track and pull the train up. A gap of one centimeter, balanced thousands of times per second. A motor built into the track. Magnets colder than space, and wheels for low speed. Coils shaped like an eight, a track that bends like a snake, guideways in the air, a line through the mountains, a lesson from Lathen, and a cabin shielded from its own magnets.""",
   "L0 series maglev", "11 PARTS. 0 WHEELS ON THE RAIL.", chapter="The verdict", cuts=6)
sc("""A maglev looks like science fiction, but every part of it solves a very real problem. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Shanghai Maglev", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Transrapid 09.jpg", 0.45, 0.48),
    2: ("File:Transrapid 07 in Lathen 2020.jpg", 0.55, 0.52),
    3: ("File:The Rail of Linimo.jpg", 0.6, 0.5),
    4: ("File:JR Maglev-Model-truck.JPG", 0.5, 0.5),
    5: ("File:Series L0.JPG", 0.75, 0.85),
    6: ("File:JR Maglev-Guide.png", 0.82, 0.45),
    7: ("File:Transrapid01wissel.jpg", 0.5, 0.3),
    8: ("File:1999 Transrapid Test Facility Emsland 03.jpg", 0.5, 0.4),
    9: ("File:Chuo Shinkansen construction at Shinagawa Station, August 2024.jpg", 0.5, 0.6),
    10: ("File:Transrapid 07 in Lathen (2023).jpg", 0.5, 0.5),
    11: ("File:SC Maglev Test Ride (18278623709).jpg", 0.4, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video49", "title": "Why Does a Maglev Train Float?",
           "length_scale": 1.6, "scenes": S}, open("videos/video49/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
