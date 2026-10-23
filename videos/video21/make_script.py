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
sc("""The most expensive part of a Formula One car is one you will almost never see. It is not the engine and it is not the steering wheel. It is the floor, a flat sheet of carbon fibre under the car, so important that teams spend millions of dollars designing it and guard its shape like a state secret. Today, ten parts that make an F1 car stick to the track, and why each one exists, starting with the floor.""",
   "Formula One car", "THE SECRET UNDER THE CAR", cuts=8, chapter="Intro")
sc("""A Formula One car is a fighter jet turned upside down. A wing on an airplane pushes it up. Every wing on an F1 car is designed to push it down, into the track, so the tyres can grip harder in the corners. That push is called downforce, and at high speed a modern F1 car makes more downforce than its own weight. In theory, it could drive upside down on the ceiling of a tunnel.""",
   "Formula One car corner", "AN UPSIDE DOWN JET")
sc("""As always, every fact here comes from a named source, the rules of the FIA, Formula One itself and motorsport references, all listed in the description. Let's lift the car and look underneath.""",
   "Formula One car garage", "WHY DOES THIS EXIST?")

# ---------- 1. FLOOR ----------
part(1, "The floor", "WHY IS THIS FLOOR WORTH MILLIONS?", "Why Is the Floor of an F1 Car Worth Millions?",
     """Why is the floor of an F1 car worth millions? Because the floor is a giant wing. Under the car, two long tunnels run from the front of the floor to the back. As air rushes through them, the tunnels narrow and then open up again, and the air speeds up and its pressure drops. Low pressure under the car, normal pressure on top. The whole car gets sucked down onto the track. That is called ground effect.""",
     "Formula One car underside floor")
sc("""Ground effect came back to Formula One with the new rules of twenty twenty-two. Engineers estimate that the floor makes a large share of the car's total downforce, by many estimates more than any single wing. And it does it more cleanly. Wings on top leave turbulent air behind the car, which makes it hard for the next driver to follow. Downforce from the floor leaves less of that dirty air, so cars can race closer.""",
   "Formula One 2022 car", "THE BIGGEST WING")
sc("""That is why teams cover the floor with sheets when the car is lifted in public, and why photographers are chased away from cars hanging on cranes after a crash. A few millimetres of change in the floor can be worth tenths of a second per lap. Teams build new versions through the season, each one designed in computers and tested in the wind tunnel. The sheet of carbon fibre is cheap. The knowledge inside its shape is not.""",
   "Formula One car crane", "GUARDED LIKE A SECRET")

# ---------- 2. PLANK ----------
part(2, "The plank", "WHY IS THERE WOOD UNDER AN F1 CAR?", "Why Is There a Wooden Plank Under Every F1 Car?",
     """Why is there a wooden plank under a Formula One car? Under the floor of every F1 car runs a long strip called the plank, or skid block, made of a wood based material. It was introduced in nineteen ninety-four, the year of the deaths of Ayrton Senna and Roland Ratzenberger at Imola, as one of the measures to slow the cars down. The plank forces the car to run higher off the ground.""",
     "Formula One plank skid block")
sc("""The trick is that the plank works like a measuring stick. It starts ten millimetres thick, and after the race it must still be at least nine millimetres thick at set points. If a team runs the car too low to gain more ground effect, the plank scrapes on the track and wears away. Too much wear, and the car is disqualified. In nineteen ninety-four, Michael Schumacher lost a win at the Belgian Grand Prix this way.""",
   "Michael Schumacher Benetton 1994", "A MEASURING STICK")
sc("""It still happens. At the United States Grand Prix of twenty twenty-three, Lewis Hamilton and Charles Leclerc were both disqualified after the race because their planks had worn too much. Running lower is faster, but the plank is always there, grinding away as the proof. A piece of wood under a machine worth millions decides who keeps their result.""",
   "Lewis Hamilton Mercedes 2023", "WOOD DECIDES THE RESULT")

