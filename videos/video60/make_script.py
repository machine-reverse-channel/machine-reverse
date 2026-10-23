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
sc("""Look at the back of a big bulldozer and you will see something strange. A giant steel claw, hanging there like a scorpion's tail. Most people think the blade at the front is the whole machine. But on hard ground, the blade is useless without that claw. Today, eleven parts of a bulldozer, and why each one exists, starting with the claw.""",
   "bulldozer ripper", "WHY IS THERE A CLAW?", cuts=8, chapter="Intro")
sc("""Bulldozers build roads, airports, dams and mines. They clear land after disasters and push rock in quarries all day long. The biggest ones weigh more than a hundred tonnes, and they move dirt that no human crew could ever move by hand. Every part on them is built for brute force, and for surviving it.""",
   "Caterpillar D11", "BRUTE FORCE")
sc("""As always, every fact comes from a named source, machine makers, engineering references, and museum archives, all listed in the description. Let's start at the back.""",
   "bulldozer ripper", "WHY DOES THIS EXIST?")

# ---------- 1. RIPPER ----------
part(1, "The claw on the back", "WHY DOES THIS BULLDOZER HAVE A CLAW?", "Why Do Bulldozers Have a Claw on the Back?",
     """Why do bulldozers have a giant claw on the back? It is called a ripper. A blade can only push loose material. On hard, packed ground, frozen soil or soft rock, it just slides over the top. So the operator lowers the ripper into the ground and drives forward, and the claw tears the ground open, like a giant plow. Then the dozer turns around and pushes the broken material with its blade.""",
     "bulldozer ripper")
sc("""Ripping is often cheaper than blasting with explosives. In many quarries and mines, rock that is cracked or layered can be ripped instead of blown up, which is safer, quieter, and needs no drilling. A big dozer with a single shank ripper can break rock that would stop almost any other machine.""",
   "dozer ripper shank", "CHEAPER THAN EXPLOSIVES")
sc("""The whole weight of the dozer pushes the ripper down, and hydraulic cylinders adjust its angle. That is one reason big dozers are so heavy. The weight is not a side effect. It is part of the tool.""",
   "bulldozer ripper", "THE WEIGHT IS THE TOOL")

# ---------- 2. RIPPER TIP ----------
part(2, "The replaceable tooth", "WHY DOES THIS CLAW HAVE A SEPARATE TIP?", "Why Does a Bulldozer Claw Have a Removable Tip?",
     """Why does the ripper have a small separate tip at its end? Because rock grinds steel away fast. The point that digs into the ground takes all the wear, and it can be worn down in hours in hard rock. So the shank, the long arm, is protected by a removable tip, and sometimes by a replaceable shield around it.""",
     "dozer ripper shank")
sc("""When the tip wears out, a mechanic knocks out a pin and slides on a new one. It takes minutes instead of replacing the whole shank, which can weigh tonnes. The same idea is used on excavator buckets, with their rows of replaceable teeth.""",
   "bulldozer ripper", "MINUTES, NOT HOURS")
sc("""The tips are made of very hard, wear resistant steel. Designers balance hardness and toughness, because a tip that is too hard can crack when it hits a boulder, and a tip that is too soft wears away. It is a small part doing the hardest job on the machine.""",
   "dozer ripper shank", "HARD BUT NOT BRITTLE")

# ---------- 3. HIGH DRIVE ----------
part(3, "The raised sprocket", "WHY IS THIS TRACK SHAPED LIKE A TRIANGLE?", "Why Do Some Bulldozer Tracks Look Like Triangles?",
     """Why do big Caterpillar dozers have tracks shaped like a triangle, instead of a flat oval? Because the drive gear, called the sprocket, is lifted high up, out of the dirt. Caterpillar introduced this elevated sprocket design in the late nineteen seventies. Before that, the sprocket sat low, at ground level, where it took every shock from the ground and was buried in mud and rock.""",
     "elevated sprocket bulldozer")
sc("""Raising it keeps the final drive, the gears that turn the sprocket, away from the worst impacts and the abrasive dirt. It also makes those parts modular, so they can be removed and replaced more easily. The lower part of the track stays long and flat on the ground, to keep the machine stable and pushing.""",
   "bulldozer sprocket", "OUT OF THE DIRT")
sc("""It became a signature of Caterpillar's track type tractors. If you see a dozer with a triangle shaped track, you can usually guess the brand from a distance. A design choice made for durability became a visual trademark.""",
   "Caterpillar D9", "A VISUAL TRADEMARK")

# ---------- 4. BLADE ----------
part(4, "The curved blade", "WHY IS THIS BLADE CURVED?", "Why Is a Bulldozer Blade Curved?",
     """Why is a bulldozer blade curved instead of flat? Because a curved blade rolls the material. As the dozer pushes, the dirt rises up the curved face and tumbles forward, folding over itself. That rolling action moves the load ahead of the blade with less effort than scraping it as a flat pile.""",
     "bulldozer blade")
