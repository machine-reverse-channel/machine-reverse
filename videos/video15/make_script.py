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
sc("""A spacesuit is a small spaceship that you wear. It has to keep you alive in a place with no air, no pressure, and temperatures that swing from about minus two hundred fifty degrees Fahrenheit to plus two hundred fifty, depending on whether you are in the Sun or in the shade. And almost every spacesuit you have ever seen is white. A standard flight-rated NASA suit has been put at around twelve million dollars. Today, ten parts of a spacesuit, and why each one exists.""",
   "astronaut spacewalk spacesuit", "WHY ARE SPACESUITS WHITE?", cuts=8, chapter="Intro")
sc("""Every part of a suit is a solution to a different way space can kill you. Too hot, too cold, too little pressure, tiny fast rocks, and the fact that if you drift away, nobody can come and get you. Let's go through them one by one.""",
   "astronaut spacewalk International Space Station", "SPACE HAS MANY WAYS TO KILL")
sc("""As always, every fact here comes from a named source, NASA pages and spaceflight references, all listed in the description. Let's start with the color.""",
   "astronaut spacesuit EMU", "WHY DOES THIS EXIST?")

# ---------- 1. WHITE ----------
part(1, "The white outer layer", "WHY IS THE SPACESUIT WHITE?", "Why Are Spacesuits White?",
     """Why are spacesuits white? To deflect sunlight. In space there is no air to carry heat away, so the Sun can heat the outside of a suit to about two hundred fifty degrees Fahrenheit, one hundred twenty-one Celsius. White reflects most of that light. The outer layer is a fabric that blends three kinds of threads, and its job is to keep the heat from ever reaching the astronaut.""",
     "astronaut white spacesuit EMU")
sc("""In the shadow, the problem reverses. Temperatures on a spacewalk can drop to about minus two hundred fifty degrees Fahrenheit. On the International Space Station, every lap around the Earth, about every ninety minutes, includes a trip through the Earth's shadow. The suit has to handle both.""",
   "spacewalk sunrise International Space Station", "EVERY LAP: SUN, THEN SHADE")
sc("""White is a bad color for a work suit on the ground, because it shows every stain. But where the main danger is the Sun's heat, a clean white surface is the best color there is.""",
   "astronaut spacewalk Earth", "WHITE REFLECTS THE SUN")

# ---------- 2. LAYERS ----------
part(2, "The many layers", "WHY IS THE SUIT MADE OF SO MANY LAYERS?", "Why Is a Spacesuit Made of So Many Layers?",
     """Why does a spacesuit have so many layers? The flexible parts are made of as many as sixteen layers of material, each one doing a different job. Some hold the pressure in, some stop the heat from passing, and some protect against tiny pieces of space dust and rock moving at huge speeds. On the Apollo suits, five of the layers were thin aluminized insulation, under an outer layer of white fabric.""",
     "spacesuit layers Thermal Micrometeoroid Garment")
sc("""Think of a thermos bottle you wear. The aluminized layers reflect heat back and forth, like the mirror inside a thermos, so very little gets through. And the outer fabric takes the scratches and the tiny impacts, so the layers below stay whole.""",
   "spacesuit insulation layers", "A THERMOS YOU WEAR")
sc("""Every layer has a cost. They make the suit stiff, heavy and hard to move in. Designing a suit is a long argument between safety and movement, and the layers are where that argument happens.""",
   "astronaut suit test", "SAFE OR FLEXIBLE")

# ---------- 3. GOLD VISOR ----------
part(3, "The gold visor", "WHY IS THE VISOR GOLD?", "Why Do Astronaut Helmets Have a Gold Visor?",
     """Why is the visor of an astronaut's helmet gold? It is a special gold coating that works like the astronaut's sunglasses. In space, the sunlight is far brighter than anything on the ground, with no air to soften it, and it carries a lot of heat. The thin layer of gold reflects most of it away, while still letting the astronaut see out.""",
     "astronaut helmet gold visor")
sc("""There is a clear helmet underneath it, the bubble that holds the air. The gold visor is pulled down over it, like a pair of sunglasses over a pair of glasses. When the astronaut is in the shade, it can be lifted.""",
   "astronaut gold visor reflection", "SUNGLASSES FOR SPACE")
