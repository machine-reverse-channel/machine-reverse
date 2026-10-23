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
sc("""A tower crane is a thin steel pole, sometimes taller than a thirty story building, with a long arm sticking out to one side. It lifts tonnes of steel over the heads of people, and on a windy night, nobody is in it. By every instinct, it should fall over. It almost never does. Today, eleven parts of a tower crane, and why each one exists.""",
   "tower crane", "WHY DOESN'T IT FALL?", cuts=8, chapter="Intro")
sc("""Tower cranes build almost every tall building in the world. They are put up in pieces, they grow with the building, and when the job is done, they disappear. Most people walk past them every day and never ask how a structure that looks this fragile can lift this much.""",
   "tower crane", "THEY BUILD EVERY CITY")
sc("""As always, every fact comes from a named source, crane makers, safety agencies, and official accident reports, all listed in the description. Let's start with the most important part, the one on the short arm.""",
   "tower crane counterweight", "WHY DOES THIS EXIST?")

# ---------- 1. COUNTERWEIGHT ----------
part(1, "The concrete blocks on the short arm", "WHY ARE THERE CONCRETE BLOCKS UP THERE?", "Why Do Tower Cranes Have Concrete Blocks on Top?",
     """Why does a tower crane carry heavy concrete blocks on its short arm? Because it is a giant seesaw. The long arm, called the jib, carries the load on one side of the mast. The short arm, called the counter jib, carries the counterweight on the other side. The blocks balance the weight of the jib and part of the load, so the mast is pushed mostly straight down, not bent to one side.""",
     "tower crane counterweight")
sc("""The counterweight can be made of several concrete slabs, adding up to tens of tonnes on a big crane. It is fixed in place, so it cannot balance every load perfectly. When the hook is empty, the crane leans a little toward the counterweight. When it lifts a heavy load, it leans the other way. The mast is designed to handle both.""",
   "tower crane", "A GIANT SEESAW")
sc("""That is also why the counterweight blocks are put on in a precise order when the crane is assembled. If the jib is not installed yet and too many blocks are added, the crane can tip backward. Every step of putting a crane together follows a written sequence from the maker.""",
   "Potain tower crane", "IN A PRECISE ORDER")

# ---------- 2. LOAD CHART ----------
part(2, "The hook that lifts less at the tip", "WHY CAN'T THIS HOOK LIFT MORE?", "Why Can a Tower Crane Lift Less at the End of Its Arm?",
     """Why can a tower crane lift a heavy load near the mast but only a small one at the tip of its jib? Because what matters is not just the weight, it is the weight times the distance. Ten tonnes close to the mast twists the crane much less than ten tonnes at the far end. So the farther out the trolley carries the hook, the lighter the load it is allowed to lift.""",
     "Potain tower crane")
sc("""Every crane has a load chart, a table that shows the maximum load at each distance. A crane that can lift around twelve tonnes near the mast may be allowed only two or three tonnes at the tip of a long jib. The operator is trained to read it, but the crane does not trust the operator alone.""",
   "tower crane jib", "THE LOAD CHART")
sc("""Inside, devices called limiters measure the load on the hoist rope and the position of the trolley. If a lift goes over the limit, the crane refuses. It stops the hoist from lifting higher and stops the trolley from moving out. It can only move in the safe direction, bringing the load closer to the mast.""",
   "tower crane", "THE CRANE SAYS NO")

# ---------- 3. FOUNDATION ----------
part(3, "The hidden foundation", "WHY IS THERE A GIANT BLOCK UNDER THE CRANE?", "Why Do Tower Cranes Need a Giant Concrete Block?",
     """Why does a tower crane need a huge block of concrete under it, hidden underground? Because the counterweight can only balance part of the load. The rest of the tipping force goes down the mast to the base. The bottom of the mast is bolted to anchors cast into a concrete foundation, often hundreds of tonnes of it, which holds the crane upright like the roots of a tree.""",
     "tower crane base foundation")
sc("""The foundation is designed for the worst case, the strongest wind at the site plus the crane's heaviest load. Engineers check the soil under it too. Weak ground can let the foundation tilt, and a crane that leans even a little at the bottom leans a lot at the top.""",
   "tower crane", "THE WORST CASE")
sc("""In two thousand six, in Bellevue, Washington, a tower crane fell onto apartment buildings during a storm, and a man inside was killed. Investigators found that the steel base the crane stood on had been poorly designed. Since then, many cities require engineers to approve every crane base before the crane goes up.""",
   "crane collapse", "BELLEVUE, 2006")

# ---------- 4. CLIMBING ----------
part(4, "The mast that grows", "WHY DOES THIS CRANE GROW TALLER?", "Why Do Tower Cranes Grow Taller By Themselves?",
     """How does a tower crane get taller as the building rises? It lifts itself. A climbing frame around the mast has hydraulic jacks that push the whole top of the crane up by a few meters. That opens a gap, and the crane uses its own hook to lift a new mast section into it. The section is bolted in, and the crane has grown one step taller.""",
     "Liebherr tower cranes")
