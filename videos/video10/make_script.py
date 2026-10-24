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
sc("""On a cold morning, before takeoff, a truck with a long arm drives up to your airplane and sprays it with a hot orange liquid, and then sometimes with a green one. It looks like a car wash. It is actually one of the most important safety steps in winter flying, because a layer of frost thinner than sandpaper can stop a wing from lifting. Today, ten parts that keep airplanes free of ice, and why each one exists.""",
   "aircraft deicing orange fluid", "WHY THE ORANGE LIQUID?", cuts=8, chapter="Intro")
sc("""Ice is one of the oldest enemies of aviation. It changes the shape of the wing, blocks sensors, and adds weight in places where it does not belong. Over the decades, airplanes and airports have collected a whole set of tools against it, some on the ground, some built into the airplane, and many of them were added after a crash.""",
   "airplane snow airport", "THE OLDEST ENEMY")
sc("""As always, every fact here comes from a named source, the Federal Aviation Administration, accident reports and aviation references, all listed in the description. Let's start with the orange liquid.""",
   "deicing truck airport", "WHY DOES THIS EXIST?")

# ---------- 1. TYPE I ----------
part(1, "The orange liquid", "WHY IS THIS LIQUID ORANGE?", "Why Do Airports Spray Orange Liquid on Planes?",
     """Why do airports spray airplanes with hot orange liquid? It is de-icing fluid, mostly glycol mixed with water, the same family of chemicals as the antifreeze in a car. It is sprayed hot, between about fifty-five and eighty degrees Celsius, at high pressure. The heat melts the snow and ice, the pressure blasts it off, and the glycol stops it from freezing again for a few minutes.""",
     "aircraft deicing Type I fluid")
sc("""This is called Type one fluid, and it is dyed orange on purpose. Glycol and water are almost invisible on a white airplane, so the color lets the crew on the truck see exactly which parts of the wing and tail are covered, and which they have missed. A big airliner can need hundreds of gallons, often between five hundred and one thousand.""",
   "deicing truck spraying wing", "THE COLOR SHOWS WHAT'S COVERED")
sc("""Orange fluid has one weakness. It is thin, and it flows off the wing quickly. It cleans the airplane, but it does not protect it for long. If snow keeps falling, the wing can be dirty again in a few minutes. That is why, in heavy snow, a second truck comes, with a different color.""",
   "snow falling airplane wing", "CLEAN, BUT NOT FOR LONG")

# ---------- 2. TYPE IV ----------
part(2, "The green liquid", "WHY IS THIS LIQUID GREEN?", "Why Do Airports Spray Green Liquid on Planes?",
     """Why do some airplanes get sprayed with green liquid after the orange one? Green means Type four anti-icing fluid. It is thick, like a gel, and it stays on the wing as a protective coat. Falling snow lands on it and melts into it instead of freezing to the wing. Depending on the weather, it can protect the airplane for much longer than the orange fluid.""",
     "Type IV anti-icing fluid green")
sc("""The clever part is that the gel is designed to stay on while the airplane is standing still, and to slide off during the takeoff run. As the airplane accelerates, the airflow shears the thick fluid off the wing, so it is gone by the time the wing needs to lift. It is called a pseudoplastic fluid, thick when still, thin when moving.""",
   "airplane takeoff snow", "THICK WHEN STILL")
sc("""Pilots use tables called holdover times, which say how long each fluid protects the airplane in each kind of weather. For the thin orange fluid, it can be just a few minutes. For the thick green one, it can be more than an hour in light conditions. If the time runs out before takeoff, the airplane must go back and be sprayed again.""",
   "deicing pad airplanes queue", "HOLDOVER TIME")

# ---------- 3. THE CRASH THAT CHANGED IT ----------
part(3, "The clean wing rule", "WHY MUST THIS WING BE PERFECTLY CLEAN?", "Why Can't Planes Take Off With Snow on the Wings?",
     """Why must a wing be perfectly clean before takeoff? Because a wing works only if its shape is exact. Even a thin layer of frost or snow makes the top surface rough, the air separates from the wing earlier, and the wing makes less lift and stalls at a lower angle. The rule is called the clean aircraft concept. No frost, ice or snow on the wings, tail or controls at takeoff.""",
     "airplane wing frost")
sc("""On the thirteenth of January nineteen eighty-two, Air Florida flight ninety took off from Washington National Airport in a snowstorm. It had been de-iced, but it waited a long time in line, and snow and ice built up again. The crew also did not turn on the engines' anti-ice system. The airplane barely climbed, hit a bridge, and fell into the frozen Potomac River. Seventy-eight people died.""",
   "Potomac River winter Washington", "AIR FLORIDA 90")
sc("""That crash and others changed winter flying. Holdover times, better fluids and stricter checks before takeoff all followed. Today, if pilots have any doubt about the wings, they go back for another spray. Being late is always better than taking off with a dirty wing.""",
   "aircraft deicing night", "BETTER LATE")

