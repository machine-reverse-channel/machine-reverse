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
sc("""When a Formula One car goes over a bump at full speed, it throws a shower of bright orange sparks from underneath. It looks like a firework, and fans love it. But the sparks are not there for the show, or at least, that is not why they were first invented. They come from a part of the car that most people never see, and it is one of many hidden parts of a machine that can reach nearly three hundred seventy-five kilometers an hour. Today, ten parts of a Formula One car, and why each one exists.""",
   "Formula One car sparks", "WHY DO F1 CARS THROW SPARKS?", cuts=8, chapter="Intro")
sc("""A Formula One car must weigh at least seven hundred ninety-eight kilograms with the driver, and it can pull up to six g in a corner. Every part is designed for speed, and also for rules, because the sport is run by a very long rulebook. Let's go through the parts one by one.""",
   "Formula One car racing", "A MACHINE MADE OF RULES")
sc("""As always, every fact here comes from a named source, reference works and motorsport reports, all listed in the description. Let's start with the sparks.""",
   "Formula One sparks night", "WHY DOES THIS EXIST?")

# ---------- 1. SKID BLOCKS ----------
part(1, "The titanium skid blocks", "WHY DOES THIS CAR THROW SPARKS?", "Why Do F1 Cars Throw Sparks?",
     """Why do Formula One cars throw sparks? Because they scrape the track. Under the car there are skid blocks, and since a rule change in twenty fifteen, they must be made of a titanium alloy. When the car gets low and the floor touches the asphalt, the titanium rubs against the road and throws white-hot shards of metal, and those are the sparks you see.""",
     "Formula One car skid block sparks")
sc("""The blocks protect the plank, a long flat strip under the car. And the car gets low on purpose, because the lower the floor, the more the car is sucked down onto the road. The sparks are a sign that the car is working as planned, as close to the ground as it can go.""",
   "Formula One underside sparks", "A SIGN IT'S WORKING")
sc("""The reason for titanium was not the show. The FIA said the change was mainly for safety, since the old blocks were made of a heavy metal, and pieces that fell off could be dangerous. The sparks were a bonus, which the sport was happy to keep.""",
   "Formula One FIA titanium skid", "SAFETY FIRST, SPARKS SECOND")

# ---------- 2. PLANK ----------
part(2, "The plank", "WHY IS THERE A PLANK UNDER THE CAR?", "Why Is There a Plank Under a Formula One Car?",
     """Why is there a plank under a Formula One car? To stop the teams from running too low. After the San Marino Grand Prix of nineteen ninety-four, a ten millimeter plank was added under the body to enforce a minimum ride height. If it wears down by more than one millimeter during a race weekend, the car is disqualified.""",
     "Formula One plank skid underside")
sc("""Without a limit, teams would lower the cars until they scrape the road, to get as much downforce as possible, which makes the cars dangerous. The plank is a referee under the car. At the end of a race, the officials measure it, and if it is too thin, the car was too low.""",
   "Formula One plank measurement", "A REFEREE UNDER THE CAR")
sc("""Skid blocks made of titanium sit inside the plank, at the points where it touches. They take the wear, and they are the part that lights up the night. So the sparks and the plank are the same story. A rule to keep the cars safe, and a result that looks like fire.""",
   "Formula One car floor wear", "THE SAME STORY")

# ---------- 3. GROUND EFFECT ----------
part(3, "The floor", "WHY IS THE FLOOR SHAPED LIKE THIS?", "Why Does an F1 Car Stick to the Road?",
     """Why does a Formula One car seem to stick to the road? The answer is mostly under the car. The floor is shaped like a tunnel, and the air under it seals the gap with the ground and creates a low pressure area that pulls the car down. It is called ground effect, and it has shaped race cars for decades. At about one hundred ninety kilometers an hour, the downforce is twice the car's weight.""",
     "Formula One car floor ground effect")
sc("""Twice its own weight, pushing down. That means that, in theory, at high speed, the car could drive upside down on the roof of a tunnel. The tyres are not the only thing that grip. The air does a big share of the work.""",
   "Formula One car downforce", "UPSIDE DOWN IN THEORY")