sc("""And the gold is not just for show. It also reflects the astronaut, and the whole station, in a mirror, which is why so many famous space photos show the photographer inside the visor.""",
   "astronaut visor reflection Earth", "A MIRROR TO THE WORLD")

# ---------- 4. COOLING GARMENT ----------
part(4, "The tube underwear", "WHY IS THERE UNDERWEAR FULL OF TUBES?", "Why Do Astronauts Wear Underwear Full of Tubes?",
     """Why do astronauts wear a suit full of tubes under their spacesuit? It is called the Liquid Cooling and Ventilation Garment. About three hundred feet of tubing is woven into a tight-fitting piece of clothing, and chilled water flows through it to take heat away from the body. A spacewalk is hard work, and in a sealed suit, an astronaut would quickly overheat without a way to take the heat away.""",
     "astronaut liquid cooling garment")
sc("""The heat has to go somewhere. It is carried by the water to the backpack, and from there it is released into space. The same idea as a car radiator, but with vacuum on the other side.""",
   "astronaut cooling garment radiator", "THE BODY'S RADIATOR")
sc("""The ventilation part takes away the gases the astronaut breathes out. So underwear, in this case, is part of the life support system. And without it, the white suit would just be a very clean oven.""",
   "astronaut suit underwear", "OTHERWISE, AN OVEN")

# ---------- 5. BACKPACK ----------
part(5, "The life support backpack", "WHY DOES THE SUIT HAVE A BACKPACK?", "What Is Inside an Astronaut's Backpack?",
     """What is inside an astronaut's backpack? It is the Primary Life Support System, the part that keeps the suit alive. It supplies oxygen, removes the carbon dioxide, circulates the cooling water, and holds a regulator that keeps the suit at the right pressure. Its primary supply lasts about eight hours, with another thirty minutes of backup.""",
     "astronaut life support backpack PLSS")
sc("""Eight hours is a long day of work, and the margin matters. A spacewalk is planned like a mountain climb, with a clear turnaround time, and a reserve that nobody wants to use. When a suit runs low, the astronaut heads back to the airlock.""",
   "astronaut spacewalk airlock", "A CLEAR TURNAROUND TIME")
sc("""And the backpack is also a good example of how heavy a suit is. On Earth, the full suit for the space station, with its backpack, weighs about three hundred nineteen pounds. In space, nobody feels that weight.""",
   "astronaut suit weightless", "HEAVY ON EARTH, FREE IN SPACE")

# ---------- 6. STRIPES ----------
part(6, "The red stripes", "WHY DO SOME SUITS HAVE RED STRIPES?", "Why Do Some Spacesuits Have Red Stripes?",
     """Why do some spacesuits have red stripes? So you can tell the astronauts apart. Out on a spacewalk, two white suits with two gold visors look almost identical, and that is a problem for the people watching the cameras on the ground. Some suits have stripes to help tell one spacewalker from another. On the Apollo program, the commander's stripes were introduced on Apollo 13, for exactly that reason.""",
     "astronaut suit red stripes")
sc("""It sounds like a small thing. But in a spacewalk, mission control has to know who is working on what. If the instructions are meant for one person and the other follows them, the mistake could cost a lot, and a stripe is a very cheap fix.""",
   "two astronauts spacewalk stripes", "A VERY CHEAP FIX")
sc("""So the stripes are a safety feature as well as a fashion detail. And in a vehicle built from carefully weighed parts, a stripe of paint is about as light as a safety feature can be.""",
   "astronaut spacewalk suit stripe", "LIGHT AS PAINT")

# ---------- 7. SNOOPY CAP ----------
part(7, "The Snoopy cap", "WHY DO ASTRONAUTS WEAR A CLOTH CAP UNDER THE HELMET?", "Why Do Astronauts Wear a Cloth Cap Under Their Helmets?",
     """Why does an astronaut wear a cloth cap under the helmet? It holds the microphones and earphones. It is called a communications carrier assembly, and on Apollo, the cap was nicknamed the Snoopy cap, because the colors looked like the cartoon dog. Inside a sealed helmet, the microphones and earphones have to stay close to the mouth and the ears, and the cap holds them there.""",
     "astronaut Snoopy cap communications")