sc("""Blades come in different shapes for different jobs. A straight blade is good for leveling and grading. A U blade has big wings at the sides, so it can carry a large load over long distances without spilling it. A semi U blade is in between. The cutting edge at the bottom is a bolted on strip of hardened steel, replaced when it wears down.""",
   "bulldozer blade", "U, S AND STRAIGHT")
sc("""Hydraulic cylinders lift the blade, tilt it from side to side and sometimes pitch it forward or back. Modern dozers can even control the blade automatically with GPS, cutting the ground to an exact design within a few centimeters, without survey stakes.""",
   "bulldozer", "BLADES GUIDED BY GPS")

# ---------- 5. TRACKS ----------
part(5, "The steel tracks", "WHY DO BULLDOZERS USE TRACKS?", "Why Do Bulldozers Use Tracks Instead of Wheels?",
     """Why do bulldozers use tracks instead of wheels? Because pushing is all about grip. A dozer can only push as hard as its tracks can grip the ground before they slip. Tracks put a long strip of steel on the ground, with grousers, little ridges that dig in. That gives far more traction on soft or loose ground than tires could.""",
     "bulldozer track")
sc("""Tracks also spread the weight. A heavy dozer can drive across soft ground where a truck would sink. Special swamp dozers have extra wide tracks, so their ground pressure is very low, and they can work in marshes and wetlands.""",
   "bulldozer track", "WIDE TRACKS FOR SWAMPS")
sc("""The price is wear. The steel links, pins, rollers and sprockets grind against dirt and rock all day. On big machines, the undercarriage can be one of the biggest maintenance costs. A track that looks indestructible is actually slowly wearing out with every meter.""",
   "bulldozer track", "SLOWLY WEARING OUT")

# ---------- 6. CAB ----------
part(6, "The cage around the operator", "WHY IS THE CAB IN A STEEL CAGE?", "Why Is a Bulldozer Cab Inside a Steel Cage?",
     """Why is the bulldozer operator's cab built inside a strong steel frame? It is called a rollover protective structure, or ROPS. Dozers work on slopes, at the edge of cliffs and on loose fill. If one rolls over, the cab must not collapse onto the operator. The frame is tested to carry the machine's weight and absorb the energy of a rollover.""",
     "bulldozer ROPS")
sc("""It only works if the operator stays inside, so a seat belt is essential. Studies of rollover accidents found that operators who wore seat belts in a ROPS cab usually survived, while many who were thrown out or tried to jump did not.""",
   "bulldozer cab", "WEAR THE BELT")
sc("""Many dozers also have a falling object protective structure, to protect against rocks or trees falling from above. Forestry and demolition dozers often get extra screens and guards. The cab looks like a small office, but it is built like a safety cell.""",
   "bulldozer cab", "A SAFETY CELL")

# ---------- 7. SUPER DOZER ----------
part(7, "The biggest bulldozer", "WHY IS THIS BULLDOZER SO HUGE?", "Why Was the World's Biggest Bulldozer Built?",
     """Why would anyone build a bulldozer weighing about a hundred and fifty tonnes? Because in some mines, a bigger dozer moves material more cheaply. The Komatsu D five seven five A is one of the largest production bulldozers ever made. Its super dozer version has a blade more than seven meters wide that can push about seventy cubic meters of material at once.""",
     "Komatsu D575A")
sc("""The engine makes more than a thousand horsepower. In big coal mines, the giant dozer can push huge amounts of overburden, the rock and soil above the coal, down a slope, straight into the mined out area. That can replace trucks for some jobs.""",
   "Komatsu D575A", "OVER 1,000 HORSEPOWER")
sc("""Like giant mining trucks, it cannot be driven between sites. It is taken apart and moved on many trucks, then reassembled. Caterpillar's D eleven, its rival, is a common sight in mines worldwide. These machines are the heavyweights of moving earth.""",
   "Caterpillar D11", "THE HEAVYWEIGHTS")

# ---------- 8. PUSH BLOCK ----------
part(8, "The bulldozer pushing another machine", "WHY IS THIS BULLDOZER PUSHING A SCRAPER?", "Why Do Bulldozers Push Other Machines?",
     """Why do you sometimes see a bulldozer pushing another machine from behind? The other machine is a scraper, a big wheeled earthmover that slices a thin layer of soil into its bowl. Scrapers are fast on the road, but loading is hard work. So a dozer pushes the scraper from behind while it loads, giving it the extra force it needs to fill quickly.""",
     "bulldozer pushing scraper")
sc("""The dozer uses a special reinforced plate, or push block, so it does not damage its blade or the scraper. One pusher dozer can serve several scrapers, loading them one after another. It is a choreography of machines on big road and airport projects.""",
   "bulldozer push block", "A CHOREOGRAPHY")
sc("""This teamwork is also why dozers are built so strong. They push their own load all day, and then they push other machines too. The bulldozer is the muscle that the rest of the site leans on.""",
   "bulldozer", "THE MUSCLE OF THE SITE")