# ---------- 3. DIFFUSER ----------
part(3, "The diffuser", "WHY DOES THE BACK OPEN UP LIKE THIS?", "Why Does the Back of an F1 Car Open Up Like This?",
     """Why does the back of an F1 car open up into these curved channels? This is the diffuser, the exit of the tunnels under the floor. It gets taller and wider towards the back, so the fast air under the car can slow down gradually and rejoin the air behind the car. That gentle expansion keeps the air under the car moving fast, and keeps the pressure under the floor low.""",
     "Formula One diffuser")
sc("""The diffuser is so powerful that it once decided a world championship. In two thousand nine, Brawn GP, a team that had been rescued from closure only weeks before the season, arrived with a double diffuser, a clever second deck that used a gap in the rules. Other teams protested. The design was declared legal, and Jenson Button won six of the first seven races on his way to the title.""",
   "Brawn GP BGP 001", "A LOOPHOLE WON THE TITLE")
sc("""Rival teams copied the idea within months, and the rules banned double diffusers for twenty eleven. Since then, the diffuser has been one of the most tightly regulated areas on the car. Every surface is in a box defined by the rules, and engineers fight over millimetres inside that box. It is where the floor's work is finished.""",
   "Formula One car rear", "MILLIMETRES IN A BOX")

# ---------- 4. FRONT WING ----------
part(4, "The front wing", "WHY IS THE FRONT WING SO COMPLEX?", "Why Is an F1 Front Wing So Complicated?",
     """Why is the front wing of an F1 car made of so many layers? Because it is the first thing that touches the air. The front wing makes downforce for the front wheels, but its bigger job is to steer the air for the rest of the car. It decides how much air goes under the floor, how the air flows around the front tyres, and how it reaches the sidepods.""",
     "Formula One front wing")
sc("""The tyres are the problem. A spinning, open wheel throws turbulent air everywhere, and that turbulence can ruin the floor behind it. So the front wing is shaped to push that messy air away from the car. It is also adjustable. In a pit stop, mechanics can turn a small screw on the flaps to change the angle, and change the balance of the car for the next stint.""",
   "Formula One pit stop front wing adjustment", "IT STEERS THE AIR")
sc("""Front wings are also fragile, and that is on purpose. They break on contact, absorbing energy and staying close to the car instead of turning into a heavy flying object. Teams bring many spare wings to each race, because a broken front wing is one of the most common damages in Formula One. The rules made the wing simpler in twenty twenty-two, but it is still one of the most expensive single parts on the car.""",
   "Formula One broken front wing", "MADE TO BREAK")

# ---------- 5. DRS ----------
part(5, "The rear wing flap", "WHY DOES THIS WING OPEN?", "Why Does the F1 Rear Wing Open on the Straights?",
     """Why does the rear wing of an F1 car open on the straights? Downforce has a price, called drag. The wings that push the car into the corners also hold it back on the straights. From twenty eleven, Formula One used DRS, the drag reduction system. A flap on the rear wing opened on certain straights when a driver was within one second of the car in front, cutting drag and adding speed to make overtaking easier.""",
     "Formula One DRS open rear wing")
sc("""When the flap opens, the wing stalls. Less downforce, less drag, and the car gains around ten kilometres per hour by the end of the straight. The moment the driver brakes, the flap closes again and the downforce comes back for the corner. In twenty twenty-six, new rules went further. Both the front and the rear wings now move, opening on straights for every car to save energy, and closing for the corners.""",
   "Formula One rear wing", "WINGS THAT MOVE")
sc("""Moving wings were banned in Formula One for decades. In the late nineteen sixties, wings on tall stilts broke off at speed and caused terrible crashes, and the rule makers banned moving aerodynamic devices. DRS returned the idea under strict control, with a hydraulic actuator that only works when the system allows it. The open wing is the tool. The rule book decides when you may use it.""",
   "1969 Formula One car high wing", "BANNED, THEN BACK")

# ---------- 6. BARGEBOARDS ----------
part(6, "The bargeboards", "WHY WERE THESE BLADES BANNED?", "Why Did F1 Ban These Strange Blades?",
     """Why did old F1 cars have this forest of small blades on the side? These were the bargeboards, a cluster of curved carbon fins between the front wheels and the sidepods. Their job was to catch the turbulent air coming off the front tyres and send it away from the floor, while creating small spinning vortices that sealed the edges of the floor, like an invisible curtain.""",
     "Formula One bargeboard")
