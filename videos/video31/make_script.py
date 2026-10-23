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
sc("""Look at the fuel gauge in your car. Next to the little fuel pump symbol, there is a tiny arrow. Most drivers have never noticed it, and it answers a question every driver has asked at a petrol station. Your car is full of small parts like that, hiding in plain sight. Today, ten of them, and why each one exists.""",
   "car fuel gauge", "WHY IS THIS ARROW HERE?", cuts=8, chapter="Intro")
sc("""These are not expensive parts. They are dots, lines, arrows and little hairs. But each one was added by an engineer to solve a real problem, a safety risk, a glue that would fail in the sun, or a driver standing at the wrong pump. Once you know them, you will see them on every car.""",
   "car dashboard", "HIDING IN PLAIN SIGHT")
sc("""As always, every fact here comes from a named source, car makers, safety agencies and automotive references, all listed in the description. Let's start with the arrow.""",
   "car interior", "WHY DOES THIS EXIST?")

# ---------- 1. FUEL ARROW ----------
part(1, "The fuel gauge arrow", "WHY IS THERE AN ARROW NEXT TO THE FUEL GAUGE?", "Why Is There a Little Arrow Next to Your Fuel Gauge?",
     """Why is there a little arrow next to your fuel gauge? It tells you which side of the car the fuel door is on. If the arrow points left, the filler is on the left. If it points right, it is on the right. It exists for the moment you drive a rented or borrowed car into a petrol station and do not know which side to stop on.""",
     "fuel gauge arrow")
sc("""There is no single rule for which side the fuel door goes on. Car makers choose based on the layout of the car underneath, where the tank, the exhaust and the other parts fit best. So two cars from the same brand can have the filler on opposite sides, and drivers guess wrong all the time.""",
   "car fuel door", "NO SINGLE RULE")
sc("""The arrow is often credited to Jim Moylan, a designer at Ford, who suggested it in a memo in the nineteen eighties after pulling up to the wrong side of the pump on a rainy day. It appeared on Ford cars and slowly spread to almost every car in the world. One small idea, saving millions of drivers a few embarrassing seconds.""",
   "petrol station car", "ONE MEMO")

# ---------- 2. FRIT ----------
part(2, "The black dots", "WHY ARE THERE BLACK DOTS ON THE WINDSCREEN?", "Why Are There Black Dots on Your Windshield?",
     """Why are there black dots around the edge of your windscreen? They are part of a black band called the frit, a ceramic paint baked into the glass. The windscreen is glued to the car, and that glue is damaged by sunlight. The black band blocks the sun, so the glue stays strong for years.""",
     "windshield frit dots")
sc("""The band also gives the glue a rough surface to grip, and it hides the glue from view so the edge looks clean. The dots are there because of heat. A solid black band heats up much more than clear glass. Fading the black into smaller and smaller dots spreads the heat more gently, and reduces stress in the glass.""",
   "windscreen edge", "A GENTLE FADE")
sc("""The dots also make the change from black to clear look smoother to the eye, and they can reduce a slight distortion at the edge of the glass. You will find a patch of dots behind the rear view mirror too, shading the area where the sun would shine between the sun visors. Nothing on the windscreen is there by accident.""",
   "rear view mirror windscreen", "NOTHING BY ACCIDENT")

# ---------- 3. TREAD WEAR BARS ----------
part(3, "The tread wear bars", "WHY ARE THERE BUMPS INSIDE THE TYRE GROOVES?", "Why Are There Little Bumps Inside Tire Grooves?",
     """Why are there small bumps hidden inside the grooves of your tyres? They are tread wear indicators. Each bump is a little bar of rubber that sits about one point six millimetres above the bottom of the groove. When the tyre wears down to the level of the bars, it is time to replace it.""",
     "tire tread wear indicator")
sc("""One point six millimetres is the legal minimum tread depth in many countries, including the European Union. The grooves in a tyre carry water away, so the rubber can touch the road. When the grooves become too shallow, water stays under the tyre and the car can start to float on it, which is called aquaplaning.""",
   "aquaplaning", "WATER NEEDS A WAY OUT")
sc("""You do not need a gauge to check. When the surface of the tread becomes level with the bars, the tyre is at its limit. Many tyres also mark the position of the bars with a small triangle or logo on the shoulder. A tiny bump of rubber turns a safety check into something anyone can see.""",
   "tyre tread", "ANYONE CAN CHECK")

