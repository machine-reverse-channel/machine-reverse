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
sc("""For thirty years, the coolest cars in the world had headlights that hid. The Lamborghini Countach, the Ferrari F forty, the Mazda M X five, the Corvette. Press a button, and the lights flipped up out of the bonnet like opening eyes. Then, in two thousand four, the last ones disappeared. Today, ten parts of car headlights, and the engineering story of why pop ups died.""",
   "pop-up headlights", "WHERE DID THEY GO?", cuts=8, chapter="Intro")
sc("""Headlights look like a simple part. But they sit at the meeting point of laws, safety, aerodynamics and new technology. Every time one of those changed, headlights changed too. The pop up headlight was born from one set of rules, and killed by another.""",
   "car headlights", "LAWS, SAFETY, AIR")
sc("""As always, every fact here comes from a named source, safety regulations, car makers and automotive references, all listed in the description. Let's start with the pop ups.""",
   "Mazda MX-5 pop-up headlights", "WHY DOES THIS EXIST?")

# ---------- 1. POP-UPS ----------
part(1, "The pop-up headlights", "WHY DID THESE HEADLIGHTS HIDE?", "Why Did Cars Have Pop-Up Headlights?",
     """Why did so many sports cars have headlights that popped up? Because designers wanted a very low, pointed nose, to cut through the air. But in the United States, the law required headlights to be at least about fifty-six centimetres above the ground. On a low sports car, the nose was simply too low for that.""",
     "pop-up headlights")
sc("""The solution was to hide the lights inside the bonnet, and raise them only when needed. With the lights down, the nose stayed low and smooth. With the lights up, they met the height rule. A car like the Mazda M X five or the Lotus Esprit could have both a wedge shaped nose and legal headlights.""",
   "Lotus Esprit", "LOW NOSE, LEGAL LIGHTS")
sc("""The flip up movement also became part of the fun. Owners would wink the lights at each other, and the cars seemed to come alive at night. For a generation of car fans, pop up headlights became the symbol of a sports car, as much as a loud engine or a big wing.""",
   "Mazda MX-5 NA", "THE WINK")

# ---------- 2. WHY THEY DIED ----------
part(2, "The end of pop-ups", "WHY DID POP-UP HEADLIGHTS DISAPPEAR?", "Why Did Pop-Up Headlights Disappear?",
     """Why did pop up headlights disappear? Several reasons arrived at the same time. The first was safety. New rules in Europe aimed to protect pedestrians hit by cars. A raised headlight has hard edges and corners, right where a person's legs or body would hit the car. Designers had to make the front of the car smoother and softer.""",
     "Chevrolet Corvette C5")
sc("""The second reason was weight and cost. Each pop up headlight needs a motor, a mechanism and wiring, and it can break. The third was aerodynamics. When the lights are up, the clean low nose suddenly has two bricks sticking into the wind, adding drag exactly when you drive at night.""",
   "pop-up headlight motor", "MOTORS AND DRAG")
sc("""The last reason was new technology. Smaller, brighter lights could be placed low in a smooth nose and still meet the rules. The Chevrolet Corvette and the Lotus Esprit kept pop ups until two thousand four, and then they were gone. The problem they solved no longer existed.""",
   "modern headlights", "THE PROBLEM WAS SOLVED")

# ---------- 3. SEALED BEAM ----------
part(3, "The sealed beam", "WHY WERE ALL HEADLIGHTS THE SAME?", "Why Did Old American Cars Have Identical Headlights?",
     """Why did old American cars all have the same round or rectangular headlights? Because of a rule. From the end of the nineteen thirties, US law required standard sealed beam headlights. The lamp, the reflector and the glass were one sealed unit, made in only a few standard sizes and shapes.""",
     "sealed beam headlight")
sc("""The idea was practical. If a light failed, you could buy a new one at any shop in the country, and it would fit. But it also froze design. Every car had to use the same few lamps, and designers could not shape the lights to match the body. That is one reason pop ups became popular, because they hid the ugly standard lamps.""",
   "1970s car headlights", "ONE SIZE FOR ALL")
sc("""The rule changed in the nineteen eighties, when the United States allowed headlights with replaceable bulbs, shaped freely by the designer. Lights could now be low, wide and curved to the body. That change, more than anything else, opened the door to the smooth faces of modern cars.""",
   "Lincoln Mark VII", "THE RULE CHANGED")

