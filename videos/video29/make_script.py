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
sc("""Your car door opens sideways, like a door in a house. A Lamborghini door goes straight up. A Mercedes from the nineteen fifties opens like the wings of a seagull. A McLaren door swings up and out like a butterfly. They look like showing off, but most of them started as an engineering problem. Today, ten parts of upward opening doors, and why each one exists.""",
   "Lamborghini Countach doors open", "WHY DO THEY OPEN UP?", cuts=8, chapter="Intro")
sc("""The basic problem is simple. A supercar is low, wide and stiff. The structure that makes it fast, a strong frame running along the sides of the cabin, also gets in the way of a normal door. And a long door that swings sideways needs a lot of space next to the car. Designers have found many different answers to that one problem.""",
   "supercar doors open", "LOW, WIDE AND STIFF")
sc("""As always, every fact here comes from a named source, the car makers and automotive references, all listed in the description. Let's start with the most famous one.""",
   "Lamborghini scissor doors", "WHY DOES THIS EXIST?")

# ---------- 1. SCISSOR ----------
part(1, "The scissor doors", "WHY DOES THIS DOOR GO STRAIGHT UP?", "Why Do Lamborghini Doors Go Straight Up?",
     """Why does a Lamborghini door go straight up? It started with the Countach in the nineteen seventies. The car was very wide and very low, with a wide structure along its sides. A normal door would have been long and heavy, and it would need a lot of space beside the car to open. A door that rotates upward, on a hinge at the front, needs almost no space beside the car at all.""",
     "Lamborghini Countach")
sc("""The idea came from the designer Marcello Gandini, who first used it on a concept car, the Alfa Romeo Carabo, in nineteen sixty-eight. On the Countach it also had a practical side. The rear view was so poor that drivers often reversed by opening the door, sitting on the sill and looking back over the car.""",
   "Alfa Romeo Carabo", "BORN ON A CONCEPT CAR")
sc("""After the Countach, scissor doors became a Lamborghini signature. The Diablo, the Murcielago, the Aventador and the Revuelto all have them. Today they are partly tradition, but they still solve the original problem. You can open a Lamborghini in a narrow parking space where a long, normal door would hit the car next to it.""",
   "Lamborghini Aventador doors", "A SIGNATURE")

# ---------- 2. GULLWING ----------
part(2, "The gullwing doors", "WHY DOES THIS DOOR OPEN LIKE A WING?", "Why Does the Mercedes 300 SL Have Gullwing Doors?",
     """Why does the Mercedes three hundred S L have doors that open like wings? Because of its frame. The car was built on a light frame made of thin steel tubes, called a space frame. To make it stiff, the tubes ran high along the sides of the car, right where a normal door would be. There was simply no room for a normal door.""",
     "Mercedes-Benz 300 SL gullwing")
sc("""The solution was to hinge the doors on the roof. When they open, they lift up and reveal a high, wide sill that the driver has to climb over. With both doors open, the car looks like a seagull with its wings raised, which is where the name gullwing comes from. The road car arrived in nineteen fifty-four, based on a racing car.""",
   "Mercedes-Benz 300 SL space frame", "NO ROOM FOR A NORMAL DOOR")
sc("""Getting in was not easy. The steering wheel could even tilt out of the way, to help the driver climb in. But the stiff, light frame made the car fast, and the doors made it famous. More than fifty years later, Mercedes brought the gullwing back on the S L S A M G, as a tribute to the original.""",
   "Mercedes-Benz SLS AMG doors", "A FAMOUS SOLUTION")

# ---------- 3. BUTTERFLY ----------
part(3, "The butterfly doors", "WHY DOES THIS DOOR SWING UP AND OUT?", "Why Do McLaren Doors Open Like Butterfly Wings?",
     """Why do McLaren doors swing up and out, like butterfly wings? Because they carry part of the roof with them. The hinge sits on the windscreen pillar, and the door rotates up and forward and outward at the same time. When it opens, it takes a piece of the roof along, leaving a big opening for the driver to step in.""",
     "McLaren F1 doors open")
sc("""The McLaren F one road car of the nineteen nineties needed this. It had the driver in the centre, with a passenger seat on each side, slightly behind. To reach the middle seat, you need a huge opening. Butterfly doors that lift part of the roof make it possible to get in and slide across.""",
   "McLaren F1 interior", "THE DRIVER SITS IN THE MIDDLE")
sc("""Modern McLarens still use the idea. The carbon fibre cabin has high, strong sills, and the low roof would hit your head with a normal door. Opening upward and outward gives more room for your head and your legs, and it needs less space beside the car than a long normal door.""",
   "McLaren 720S doors", "ROOM FOR YOUR HEAD")

