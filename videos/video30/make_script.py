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
sc("""Watch the wheels of a Rolls-Royce as it drives away. The wheels spin, but the R R logo in the middle stays perfectly upright, as if it were painted on the air. It is not magic, and it is not a camera trick. Today, ten parts of a Rolls-Royce that look like luxury tricks, and the engineering reason behind each one.""",
   "Rolls-Royce wheel", "WHY DOESN'T IT SPIN?", cuts=8, chapter="Intro")
sc("""Rolls-Royce has one simple idea behind almost everything it builds. The car should feel calm, quiet and effortless, for the person in the back seat as much as for the driver. Many of its strange parts exist to protect that feeling, by hiding effort, noise and small annoyances that other cars simply accept.""",
   "Rolls-Royce Phantom", "CALM AND EFFORTLESS")
sc("""As always, every fact here comes from a named source, Rolls-Royce and automotive references, all listed in the description. Let's start with the wheels.""",
   "Rolls-Royce Phantom side", "WHY DOES THIS EXIST?")

# ---------- 1. WHEEL ----------
part(1, "The floating wheel logo", "WHY DOES THIS LOGO NEVER SPIN?", "Why Do Rolls-Royce Wheel Logos Never Spin?",
     """Why does the logo in the middle of a Rolls-Royce wheel never spin? Because it is not attached to the wheel. The badge sits on its own small bearing, so it can turn freely. Under the badge, a small weight is fixed at the bottom. As the wheel turns, gravity keeps pulling that weight down, so the badge always stays upright.""",
     "Rolls-Royce wheel centre")
sc("""It works like a pendulum. The wheel rotates around the badge, but the weight keeps the badge level, the same way a hanging picture stays straight while you turn the frame around it. Rolls-Royce calls them self righting wheel centres. They became a feature of its cars in the two thousands.""",
   "Rolls-Royce Ghost wheel", "A TINY PENDULUM")
sc("""Why bother? Because photos of parked cars always show a perfectly straight logo, and when the car moves, the logo stays readable. It is a small detail, but it says the same thing as the rest of the car. Even the wheels should look calm.""",
   "Rolls-Royce Cullinan wheel", "EVEN THE WHEELS LOOK CALM")

# ---------- 2. UMBRELLA ----------
part(2, "The umbrella in the door", "WHY IS THERE AN UMBRELLA IN THE DOOR?", "Why Do Rolls-Royce Doors Hide an Umbrella?",
     """Why is there an umbrella hidden inside the door of a Rolls-Royce? Because the moment of getting out of the car is part of the experience. If it rains, the passenger should not step out and get wet while someone looks for an umbrella. So it sits in a tube inside the door, ready to slide out.""",
     "Rolls-Royce umbrella door")
sc("""The engineering problem is the water. A wet umbrella put back into a door would drip into the car and could damage it over time. So the umbrella sits in its own compartment, designed to let it dry, away from the rest of the door. The fabric is also treated to shed water quickly.""",
   "Rolls-Royce door", "WHAT ABOUT THE WATER?")
sc("""It is a tiny part, but it became one of the most famous details of the brand. It shows how Rolls-Royce thinks. Not only about how the car drives, but about the full minute before and after the drive, including the walk to the front door.""",
   "Rolls-Royce Phantom door open", "THE WHOLE JOURNEY")

# ---------- 3. SPIRIT OF ECSTASY ----------
part(3, "The hiding mascot", "WHY DOES THIS STATUE DISAPPEAR?", "Why Does the Rolls-Royce Statue Disappear Into the Car?",
     """Why does the little silver statue on a Rolls-Royce bonnet disappear into the car? The statue is the Spirit of Ecstasy, and it is a target for thieves. On modern Rolls-Royce cars, it sits on a mechanism that can pull it down into the grille. When the car is locked, or if someone tries to pull it off, it drops out of sight.""",
     "Spirit of Ecstasy")
sc("""The mechanism is also about safety. A hard metal statue on the front of a car could hurt a pedestrian in an accident. If the car hits something, the mascot is designed to retract quickly, so it does not stick out. A beautiful ornament becomes a safer part of the car.""",
   "Spirit of Ecstasy Rolls-Royce", "SAFETY TOO")
sc("""The statue itself goes back to nineteen eleven, sculpted by Charles Sykes. More than a century later, it is still on every car, now made lower and slightly leaner to help the airflow. On the electric Spectre, Rolls-Royce reshaped it to cut through the air better.""",
   "Rolls-Royce Spectre", "SINCE 1911")

# ---------- 4. COACH DOORS ----------
part(4, "The coach doors", "WHY DOES THIS DOOR OPEN BACKWARDS?", "Why Do Rolls-Royce Rear Doors Open Backwards?",
     """Why do the rear doors of a Rolls-Royce open backwards? They are hinged at the rear, like the doors of an old horse drawn coach, which is why Rolls-Royce calls them coach doors. With the door open, there is no door frame in front of the passenger, so they can step out facing forward, upright and calm.""",
     "Rolls-Royce coach doors")