# ---------- 4. DEICING PAD ----------
part(4, "The de-icing pad", "WHY IS THERE A PARKING LOT NEAR THE RUNWAY?", "Why Do Big Airports Have a Special Parking Lot for De-Icing?",
     """Why do many big airports have a special parking area right next to the runway? It is the de-icing pad. Instead of spraying the airplane at the gate and then taxiing for twenty minutes, the airplane is sprayed just before takeoff, so the protection lasts until it leaves the ground. Several airplanes can be treated at the same time, like a drive through.""",
     "deicing pad airport")
sc("""The pads are also built for the environment. The used fluid is full of glycol, and when it breaks down in rivers and lakes, it uses up oxygen that fish need. So the pads have special drains, and some airports use glycol recovery trucks that vacuum up the used fluid and slush. Some of it can even be recycled.""",
   "glycol recovery vehicle", "THE FLUID IS RECOVERED")
sc("""At the pad, the crew stays in contact by radio with the de-icing team, who tell them which fluid was used and when the spraying started. That start time is when the holdover clock begins. From that moment, the pilots know exactly how much time they have to take off.""",
   "deicing truck cockpit view", "THE CLOCK STARTS")

# ---------- 5. WING ANTI-ICE ----------
part(5, "The hot wing edges", "WHY IS THE FRONT OF THIS WING HOT?", "Why Is the Front of an Airplane Wing Heated?",
     """Why are the front edges of an airliner's wings heated in flight? Because flying through clouds below freezing can build ice on the leading edge, the part that hits the air first. On many jets, hot air is taken from the engines, called bleed air, and piped through the inside of the leading edge, so ice cannot form there.""",
     "wing leading edge slats")
sc("""Ice in flight is different from snow on the ground. Clouds can contain supercooled water, tiny droplets still liquid below zero degrees, that freeze the instant they touch the airplane. The leading edge collects most of them, so that is where the heat goes. Newer airplanes like the Boeing seven eight seven use electric heating mats instead of bleed air.""",
   "airplane wing clouds", "SUPERCOOLED WATER")
sc("""The pilots turn the wing anti-ice on when they fly in icing conditions, and many airplanes have an ice detector that warns them. Heating a wing uses energy, so the system is not on all the time. It is a tool for the moments when the air is full of water that wants to freeze.""",
   "airliner cockpit overhead panel anti-ice", "ON WHEN NEEDED")

# ---------- 6. ENGINE INLET ----------
part(6, "The hot engine lip", "WHY IS THE FRONT OF THE ENGINE HEATED?", "Why Are Jet Engine Inlets Heated?",
     """Why is the front lip of a jet engine heated? Because ice on the inlet can break off and be swallowed by the engine, damaging the fan blades, and ice can also disturb the airflow into the engine. Hot air from the engine itself is piped into the lip of the inlet, keeping it above freezing.""",
     "jet engine inlet lip")
sc("""That system was part of the Air Florida story. Investigators found that the crew did not turn on engine anti-ice. Ice blocked a pressure probe in the engines that measures thrust, so the instruments showed more power than the engines were really making. The pilots took off with less thrust than they thought.""",
   "jet engine snow", "THE WRONG NUMBERS")
sc("""Today, engine anti-ice is on many checklists for taxi and takeoff in cold, wet weather. A small switch on the overhead panel, a little hot air sent to the right place, and the engine can breathe through a snowstorm.""",
   "engine anti-ice switch cockpit", "A SMALL SWITCH")

# ---------- 7. BOOTS ----------
part(7, "The rubber boots", "WHY IS THIS WING EDGE MADE OF RUBBER?", "Why Do Some Planes Have Rubber on Their Wings?",
     """Why do many propeller airplanes have black rubber strips on the front of their wings? They are de-icing boots. When ice builds up, air is pumped into tubes inside the rubber, the boots inflate, and the ice cracks and is blown away by the wind. Then they deflate again. Smaller airplanes use them because they do not have much hot air from their engines to spare.""",
     "deicing boots wing")
sc("""Boots remove ice after it forms, so they only protect the area they cover. On the thirty-first of October nineteen ninety-four, American Eagle flight four one eight four, an ATR seventy-two, was holding near Roselawn, Indiana, in freezing drizzle. Large drops froze into a ridge of ice behind the boots, where they could not reach. The airplane rolled out of control and crashed, killing all sixty-eight people on board.""",
   "ATR 72 aircraft", "ROSELAWN 1994")
sc("""After Roselawn, the rules for flying in freezing drizzle and large drops were rewritten, and pilots were trained to recognize the signs of severe icing. The boots did their job. The problem was ice in a place the boots could not reach. In aviation, protection ends exactly where the protected area ends.""",
   "turboprop wing leading edge", "WHERE PROTECTION ENDS")

