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
sc("""The Space Shuttle came back from space like a meteor, wrapped in plasma hotter than lava. And the only thing between the astronauts and that fire was a skin of about twenty-four thousand tiles, each one glued on by hand. Look closely and the tiles are not all the same. Some are black, some are white, some are gray, and each color has a reason. Today, ten parts of the shuttle's heat shield, and why each one exists.""",
   "Space Shuttle thermal tiles", "WHY IS IT COVERED IN TILES?", cuts=8, chapter="Intro")
sc("""A spacecraft that returns from orbit is moving about twenty-five times the speed of sound. The air in front of it cannot get out of the way, so it is squeezed and heated until it glows. The shuttle was the first spacecraft designed to survive that over and over, and the answer was not a thick shield that burns away. It was a skin of glass that barely conducts heat at all.""",
   "Space Shuttle reentry", "A SKIN OF GLASS")
sc("""As always, every fact here comes from a named source, NASA documents and spaceflight references, all listed in the description. Let's start with the part that covers most of the belly.""",
   "Space Shuttle Discovery landing", "WHY DOES THIS EXIST?")

# ---------- 1. BLACK BELLY ----------
part(1, "The black belly tiles", "WHY IS THE BELLY BLACK?", "Why Is the Space Shuttle's Belly Covered in Black Tiles?",
     """Why is the underside of the shuttle covered in black tiles? Because that is where the heat hits. The black tiles, called high temperature tiles, protect against up to two thousand three hundred degrees Fahrenheit, about one thousand two hundred sixty Celsius. More than twenty thousand of them covered the belly, the landing gear doors and other hot spots. The tile itself is white. The black is a glassy coating that is added on top.""",
     "Space Shuttle black tiles underside")
sc("""The tile is made of silica glass fibers, and it is about ninety percent empty space, with a density of only nine pounds per cubic foot. That is why a tile fresh out of an oven can be held by its edges with a bare hand, while its center is still glowing red. It stores heat well, and releases it slowly, and that gave the shuttle time to land before the heat reached the metal.""",
   "Space Shuttle tile glowing", "90% EMPTY SPACE")
sc("""The black coating matters too. A dark, glassy surface is very good at radiating heat away into the air, so the tile sheds energy instead of soaking it up. The same material that looks like a simple paint job is part of the engineering.""",
   "Space Shuttle belly tiles", "THE BLACK IS ENGINEERING")

# ---------- 2. WHITE TOP ----------
part(2, "The white tiles on top", "WHY IS THE TOP WHITE?", "Why Are the Top Tiles of the Space Shuttle White?",
     """Why are the tiles on top of the shuttle white? Because the top does not get as hot. During reentry the orbiter flew with its nose high and its belly forward, so the upper surfaces were shielded from the worst of it. White low temperature tiles were used where the temperatures stayed below about one thousand two hundred degrees Fahrenheit, six hundred forty-nine Celsius.""",
     "Space Shuttle white tiles upper surface")
sc("""White also helped in orbit. The orbiter spent about half of every ninety minute orbit in direct sunlight, and white surfaces reflect much of that heat. Black on the bottom to shed heat, white on top to reflect it. Two colors, two jobs.""",
   "Space Shuttle in orbit sunlight", "BLACK SHEDS, WHITE REFLECTS")
sc("""This is a good example of how a spacecraft is designed one square foot at a time. Every part of the surface has its own temperature, and the engineers chose the lightest material that could survive it. A heavier tile everywhere would have meant less cargo in the payload bay.""",
   "Space Shuttle payload bay", "THE LIGHTEST THAT SURVIVES")

# ---------- 3. GAPS ----------
part(3, "The gaps between tiles", "WHY ARE THERE GAPS BETWEEN THE TILES?", "Why Are There Gaps Between the Space Shuttle's Tiles?",
     """Why are there small gaps between the tiles? Because the tiles are made of ceramic, which is stiff and brittle, and the aluminum skin underneath bends and expands. If the tiles touched each other, they would crack. So the tiles were glued to a felt pad, called a strain isolation pad, which was glued to the skin, and the gaps let everything move without breaking.""",
     "Space Shuttle tile gaps")
sc("""The gaps also had to be filled, because hot plasma could flow into them and burn through. Gap fillers, fabric strips placed between the tiles, kept the plasma out while still allowing the tiles to move. A tiny gap is a weak point, and the shuttle had thousands of them.""",
   "Space Shuttle gap filler tile", "THOUSANDS OF WEAK POINTS")
sc("""So the heat shield was not one smooth shell. It was a mosaic, held together by glue, felt and fabric, built so that a stiff material could live on a flexing machine. That mosaic is also why the shuttle needed so much work between flights.""",
   "Space Shuttle tile technician", "A MOSAIC OF GLASS")

