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
sc("""Look at almost any big cargo ship in port, and you will see the same thing. Black or blue on top, and a band of red below, right down to the keel. Container ships, tankers, bulk carriers, all red underneath. It is not a fashion. That red is a weapon, in a war against tiny animals that has lasted for centuries. Today, ten parts of a cargo ship's hull, and why each one exists.""",
   "cargo ship red hull", "WHY RED?", cuts=8, chapter="Intro")
sc("""The ocean is full of life, and much of it wants to live on a ship. Barnacles, mussels, weed and slime all grow on any surface left in the water. On a ship, that growth is called fouling, and it is one of the most expensive problems in shipping.""",
   "barnacles on hull", "LIFE WANTS TO LIVE ON SHIPS")
sc("""As always, every fact here comes from a named source, maritime organisations and naval references, all listed in the description. Let's start with the red.""",
   "ship in dry dock", "WHY DOES THIS EXIST?")

# ---------- 1. RED PAINT ----------
part(1, "The red paint", "WHY IS THIS SHIP RED UNDERNEATH?", "Why Are Cargo Ships Red Below the Waterline?",
     """Why are cargo ships red below the waterline? Because of the paint that keeps sea life away. It is called antifouling paint. For a long time, the most common ingredient was copper oxide, a copper compound that is poisonous to barnacles and other creatures, and naturally reddish.""",
     "antifouling paint ship")
sc("""The paint slowly releases tiny amounts of copper into the water right next to the hull. Young barnacles and other larvae that try to settle on the surface are killed or driven away. Many modern paints work in a self polishing way, slowly wearing off as the ship moves, always exposing a fresh layer.""",
   "ship hull paint", "A SLOW RELEASE")
sc("""Today, antifouling paint can be made in many colours, and some ships are painted black, blue or grey underneath. But red stayed the tradition, partly because of the copper, and partly because it makes it easy to see where the antifouling stops. Red below, other colours above, has become the uniform of the sea.""",
   "red hull ship dry dock", "THE UNIFORM OF THE SEA")

# ---------- 2. COPPER ----------
part(2, "The copper sheathing", "WHY DID WOODEN SHIPS HAVE COPPER BOTTOMS?", "Why Did Old Ships Have Copper Bottoms?",
     """Why did old wooden warships have bottoms covered in copper? To protect them from a small creature called the shipworm. It is actually a kind of clam that bores into wood, eating tunnels through the planks of a ship. A wooden hull could be eaten from inside in just a few years in warm waters.""",
     "copper sheathing ship")
sc("""In the seventeen sixties, the Royal Navy tried covering a ship's hull with thin sheets of copper. It worked. The copper stopped the shipworm and also kept weed and barnacles away, so ships stayed faster for longer. Within a couple of decades, much of the fleet was copper bottomed.""",
   "HMS Victory hull", "THE ROYAL NAVY TRIED IT")
sc("""Copper bottomed ships could stay at sea longer and sail faster than their enemies, a real advantage in war. That is where the English expression copper bottomed comes from, meaning something safe and reliable. The red paint on modern ships is the direct descendant of those copper sheets.""",
   "copper hull sheathing", "COPPER BOTTOMED")

# ---------- 3. TBT ----------
part(3, "The banned paint", "WHY WAS THIS SHIP PAINT BANNED?", "Why Was the Best Ship Paint Ever Banned?",
     """Why was one of the most effective ship paints ever made banned around the world? It contained a chemical called tributyltin, or T B T. From the nineteen sixties, it was used in antifouling paint, and it worked extremely well. Hulls stayed clean for years.""",
     "antifouling ship hull")
sc("""But T B T did not only kill barnacles. It leaked into harbours and coastal waters and harmed a wide range of sea life. Oyster farms in France collapsed, with deformed shells, and some sea snails developed abnormal changes. The chemical was found to be one of the most toxic substances ever deliberately put into the sea.""",
   "oyster farm", "IT HARMED THE OCEAN")
sc("""France began restricting it in the early nineteen eighties. The International Maritime Organization later agreed a global ban, which fully took effect in two thousand eight. Ships had to switch to other paints, many based on copper again. A perfect solution for ships turned out to be a disaster for the ocean.""",
   "ship being painted", "A GLOBAL BAN")

