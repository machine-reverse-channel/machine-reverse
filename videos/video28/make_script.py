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
sc("""Your car has one radiator. The Bugatti Veyron has ten. Not because Bugatti wanted to show off, but because a car that makes more than one thousand horsepower turns a huge amount of fuel into heat, and that heat has to go somewhere, or the car destroys itself in minutes. Today, ten parts of a Bugatti that exist because of one crazy goal, and why each one exists.""",
   "Bugatti Veyron", "WHY 10 RADIATORS?", cuts=8, chapter="Intro")
sc("""The goal came from Ferdinand Piech, the head of the Volkswagen Group at the end of the nineteen nineties. He wanted a car with more than one thousand metric horsepower, a top speed above four hundred kilometres per hour, and the comfort to drive it to the opera. Engineers said it was nearly impossible. The Veyron arrived in two thousand five, and every strange part on it is a solution to that goal.""",
   "Bugatti Veyron front", "1001 HORSEPOWER")
sc("""As always, every fact here comes from a named source, Bugatti, Volkswagen and automotive references, all listed in the description. Let's start with the heat.""",
   "Bugatti Veyron rear", "WHY DOES THIS EXIST?")

# ---------- 1. RADIATORS ----------
part(1, "The ten radiators", "WHY DOES THIS CAR NEED 10 RADIATORS?", "Why Does a Bugatti Need 10 Radiators?",
     """Why does a Bugatti Veyron need ten radiators? Because of a basic rule of engines. Only part of the energy in the fuel becomes motion. Most of it becomes heat. For every horsepower that pushes the car forward, an engine produces even more energy as heat. At full power, the Veyron's engine is producing a huge amount of heat, and a normal radiator would be overwhelmed in seconds.""",
     "Bugatti Veyron radiator")
sc("""So the heat is split into separate systems. Three radiators cool the engine. One heat exchanger cools the air coming from the turbochargers. Two serve the air conditioning. And separate coolers handle the engine oil, the gearbox oil, the differential oil, and the hydraulic oil that moves the rear wing. Ten in total, each one sized for its own job.""",
   "Bugatti Veyron side intake", "TEN JOBS, TEN RADIATORS")
sc("""That is why the Veyron is covered in openings. The big horseshoe grille, the intakes in the front, the openings on the sides and on the roof. They are not decoration. They are the mouths that feed air to the radiators. A Bugatti at full speed is as much a cooling machine as it is a car.""",
   "Bugatti Veyron air intakes", "A COOLING MACHINE")

# ---------- 2. W16 ----------
part(2, "The W16 engine", "WHY IS THIS ENGINE SHAPED LIKE A W?", "Why Does a Bugatti Have a W16 Engine?",
     """Why does a Bugatti have an engine shaped like a W? To fit sixteen cylinders into a short space. A V sixteen would have been very long, and a long engine makes a long, heavy car. Instead, the W sixteen is like two narrow V eight engines joined together at an angle. Seen from the front, the four rows of cylinders form a W.""",
     "Bugatti W16 engine")
sc("""The idea came from Volkswagen's VR six engine, which put six cylinders in a very narrow V so they could share one cylinder head. Bugatti's engineers took two of those narrow blocks and joined them on one crankshaft. The result is an eight litre engine with sixteen cylinders and sixty-four valves, about as long as a normal V eight.""",
   "Volkswagen VR6 engine", "TWO NARROW ENGINES IN ONE")
sc("""More cylinders means more power from the same engine speed, and smoother running. The W sixteen gave the Veyron its thousand horsepower, and later versions in the Chiron produced around fifteen hundred and more. It is one of the most complex production engines ever made, and it is also one of the reasons the car needs so many radiators.""",
   "Bugatti Chiron engine", "SIXTEEN CYLINDERS")

# ---------- 3. TURBOS ----------
part(3, "The four turbochargers", "WHY DOES THIS ENGINE HAVE 4 TURBOS?", "Why Does a Bugatti Engine Have 4 Turbos?",
     """Why does the Bugatti engine have four turbochargers? A turbo uses the exhaust gas to spin a turbine that pushes more air into the engine. More air means more fuel can burn, and more power. But one huge turbo would be slow to react. Four smaller turbos respond faster, and they can be shared among the sixteen cylinders.""",
     "Bugatti turbocharger")
sc("""On the Chiron, Bugatti made the turbos work in stages. At low engine speed, only two turbos are active, so they spin up quickly and the car responds immediately. At higher speed, the other two join in, and all four deliver full power. The driver feels a smooth, endless push, instead of a sudden kick.""",
   "Bugatti Chiron rear", "TWO, THEN FOUR")
sc("""Turbos also add heat, because compressing air makes it hot. Hot air is less dense and makes less power. That is why the Bugatti has a system to cool the compressed air before it enters the engine, with its own heat exchanger. One more radiator. Every part that adds power also adds heat.""",
   "intercooler", "POWER MEANS HEAT")