sc("""With a normal rear door, you twist your body and squeeze past the door to get out. With a coach door, you simply stand up and walk forward. And when the front and rear doors are both open, the whole side of the cabin opens like a gate. It makes getting in and out look elegant, which matters for a car often filmed at events.""",
   "Rolls-Royce Phantom doors open", "STAND UP AND WALK")
sc("""Rear hinged doors can be dangerous if they swing open while moving, which is why they had a bad reputation in the past. Modern Rolls-Royce doors are locked while driving, and a button inside closes them with a motor. The passenger never has to stretch out and pull a heavy door shut.""",
   "Rolls-Royce Ghost doors", "A BUTTON CLOSES IT")

# ---------- 5. STARLIGHT ----------
part(5, "The starlight headliner", "WHY ARE THERE STARS ON THE CEILING?", "Why Do Rolls-Royce Cars Have Stars on the Ceiling?",
     """Why is there a sky full of stars on the ceiling of a Rolls-Royce? It is called the Starlight headliner. Hundreds or even more than a thousand tiny lights are woven into the leather of the roof lining. They are the ends of fibre optic cables, thin strands of glass that carry light from a hidden source.""",
     "Rolls-Royce starlight headliner")
sc("""Each point of light is placed by hand, and customers can even ask for a real constellation, like the sky on the night they were born. Because the light comes through fibres, there is no heat and no bulb in the roof. The whole sky is lit from a source far away from the passengers.""",
   "Rolls-Royce interior", "PLACED BY HAND")
sc("""The reason is the same calm feeling. At night, a dark cabin feels small and closed. A soft starry sky makes it feel open and relaxed, without the glare of a normal reading light. It became one of the most requested options in the history of the brand.""",
   "Rolls-Royce Phantom interior", "A CALMER CABIN AT NIGHT")

# ---------- 6. FLAGBEARER ----------
part(6, "The camera that reads the road", "WHY DOES THIS CAR LOOK AT THE ROAD?", "Why Does a Rolls-Royce Watch the Road Ahead?",
     """Why does a Rolls-Royce have cameras that watch the road ahead? To prepare the suspension. Rolls-Royce calls the system Flagbearer. Cameras in the windscreen look at the road in front of the car, and if they see a bump, the suspension adjusts before the wheels reach it.""",
     "Rolls-Royce Phantom windscreen")
sc("""The name comes from history. In the early days of the car in Britain, a person had to walk in front of a motor vehicle carrying a red flag, to warn others. Rolls-Royce named its camera after that person, because it also walks ahead and warns the car about what is coming.""",
   "Red Flag Act", "THE MAN WITH THE RED FLAG")
sc("""The goal is what Rolls-Royce calls the magic carpet ride. Air springs and electronically controlled dampers soften each bump, and the camera gives them time to get ready. The car should feel like it floats over the road, not like it is fighting it.""",
   "Rolls-Royce air suspension", "THE MAGIC CARPET RIDE")

# ---------- 7. POWER RESERVE ----------
part(7, "The power reserve gauge", "WHY IS THERE NO REV COUNTER?", "Why Doesn't a Rolls-Royce Have a Rev Counter?",
     """Why does a Rolls-Royce have no rev counter? A normal sports car shows how fast the engine is spinning, so the driver can push it to the limit. A Rolls-Royce shows a gauge called the power reserve instead. It tells you how much of the engine's power you are not using.""",
     "Rolls-Royce power reserve gauge")
sc("""The gauge usually shows a large reserve, often close to one hundred percent. That is the point. The six point seven five litre V twelve engine is designed to make huge pulling force at low engine speed, so the car moves smoothly without ever working hard. The gauge reminds the driver how much is still available.""",
   "Rolls-Royce V12 engine", "MOST OF THE POWER IS WAITING")
sc("""It is a dashboard that matches the brand's idea. A sports car tells you how hard it is working. A Rolls-Royce tells you how easy everything is. The name sounds like a fine mechanical watch, where a power reserve shows how long the watch can keep running. The idea is the same. Look at it, and you know you will never run short.""",
   "Rolls-Royce Phantom dashboard", "HOW EASY IT IS")

# ---------- 8. GRILLE ----------
part(8, "The Pantheon grille", "WHY IS THIS GRILLE SHAPED LIKE A TEMPLE?", "Why Is the Rolls-Royce Grille Shaped Like a Temple?",
     """Why does the Rolls-Royce grille look like the front of a Greek temple? It is called the Pantheon grille, after the ancient building in Rome. Its vertical bars and straight, proud shape were inspired by classical architecture, and it has been the face of the brand for over a century.""",
     "Rolls-Royce Pantheon grille")