# ---------- 4. TYRE HAIRS ----------
part(4, "The tyre hairs", "WHY DO NEW TYRES HAVE LITTLE HAIRS?", "Why Do New Tires Have Little Rubber Hairs?",
     """Why do new tyres have little rubber hairs sticking out of them? They are a side effect of how tyres are made. A tyre is pressed into a hot mould, and the rubber flows into every corner. Air trapped inside the mould would leave holes and weak spots, so the mould has tiny holes to let the air escape.""",
     "new tire rubber hairs")
sc("""As the air escapes, a little rubber flows into those holes too. When the tyre comes out of the mould, the rubber in the holes stays attached as thin hairs. Tyre makers call them vent spews. They have no job on the road. They are the fingerprints of air leaving the mould.""",
   "tire mould", "VENT SPEWS")
sc("""They are harmless, and they wear away after the first few hundred kilometres. Some tyre makers now use a different kind of vent that leaves no hairs, to give the tyre a cleaner look. But if you see them, you know the tyre is new, and that it was made without air bubbles inside.""",
   "new tyre", "FINGERPRINTS OF THE MOULD")

# ---------- 5. QUARTER GLASS ----------
part(5, "The small rear window", "WHY IS THIS SMALL WINDOW HERE?", "Why Do Rear Car Doors Have a Small Fixed Window?",
     """Why do many rear car doors have a small fixed window at the back? Because of the wheel. The rear wheel arch cuts into the bottom of the rear door. When the main window slides down into the door, it would hit the wheel arch before it disappears. So the window is made smaller, and the gap is filled with a fixed piece of glass.""",
     "car rear door quarter glass")
sc("""That is why, in many cars, the rear window only goes down partway, or the door has a small triangle of glass that never moves. Engineers would rather have a fully opening window, but the shape of the door simply does not leave enough room inside it for the whole glass.""",
   "car rear window", "NO ROOM INSIDE THE DOOR")
sc("""The small fixed glass also lets light in and gives passengers a better view, so the back of the cabin does not feel closed. Some modern cars hide it behind a black panel instead. The next time a rear window stops halfway, you will know there is a wheel just below it.""",
   "car rear door", "A WHEEL JUST BELOW")

# ---------- 6. THIRD BRAKE LIGHT ----------
part(6, "The third brake light", "WHY IS THERE A BRAKE LIGHT UP HERE?", "Why Do Cars Have a Third Brake Light?",
     """Why do cars have a third brake light, high up in the middle? So the driver behind can see you brake, even through the car in front of them. The two normal brake lights are low, at the height of the other car's bumper. The third one is at eye level, often visible through the windows of the cars in between.""",
     "third brake light")
sc("""In the United States, it became required on new cars in the nineteen eighties, after studies found it helped reduce rear end crashes. Many other countries followed. It has a special job, because it lights up only when you brake. It is never confused with the tail lights at night.""",
   "car brake lights", "ONLY WHEN YOU BRAKE")
sc("""Today it is often a thin strip of LEDs in the rear window or the spoiler. LEDs light up a fraction of a second faster than old bulbs, which gives the driver behind a little more time to react. At highway speed, that fraction of a second can be a few metres of stopping distance.""",
   "LED brake light", "A FEW METRES")

# ---------- 7. SHARK FIN ----------
part(7, "The shark fin", "WHY IS THERE A SHARK FIN ON THE ROOF?", "Why Do Cars Have a Shark Fin on the Roof?",
     """Why do modern cars have a little shark fin on the roof? It is an antenna cover. Cars used to have a long metal rod for the radio. Today, a car may need antennas for the radio, satellite navigation, phone connection and emergency calls. The fin holds several of them in one small, hard shell.""",
     "shark fin antenna")
sc("""The roof is the best place for antennas, because it has the clearest view of the sky, and the metal roof below acts as a reflector that helps the signal. A long rod antenna makes wind noise, adds a little drag, and can be broken in a car wash. The fin solves all three.""",
   "car roof antenna", "THE CLEAREST VIEW OF THE SKY")
sc("""The shape is not just for style. A low, curved fin lets air flow smoothly over it, with less noise at speed. Inside, there are small circuit boards tuned to each kind of signal. The fin is a tiny communication tower that rides on top of your car.""",
   "shark fin antenna car", "A TINY TOWER")

# ---------- 8. REAR WINDOW LINES ----------
part(8, "The rear window lines", "WHY ARE THERE LINES ON THE REAR WINDOW?", "Why Are There Lines on Your Rear Window?",
     """Why are there thin lines across your rear window? They are heating wires. The lines are made of a conductive paint, printed onto the glass and baked in. When you press the defrost button, electricity flows through them, and they warm up just enough to clear ice, frost and mist.""",
     "rear window defroster lines")