# ---------- 4. ROOF INTAKES ----------
part(4, "The roof intakes", "WHY ARE THERE SCOOPS BEHIND THE ROOF?", "Why Does a Bugatti Veyron Have Scoops on the Roof?",
     """Why does the Bugatti Veyron have two scoops behind the roof? They feed air to the engine. The W sixteen breathes an enormous amount of air at full power. The air on the roof is clean and fast, away from the hot air and dirt around the wheels. The scoops catch it and send it straight down to the engine's air intake.""",
     "Bugatti Veyron roof intake")
sc("""On a mid engined car, the engine sits right behind the passengers, and air has to find a way in. Many supercars use side intakes, but the roof scoops on the Veyron give a direct, short path to the engine. At high speed, the moving air even pushes itself in, like a gentle supercharger called ram air.""",
   "Bugatti Veyron top view", "CLEAN, FAST AIR")
sc("""Bugatti says that at full power, its W sixteen engines swallow tens of thousands of litres of air every minute. That is more air than a person breathes in several days. The scoops on the roof are the open mouth of that giant set of lungs.""",
   "Bugatti Veyron engine bay", "GIANT LUNGS")

# ---------- 5. AIRBRAKE ----------
part(5, "The airbrake wing", "WHY DOES THIS WING STAND UP?", "Why Does a Bugatti Wing Stand Up When Braking?",
     """Why does the rear wing of a Bugatti stand up when it brakes? It is an airbrake. Under hard braking at high speed, the wing tilts steeply, like a wall against the wind. The air pushes on it, adding a lot of braking force, and it pushes the rear of the car down, so the rear tyres can brake harder too.""",
     "Bugatti Veyron rear wing airbrake")
sc("""Stopping from more than four hundred kilometres per hour is one of the hardest jobs on the car. The brakes turn the car's energy into heat, and at that speed the amount of energy is enormous. The airbrake shares the work. It also stabilises the car, because heavy braking normally makes the rear go light and nervous.""",
   "Bugatti Chiron rear wing", "SHARING THE WORK")
sc("""The wing moves with hydraulics, and it changes its angle for different jobs. Low for top speed, higher for handling, and steep for braking. The hydraulic oil gets its own radiator, of course. On a Bugatti, even the wing has a cooling system.""",
   "Bugatti Veyron Super Sport", "EVEN THE WING IS COOLED")

# ---------- 6. FUEL TANK ----------
part(6, "The fuel tank", "WHY WOULD THIS TANK BE EMPTY IN 12 MINUTES?", "Why Would a Bugatti Run Out of Fuel in 12 Minutes?",
     """Why would a Bugatti Veyron run out of fuel in about twelve minutes at top speed? Because at full power, the engine burns fuel at an incredible rate. The Veyron's tank holds about one hundred litres. At top speed, the engine would use all of it in roughly twelve minutes, according to Bugatti's own figures.""",
     "Bugatti Veyron fuel cap")
sc("""That is the price of power. Every horsepower needs fuel, and a thousand horsepower needs a fire hose of it. In normal driving, the Veyron is much more reasonable, but still thirsty. The fuel system has multiple pumps to keep the engine fed, even under strong acceleration and cornering forces.""",
   "Bugatti Veyron driving", "A FIRE HOSE OF FUEL")
sc("""Twelve minutes at top speed sounds dramatic, but in reality it is almost impossible to stay at top speed that long. No public road and very few test tracks are long enough. The tyres are also designed for limited time at maximum speed. The fuel tank, the tyres and the cooling were all designed around the same few minutes of extreme speed.""",
   "Bugatti Chiron road", "A FEW MINUTES OF EXTREME")

# ---------- 7. HORSESHOE ----------
part(7, "The horseshoe grille", "WHY IS THE GRILLE SHAPED LIKE A HORSESHOE?", "Why Is the Bugatti Grille Shaped Like a Horseshoe?",
     """Why is the Bugatti grille shaped like a horseshoe? It is a tradition from the original Bugatti company, founded by Ettore Bugatti in Molsheim, France, in nineteen o nine. His classic cars carried a radiator shaped like a horseshoe, and it became the face of the brand. Ettore was a lover of horses, and the shape became part of the legend.""",
     "Bugatti Type 35")
sc("""On the modern Bugatti, the horseshoe is not just a logo. It is a real air intake, feeding cooling air to the radiators behind it. The designers had to make the brand's most famous shape work as an engineering part. Its size and position were tuned with the rest of the front intakes to feed the cooling system at four hundred kilometres per hour.""",
   "Bugatti Chiron front grille", "A LOGO THAT BREATHES")
sc("""The Bugatti Type thirty-five of the nineteen twenties, with its horseshoe radiator, was one of the most successful racing cars in history, winning more than a thousand races. When Volkswagen revived the brand, keeping that shape was a way of connecting the new hypercar to the old champion. One shape, a hundred years apart.""",
   "Bugatti Type 35 racing", "A HUNDRED YEARS APART")

# ---------- 8. C-LINE ----------
part(8, "The C line", "WHY IS THERE A GIANT C ON THE SIDE?", "Why Does a Bugatti Chiron Have a Giant C on the Side?",
     """Why does the Bugatti Chiron have a giant curved line on its side? It is called the Bugatti line, or the C line. It looks like a pure design signature, sweeping around the door. But it is also an air channel. The curve guides air into the intakes that feed the engine and the coolers.""",
     "Bugatti Chiron side")