sc("""And the lower the floor, the stronger the effect. That is why the sparks happen, because the car wants to be pulled to the road, and the road can only be so close. The rule, and the physics, have the car riding the edge.""",
   "Formula One car low ride height", "THE LOWER, THE STRONGER")

# ---------- 4. REAR WING AND DRS ----------
part(4, "The rear wing flap", "WHY DOES THE REAR WING OPEN?", "Why Does the Rear Wing of an F1 Car Open?",
     """Why does the rear wing of the car open? It is the Drag Reduction System, introduced in twenty eleven. A flap in the rear wing opens, which lowers the drag and gives the car more speed. The driver triggers it, and it can only be used in specific places, so that a driver who is close behind another car can try to pass.""",
     "Formula One DRS rear wing open")
sc("""The rear wing normally pushes the car down, which is good in corners, but also slows it on straights, like a hand held out of a car window. When the flap opens, the wing lets more air pass, and the car goes faster in a straight line.""",
   "Formula One DRS straight", "LESS DRAG ON THE STRAIGHT")
sc("""It is a system designed for overtaking, not for racing alone. The rules only allow it in certain zones, so it helps the car behind, not the one in front. A part of the car that exists to make races more exciting.""",
   "Formula One overtaking DRS", "A PART MADE FOR OVERTAKING")

# ---------- 5. FRONT WING ----------
part(5, "The front wing", "WHY IS THE FRONT WING SO COMPLICATED?", "Why Is the Front Wing of an F1 Car So Complicated?",
     """Why is the front wing so complicated? It is the first part of the car to meet the air, and the way it bends the air decides how everything behind it works. The rules allow a width of one thousand eight hundred millimeters, with up to four elements, and a maximum of five millimeters of bending. Teams spend huge sums on every curve of it.""",
     "Formula One front wing")
sc("""The front wing creates downforce for the front tyres, and it also sends air around the wheels and toward the floor. If it is wrong by a few millimeters, the whole car can feel different. It is a part where tiny changes matter more than almost anywhere else.""",
   "Formula One front wing airflow", "A FEW MILLIMETERS MATTER")
sc("""The limit on how much it can bend is also a rule. A wing that flexes at speed changes how the air flows, so the rule says it can bend no more than five millimeters. The sport writes a new line in the rulebook every time someone finds a clever trick.""",
   "Formula One wing flex test", "A RULE FOR EVERY TRICK")

# ---------- 6. BRAKES ----------
part(6, "The glowing brake discs", "WHY DO THE BRAKES GLOW?", "Why Do F1 Brake Discs Glow Red?",
     """Why do the brakes glow? Because braking turns the car's speed into heat. The brake discs are made of carbon composite and can take temperatures of up to one thousand degrees Celsius. Each caliper has six pistons clamping the pads, and an average car can slow from one hundred kilometers an hour to a stop in less than fifteen meters.""",
     "Formula One brake disc glowing")
sc("""Stopping a car from high speed means deceleration of five to six g, which pushes the driver forward in the seat. The discs glow red and orange, and in the dark you can see them shine through the wheel. It is not a flaw. It is physics, made visible.""",
   "Formula One braking g-force", "5 TO 6 G OF BRAKING")
sc("""Carbon is used because it is light and keeps working at very high temperatures, where steel would struggle. The same material that lights up the corner in a night race is what keeps the car on the track.""",
   "Formula One carbon brake", "CARBON LOVES HEAT")

# ---------- 7. STEERING WHEEL ----------
part(7, "The steering wheel", "WHY DOES THIS STEERING WHEEL HAVE SO MANY BUTTONS?", "Why Does an F1 Steering Wheel Have So Many Buttons?",
     """Why does the steering wheel of an F1 car look like a game controller? Because the driver controls the car from it. It weighs about one point three kilograms, can cost around fifty thousand dollars, and is made of carbon fiber with titanium, silicon, fiberglass and copper parts. The buttons and dials change settings of the engine, the brakes and the car while driving.""",
     "Formula One steering wheel buttons")
sc("""There is no time to reach for a switch on the dashboard at those speeds, so everything is within reach of the thumbs. A driver may need to change brake balance, adjust the engine, or talk to the team, all while pulling several g in a corner.""",
   "Formula One driver steering wheel", "EVERYTHING UNDER THE THUMBS")