# ---------- 4. BARNACLES ----------
part(4, "The barnacles", "WHY ARE BARNACLES SO EXPENSIVE?", "Why Are Barnacles a Ship's Worst Enemy?",
     """Why are tiny barnacles such a big problem for giant ships? Because they make the hull rough. A smooth hull slides through the water. A hull covered in barnacles, weed and slime drags a thick layer of water with it, and that friction costs power.""",
     "barnacles")
sc("""Heavy fouling can increase the fuel a ship burns by tens of percent. For a large ship, that can mean thousands of tonnes of extra fuel per year, and much more pollution. Navies have studied this for decades, because a fouled warship is slower and has less range.""",
   "fouled ship hull", "THOUSANDS OF TONNES OF FUEL")
sc("""Barnacles are also remarkably good at sticking. Their glue is one of the strongest natural adhesives known, and scientists study it for medical and industrial uses. Once a barnacle has settled, scraping it off is hard work. Stopping it from landing in the first place is the whole strategy.""",
   "barnacle", "THE STRONGEST GLUE")

# ---------- 5. BOOT TOP ----------
part(5, "The boot top", "WHY IS THERE A STRIPE AT THE WATERLINE?", "Why Do Ships Have a Stripe at the Waterline?",
     """Why do many ships have a separate stripe of colour at the waterline? It is called the boot top. That band of the hull is sometimes underwater and sometimes in the air, as the ship is loaded, unloaded, and rolls in the waves. It gets wet, dry, sunlight and scraping from docks and tugboats.""",
     "boot topping ship")
sc("""Those conditions are tougher than either the deep underwater hull or the top sides. So the boot top is painted with a special tough coating, designed to resist wear, sunlight and fouling at the same time. The stripe makes it easy to see where that special paint is.""",
   "ship waterline", "THE TOUGHEST ZONE")
sc("""On a loaded ship, the boot top may be completely underwater. On an empty ship, the red bottom can rise high above the sea. Watching how much red shows is a quick way to tell whether a cargo ship is full or empty, even from the shore.""",
   "empty cargo ship", "FULL OR EMPTY?")

# ---------- 6. DRAFT MARKS ----------
part(6, "The draft marks", "WHY ARE THERE NUMBERS ON THE BOW?", "Why Do Ships Have Numbers on the Front?",
     """Why are there numbers painted down the front and back of a ship? They are draft marks, and they show how deep the ship sits in the water. On metric marks, each number is ten centimetres tall, with gaps of ten centimetres between them, so the water level can be read precisely.""",
     "draft marks ship")
sc("""The draft decides whether a ship can enter a port, pass through a canal or cross a shallow area. It also tells how much cargo the ship is carrying. A surveyor reads the marks at the bow, the middle and the stern, and from the depth, calculates the weight of cargo on board.""",
   "ship draft marks bow", "WEIGHING CARGO BY DEPTH")
sc("""This is called a draft survey, and for bulk cargo like coal, grain or iron ore, it is often how the cargo is weighed and paid for. A few painted numbers can decide a sale worth millions. It is one of the oldest measuring methods in trade, and still in daily use.""",
   "bulk carrier", "WORTH MILLIONS")

# ---------- 7. SILICONE ----------
part(7, "The slippery coating", "WHY IS THIS HULL SO SLIPPERY?", "Why Do Some Ships Have Slippery Hulls?",
     """Why do some modern ships have hulls coated in a slippery, rubbery layer? It is a foul release coating, often based on silicone. Instead of poisoning sea life, it makes the surface so smooth and slippery that creatures cannot stick well. When the ship moves, the water washes most of them off.""",
     "foul release coating")
sc("""These coatings release no poison into the sea, which makes them attractive as rules on toxic paints get stricter. They work best on ships that move fast and often, because the flowing water is what cleans them. A ship that sits still for weeks may still collect growth.""",
   "ship hull smooth", "NO POISON")
