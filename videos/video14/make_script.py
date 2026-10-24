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
sc("""The Saturn V is the rocket that took humans to the Moon, and it is covered in black and white stripes, like a giant barber pole. Those markings are not decoration. The rocket stood one hundred eleven meters tall, weighed almost three million kilograms, and every part of it was built for one single job, getting three people to the Moon. Today, nine parts of the Saturn V, and why each one exists.""",
   "Saturn V rocket", "WHY BLACK AND WHITE?", cuts=8, chapter="Intro")
sc("""Ten Saturn V launches carried people. Nine took astronauts to the Moon, and one stayed in Earth orbit as a test. It was a machine so large that it needed a building to be stacked in, and yet nothing on it was there by accident.""",
   "Saturn V launch Apollo", "NOTHING BY ACCIDENT")
sc("""As always, every fact here comes from a named source, NASA documents and spaceflight references, all listed in the description. Let's start with the paint.""",
   "Saturn V Apollo 11 launch", "WHY DOES THIS EXIST?")

# ---------- 1. PAINT ----------
part(1, "The black and white paint", "WHY IS THE ROCKET BLACK AND WHITE?", "Why Was the Saturn V Painted Black and White?",
     """Why was the Moon rocket painted black and white? Both colors had a job. The white paint reflected the sunlight, keeping the rocket cool while it sat on the pad in the hot Florida sun. A cooler tank means less fuel boiling off, and a safer rocket. The black markings helped ground cameras measure the roll, the spin of the rocket as it rose.""",
     "Saturn V black and white paint")
sc("""The early Saturn rockets had more black than the later ones. On those flights, the fuel tanks under the black areas registered heat spikes, because the dark paint absorbed the heat of the Sun. So on later Saturn V rockets, the upper black stripes and the band on the first stage were painted over in white.""",
   "Saturn I rocket black white stripes", "TOO MUCH BLACK, TOO HOT")
sc("""So the pattern on the rocket is the result of tests. Engineers painted it, watched the temperatures, and then repainted it. It is a good reminder that even the most famous design of the century was changed by data.""",
   "Saturn V Apollo pad", "REPAINTED BY DATA")

# ---------- 2. F-1 ENGINES ----------
part(2, "The five F-1 engines", "WHY DOES IT HAVE FIVE HUGE ENGINES?", "Why Does the Saturn V Have Five Giant Engines?",
     """Why does the bottom of the Saturn V have five giant engines? Because the rocket had to lift almost three million kilograms off the ground. The first stage had five Rocketdyne F-1 engines, arranged in a cross with one in the middle, and together they produced about thirty-three thousand kilonewtons of thrust at sea level. That is about seven and a half million pounds.""",
     "Saturn V F-1 engines")
sc("""The first stage burned for only about one hundred fifty seconds. In two and a half minutes, it used up most of its propellant, kerosene and liquid oxygen, and pushed the rocket up to the edge of space. After that, the huge stage had done all it could do, and it was dropped.""",
   "Saturn V S-IC first stage", "150 SECONDS OF FIRE")
sc("""The shape of that cross matters too. One engine in the center and four around it means a layout that stays balanced, and a design in which the outer engines can be tilted to steer the rocket. It is one of the most powerful engine clusters ever flown.""",
   "Saturn V first stage engines", "A CROSS OF FIRE")

# ---------- 3. LAUNCH ESCAPE TOWER ----------
part(3, "The escape tower", "WHY IS THERE A TOWER ON TOP?", "Why Does the Saturn V Have a Tower on Top?",
     """Why is there a thin tower on the very top of the rocket? It is the Launch Escape System, a rocket motor built to save the crew. If the Saturn V ever started to fail on the pad or in the first minutes, the escape rocket would pull the crew capsule up and away from the exploding rocket, and the capsule would come down on its parachutes.""",
     "Saturn V launch escape system tower")
sc("""It is a rocket on top of a rocket, designed to be used only if everything goes wrong. If everything went right, it was never used. On a normal flight, it was dropped shortly after the second stage took over, because by then it was dead weight.""",
   "Apollo launch escape tower jettison", "USED ONLY IF IT ALL GOES WRONG")