# ---------- 8. PITOT ----------
part(8, "The heated tubes", "WHY ARE THESE LITTLE TUBES HEATED?", "Why Are the Tubes on an Airplane's Nose Heated?",
     """Why are the small tubes on an airplane's nose heated? They are pitot tubes, and they measure airspeed. Air rams into the hole at the front, and the pressure tells the airplane how fast it is moving through the air. If ice blocks the hole, the airspeed reading becomes wrong. So the tubes are heated electrically, sometimes so hot you could burn your hand on the ground.""",
     "pitot tube aircraft")
sc("""On the first of June two thousand nine, Air France flight four four seven flew through a storm over the Atlantic at night. Ice crystals blocked the pitot tubes for less than a minute. The autopilot disconnected, the crew was confused by the wrong speeds, and the airplane stalled and fell into the ocean. Two hundred twenty-eight people died. The tubes on that type of airplane were replaced after the accident.""",
   "Airbus A330 Air France", "AIR FRANCE 447")
sc("""Airplanes have several pitot tubes, so the systems can compare them and spot a bad one. On the ground, they are often covered with red covers that say remove before flight, to keep insects and dirt out. A tiny tube on the nose, and a whole airliner depends on it.""",
   "pitot tube cover remove before flight", "A TINY TUBE")

# ---------- 9. WING LIGHT ----------
part(9, "The light that shines on the wing", "WHY IS THERE A LIGHT POINTING AT THE WING?", "Why Do Airplanes Have a Light Pointing at the Wing?",
     """Why is there a light on the side of an airplane that shines on its own wing? It is the wing inspection light. At night, the pilots and the cabin crew can switch it on to look at the leading edge of the wing and the engines, to check for ice. Without it, at night, nobody could see whether ice was building up on the wing.""",
     "wing inspection light airliner")
sc("""It sounds simple, because it is. Even with sensors and heaters, aviation likes a human check. Before takeoff in winter, crews often look at the wing from the cabin. If a passenger sees snow on the wing after de-icing, the crew wants to know. A light and a pair of eyes can stop an accident.""",
   "airplane wing night window", "A HUMAN CHECK")
sc("""Many passengers notice this light at night and think something is wrong. It is just the airplane looking at itself. It is one of the few parts on this list that you can actually see from your seat.""",
   "airplane window night wing light", "THE PLANE LOOKS AT ITSELF")

# ---------- 10. ICE DETECTOR ----------
part(10, "The vibrating probe", "WHY DOES THIS PROBE VIBRATE?", "Why Do Airplanes Have a Vibrating Probe on the Nose?",
     """How does an airplane know it is collecting ice? Many airliners have a small probe sticking out into the airflow, the ice detector. Inside, a little rod vibrates at a fixed frequency. When ice builds up on it, the extra weight makes it vibrate more slowly. The system notices the change, warns the pilots, and on some airplanes turns the anti-ice on by itself.""",
     "aircraft ice detector probe")
sc("""After each detection, the probe heats itself to melt its own ice, and then starts counting again. That way it can keep telling the crew if they are still in icing conditions. It is a tiny scale, weighing ice in real time, hundreds of times faster than any person could.""",
   "aircraft sensor fuselage", "A TINY SCALE FOR ICE")
sc("""From the orange truck at the gate to the vibrating probe on the nose, all ten parts do the same job. They keep the airplane exactly the shape it was designed to be. Because a wing does not care how big or modern the airplane is. With ice on it, it is just a worse wing.""",
   "airliner winter takeoff", "JUST A WORSE WING")

# ---------- VERDICT ----------
sc("""So here are the ten. Orange fluid that cleans, and green fluid that protects. A clean wing rule written by a crash, and a special pad next to the runway. Hot wing edges, hot engine lips, rubber boots that break the ice, heated tubes for airspeed, a light that shines on the wing, and a probe that weighs ice as it forms.""",
   "deicing airplane winter", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you sit through de-icing, you will know why it is worth the wait. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "airplane takeoff snow", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Deicing Copenhagen Airport.JPG", 0.3, 0.4),
    2: ("File:WestJet 737-700 getting a spray (4063116066).jpg", 0.17, 0.46),
    3: ("File:Ice on an aircraft wing.jpg", 0.4, 0.6),
    4: ("File:Deice Pad - Denver Airport (53816863550).jpg", 0.3, 0.62),
    5: ("File:MD-80 wing, landing, focus on leading edge slats (7984780550).jpg", 0.5, 0.3),
    6: ("File:Inlet of jet engine.jpg", 0.5, 0.5),
    7: ("File:Pneumatic deice boot detail.JPG", 0.5, 0.5),
    8: ("File:ILA-Pitotrohr.jpg", 0.7, 0.72),
    9: ("File:Aircraft element - wing and front left side 2.JPG", 0.62, 0.5),
    10: ("File:Ice detection probe on Global 6000 (1).jpg", 0.43, 0.5),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video10", "title": "Why Do Airports Spray Orange Liquid on Planes?",
           "length_scale": 1.6, "scenes": S}, open("videos/video10/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