sc("""The Chiron makes about fifteen hundred horsepower, half again as much as the original Veyron. More power meant even more heat, so the designers needed more air. Instead of adding more holes, they built a giant intake into the most visible line of the car. The style and the cooling are the same thing.""",
   "Bugatti Chiron", "STYLE IS COOLING")
sc("""This is a theme across all Bugatti design. Almost every surface has to do a job for the air, whether it is pushing the car down, feeding a radiator, or cooling the brakes. The designers like to say that form follows performance. On a car this fast, there is no space for a line that does nothing.""",
   "Bugatti Chiron rear lights", "FORM FOLLOWS PERFORMANCE")

# ---------- 9. GEARBOX ----------
part(9, "The gearbox", "WHY IS THIS GEARBOX SO SPECIAL?", "Why Does a Bugatti Need a Special Gearbox?",
     """Why does a Bugatti need such a special gearbox? Because no normal gearbox could handle the force. The W sixteen produces a huge twisting force, called torque, well over one thousand newton metres. A normal car gearbox would break. The Veyron uses a seven speed dual clutch gearbox, developed with the British engineering company Ricardo, built to survive that torque.""",
     "Bugatti Veyron gearbox")
sc("""It changes gear in a fraction of a second, without interrupting the power, using the same dual clutch idea as in racing cars. The gearbox also has to send power to all four wheels, because no two tyres could put a thousand horsepower onto the road. Four wheel drive is the only way the Bugatti can use its power from a standing start.""",
   "Bugatti Veyron launch", "ALL FOUR WHEELS")
sc("""And of course, the gearbox gets hot too. It has its own oil cooler, and so does the rear differential. If you count the radiators again, you will find them for the gearbox and the differential. The ten radiators are a list of everything the Bugatti's power touches.""",
   "Bugatti Veyron underside", "EVERYTHING THE POWER TOUCHES")

# ---------- 10. TEST TRACK ----------
part(10, "The test track", "WHY DOES THIS TRACK HAVE A 9 KM STRAIGHT?", "Why Does Bugatti Test on a Secret 9 km Straight?",
     """Why does Bugatti test its cars on a track with a straight about nine kilometres long? Because there are almost no places on Earth where a car can reach four hundred kilometres per hour. Volkswagen's test track at Ehra-Lessien, in Germany, has one of the longest straights of any test track in the world, and it is closed to the public.""",
     "Ehra-Lessien test track")
sc("""In twenty ten, the Veyron Super Sport set a production car record there of more than four hundred thirty-one kilometres per hour. In twenty nineteen, a modified Chiron, driven by Andy Wallace, became the first car to pass three hundred miles per hour, reaching about four hundred ninety kilometres per hour, at the same track.""",
   "Bugatti Chiron Super Sport 300+", "300 MILES PER HOUR")
sc("""At those speeds, the cooling, the tyres, the wing and the fuel are all at their very limit, and the straight must be long enough to accelerate and then stop safely. The ten radiators, the W sixteen, the airbrake and the special tyres all meet on that straight. It is the one place where the whole crazy design finally makes sense.""",
   "Bugatti Veyron Super Sport", "WHERE IT ALL MAKES SENSE")

# ---------- VERDICT ----------
sc("""So here are the ten. Ten radiators for ten kinds of heat. A W sixteen engine to fit sixteen cylinders. Four turbos that work in stages. Scoops on the roof, a wing that becomes a brake, a tank that empties in twelve minutes, a horseshoe that breathes, a C that feeds air, a gearbox built for crazy torque, and a nine kilometre straight to use it all.""",
   "Bugatti Chiron and Veyron", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A Bugatti is what happens when engineers are told that the impossible is the target. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Bugatti night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Bugatti Veyron EB 16.4 (2008) (52570116555).jpg", 0.45, 0.8),
    2: ("File:Bugatti W16, Berlin (1X7A3942).jpg", 0.35, 0.3),
    3: ("File:Twin Turbos on one side of a Bugatti W16 engine (53249394775).jpg", 0.3, 0.45),
    4: ("File:Bugatti Veyron Engine 1X7A7930.jpg", 0.2, 0.3),
    5: ("File:Bugatti Veyron EB 16.4 (2008) (52569212082).jpg", 0.16, 0.3),
    6: ("File:Bugatti-veyron-1zu18.jpg", 0.68, 0.42),
    7: ("File:Bugatti Veyron EB 16.4 Grand Sport (2010) (52129289255).jpg", 0.4, 0.5),
    8: ("File:Bugatti Chiron, Auto 2025, Zurich (20251029-P1074241).jpg", 0.2, 0.45),
    9: ("File:W16 Engine Bugatti Chiron-P1010490.jpg", 0.65, 0.55),
    10: ("File:2020 Bugatti Chiron Super Sport 300+ Rear.jpg", 0.1, 0.55),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video28", "title": "Why Does a Bugatti Need 10 Radiators?",
           "length_scale": 1.6, "scenes": S}, open("videos/video28/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
