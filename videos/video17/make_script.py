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
sc("""Look at pictures of satellites, and you will see something odd. Many of them look as if they were wrapped in crumpled gold foil, like a giant gift. It is not gold, and it is not for decoration. It is one of the most effective insulators ever invented, and it works in a place where the usual kind of insulation does not work at all. Today, nine parts of that blanket, and of the machines it protects, and why each one exists.""",
   "satellite gold foil insulation", "WHY GOLD FOIL?", cuts=8, chapter="Intro")
sc("""In space there is almost no air, so heat can not travel by touching or by moving air. It travels as radiation, the same way the Sun warms your face. And that changes everything about how you keep something warm, or keep it cool.""",
   "satellite in orbit", "NO AIR, ONLY RADIATION")
sc("""As always, every fact here comes from a named source, space agency pages and reference works, all listed in the description. Let's start with the foil itself.""",
   "spacecraft thermal blanket", "WHY DOES THIS EXIST?")

# ---------- 1. GOLD LOOK ----------
part(1, "The gold blanket", "WHY IS THIS SATELLITE WRAPPED IN GOLD FOIL?", "Why Are Satellites Wrapped in Gold Foil?",
     """Why are satellites wrapped in gold-colored foil? It is called multi-layer insulation. It is not gold. The gold color comes from an amber-colored plastic called Kapton, laid over a thin silvery layer of aluminized Mylar. The blanket stops heat from flowing in or out of the spacecraft by radiation, which is the main way heat moves in a vacuum.""",
     "spacecraft multi-layer insulation gold foil")
sc("""A typical blanket has forty or more layers, and each one is only about six micrometers thick, thinner than a human hair. The outer layers are thicker and stronger, because they take the damage from dust and sunlight. A forty layer blanket is only about twenty millimeters thick.""",
   "multi-layer insulation blanket layers", "40 LAYERS, 20 MILLIMETERS")
sc("""So the gold look is a side effect. The real design is a stack of mirrors, built to bounce heat back where it came from. It just happens that the plastic on top is the color of gold.""",
   "satellite gold blanket close", "A STACK OF MIRRORS")

# ---------- 2. MANY LAYERS ----------
part(2, "The stack of layers", "WHY DOES THIS BLANKET HAVE SO MANY LAYERS?", "Why Does a Satellite Blanket Have Forty Layers?",
     """Why does the blanket need so many layers? Each extra layer cuts the heat that gets through. Imagine one surface at room temperature, radiating about four hundred sixty watts for every square meter. Put a single thin opaque layer a short distance in front of it, and the loss falls to about half, about two hundred thirty watts. Every new layer cuts it further.""",
     "multi-layer insulation reflective layers")
sc("""Each layer is a mirror that sends part of the heat back. With dozens of mirrors in a row, almost no heat makes it from the hot side to the cold side. It is like a hall of mirrors that is built to keep light in, but for heat.""",
   "reflective layers heat radiation", "A HALL OF MIRRORS FOR HEAT")
sc("""This kind of insulation is described as the most effective kind in cryogenics, the science of very cold things. For cold tanks and instruments, it is a standard way to keep them cold with little weight.""",
   "cryogenic insulation tank", "THE BEST INSULATOR")

# ---------- 3. SPACERS ----------
part(3, "The thin spacer mesh", "WHY IS THERE A NET BETWEEN THE LAYERS?", "Why Is There a Thin Net Between the Foil Layers?",
     """Why is there a thin net between the layers? Because the layers must not touch. If two layers touch, heat can flow between them by conduction, and the mirror trick stops working. So the layers are kept apart by an extremely thin cloth mesh, sometimes described as a bridal veil, or by being crinkled so they touch only at a few points.""",
     "multi-layer insulation spacer scrim")
sc("""The spacer has to be almost invisible to heat. It must keep the layers apart, but it can not carry heat between them. That is why it is made as thin and open as possible, a few threads in a lot of empty space.""",
   "thin mesh netting spacer", "ALMOST INVISIBLE TO HEAT")
sc("""It is a funny design problem. The best insulator is mostly nothing, held together by something that is almost nothing. And in the vacuum of space, almost nothing is exactly what is needed.""",
   "satellite blanket crinkled foil", "MOSTLY NOTHING")

# ---------- 4. SEAMS AND VENTS ----------
part(4, "The seams and holes", "WHY DOES THE BLANKET HAVE TINY HOLES?", "Why Do Satellite Blankets Have Tiny Holes?",
     """Why does a blanket made to keep heat out have tiny holes? Because it also has to survive the launch. Air trapped between the layers would expand when the rocket reaches the vacuum, and could balloon or tear the blanket. So holes are made, to let the air out. The price is that perforations reduce the effectiveness of the insulation a little.""",
     "multi-layer insulation vent perforations")
sc("""The seams and gaps are the other weak point. Most of the heat that leaks through a blanket does it through the seams, not through the layers. That is why engineers put so much care into how a blanket is cut and joined, and sometimes use pins instead of stitches to hold it together.""",
   "spacecraft blanket seams", "THE SEAMS LEAK")
sc("""A perfect insulator on paper is never perfect in real life. The honest engineering question is how little leaks out, and the answer is almost always found in the edges.""",
   "satellite blanket edge", "THE EDGES DECIDE")

# ---------- 5. GROUNDING ----------
part(5, "The metal in the stitching", "WHY ARE THERE METAL SPACERS IN THE BLANKET?", "Why Are Some Satellite Blankets Stitched With Metal?",
     """Why are some blankets stitched with metal parts? In some designs, aluminum spacers replace cloth at the sewn points, so that all the layers stay electrically grounded. Tying every layer to the structure keeps any single layer from floating on its own.""",
     "multi-layer insulation grounding aluminum spacers")