# ---------- 4. HALOGEN ----------
part(4, "The halogen bulb", "WHY IS THERE GAS INSIDE THIS BULB?", "Why Do Halogen Headlight Bulbs Have Gas Inside?",
     """Why is there gas inside a halogen headlight bulb? A normal bulb has a thin metal wire, a filament, that glows when it gets hot. Over time, metal from the filament evaporates and blackens the glass, and the filament gets thinner until it breaks. A halogen bulb adds a small amount of a gas such as iodine or bromine.""",
     "halogen bulb")
sc("""That gas creates a chemical cycle. The evaporated metal combines with the gas, and later lands back on the hot filament. The glass stays clear, and the filament can run hotter, which makes the light brighter and whiter. That is why halogen bulbs are made of quartz glass, which can handle the heat.""",
   "halogen headlight", "A CHEMICAL CYCLE")
sc("""Halogen bulbs became the standard in car headlights for decades. They are cheap and simple. But a hot quartz bulb is sensitive. The oil from a fingertip can create a hot spot on the glass and make it fail early, which is why mechanics never touch the glass with bare fingers.""",
   "H4 bulb", "DON'T TOUCH THE GLASS")

# ---------- 5. XENON ----------
part(5, "The xenon lamp", "WHY IS THIS LIGHT SO BLUE?", "Why Are Xenon Headlights So Blue and Bright?",
     """Why are some headlights bright and slightly blue? They are xenon lamps, also called high intensity discharge. Instead of a glowing wire, they create a small electric arc between two electrodes, inside a capsule filled with xenon gas and metal salts. The arc produces a very bright, white light.""",
     "xenon headlight")
sc("""Xenon lamps produce about three times as much light as halogen bulbs, while using less power. They need a high voltage pulse to start, which is why they take a moment to reach full brightness. The first car to use them was the B M W seven series in the early nineteen nineties.""",
   "HID lamp", "THREE TIMES THE LIGHT")
sc("""Because they are so bright, xenon lights are often placed behind a projector lens, a small glass lens that shapes the beam with a sharp cut off line. Without it, they would dazzle other drivers. Fitting xenon bulbs into a reflector made for halogen, without that control, is illegal in many countries for exactly that reason.""",
   "projector headlight", "A SHARP CUT OFF")

# ---------- 6. YELLOW ----------
part(6, "The yellow headlights", "WHY WERE FRENCH HEADLIGHTS YELLOW?", "Why Did French Cars Have Yellow Headlights?",
     """Why did French cars have yellow headlights? Because it was the law. From nineteen thirty-seven, France required headlights to give a yellow light. The idea was that yellow light causes less glare for oncoming drivers, and might cut through fog and rain better than white light.""",
     "yellow headlights")
sc("""Some people also believed it helped identify French cars, and that the yellow light was less tiring for the eyes. The science behind it was never fully settled. Yellow light does reduce some glare, but it also contains less total light. Drivers saw slightly less, but others were dazzled a little less.""",
   "Citroen DS", "LESS GLARE, LESS LIGHT")
sc("""The rule ended in the nineteen nineties, when Europe harmonised its rules and white headlights became the standard everywhere. Today, yellow headlights are a nostalgic detail, still fitted by some classic car owners to make an old French car look right. A whole country's night roads were once yellow.""",
   "classic French car", "A YELLOW COUNTRY")

# ---------- 7. LED ----------
part(7, "The LED headlights", "WHY ARE HEADLIGHTS NOW SO THIN?", "Why Are Modern Headlights So Thin?",
     """Why are modern headlights so thin? Because of LEDs. A light emitting diode is a tiny chip that glows when electricity passes through it. It is much smaller than a bulb, so many LEDs can be arranged in a thin strip or any shape the designer wants. Lights can now be just a few centimetres tall.""",
     "LED headlight")
sc("""LEDs also last much longer than bulbs, often as long as the car itself, and they use less energy. They light up instantly, and they can be switched on and off very quickly, which opens the door to smarter lights. Full LED headlights reached production cars in the late two thousands.""",
   "LED headlamp car", "LONGER LIFE, LESS ENERGY")
sc("""That is the final answer to why pop ups died. A thin LED strip can be placed in a low, smooth nose, meet every height rule, and still look sharp. The low sports car nose that once needed pop up lights can now have permanent ones that are almost invisible.""",
   "sports car headlights", "THE FINAL ANSWER")

# ---------- 8. MATRIX ----------
part(8, "The matrix headlights", "WHY DOES THIS HEADLIGHT HAVE MANY EYES?", "Why Do Matrix Headlights Have So Many LEDs?",
     """Why do some headlights have dozens of small LEDs inside? They are matrix headlights. A camera behind the windscreen watches the road for other cars. When it sees one, the headlight switches off only the small LEDs that would shine at that car, and keeps the high beam on everywhere else.""",
     "matrix LED headlight")