# ---------- 9. ARMOR ----------
part(9, "The armored bulldozer", "WHY DOES THIS BULLDOZER HAVE ARMOR?", "Why Do Armies Use Armored Bulldozers?",
     """Why do some armies use bulldozers covered in armor? Because engineers need to clear roads, fill trenches, remove obstacles and build defenses, often under fire. The Israeli army uses heavily armored versions of the Caterpillar D nine, with bulletproof glass, armor plates and even cage armor against rockets.""",
     "armored bulldozer")
sc("""Armies around the world use armored dozers to clear the path for other vehicles, push away roadside bombs, and build protective walls of earth. The armor can add many tonnes, but the D nine is heavy and powerful enough to carry it.""",
   "IDF armored Caterpillar D9 bulldozer", "CLEARING THE PATH")
sc("""It shows how useful the basic machine is. A civilian dozer and a military one push dirt the same way. The only difference is what they need to survive while doing it.""",
   "Caterpillar D9", "THE SAME MACHINE")

# ---------- 10. LANDFILL ----------
part(10, "The landfill tracks", "WHY DOES THIS DOZER HAVE SPECIAL TRACKS?", "Why Do Landfill Bulldozers Have Special Tracks?",
     """Why do bulldozers working in landfills look different? Because trash is a terrible surface to drive on. It is soft, full of sharp metal and wire, and packed with things that can wrap around rollers. Landfill dozers get special guards around the undercarriage, sealed parts, and screens that keep trash out of the radiator.""",
     "bulldozer landfill")
sc("""Their main job is to spread and compact the waste, crushing it into thin layers so the landfill holds more and settles less. Some landfills use compactors with steel wheels and big teeth, but tracked dozers are still used to push and spread the trash.""",
   "bulldozer landfill", "CRUSHING THE TRASH")
sc("""Landfill space is expensive, and every cubic meter saved by compaction means the site lasts longer. So the machine driving across your old trash is not just moving it. It is squeezing years of extra life out of the hole in the ground.""",
   "bulldozer landfill", "YEARS OF EXTRA LIFE")

# ---------- 11. YELLOW ----------
part(11, "The yellow paint", "WHY ARE BULLDOZERS YELLOW?", "Why Are Bulldozers Yellow?",
     """Why are bulldozers and so many construction machines yellow? Because yellow is easy to see. In late nineteen thirty one, Caterpillar switched its machines from gray to a bright color it called Highway Yellow. Machines were starting to work on roads with traffic, and a bright color made them more visible to drivers and to workers on site.""",
     "Caterpillar D9")
sc("""It also stands out against dirt, rock and forest, at dawn, at dusk and in dust. Other makers followed with yellow or orange, and today the color is so common that people call it construction yellow. Some brands chose orange, red or green to stand out from Caterpillar, but bright colors won everywhere.""",
   "bulldozer", "HIGHWAY YELLOW")
sc("""A simple color choice became the uniform of an entire industry. When kids draw a bulldozer, they draw it yellow. And it all started as a way to keep people from getting hit by the machines.""",
   "bulldozer", "THE UNIFORM OF AN INDUSTRY")

# ---------- VERDICT ----------
sc("""So here are the eleven. A claw on the back that tears the ground, with a tip that can be replaced in minutes. A raised sprocket that keeps the gears out of the dirt, a curved blade that rolls the load, and tracks that grip. A cage around the operator, a giant built for mines, a dozer that pushes other machines, armor for war, special tracks for trash, and a yellow coat to be seen.""",
   "bulldozer", "11 PARTS. 1 CLAW.", chapter="The verdict", cuts=6)
sc("""Next time you pass a construction site, look at the back of the bulldozer, and you will know what that claw is for. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "bulldozer", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Liebherr bulldozer-20240815-RM-171945.jpg", 0.88, 0.6),
    2: ("File:Liebherr bulldozer-20240815-RM-171945.jpg", 0.9, 0.8),
    3: ("File:CatD11T.jpg", 0.68, 0.4),
    4: ("File:Cat D11 View 2.jpg", 0.25, 0.6),
    5: ("File:Caterpillar track shingle.JPG", 0.5, 0.4),
    6: ("File:Sd8n Big bulldozer.jpg", 0.27, 0.15),
    7: ("File:CatD11T part.jpg", 0.55, 0.5),
    8: ("File:Leading a Scraper Unit - DPLA - b327ad8ba9e71ee28d31460cab0814d1.jpg", 0.2, 0.65),
    9: ("File:IDF-D9-Zachi-Evenor-001.jpg", 0.6, 0.3),
    10: ("File:Landfill compactor.jpg", 0.45, 0.75),
    11: ("File:Komatsu bulldozer pushing coal in Power plant Ljubljana (winter 2017).jpg", 0.3, 0.35),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video60", "title": "Why Do Bulldozers Have a Claw on the Back?",
           "length_scale": 1.6, "scenes": S}, open("videos/video60/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