# ---------- 4. KOENIGSEGG ----------
part(4, "The rotating doors", "WHY DOES THIS DOOR TURN SIDEWAYS?", "Why Do Koenigsegg Doors Rotate Forward?",
     """Why does a Koenigsegg door rotate and swing forward at the same time? The company calls it the dihedral synchro helix door. As it opens, the door moves outward and then turns ninety degrees, standing upright next to the front of the car. It sounds complicated, but it solves two problems at once.""",
     "Koenigsegg doors open")
sc("""First, the door moves out of the way of the high sill, so the opening is large. Second, it ends up standing beside the front wheel, not above the car and not far to the side. That means it needs little space around the car, and it does not hit a low ceiling in a garage or a high kerb beside the road.""",
   "Koenigsegg Agera doors", "OUT OF THE WAY")
sc("""The mechanism is a precise piece of engineering, with a hinge that guides the door along a curved path. Koenigsegg uses it on all its cars, from the early models to the Jesko and the Gemera. It shows that even a door can become a showcase of the same engineering that goes into the engine.""",
   "Koenigsegg Jesko", "A SHOWCASE")

# ---------- 5. FALCON WING ----------
part(5, "The falcon wing doors", "WHY DOES THIS DOOR HAVE TWO HINGES?", "Why Do Tesla Model X Doors Have Two Hinges?",
     """Why does the rear door of a Tesla Model X have two hinges? It is called a falcon wing door. A simple gullwing door on a tall car would swing far out to the side as it lifts. The falcon wing door has a hinge in the roof and a second hinge in the middle, so it folds as it rises, staying close to the car.""",
     "Tesla Model X falcon wing doors")
sc("""According to Tesla, the door needs only about thirty centimetres of space beside the car to open. That makes it easier to get into the rear seats in a tight parking space, and it gives a tall opening, so you do not have to bend down to put a child in a seat. Sensors check for obstacles as it opens.""",
   "Tesla Model X doors open", "THIRTY CENTIMETRES")
sc("""It is not a supercar, but it uses the same idea. When there is little space beside the car, go up. The price is complexity. Two hinges, motors and sensors are more expensive and can go wrong more easily than a simple sliding door, which is why most family cars still use one.""",
   "Tesla Model X", "GO UP, NOT OUT")

# ---------- 6. SILL ----------
part(6, "The high sill", "WHY IS THIS STEP SO HIGH?", "Why Do Supercars Have Such a High Sill?",
     """Why do you have to climb over such a high sill to get into a supercar? Because the sill is the backbone of the car. Most supercars are built around a tub, a stiff shell made of carbon fibre or aluminium. The thick sides of the tub run along the cabin, under the doors, and carry a lot of the car's strength.""",
     "carbon fibre monocoque supercar")
sc("""A stiff car handles better, because the suspension can do its job without the body twisting. And a tall side structure protects the people inside in a side crash. Making the sill lower would mean making it weaker, or heavier. So the engineers keep it high, and design the door around it.""",
   "McLaren MonoCell", "THE BACKBONE")
sc("""That is the real reason so many supercar doors open upward. A door that opens up takes part of the roof or the top of the sill with it, and makes the opening bigger without cutting into the strong structure below. The unusual door is the price of a stiff, light car.""",
   "supercar door sill", "THE REAL REASON")

# ---------- 7. GAS STRUT ----------
part(7, "The gas struts", "WHY DOESN'T THIS HEAVY DOOR FALL?", "Why Don't Supercar Doors Fall Down?",
     """Why doesn't a heavy door that opens upward fall on your head? Because of the gas struts. A gas strut is a cylinder filled with gas under pressure. When the door opens, the gas pushes a rod out, and that push holds the weight of the door. It is the same part that holds up the boot lid on a normal car.""",
     "gas strut")
sc("""On a door that opens sideways, gravity does not matter much. On a door that opens upward, the whole weight of the door is lifted every time. The struts are chosen so the force nearly balances that weight. The door feels light, rises with a small push, and stays open without a latch.""",
   "Lamborghini door hinge", "BALANCING THE WEIGHT")
sc("""The gas inside the struts is affected by temperature, and the seals wear out over time. On a cold day, a door may not rise as easily. On an old car, a worn strut can let the door drift down. That is why owners of cars with upward doors replace the struts as normal maintenance.""",
   "gas spring", "WEAR AND COLD")

# ---------- 8. ROOF CUT ----------
part(8, "The roof cut", "WHY DOES THIS DOOR CUT INTO THE ROOF?", "Why Do Ford GT Doors Cut Into the Roof?",
     """Why does the door of a Ford G T cut into the roof? Because the car is so low. The original Ford G T forty, which won Le Mans in the nineteen sixties, was only about forty inches tall, around one metre. That is where its name comes from. With a roof that low, a normal door would leave almost no opening for the driver's head.""",
     "Ford GT40 doors")