sc("""The result is a high beam that never dazzles. You can drive with full lights all night, and the system cuts a dark tunnel around every oncoming car and every car ahead. Audi was one of the first to bring this to production cars, in the two thousand tens.""",
   "Audi matrix LED", "A DARK TUNNEL")
sc("""The newest systems use thousands or even more than a million tiny pixels, and can project symbols onto the road, like a warning or a guiding line. The headlight is no longer just a lamp. It is a smart projector, guided by a camera and a computer.""",
   "digital headlight", "A SMART PROJECTOR")

# ---------- 9. WASHERS ----------
part(9, "The headlight washers", "WHY DO HEADLIGHTS HAVE WASHERS?", "Why Do Some Cars Have Headlight Washers?",
     """Why do some cars have little washers that spray the headlights? Because dirt on a bright headlight is dangerous. Mud and dust scatter the light in all directions, instead of keeping it below the cut off line. A dirty xenon or LED headlight can dazzle oncoming drivers even with low beams.""",
     "headlight washer")
sc("""For that reason, European rules have required headlight cleaning on cars with very powerful low beams, above a set brightness. The washers are often hidden in the bumper and pop out when you wash the windscreen, spraying a short, strong jet of water at the headlights.""",
   "headlight washer nozzle", "A HIDDEN JET")
sc("""It is a small example of how one change creates another. Brighter lights helped drivers see, but created a glare problem. The washer is the fix for that glare problem. Some modern LED headlights are efficient enough to avoid the rule, which is why washers are disappearing too.""",
   "car bumper headlights", "ONE FIX LEADS TO ANOTHER")

# ---------- 10. DRL ----------
part(10, "The daytime running lights", "WHY ARE THESE LIGHTS ON IN DAYLIGHT?", "Why Do Cars Have Lights On During the Day?",
     """Why do cars keep some lights on during the day? To be seen. Daytime running lights make a car easier to spot from far away, especially in dull weather, low sun or shadows. They are not meant to help the driver see. They are meant to help everyone else see the car.""",
     "daytime running lights")
sc("""The idea came from Scandinavia, where winter days are dark and short. Sweden made daytime lights mandatory in the nineteen seventies. The European Union required daytime running lights on new cars from two thousand eleven, after studies suggested they help reduce some types of daytime crashes.""",
   "Volvo daytime running lights", "BORN IN SCANDINAVIA")
sc("""Because daytime lights are always on, LEDs became perfect for them. They use little energy and last for years. Designers then turned them into signatures, with shapes that make each brand recognisable from far away. A safety rule became the new face of the car.""",
   "LED daytime running lights", "A NEW FACE")

# ---------- VERDICT ----------
sc("""So here are the ten. Pop ups for a low nose and a height law. Safety, weight and drag that killed them. Sealed beams that froze design. Halogen bulbs with a chemical cycle. Xenon arcs that shine three times brighter. Yellow lights from a French law. Thin LEDs that finally solved the problem. Matrix lights that never dazzle. Washers that keep them clean. And daytime lights that help others see you.""",
   "car headlights night", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Pop up headlights did not die because people stopped loving them. They died because the problem they solved disappeared. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which car with pop ups is your favourite.""",
   "pop-up headlights night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Toyota Sprinter Trueno AE86 2 door.jpg', 0.52, 0.6),
    2: ('File:Chevrolet Corvette C5 Haynes.jpg', 0.75, 0.48),
    3: ('File:Headlight lens optics.jpg', 0.4, 0.45),
    4: ('File:Halogen light bulb.JPG', 0.3, 0.4),
    5: ('File:2014 Proton Suprima S Premium - Headlights.jpg', 0.55, 0.45),
    6: ('File:1957 Panhard Dyna Z (France Domestic) (8391189016).jpg', 0.3, 0.45),
    7: ('File:BMW M4 (G83) 1X7A7098.jpg', 0.4, 0.53),
    8: ('File:2015 Audi A4 B9 S line Tangorot LED-Matrix-Scheinwerfer Detail.jpg', 0.55, 0.6),
    9: ('File:Audi A8 L 55 TFSI Quattro D5 Floret Silver Metallic (6).jpg', 0.8, 0.8),
    10: ('File:LED DaytimeRunningLights.jpg', 0.45, 0.65),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video34", "title": "Why Did Pop-Up Headlights Disappear?",
           "length_scale": 1.6, "scenes": S}, open("videos/video34/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