# ---------- 4. NOSE ----------
part(4, "The nose cap", "WHY IS THE NOSE DIFFERENT?", "Why Is the Space Shuttle's Nose Not Covered in Tiles?",
     """Why is the nose of the shuttle a different color from the rest? Because the nose and the leading edges of the wings get hotter than any tile could survive. For those spots, engineers used a material called reinforced carbon-carbon, light gray in color, which can take temperatures of up to about two thousand seven hundred fifty degrees Fahrenheit, one thousand five hundred ten Celsius.""",
     "Space Shuttle nose cap")
sc("""It is made of layers of carbon fabric, baked until it becomes a hard carbon structure, and then coated to protect it from burning in the air. It is light and strong, and it can handle heat that would melt metal. But it is also much more expensive, and much harder to make, than a tile.""",
   "Space Shuttle nose", "HEAT THAT MELTS METAL")
sc("""Only the places that really needed it got this material. Everywhere else, tiles and blankets did the job for less weight. That is the rule of the whole system, use the weakest material that still works.""",
   "Space Shuttle Atlantis nose", "ONLY WHERE IT'S NEEDED")

# ---------- 5. WING EDGE ----------
part(5, "The wing edge panels", "WHY IS THE WING EDGE GRAY?", "Why Are the Space Shuttle's Wing Edges Gray?",
     """Why are the front edges of the shuttle's wings gray instead of black? They are made of the same carbon material as the nose, in panels. Each wing had twenty-two of them, numbered one to twenty-two. They sit at the very front of the wing, where the air hits first and the heat is the highest.""",
     "Space Shuttle wing leading edge reinforced carbon-carbon")
sc("""This is also where Columbia was lost. On the first of February, two thousand three, the orbiter broke apart on its way home. A piece of foam from the external tank had hit the left wing's front edge during launch, and the damage let hot gas into the wing during reentry. All seven astronauts were killed.""",
   "Space Shuttle Columbia", "A HOLE IN THE EDGE")
sc("""The wing edge is the part of the shuttle that taught NASA the most about how fragile a heat shield can be. After Columbia, every flight included a careful inspection of the wing edges and the belly while still in orbit. The lesson was simple, a heat shield can only be trusted once it has been checked.""",
   "Space Shuttle Discovery wing", "CHECK BEFORE YOU COME HOME")

# ---------- 6. WHITE BLANKETS ----------
part(6, "The white felt", "WHY ARE THESE WHITE PATCHES SOFT?", "Why Is Part of the Space Shuttle Covered in White Felt?",
     """Why are some parts of the shuttle covered in soft white material instead of tiles? Because some places barely get hot. On the upper part of the fuselage, the payload bay doors and parts of the sides, the temperature stayed below about seven hundred degrees Fahrenheit, three hundred seventy-one Celsius. There, a blanket of white Nomex felt was enough.""",
     "Space Shuttle payload bay doors white blanket")
sc("""Felt is lighter than tiles, faster to install, and tougher against impacts. Over the program, more and more areas switched from tiles to blankets, because every pound saved on the heat shield meant a pound more of payload. The shuttle's skin kept being redesigned for the lowest weight.""",
   "Space Shuttle orbiter white blanket", "SAVE EVERY POUND")
sc("""It is a humble material on the most expensive vehicle ever flown. And that is how the best engineering looks. Not the fanciest material everywhere, but the right material in each place.""",
   "Space Shuttle Endeavour", "THE RIGHT MATERIAL")

# ---------- 7. TILE NUMBERS ----------
part(7, "The tile numbers", "WHY DOES EVERY TILE HAVE A NUMBER?", "Why Does Every Space Shuttle Tile Have a Number?",
     """Why does every tile have a number written on it? Because no two are the same. About twenty-four thousand three hundred tiles were individually fitted to the orbiter, and they are not interchangeable. The curves of the shuttle's body change from point to point, so each tile had to be cut to fit its own place.""",
     "Space Shuttle tile numbers")
sc("""Each tile was machined by computer from a block, and then checked against the spot where it would go. If a tile was damaged, technicians did not grab a spare from a shelf. They made a new one for that exact position, using its number to find the right shape.""",
   "Space Shuttle tile processing", "NO TWO ALIKE")
sc("""When Columbia first arrived at Kennedy Space Center in nineteen seventy-nine, thousands of its tiles were still missing, and the team spent months putting them on. A heat shield made of thousands of custom pieces is not built fast. It is assembled, one tile at a time.""",
   "Space Shuttle Columbia tiles Kennedy", "ONE TILE AT A TIME")

# ---------- 8. WATERPROOFING ----------
part(8, "The waterproofing", "WHY WAS RAIN A PROBLEM FOR THESE TILES?", "Why Did the Space Shuttle Tiles Need Waterproofing?",
     """Why did a spacecraft that flies in space need to be waterproofed? Because the tiles are mostly air, and they act like a sponge. If a tile soaked up rain, it would be heavier, and water that froze or boiled could damage it in flight. So technicians injected a waterproofing chemical into the tiles with a syringe, and added a coating of another material to make it last.""",
     "Space Shuttle tile waterproofing")