sc("""So every layer is connected to the structure of the spacecraft. The insulation is a thermal part and an electrical part at the same time, and the metal at the stitches is what links one to the other.""",
   "satellite electrostatic charge", "NO LOOSE LAYERS")
sc("""It is the sort of detail that nobody sees in the picture. A satellite has to handle electricity as well as the cold and the heat, and even a blanket of foil is part of that design.""",
   "satellite electrical grounding", "HEAT AND ELECTRICITY")

# ---------- 6. SUNSHIELD ----------
part(6, "The giant sunshield", "WHY DOES THIS TELESCOPE HAVE A GIANT SILVER SHIELD?", "Why Does the Webb Telescope Have a Giant Sunshield?",
     """Why does the James Webb Space Telescope have a giant silver shield? It is a sunshield, made of five layers of thin plastic film, each about one tenth of a millimeter thick. Fully open, it is about fourteen by twenty-one meters. Each layer is Kapton with aluminum on both sides, and the two layers closest to the Sun also have a coating of doped silicon.""",
     "James Webb Space Telescope sunshield")
sc("""On one side, the Sun, the Earth and the Moon. On the other, a telescope that has to stay colder than fifty kelvin, or minus two hundred twenty-three degrees Celsius. The spacecraft side of the shield sits at about three hundred kelvin, a warm room, while the instruments are in the shade at the other side.""",
   "James Webb telescope sunshield layers", "A WARM ROOM BESIDE A FREEZER")
sc("""So the sunshield is the same idea as the gold foil, but scaled up to the size of a tennis court. Layers of mirrors and gaps, stacked to keep the heat on one side, and the cold on the other.""",
   "James Webb Space Telescope deployment", "THE SAME IDEA, TENNIS COURT SIZE")

# ---------- 7. GOLD MIRROR ----------
part(7, "The gold mirror", "WHY IS THIS MIRROR GOLD?", "Why Is the Webb Telescope's Mirror Gold?",
     """Why is the mirror of the Webb telescope gold? Because gold is an excellent reflector of infrared light, and infrared is what Webb was built to see. The mirror is made of eighteen hexagonal segments, made of beryllium and plated with gold, that together form a mirror six and a half meters wide. A thin glass layer covers the gold for protection.""",
     "James Webb Space Telescope gold mirror")
sc("""Here the gold is real, and the reason is science. Infrared light carries the faint heat of very old, very distant galaxies. A gold mirror collects that light and sends it into the instruments, and almost none is lost.""",
   "James Webb Space Telescope mirror segments", "REAL GOLD, REAL SCIENCE")
sc("""Why beryllium? It is a light metal, a good fit for a mirror that has to be carried to space. Webb is a machine where the mirror, the shield and the cold are all one design, and the gold is the part you can see.""",
   "James Webb Space Telescope hexagon mirror", "ONE DESIGN, ONE GOAL")

# ---------- 8. COLD ----------
part(8, "The cold instruments", "WHY MUST THIS TELESCOPE BE SO COLD?", "Why Must the Webb Telescope Be So Cold?",
     """Why does the Webb telescope have to be so cold? To see infrared light, it can not be warm itself. Anything with heat glows in infrared, and a warm telescope would blind its own detectors. So Webb must stay below fifty kelvin, minus two hundred twenty-three degrees Celsius, so that the faint light of ancient galaxies is not drowned by its own glow.""",
     "James Webb Space Telescope instruments cold")
sc("""Every layer of the sunshield, every blanket and every radiator on the telescope has the job of getting rid of heat, or keeping it out. The whole telescope is a cold machine, built to sit in the shadow of its own shield.""",
   "James Webb telescope thermal", "BUILT TO BE COLD")
sc("""A telescope that sees heat, and must hide from heat. That is the strange logic of infrared astronomy, and the gold foil's cousin is the sunshield that makes it work.""",
   "infrared telescope cooling", "SEES HEAT, HIDES FROM HEAT")

# ---------- 9. L2 ----------
part(9, "The faraway orbit", "WHY DOES THE TELESCOPE FLY SO FAR AWAY?", "Why Is the Webb Telescope a Million Miles From Earth?",
     """Why is the Webb telescope so far from Earth? It sits about one point five million kilometers away, at a point called L2, on the side of Earth opposite from the Sun. From there, the Sun, the Earth and the Moon are all in the same direction, so one sunshield can block all three. Closer to Earth, the planet itself would be one more source of heat to block.""",
     "James Webb Space Telescope L2 orbit")
sc("""It was launched on the twenty-fifth of December, two thousand twenty-one, on an Ariane five rocket from French Guiana. And it works as an example of how the foil and the shield and the orbit are all parts of one solution, to one problem, keeping something cold in a very hot place.""",
   "James Webb launch Ariane 5", "ONE PROBLEM, ONE SOLUTION")
sc("""That is the story of gold foil in space. It starts as a blanket on a satellite, and ends as the shield of one of the most advanced telescopes ever built. The idea is the same, the mirror, the gap, and the layers.""",
   "James Webb Space Telescope space", "FROM BLANKET TO TELESCOPE")

# ---------- VERDICT ----------
sc("""So here are the nine. A blanket that looks like gold but is plastic, dozens of layers, a net that keeps them apart, and holes for the launch. Metal that keeps the layers grounded, a sunshield the size of a tennis court, a mirror made of real gold, the cold it protects, and an orbit far from home.""",
   "satellite space sunrise", "9 PARTS. 9 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see a satellite wrapped in gold, you will know it is a stack of mirrors for heat. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "satellite gold foil museum", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video17", "title": "Why Are Satellites Wrapped in Gold Foil?",
           "length_scale": 1.6, "scenes": S}, open("videos/video17/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