sc("""So the wheel is a mini control room that is gripped with both hands. It is one of the most expensive pieces of the car, per kilogram, and it is the one thing that the driver touches the whole race.""",
   "Formula One cockpit steering wheel", "THE DRIVER'S CONTROL ROOM")

# ---------- 8. TYRES ----------
part(8, "The tyres", "WHY DO F1 CARS HAVE SMOOTH TYRES?", "Why Do F1 Cars Use Smooth Tyres?",
     """Why do Formula One cars use tyres with no tread? Those are slick tyres, used in normal dry conditions, and the smooth surface puts the most rubber on the road. Since two thousand twenty-two, the wheels have been eighteen inches, up from thirteen, and the overall tyre diameter grew from six hundred seventy to seven hundred twenty millimeters.""",
     "Formula One slick tyres")
sc("""A tyre with grooves has less rubber touching the ground, and that means less grip. On a dry track, the grooves would only reduce grip. But on a wet track, a slick tyre can not push the water away, so the cars switch to tyres with grooves.""",
   "Formula One wet tyres", "NO TREAD, MORE GRIP")
sc("""The tyre is the only part of the car that touches the road, so it is where all of the power, the braking and the cornering force has to go. Everything the car can do is limited by four patches of rubber.""",
   "Formula One tyre contact patch", "FOUR PATCHES OF RUBBER")

# ---------- 9. FUEL ----------
part(9, "The fuel", "WHY IS FUEL LIMITED IN A RACE?", "Why Is an F1 Car Only Allowed 110 Kilograms of Fuel?",
     """Why is fuel limited in a race? The rules allow a maximum of one hundred ten kilograms for the whole race, and at least one kilogram must be handed to the FIA for checks after it. The limit makes the teams build engines that get more energy out of every drop. The fuel is also getting greener, with ten percent ethanol since two thousand twenty-two.""",
     "Formula One fuel refuelling")
sc("""A car that has to finish a race on a limited amount of fuel must be efficient. The engineers can not just burn more to go faster. So the rule pushes the sport toward engines that waste less, and fuels that are more sustainable.""",
   "Formula One engine efficiency", "EFFICIENCY IS THE RULE")
sc("""The sample is checked after the race, to make sure the fuel is what the team said it was. A fuel that does not match what the team declared can get it in trouble. Fuel is one more thing the officials watch closely.""",
   "Formula One FIA fuel sample", "THE FUEL IS CHECKED TOO")

# ---------- 10. SURVIVAL CELL ----------
part(10, "The survival cell", "WHY IS THE COCKPIT BUILT LIKE A TUB?", "What Is the Safety Tub of an F1 Car?",
     """What is the strong shell around the driver? It is called the monocoque, or survival cell. It is made of reinforced carbon fiber, lined with Kevlar and fire-resistant materials, to protect the driver from high-impact crashes and fires. The rest of the car can break apart in an accident, but this cell is built to stay in one piece.""",
     "Formula One monocoque survival cell")
sc("""That is why crashes at over two hundred kilometers an hour can end with the driver walking away. The engine, the wheels and the wings can fly off, and absorb the force, while the cell protects the person inside. The car is designed to break in a way that spares the driver.""",
   "Formula One crash survival cell", "BREAK THE CAR, SAVE THE DRIVER")
sc("""On top of this cell sits another safety part, a curved bar that you see over every driver's head. That is a story for another video, and it is one of the most important safety parts ever added to a racing car.""",
   "Formula One halo cockpit", "AND ABOVE IT, THE HALO")

# ---------- VERDICT ----------
sc("""So here are the ten. Titanium blocks that throw sparks, a plank that keeps the car off the ground, a floor that sucks the car down, a rear wing that opens, and a front wing measured in millimeters. Glowing brakes, a steering wheel full of buttons, smooth tyres, limited fuel, and a shell that protects the driver.""",
   "Formula One race sunset", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see sparks flying from a Formula One car, you will know what they are, and why they are there. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Formula One night race sparks", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video19", "title": "Why Do F1 Cars Throw Sparks?",
           "length_scale": 1.6, "scenes": S}, open("videos/video19/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