sc("""It sounds almost silly, a rocket ship and a syringe. But a heat shield that fails because of rain on the runway would be an embarrassing way to lose a mission. The details that look the smallest are often the ones that keep the whole thing working.""",
   "Space Shuttle rain launch pad", "A ROCKET SHIP AND A SYRINGE")
sc("""That care is also why the shuttle spent weeks in a hangar between missions. Technicians looked at tiles one by one, replaced the damaged ones, and checked the waterproofing, before the orbiter went back on the pad.""",
   "Space Shuttle orbiter processing facility", "WEEKS IN THE HANGAR")

# ---------- 9. INSPECTION BOOM ----------
part(9, "The inspection boom", "WHY DOES THE SHUTTLE CARRY A GIANT STICK?", "Why Did the Space Shuttle Carry a Fifty-Foot Boom?",
     """Why did the shuttle carry a long boom on its side? After Columbia, NASA added a fifty-foot extension for the robotic arm, called the Orbiter Boom Sensor System, with laser sensors on the end. Astronauts used it to scan the wing edges and the belly in space, looking for cracks or holes. First flown on mission STS-114, in two thousand five.""",
     "Space Shuttle OBSS boom inspection")
sc("""Before that, the crew had no way to check the heat shield after launch. With the boom, they could look at the wing edges, the nose and the belly, and send the images to the ground, where engineers could decide if the shuttle was safe to bring back.""",
   "Space Shuttle robotic arm inspection", "INSPECTING IN ORBIT")
sc("""It was a simple idea, a long stick with sensors on it, but it changed how every mission ended. Now a hole in the heat shield could be found in orbit, instead of during reentry.""",
   "Space Shuttle STS-114 Discovery", "FOUND IN ORBIT")

# ---------- 10. GAP FILLERS ----------
part(10, "The sticking-out gap filler", "WHY WAS THIS STRIP SPACE-WALKED OUT?", "Why Did an Astronaut Pull a Strip Out of the Space Shuttle?",
     """Why did an astronaut pull a strip of fabric from the belly of the shuttle in space? On mission STS-114, two gap fillers were sticking out of the tiles on the belly of Discovery, each less than about one point two inches. NASA estimated that, left alone, they could raise the heating during reentry by about twenty-five percent. A strip of fabric had become a safety question.""",
     "Space Shuttle STS-114 gap filler")
sc("""An astronaut was sent out on the end of the robotic arm, to a spot under the shuttle, and pulled the two fillers out with his hands. The job took only a few minutes, and the shuttle landed safely.""",
   "Space Shuttle spacewalk repair", "FIXED WITH BARE HANDS")
sc("""And that is the shuttle's heat shield in a nutshell. Thousands of small parts, each one chosen for its own place, each one a possible weak point, and a whole crew watching them until the wheels touched the runway.""",
   "Space Shuttle landing runway", "EVERY PIECE MATTERS")

# ---------- VERDICT ----------
sc("""So here are the ten. Black tiles for the heat, white tiles on top, gaps to let the skin move, a gray nose and wing edges made of carbon, soft white felt where it stays cooler. Numbered tiles, one for each place, a waterproofing syringe, a boom to inspect the damage, and a strip of fabric that mattered more than it looked.""",
   "Space Shuttle landing", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see a shuttle in a museum, look at the belly. It is not a black paint job. It is a skin of glass, built for the hottest ride a human has ever taken. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Space Shuttle museum", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:STS-114 Discovery thermal protection system (S114-E-6405).jpg", 0.45, 0.5),
    2: ("File:Discovery - thermal protection tiles.jpg", 0.3, 0.6),
    3: ("File:Shuttle heat shield.jpg", 0.5, 0.55),
    4: ("File:Space Shuttle Discovery Nose (29553281).jpeg", 0.5, 0.5),
    5: ("File:Tested RCC panel with hole.JPG", 0.5, 0.35),
    6: ("File:STS080-307-012 - STS-080 - View of payload bay doors being opened - DPLA - fe26b5aa28266d55a7585fdad347c49d.jpg", 0.5, 0.4),
    7: ("File:STS-118 damaged tile.jpg", 0.3, 0.45),
    8: ("File:Silica Space Shuttle thermal protection (TPS) tile, c 1980. (9663807484).jpg", 0.5, 0.5),
    9: ("File:S114E5333 - STS-114 - Orbiter Boom Sensor System extended - DPLA - 6e3fd7f915349a5b57eb2372fbdae23d.jpg", 0.4, 0.3),
    10: ("File:S114E6666 - STS-114 - Gap filler material - DPLA - e059ad12a23a5e6da6f818e73da8fb3d.jpg", 0.45, 0.55),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video12", "title": "Why Was the Space Shuttle Covered in Tiles?",
           "length_scale": 1.6, "scenes": S}, open("videos/video12/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