sc("""A crane standing on its own can only go so high before the wind and the loads bend the mast too much. So tall cranes are tied to the building with steel collars and braces every few floors. The building that the crane is building becomes its support.""",
   "tower crane", "TIED TO THE BUILDING")
sc("""Climbing is one of the most dangerous moments in a crane's life. During the jump, the top of the crane is held only by the climbing frame. Wind limits are lower, the jib must be balanced exactly, and nobody is allowed to lift anything else. It is done slowly, by specialist crews, following the maker's procedure step by step.""",
   "tower crane mast climbing", "THE DANGEROUS JUMP")

# ---------- 5. FREE SLEW ----------
part(5, "The crane that spins in the wind", "WHY IS THIS CRANE LEFT FREE TO SPIN?", "Why Are Tower Cranes Left to Spin in the Wind at Night?",
     """Why do crane operators release the brakes at night, so the crane can spin freely in the wind? Because a crane fighting the wind is in danger, and a crane turning with it is not. When the slewing brake is released, the wind pushes the jib around until it points downwind, like a weathervane. The long jib then shows its narrow end to the wind, and the force on the crane drops.""",
     "Liebherr tower crane")
sc("""If the brake were locked, a storm hitting the side of the jib could push with enormous force, and the crane might break or topple. So the rule on most sites is simple. When work stops, raise the hook, park the trolley, and set the crane to free slew. People who see cranes turning on their own at night are watching a safety system work.""",
   "tower crane", "LIKE A WEATHERVANE")
sc("""During the day, cranes have an anemometer on top that measures the wind. Above a certain speed, often around seventy kilometers an hour for normal work and lower for big flat loads, lifting must stop. A sheet of plywood or a glass panel acts like a sail, and the wind can swing it out of control.""",
   "crane anemometer", "STOP AT 70 KM/H")

# ---------- 6. SLEWING RING ----------
part(6, "The giant bearing", "WHY DOES THIS CRANE TURN ON A GIANT BEARING?", "Why Does a Tower Crane Turn on a Giant Bearing?",
     """Why does the top of a tower crane sit on a giant ring? Because the whole upper crane, the jib, the counter jib, the counterweight and the cab, has to turn around on top of the mast while carrying the load. The slewing ring is a huge ball or roller bearing that holds all of that weight, while letting it rotate smoothly in a full circle.""",
     "tower crane slewing ring")
sc("""The ring has gear teeth cut into it. Electric motors with small gears turn against those teeth, slowly rotating the crane. Frequency drives let them start and stop very smoothly, because a sudden stop would make the load swing like a pendulum, tens of meters below.""",
   "tower crane slewing", "NO SUDDEN STOPS")
sc("""The bolts that hold the slewing ring are among the most critical in the crane. They are tightened to an exact force and inspected regularly. If they loosen or crack, the top of the crane can separate from the mast. A few bolts are all that hold the top in place.""",
   "tower crane", "A FEW CRITICAL BOLTS")

# ---------- 7. CAB ----------
part(7, "The cab at the top", "WHY DOES THE OPERATOR SIT UP HERE?", "Why Do Crane Operators Sit So High Up?",
     """Why does the crane operator sit in a small cab at the top, tens of meters up? Because from there, they can see most of the site and the path of the load. On a busy site, the hook travels over workers, roads and other cranes. Being high up and close to the slewing ring also lets the operator feel how the crane moves.""",
     "tower crane cab")
sc("""Getting there means climbing ladders inside the mast, sometimes for more than ten minutes on very tall cranes. So many operators go up once at the start of the shift and stay there all day, with food and water. Some newer cranes have lifts in the mast, and some are controlled by remote from the ground.""",
   "Potain crane cab", "UP ONCE A DAY")
sc("""Even from the cab, the operator often cannot see the load, for example when it is behind a wall or several floors down. So a signaler on the ground or on the building guides each lift by radio. The operator moves the load blind, trusting the voice in their ear.""",
   "tower crane", "MOVING BLIND")

# ---------- 8. LUFFING JIB ----------
part(8, "The arm that points up", "WHY DOES THIS CRANE'S ARM POINT UP?", "Why Do Some Tower Cranes Have Arms That Point Up?",
     """Why do some tower cranes have a jib that tilts up into the sky instead of sticking out flat? Because in a crowded city, a flat jib would swing over neighboring buildings, roads and other cranes. A luffing jib crane changes its reach by raising or lowering the jib. When it does not need to reach far, the jib points almost straight up, taking very little space.""",
     "luffing jib crane")
sc("""Swinging a load over someone else's property is called oversailing, and in many cities it needs permission from the owner. Luffing cranes avoid most of it. They also let many cranes work close together on one site, each one raising its jib to pass above or below the others.""",
   "luffing jib crane", "OVERSAILING")
sc("""The price is complexity. A luffing crane needs a strong winch to raise and lower the jib with the load, and the jib itself is heavier. But in places like London, New York or Hong Kong, where every meter of sky is shared, the forest of upward pointing cranes is a common sight.""",
   "tower crane", "A FOREST OF ARMS")