sc("""Every Apollo crew rode under that tower knowing it was there. It is a strange part, because its success is measured by never needing it. A safety system that works is one that nobody ever sees fire.""",
   "Apollo capsule launch escape system", "A SAFETY NET YOU NEVER SEE")

# ---------- 4. INTERSTAGE ----------
part(4, "The interstage ring", "WHY IS THERE A RING BETWEEN THE STAGES?", "Why Does the Saturn V Have a Ring Between Its Stages?",
     """Why is there a ring between the stages? It is called the interstage, and it joins two stages that burn at different times. Its job comes at the next stage's ignition. About three minutes and twelve seconds into the flight, the interstage ring dropped away from the second stage. The ring was only about one meter from the outer engines, so it had to fall cleanly.""",
     "Saturn V interstage")
sc("""The second stage engines had to light while still attached to the first stage's top, with the ring around them. When the ring dropped, the engines could burn freely, with nothing in front of the nozzles. Any problem, and the second stage could be damaged.""",
   "Saturn V stage separation", "ONE METER FROM THE FLAME")
sc("""So a simple ring of metal had to be strong enough to hold a stage, and light enough to be dropped. And like many parts of a rocket, it worked perfectly or not at all.""",
   "Saturn V interstage separation Apollo", "WORKS OR FAILS")

# ---------- 5. INSTRUMENT UNIT ----------
part(5, "The instrument ring", "WHAT IS THIS RING NEAR THE TOP?", "What Is the Ring Near the Top of the Saturn V?",
     """What is the ring near the top of the Saturn V? It is the Instrument Unit, the rocket's brain. It sat on top of the third stage and held the guidance, navigation and control equipment. It was designed at the Marshall Space Flight Center and built by IBM. The ring is six point six meters wide and only about ninety-one centimeters tall, and it weighs about two thousand kilograms.""",
     "Saturn V instrument unit")
sc("""A rocket cannot be steered by a person from the ground at that speed. So the unit measured where the rocket was, compared it to the plan, and told the engines how to point. In the end, the thing that put a spacecraft on its way to the Moon was a ring, a bit taller than a kitchen counter.""",
   "Saturn V guidance computer", "THE ROCKET'S BRAIN")
sc("""It is almost funny that so much depended on so thin a part. But a computer is mostly the volume of wires and boxes that keep it alive, and the ring was just big enough to hold them.""",
   "Saturn V instrument unit ring", "A THIN RING, A BIG JOB")

# ---------- 6. S-II ----------
part(6, "The second stage", "WHY IS THE SECOND STAGE A DIFFERENT FUEL?", "Why Did the Saturn V's Upper Stages Burn Hydrogen?",
     """Why did the upper stages of the Saturn V burn a different fuel? The first stage burned kerosene, which is dense and gives a lot of push for its volume. The second and third stages burned liquid hydrogen with liquid oxygen. Hydrogen gives much more energy for each kilogram, which matters most once the rocket is high and every kilogram counts. The second stage used five J-2 engines and burned for about three hundred ninety-five seconds.""",
     "Saturn V S-II second stage")
sc("""The price is the cold. Liquid hydrogen has to be kept at hundreds of degrees below zero, and it takes up a lot of room. That is why the second stage was a huge tank, nearly twenty-five meters tall, with so little else around it.""",
   "Saturn V S-II stage tank", "A TANK OF COLD")
sc("""So the Saturn V used the right fuel at each point of the trip. Dense fuel to leave the ground, and light, powerful fuel to go the rest of the way. Fuel was chosen the same way everything else was, for the job.""",
   "Saturn V stages fuel", "THE RIGHT FUEL FOR EACH STEP")

# ---------- 7. S-IVB ----------
part(7, "The third stage", "WHY DID THE THIRD STAGE LIGHT TWICE?", "Why Did the Saturn V's Third Stage Fire Twice?",
     """Why did the third stage fire two times? The first burn, about one hundred sixty-five seconds, put the spacecraft into orbit around the Earth. After a short pause, with the crew checking everything, the single J-2 engine lit a second time, for about three hundred twelve seconds, and sent them toward the Moon. This second burn is called the trans-lunar injection.""",
     "Saturn V S-IVB third stage")
sc("""Starting in orbit gave the crew time to check the spacecraft before committing to the Moon. If something was wrong, they could stay near Earth. If everything was fine, the second burn took them out. It was a safe way to start a very long trip.""",
   "Apollo Earth orbit translunar injection", "CHECK FIRST, THEN GO")