sc("""By the late twenty tens, bargeboards had become some of the most complex parts ever put on a racing car, with dozens of slots and edges. They worked brilliantly for the car carrying them. But they threw the air into a storm behind the car. A driver following closely lost a big part of his downforce and could not get close enough to pass.""",
   "Formula One 2019 car sidepod bargeboard", "TOO GOOD FOR RACING")
sc("""So the rules of twenty twenty-two banned them. The new cars were designed around the floor, with simpler bodywork on top, so that the car behind could follow more closely. It is a lesson that keeps returning in Formula One. A part can be too good. When it makes racing worse, the rule makers simply delete it.""",
   "Formula One 2022 cars racing", "DELETED BY THE RULES")

# ---------- 7. SIDEPODS ----------
part(7, "The sidepods", "WHY ARE THE SIDEPODS SHAPED LIKE THIS?", "Why Do F1 Sidepods All Look Different?",
     """Why are the sides of an F1 car shaped in such strange ways? These are the sidepods, and inside them are the radiators that cool the engine, the battery and the electronics. A Formula One power unit turns a lot of fuel into heat, and that heat must leave the car. The sidepods take in air at the front, pass it through the radiators, and release it at the back.""",
     "Formula One sidepod")
sc("""But the outside shape is pure aerodynamics. When the new rules arrived in twenty twenty-two, each team found its own answer. Mercedes tried almost no sidepods at all, a design fans called zero pod. Ferrari had a wide, scooped shape. Red Bull carved a deep undercut below the sidepod, to send clean air to the back of the floor. Red Bull won the most races, and soon most teams copied the undercut.""",
   "Red Bull RB19 sidepod", "SAME RULES, DIFFERENT CARS")
sc("""Every sidepod is a compromise. Bigger inlets cool better but add drag. Smaller ones are faster but the engine can overheat, especially in hot races like Singapore. That is why you sometimes see cars with extra cooling gills opened up for a hot weekend. The shape you see changes from race to race, depending on the weather.""",
   "Formula One car cooling louvres", "COOLING VS. SPEED")

# ---------- 8. LOTUS 79 ----------
part(8, "The sliding skirts", "WHY WAS THIS CAR SO FAST?", "Why Was the Lotus 79 Almost Unbeatable?",
     """Why was this black and gold car almost unbeatable? This is the Lotus seventy-nine, and it brought ground effect to Formula One. Colin Chapman's team shaped the sidepods like upside down wings, and closed the gap between the car and the track with sliding skirts that rubbed along the ground. The air under the car was sealed in, and the car was sucked to the track.""",
     "Lotus 79")
sc("""In nineteen seventy-eight, Mario Andretti won the world championship with it, and his team mate Ronnie Peterson finished second. Rival teams rushed to copy the idea. But ground effect had a dark side. If a skirt was damaged or the car went over a kerb, the seal broke and the downforce vanished in an instant, often in a fast corner.""",
   "Mario Andretti Lotus 1978", "SEALED TO THE TRACK")
sc("""Cornering speeds rose so fast that the drivers' bodies took huge forces, and the accidents became more violent. Sliding skirts were banned from nineteen eighty-one, and from nineteen eighty-three, Formula One required flat bottoms. Ground effect disappeared for almost forty years, until engineers learned how to bring it back safely in twenty twenty-two, with shaped tunnels instead of skirts.""",
   "Formula One 1982 car", "BANNED FOR 40 YEARS")

# ---------- 9. FAN CAR ----------
part(9, "The fan", "WHY DOES THIS CAR HAVE A FAN?", "Why Did This F1 Car Have a Giant Fan?",
     """Why does this Formula One car have a giant fan on its back? This is the Brabham BT forty-six B, designed by Gordon Murray in nineteen seventy-eight. Officially, the fan was there to cool the engine. In reality, it sucked the air out from under the car, creating a vacuum that pulled the car down, even at low speed in slow corners, where wings do almost nothing.""",
     "Brabham BT46B fan car")