sc("""So the door was extended into the roof. When it opens, it takes a large piece of the roof with it, and the driver can step in and lower themselves into the seat. In racing, this mattered even more, because drivers wear helmets and must get in and out quickly during driver changes.""",
   "Ford GT40", "ONE METRE TALL")
sc("""The modern Ford G T cars kept the idea. Many low race cars and supercars use doors that cut deep into the roof. It is the same lesson as the gullwing, approached from the top instead of the side. When the car is low, the door needs to borrow space from the roof.""",
   "Ford GT 2017 doors", "BORROW FROM THE ROOF")

# ---------- 9. DELOREAN ----------
part(9, "The torsion bars", "WHY DOES THIS DOOR HAVE A TWISTED BAR?", "Why Do DeLorean Doors Have Torsion Bars?",
     """Why do the gullwing doors of the DeLorean have twisted metal bars in the roof? To lift heavy doors. The DeLorean was covered in stainless steel panels, which made the doors heavy. Gas struts alone could not lift them comfortably. So each door also has a torsion bar, a steel bar that is twisted when the door closes, and untwists to help lift it.""",
     "DeLorean DMC-12 doors open")
sc("""The torsion bars were made with help from the aerospace company Grumman and treated with extreme cold, a process that helps the steel hold its shape. The bar stores energy like a spring. Together with gas struts, it lets a heavy door rise with a light push and stay open.""",
   "DeLorean DMC-12", "A TWISTED SPRING")
sc("""Gullwing doors on a low car also need very little space beside the car to open. That is one reason the DeLorean became so memorable, along with its role in a famous time travel film. Behind the movie fame, the doors are a clever answer to a heavy problem.""",
   "DeLorean", "A CLEVER ANSWER")

# ---------- 10. ROLLOVER ----------
part(10, "The rollover bolts", "WHAT IF THIS CAR LANDS ON ITS ROOF?", "Why Do Gullwing Doors Have Explosive Bolts?",
     """What happens if a car with gullwing doors lands on its roof? The doors are hinged to the roof, so they cannot open. The people inside could be trapped. That is a real risk, and it is the most serious problem with doors that open upward.""",
     "Mercedes-Benz SLS AMG gullwing")
sc("""Mercedes solved it on the S L S A M G with small explosive charges in the door hinges. If sensors detect that the car has rolled over, the charges fire and separate the hinges. The doors can then be pushed out and removed, so the people inside can get out, or rescuers can reach them.""",
   "Mercedes-Benz SLS AMG", "SMALL CHARGES IN THE HINGES")
sc("""It is a good example of how every clever part creates a new problem that needs another clever part. The gullwing door solved the problem of the high frame. The explosive hinges solve the problem of the gullwing door. Engineering is often a chain of solutions.""",
   "Mercedes-Benz SLS AMG roadster", "A CHAIN OF SOLUTIONS")

# ---------- VERDICT ----------
sc("""So here are the ten. Scissor doors for wide, low cars. Gullwings for a frame with no room. Butterfly doors that carry part of the roof. Rotating doors that stay out of the way. Falcon wings for tight spaces. A high sill that is the car's backbone. Struts that hold the weight. Roofs cut for helmets. Twisted bars for heavy steel. And explosive bolts for the worst day.""",
   "supercar doors", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A door that opens upward is not just showing off. It is the answer to a car that is low, wide and stiff. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which door you would want on your own car.""",
   "Lamborghini night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Lamborghini Countach LP500 S (52687277904).jpg', 0.25, 0.3),
    2: ('File:Doors of Mercedes-Benz 300 SL Gullwing at Legendy 2014.JPG', 0.3, 0.35),
    3: ('File:NEC Birmingham 1992 Car Show Mclaren - 49998978063.jpg', 0.45, 0.25),
    4: ('File:2012-03-07 Motorshow Geneva 4598.JPG', 0.25, 0.55),
    5: ('File:Tesla Model X P100DL.jpg', 0.6, 0.28),
    6: ('File:McLaren 720S-doors open.jpg', 0.62, 0.6),
    7: ('File:McLaren F1 door mechanism.jpg', 0.47, 0.3),
    8: ('File:Ford GT40 at London Motor Museum (Ank Kumar) 02.jpg', 0.48, 0.35),
    9: ('File:1981 DeLorean DMC-12 - 15966569236.jpg', 0.4, 0.3),
    10: ('File:Mercedes-Benz SLS AMG (C 197) – Frontansicht geöffnet, 10. August 2011, Düsseldorf.jpg', 0.45, 0.3),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video29", "title": "Why Do Supercar Doors Open Upward?",
           "length_scale": 1.6, "scenes": S}, open("videos/video29/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