sc("""And after the second burn, the third stage had done its work. It stayed behind, while the crew went on in the spacecraft. The most powerful rocket ever flown by humans was, in the end, a way to push a very small capsule faster than anything had gone.""",
   "Apollo S-IVB translunar", "A VERY SMALL PASSENGER")

# ---------- 8. S-IC FIRST STAGE ----------
part(8, "The giant first stage", "WHY IS THE FIRST STAGE SO TALL?", "Why Is the Saturn V's First Stage So Huge?",
     """Why was the first stage so enormous? It stood forty-two meters tall and weighed about two million two hundred thousand kilograms with fuel, most of the rocket's total weight. Almost all of that was propellant. The first stage had to carry its own fuel and the weight of everything above it, and the higher the rocket went, the less it needed to carry, so most of that mass was dropped at the first stage.""",
     "Saturn V S-IC first stage Johnson Space Center")
sc("""This is the basic problem of rockets. To lift fuel, you need more fuel. A rocket that carries everything to the Moon at once would be impossibly heavy. So it is built in stages, each one throwing away the part that is empty.""",
   "Saturn V stage empty tank", "TO LIFT FUEL YOU NEED FUEL")
sc("""The Saturn V is the answer to that problem at its most extreme. More than ninety percent of the rocket on the pad was never going to reach the Moon. It was only there to carry the last part of it.""",
   "Saturn V rollout", "MOST OF IT NEVER GOES")

# ---------- 9. THE SPACECRAFT ----------
part(9, "The tiny spacecraft on top", "WHY IS THE SPACECRAFT SO SMALL?", "Why Is the Apollo Spacecraft So Small Compared to the Saturn V?",
     """Why is the spacecraft so small compared to the rocket? Because it is the only part that goes to the Moon. The whole Saturn V, almost one hundred twelve meters of it, existed to move one small capsule and a lunar module. Nine of the ten crewed Saturn V flights took twenty-four astronauts to the Moon.""",
     "Apollo spacecraft top of Saturn V")
sc("""Everything the astronauts needed, air, food, power and a way home, had to fit in that small space, and every kilogram of it had to be lifted by the rocket below. Engineers fought for every gram, because each gram on the capsule cost far more on the ground.""",
   "Apollo command module", "EVERY GRAM COSTS KILOS")
sc("""And that is the Saturn V in a nutshell. A tower of fuel, engines and machines, there to carry a small cone to a place that no one had been, and bring it back.""",
   "Apollo 11 command module", "A TOWER FOR A TINY CONE")

# ---------- VERDICT ----------
sc("""So here are the nine. Paint that kept it cool and let cameras measure the roll, five engines in a cross, an escape tower, a ring that fell away, and a ring that was the brain. A hydrogen second stage, a third stage that lit twice, a first stage as tall as a building, and a tiny spacecraft on top.""",
   "Saturn V launch sunrise", "9 PARTS. 9 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see the black and white rocket in a museum, you will know that every stripe and every ring is there for a reason. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Saturn V museum", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Apollo 11 rollout (KSC-69PC-0234).jpg", 0.36, 0.35),
    2: ("File:Saturn V's F-1 engines.jpg", 0.55, 0.45),
    3: ("File:Space Center Houston Rocket Park Saturn V CSM.jpg", 0.74, 0.5),
    4: ("File:Saturn V Rocket -- Johnson Space Center.jpg", 0.7, 0.45),
    5: ("File:Saturn Instrument Unit - Evergreen Aviation & Space Museum - McMinnville, Oregon - DSC00846.jpg", 0.6, 0.3),
    6: ("File:S-II Stage of Saturn V Rocket (67-701-c).jpeg", 0.58, 0.65),
    7: ("File:Saturn V Rocket Stage S IVB - 1992.jpg", 0.5, 0.5),
    8: ("File:SaturnV S-IC (cropped).jpg", 0.45, 0.4),
    9: ("File:Space Center Houston Rocket Park Saturn V CSM.jpg", 0.45, 0.55),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video14", "title": "Why Was the Saturn V Painted Black and White?",
           "length_scale": 1.6, "scenes": S}, open("videos/video14/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