sc("""It raced once, at the Swedish Grand Prix of nineteen seventy-eight. Niki Lauda won by more than half a minute. Rival drivers complained that the fan threw dirt and stones at the cars behind. The car had not broken any rule, because the fan's main job was declared to be cooling. But under pressure from the other teams, Brabham withdrew it after that one race.""",
   "Niki Lauda 1978", "ONE RACE, ONE WIN")
sc("""The fan car is still remembered as one of the greatest tricks in racing history. It won every race it ever entered, because it entered only one. And the idea never died. Some modern road and race cars use fans to pull air from under the car. In Formula One, the rules now say that a part's main purpose decides whether it is legal.""",
   "Gordon Murray", "100% WIN RATE")

# ---------- 10. WIND TUNNEL ----------
part(10, "The wind tunnel model", "WHY IS THIS F1 CAR SO SMALL?", "Why Do F1 Teams Test Small Model Cars?",
     """Why do F1 teams test a smaller copy of their car? Because full size wind tunnel testing is not allowed. The rules limit teams to models of at most sixty percent of the real car, tested in wind tunnels at limited speed. Every floor, every wing, every sidepod you saw today was first shaped in computer simulations, then built as a precision model and tested in the tunnel.""",
     "Formula One wind tunnel model")
sc("""And the tunnel time is rationed. Since twenty twenty-one, Formula One uses a sliding scale. The team that finished last in the championship gets the most wind tunnel time and computer simulation, and the champion gets the least. It is a handicap system, designed to let the slower teams catch up. Every hour in the tunnel is precious, so teams plan every run.""",
   "wind tunnel", "THE CHAMPION GETS LESS")
sc("""On top of that, there is a budget cap. Since twenty twenty-one, teams have a limit on how much they can spend each year on building and developing the car. So a new floor is not just a piece of carbon. It is wind tunnel hours, computer time and money taken from a strict budget. That is the real reason the floor is worth millions.""",
   "Formula One factory", "TIME, MONEY, CARBON")

# ---------- VERDICT ----------
sc("""So here are the ten. A floor that is a hidden wing. A wooden plank that measures the cheating. A diffuser that finishes the floor's work. A front wing that steers the air. A rear wing that opens. Blades that were too good, sidepods that cool and shape, sliding skirts that were banned, a fan that won its only race, and a small model car that shapes them all.""",
   "Formula One race start", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""In Formula One, the most important part of the car is the air around it. Every surface is an argument with that air, and every rule is an argument with the engineers. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Formula One car night race", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Honda RC-F1 2.0X bottom Honda Collection Hall.jpg", 0.35, 0.5),
    2: ("File:Benetton B194 bottom2 2019 Michael Schumacher Private Collection.jpg", 0.48, 0.55),
    3: ("File:Toyota TF110 diffuser 2019 Prototyp Museum.jpg", 0.42, 0.55),
    4: ("File:McLaren MCL36A Front Wing at Formula 1 Exhibition, London.jpg", 0.5, 0.55),
    5: ("File:Mercedes AMG F1 W09 EQ Power+ DRS Rear Wing at Formula 1 Exhibition, London.jpg", 0.42, 0.22),
    6: ("File:McLaren MP4-22 bargeboard 2017 Museo Fernando Alonso.jpg", 0.35, 0.55),
    7: ("File:Max Verstappen Red Bull RB19 Petersen Automotive Museum.jpg", 0.8, 0.4),
    8: ("File:Lotus 79 JPS (51861707041).jpg", 0.4, 0.5),
    9: ("File:1978 Alfa Romeo Brabham BT46B Fan Car - Flickr - edvvc.jpg", 0.16, 0.63),
    10: ("File:2017 Manor MRT06 60% model.jpg", 0.6, 0.4),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video21", "title": "Why Is the Floor of an F1 Car Worth Millions?",
           "length_scale": 1.6, "scenes": S}, open("videos/video21/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