sc("""In space there is no air to carry sound between two people. Outside the station, astronauts can only talk by radio, and all of it goes through the cap. If the cap fails, the astronaut is silent, and a silent astronaut is a problem for everyone.""",
   "astronaut radio spacewalk", "NO AIR, ONLY RADIO")
sc("""So the cap is a tiny part with a big job. It is the link between a person in a suit, and everybody who is working to keep them alive.""",
   "astronaut helmet communications cap", "THE LINK TO EVERYONE")

# ---------- 8. HEATED GLOVES ----------
part(8, "The heated gloves", "WHY DO THESE GLOVES HAVE HEATERS?", "Why Do Astronaut Gloves Have Heaters?",
     """Why do astronaut gloves have heaters? Because hands get the coldest. On the International Space Station, the gloves have built-in heaters, with an extra battery, for the night part of each ninety-five minute orbit. The hands touch cold metal tools and handrails, and fingers are far from the warm core of the body, so they are the first to suffer.""",
     "astronaut spacesuit gloves")
sc("""Gloves are also the hardest part to make. The hand must be able to grip a tool, feel a bolt and turn a screw, inside a pressurized glove that wants to stay straight like a balloon. Astronauts say that squeezing the glove for hours is hard work.""",
   "astronaut glove grip tool", "A BALLOON ON YOUR HAND")
sc("""So a tiny heater and a battery on each hand is a part of safety too. A cold hand does not work well, and in space a hand that does not work well can be the end of a job.""",
   "astronaut hand spacewalk", "A COLD HAND CAN'T WORK")

# ---------- 9. SAFER ----------
part(9, "The rescue jetpack", "WHY DOES THE SUIT HAVE A TINY JETPACK?", "Why Do Astronauts Wear a Tiny Jetpack?",
     """Why does an astronaut wear a small jetpack on a spacewalk? It is called SAFER, which stands for Simplified Aid For EVA Rescue, and it has been used with the space station suits since nineteen ninety-eight. If an astronaut lets go of the station and starts drifting away, the jetpack can fly them back. A spacewalker is normally attached to the station with tethers, and SAFER is the backup if those fail.""",
     "astronaut SAFER jetpack")
sc("""There is no one to come and get you in space. A rescue spacecraft takes a long time to arrive, and a drifting astronaut would keep moving away. So the rescue has to be on the astronaut's back, ready to use.""",
   "astronaut free flying SAFER", "NO ONE CAN COME GET YOU")
sc("""It is a small, simple machine, small nozzles and a joystick. But it is the last line of defense, worn on station spacewalks since nineteen ninety-eight.""",
   "astronaut joystick jetpack", "THE LAST LINE OF DEFENSE")

# ---------- 10. PRESSURE ----------
part(10, "The stiff pressurized suit", "WHY IS THE SPACESUIT SO STIFF?", "Why Is a Spacesuit So Hard to Move In?",
     """Why is a spacesuit so stiff? Because it is full of air. The shuttle-era suit is kept at about four point three pounds per square inch, around thirty kilopascals, of pure oxygen. That is much lower than the air pressure on the ground, but it is enough to make the suit inflate like a balloon, and a balloon does not bend easily at the elbows and knees.""",
     "astronaut spacesuit pressurized")
sc("""Why not a lower pressure, to make it softer? Because lower pressure leaves less oxygen to breathe. A suit of pure oxygen needs about four point seven pounds per square inch, and four point three is close to the lowest limit at which astronauts can safely work.""",
   "spacesuit pressure test", "A BALANCE OF PRESSURE")
sc("""Without the suit, an astronaut in a vacuum would lose consciousness in about fifteen seconds. The stiffness is the price of being alive. And every new suit design is a new try at making it a little bit softer.""",
   "astronaut spacewalk vacuum", "STIFF, BUT ALIVE")

# ---------- VERDICT ----------
sc("""So here are the ten. White to reflect the Sun, many layers of insulation, a gold visor, underwear full of tubes, and a backpack for life support. Stripes to tell people apart, a cap with microphones, heated gloves, a rescue jetpack, and a suit that is stiff because it is full of air.""",
   "astronaut spacewalk sunrise", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see an astronaut, you will see more than a white suit. It is a spaceship, made for one person. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "astronaut spacesuit museum", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video15", "title": "Why Are Spacesuits White?",
           "length_scale": 1.6, "scenes": S}, open("videos/video15/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