sc("""The lines are spaced so heat spreads evenly across the glass. They run across the window, connected at each side by a wider strip where the wires attach. A broken line leaves a stripe of frost, which is why repair kits sell a small bottle of conductive paint to reconnect it.""",
   "rear window defogger", "EVEN HEAT")
sc("""On some cars, a few of the lines have a second job. They are the radio antenna, hidden in the glass. That is why some cars have lines that do not reach all the way across. A few thin lines, keeping your view clear and sometimes playing your music.""",
   "car rear window", "A HIDDEN ANTENNA")

# ---------- 9. LOW BEAM ----------
part(9, "The tilted low beam", "WHY DOES THIS LIGHT POINT UNEVENLY?", "Why Do Car Headlights Shine Unevenly?",
     """Why do the low beams of your car shine unevenly? Look at the light on a wall, and you will see the top edge is not straight. On one side it is lower, and on the other side it rises. It is designed that way. The low side faces oncoming traffic, so you do not blind other drivers.""",
     "car low beam pattern")
sc("""The higher side lights the edge of the road, where people walk and signs stand. That way, you see further along the side of the road without shining into anyone's eyes. The shape is built into the headlight itself, with carefully designed reflectors or lenses.""",
   "car headlight", "SEE FURTHER ON YOUR SIDE")
sc("""This is why cars driven in countries that drive on the other side of the road need their headlights adjusted. A British car in France would shine its high side straight into oncoming drivers. Some modern LED headlights can even switch the pattern electronically, at the touch of a menu.""",
   "LED headlight", "LEFT OR RIGHT")

# ---------- 10. DASH SENSOR ----------
part(10, "The dashboard sensor", "WHY IS THERE A LITTLE DOME ON THE DASHBOARD?", "Why Is There a Little Dome on Your Dashboard?",
     """Why is there a small dome on top of your dashboard, near the windscreen? It is a sensor. On many cars it measures sunlight. When strong sun shines into the car, the climate control knows to cool the cabin more, often on the side where the sun is coming in.""",
     "dashboard sunlight sensor")
sc("""On many cars, the same spot also holds a light sensor for automatic headlights. When it gets dark, or you drive into a tunnel, the sensor notices and the lights turn on. Covering it with a phone holder or a parking ticket can fool the car into thinking it is night.""",
   "car automatic headlights", "DAY OR NIGHT?")
sc("""It is a good example of how modern cars quietly measure the world around them. The climate system does not only check the temperature inside. It also checks the sun on your arm. A tiny dome on the dashboard is how your car knows it is a sunny day.""",
   "car dashboard windscreen", "A SUNNY DAY")

# ---------- VERDICT ----------
sc("""So here are the ten. An arrow that shows the side of the fuel door. Dots that protect the windscreen glue. Bumps that tell you when a tyre is worn. Hairs left by escaping air. A small window above the wheel. A high brake light at eye level. A fin full of antennas. Lines that heat the glass. A tilted beam that protects other drivers. And a dome that feels the sun.""",
   "car", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""The next time you get in your car, look for them. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which tiny part of your car you always wondered about.""",
   "car night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Car Fuel Gauge - Full Gas Tank (52958977635).jpg', 0.58, 0.5),
    2: ('File:Dülmen, Wiesmann Sports Cars, Wiesmann GT -- 2018 -- 9598.jpg', 0.8, 0.35),
    3: ('File:Autoreifen mit Verschleißanzeige.JPG', 0.55, 0.62),
    4: ('File:Close-up of Front tire of a Volkswagen car.jpg', 0.85, 0.45),
    5: ('File:1968 Rambler American 440 4-door sedan green VA-rm.jpg', 0.35, 0.5),
    6: ('File:" 12 - ITALY - FIAT Panda 4x4 - third brake light and rear window 04.jpg', 0.45, 0.2),
    7: ('File:Shark Fin Antenna of Honda City 7th Generation (5th Generation Sedan) iVTEC 2022.jpg', 0.6, 0.4),
    8: ('File:Rear window heating 20180405.jpg', 0.5, 0.5),
    9: ('File:Phare code.png', 0.55, 0.35),
    10: ('File:Chevrolet Ambient Light Sensor.jpg', 0.55, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video31", "title": "Why Is There a Little Arrow Next to Your Fuel Gauge?",
           "length_scale": 1.6, "scenes": S}, open("videos/video31/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