# ---------- 9. SELF-ERECTING ----------
part(9, "The crane that unfolds itself", "WHY CAN THIS CRANE BUILD ITSELF?", "Why Can Some Cranes Unfold Themselves in Hours?",
     """Why can this crane arrive on a truck and stand up by itself in a few hours? Because it is a self erecting crane. The mast and jib are folded for transport, and the crane carries its own motors and ballast. On site, it unfolds itself, raising the mast and swinging out the jib, without another crane to help.""",
     "self-erecting tower crane")
sc("""These cranes are made for smaller jobs, houses, low buildings and renovations, where bringing a big mobile crane for weeks would cost too much. They lift less and reach less, but they are fast to set up and easy to move to the next site.""",
   "self-erecting tower crane", "UP IN HOURS")
sc("""Because they stand on a small base with ballast instead of a deep foundation, they rely on the ground being level and firm. A soft corner, or a missing outrigger pad, is enough to tip one over. Even a small crane follows the same rule as a big one. The ground decides.""",
   "tower crane", "THE GROUND DECIDES")

# ---------- 10. DISMANTLING ----------
part(10, "The pins that came out too early", "WHY DO CRANES FALL WHEN TAKEN APART?", "Why Do Tower Cranes Fall While Being Taken Apart?",
     """Why do so many tower crane accidents happen not during lifting, but while the crane is being put up or taken down? Because in those moments, the crane is incomplete. Parts are missing, the balance is changing, and pins or bolts are removed one by one. A step done out of order can leave a section held by nothing.""",
     "crane collapse")
sc("""In April two thousand nineteen, in Seattle, a tower crane being taken apart fell onto a street during strong winds. Four people were killed, two of them in cars below. Investigators found that pins holding mast sections together had been removed early, before the sections were ready to be lifted off, to save time.""",
   "crane collapse", "SEATTLE, 2019")
sc("""That is why makers publish exact sequences for erection and dismantling, with wind limits, and why many places now require trained, certified crews for this work. The crane is strongest when complete. The moments in between are where it is weakest.""",
   "tower crane", "WEAKEST IN BETWEEN")

# ---------- 11. LAST CRANE ----------
part(11, "The crane that takes down the crane", "WHY DOES A CRANE NEED A CRANE?", "Why Does a Skyscraper Crane Need Another Crane to Get Down?",
     """How does the last crane get down from the top of a finished skyscraper? It needs another crane. When the building is done, a smaller crane is set up on the roof. It takes the big crane apart and lowers the pieces. Then an even smaller crane takes that one apart, and so on, until the last one is small enough to carry down in the building's lifts.""",
     "Tower cranes Edinburgh")
sc("""On the tallest towers in the world, this chain can take weeks. Every piece must be lowered carefully past windows that are already installed. The holes in floors and walls where the crane stood are then closed up, and from the street, nobody can tell a crane was ever there.""",
   "tower crane", "A CHAIN OF CRANES")
sc("""It is the last trick of a machine that is built to disappear. It arrives in pieces, grows with the building, holds it up, and leaves without a trace. All while staying upright, thanks to a counterweight, a foundation and a set of rules written in other people's accidents.""",
   "tower crane", "BUILT TO DISAPPEAR")

# ---------- VERDICT ----------
sc("""So here are the eleven. Concrete blocks on the short arm, and a hook that lifts less at the tip. A hidden foundation, and a mast that grows. A crane set free to spin in the wind, turning on a giant bearing, with an operator sitting at the top. An arm that points up, a crane that unfolds itself, pins that came out too early, and a crane that needs a crane to come down.""",
   "tower crane", "11 PARTS. 0 FALLS (MOSTLY).", chapter="The verdict", cuts=6)
sc("""Next time you see a tower crane turning slowly over a city at night, you will know it is doing exactly what it was designed to do. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "tower crane", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Grue chantier.JPG", 0.11, 0.25),
    2: ("File:Potain tower crane1bis.jpg", 0.12, 0.65),
    3: ("File:A shot of the One Rincon Hill construction pit, the base of the crane and advertising banners, SF.JPG", 0.67, 0.6),
    4: ("File:Liebherr tower cranes dallas texas uptown 2009-08-18.jpg", 0.6, 0.5),
    5: ("File:Liebherr tower crane at reconstruction of the GES-2 in Moscow.jpg", 0.38, 0.4),
    6: ("File:Electric motor on the slewing bearing of a remote controlled yellow Liebherr tower crane.jpg", 0.5, 0.35),
    7: ("File:Potain tower crane4 - Cabin.jpg", 0.48, 0.3),
    8: ("File:Red Crane (16014404989).jpg", 0.62, 0.3),
    9: ("File:Seymour Flats Lisburn Comedil self erecting tower cran.jpg", 0.72, 0.45),
    10: ("File:Crane collapse (day after the crane fell down) - Bellevue, Washington.jpg", 0.6, 0.6),
    11: ("File:Tower cranes Edinburgh in 2019.jpg", 0.42, 0.3),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video52", "title": "Why Don't Tower Cranes Fall Over?",
           "length_scale": 1.6, "scenes": S}, open("videos/video52/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