sc("""It started as a working part. Early cars needed a big radiator at the front, and the grille protected it while letting air through. The vertical bars were simple to make and let air flow straight in. Rolls-Royce shaped that functional part to look dignified, and it never changed the idea.""",
   "Rolls-Royce Silver Ghost", "A RADIATOR AT THE FRONT")
sc("""On the electric Spectre, there is no engine radiator to cool, but the grille stays. On some newer models, it is even lit from behind. A part born from cooling became a symbol. That is why every Rolls-Royce is recognisable from a hundred metres away, even at night.""",
   "Rolls-Royce Spectre front", "FROM COOLING TO SYMBOL")

# ---------- 9. COACHLINE ----------
part(9, "The painted coachline", "WHY IS THIS LINE PAINTED BY HAND?", "Why Is the Rolls-Royce Coachline Painted by Hand?",
     """Why is the thin line along the side of a Rolls-Royce painted by hand? It is called the coachline, and for many years it has been painted by one craftsman at the factory in Goodwood, with a brush made of squirrel hair. A machine could do it, but Rolls-Royce wants the line to show the hand of a person.""",
     "Rolls-Royce coachline")
sc("""The line runs the length of the car and must be perfectly even. The painter works freehand, with a steady hand and years of practice, and the job takes hours. Any mistake means starting again. Customers can ask for their initials or a small design painted at the end of the line.""",
   "Rolls-Royce Goodwood factory", "FREEHAND")
sc("""The coachline also goes back to horse drawn carriages, which had painted lines to show off the craftsmanship of the builder. On a Rolls-Royce it is a signature, a reminder that the car is built for one person, not mass produced on a fast line.""",
   "Rolls-Royce Ghost side", "BUILT FOR ONE PERSON")

# ---------- 10. SILENCE ----------
part(10, "The silent cabin", "WHY IS THIS CAR SO QUIET?", "Why Is a Rolls-Royce So Quiet Inside?",
     """Why is a Rolls-Royce so quiet inside? Because silence is engineered, piece by piece. Rolls-Royce uses more than a hundred kilograms of sound insulation in its cars, in the floor, the doors, the roof and around the engine. The glass is made with two layers, with a sound blocking layer in between.""",
     "Rolls-Royce interior quiet")
sc("""Even the tyres are special. They have a layer of foam inside, which absorbs the hollow sound that a normal tyre makes as it rolls. The aluminium frame is designed to avoid vibrations that could hum in the cabin. Each source of noise has its own solution.""",
   "Rolls-Royce tyre", "FOAM INSIDE THE TYRES")
sc("""The engineers even found that a cabin can be too quiet. In near total silence, people start to hear small sounds and feel uneasy. So Rolls-Royce tuned the sound of the cabin to keep a soft, low background, like a calm room. Silence, it turns out, also has to be designed.""",
   "Rolls-Royce Phantom rear seat", "TOO QUIET?")

# ---------- VERDICT ----------
sc("""So here are the ten. A floating logo that stays upright. An umbrella in the door. A statue that hides. Doors that open backwards. Stars on the ceiling. A camera that reads the road. A gauge that shows the power you are not using. A temple shaped grille. A line painted by hand. And a cabin where even the silence is engineered.""",
   "Rolls-Royce", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Luxury, at this level, is really engineering that hides effort. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which detail of a Rolls-Royce surprised you most.""",
   "Rolls-Royce night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:2012 alloy wheel of Rolls-Royce Phantom in BMW-Museum in Munich, Bayern.JPG', 0.4, 0.6),
    2: ('File:2011-03-04 Autosalon Genf 1295.JPG', 0.72, 0.45),
    3: ('File:Spirit of Ecstasy HMC.jpg', 0.45, 0.35),
    4: ('File:Geneva MotorShow 2013 - Rolls-Royce Phantom Coupé opened door.jpg', 0.3, 0.45),
    5: ('File:Rolls-Royce Phantom VIII Series II Scivaro Grey Peony Pink Iceland Moss (12).jpg', 0.35, 0.25),
    6: ('File:Rolls-Royce Phantom, Geneva International Motor Show 2018, Le Grand-Saconnex (1X7A1220).jpg', 0.4, 0.25),
    7: ('File:Rolls Royce Phantom Drophead Coupe (Ank Kumar) 01.jpg', 0.2, 0.33),
    8: ('File:Rolls-Royce Phantom front view at BMW Museum, Munich.jpg', 0.5, 0.5),
    9: ('File:Rolls-Royce Phantom VIII EWB White (12).jpg', 0.5, 0.32),
    10: ('File:Rolls Royce Ghost 2015 (23149918661).jpg', 0.45, 0.5),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video30", "title": "Why Do Rolls-Royce Wheel Logos Never Spin?",
           "length_scale": 1.6, "scenes": S}, open("videos/video30/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