sc("""A smooth hull also reduces friction, saving fuel even when it is clean. Some coatings are inspired by nature, by the skin of sharks or dolphins, which stay clean without poison. The war against barnacles is slowly moving from killing them to simply giving them nowhere to hold on.""",
   "shark skin", "NOWHERE TO HOLD ON")

# ---------- 8. DRY DOCK ----------
part(8, "The dry dock", "WHY DOES THIS SHIP LEAVE THE WATER?", "Why Do Giant Ships Have to Leave the Water?",
     """Why do giant ships have to leave the water regularly? To inspect and repaint the hull. A dry dock is a basin that can be emptied. The ship floats in, the gates close, the water is pumped out, and the ship settles onto blocks, revealing the whole underwater hull.""",
     "ship in dry dock")
sc("""Classification societies, the organisations that certify ships as safe, require regular inspections of the hull. Large ships typically visit a dry dock every few years. Workers blast off old paint and growth, check the steel, the propeller, the rudder and the anodes, and apply fresh coats of antifouling.""",
   "ship hull blasting", "INSPECT AND REPAINT")
sc("""Between dry docks, divers and underwater robots can clean the hull in the water. But for a full inspection, the ship must come out. A stop in dry dock costs time and money, which is why long lasting hull paint is so valuable to shipping companies.""",
   "hull cleaning robot", "TIME AND MONEY")

# ---------- 9. BALLAST WATER ----------
part(9, "The ballast water system", "WHY DOES THIS SHIP TREAT ITS WATER?", "Why Do Ships Have to Clean Their Ballast Water?",
     """Why do ships now have systems to treat the sea water they carry? Empty cargo ships take on sea water, called ballast, to sit deeper and stay stable. They carry it across the ocean, and pump it out when they load cargo, in a different part of the world.""",
     "ballast water treatment")
sc("""That water is full of tiny living things, larvae, plankton and bacteria. Released in a new place, some of them can spread out of control. The zebra mussel, carried in ballast water to the Great Lakes of North America, multiplied enormously and clogged water pipes and power plants, costing huge sums.""",
   "zebra mussels", "INVADERS IN THE TANKS")
sc("""Since two thousand seventeen, an international convention requires ships to manage their ballast water, and many now treat it with filters and ultraviolet light or chemicals before releasing it. The hull keeps life out with paint, and the tanks keep it in with treatment. Both protect the ocean.""",
   "ship ballast discharge", "FILTERS AND LIGHT")

# ---------- 10. TWISTLOCKS ----------
part(10, "The twistlocks", "WHY DON'T CONTAINERS FALL OFF SHIPS?", "Why Don't Shipping Containers Fall Off Ships?",
     """Why don't shipping containers fall off ships in storms? Because each corner is locked to the one below. Every container has strong steel corner castings, with oval holes. A small device called a twistlock fits into those holes, and a quarter turn locks two containers together.""",
     "twistlock container")
sc("""On deck, containers are also tied down with long steel bars called lashing rods, crossing between the stacks. Together, the twistlocks and lashings hold stacks that can be many containers high, against the rolling and pitching of the ship in heavy seas.""",
   "container lashing", "LASHING RODS")
sc("""Even so, in very bad weather, the forces can exceed the limits, and containers are sometimes lost at sea, occasionally many at once. That is why ships slow down or change course in storms. Every container on the ocean is held by a few small steel locks, turned by hand in a port.""",
   "container ship storm", "A FEW SMALL LOCKS")

# ---------- VERDICT ----------
sc("""So here are the ten. Red paint that keeps sea life away. Copper bottoms against the shipworm. A banned paint that harmed the ocean. Barnacles that burn fuel. A stripe for the toughest zone. Numbers that weigh the cargo. Slippery coatings without poison. Dry docks to inspect and repaint. Ballast water treated against invaders. And twistlocks that keep containers on board.""",
   "cargo ship", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""The red on a ship is the colour of a centuries old war against tiny creatures. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments, did you know why ships are red underneath?""",
   "cargo ship sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video38", "title": "Why Are Cargo Ships Red Below the Waterline?",
           "length_scale": 1.6, "scenes": S}, open("videos/video38/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
