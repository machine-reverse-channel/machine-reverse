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
sc("""When people picture a nuclear power plant, they picture giant curved towers with white clouds pouring out of them. Most people think those clouds are smoke, or even radiation. They are neither. They are water vapor, the same stuff as a cloud in the sky. And the towers are not even the nuclear part. Today, eleven parts of a nuclear power plant, and why each one exists, starting with those towers.""",
   "natural draft cooling tower", "IT IS NOT SMOKE", cuts=8, chapter="Intro")
sc("""A nuclear plant is, in the end, a way of boiling water. Uranium atoms split and release heat. That heat makes steam, the steam spins a turbine, and the turbine drives a generator. Most of the engineering, and most of the parts you see, exist to control that heat safely, and to get rid of the heat that cannot be turned into electricity.""",
   "nuclear power plant", "A WAY OF BOILING WATER")
sc("""As always, every fact comes from a named source, nuclear regulators, plant operators, and official accident reports, all listed in the description. Let's start with the towers.""",
   "cooling tower", "WHY DOES THIS EXIST?")

# ---------- 1. TOWER SHAPE ----------
part(1, "The curved tower", "WHY ARE THESE TOWERS SO GIANT?", "Why Do Nuclear Plants Have Those Giant Towers?",
     """Why do nuclear plants have those giant curved towers? Because a power plant must throw away a lot of heat. After the steam spins the turbine, it has to be cooled back into water, and that takes huge amounts of cooling water. The tower cools that water down. Warm water is sprayed inside near the bottom, air flows up through it, and some of the water evaporates, carrying the heat away.""",
     "natural draft cooling tower")
sc("""The tower works like a chimney with no fan. The warm, moist air inside is lighter than the air outside, so it rises, and fresh air is pulled in at the bottom. A tower can be more than a hundred and fifty meters tall, because the taller it is, the stronger the natural draft.""",
   "hyperboloid cooling tower", "A CHIMNEY WITH NO FAN")
sc("""The white cloud at the top is just water vapor condensing in the cold air, like your breath on a winter morning. The water inside the tower never touches the reactor. It is in a separate loop. That is also why coal and gas plants often have exactly the same towers.""",
   "cooling tower", "JUST WATER VAPOR")

# ---------- 2. HYPERBOLOID ----------
part(2, "The waist of the tower", "WHY IS THIS TOWER SHAPED LIKE THIS?", "Why Are Cooling Towers Shaped Like That?",
     """Why are cooling towers wide at the bottom, narrow in the middle, and wider again at the top? The shape is called a hyperboloid, and it is surprisingly strong. It can be built from straight lines. Imagine many straight steel beams leaning in a circle, all tilted the same way. Together, they make this curved shape, which resists wind and its own weight very well.""",
     "hyperboloid cooling tower")
sc("""Because it is so strong, the concrete shell can be very thin, often only around twenty centimeters, for a tower over a hundred meters tall. That is thinner, relative to its size, than an eggshell. Less concrete means a cheaper tower.""",
   "cooling tower inside", "THINNER THAN AN EGGSHELL")
sc("""The shape also helps the air. The wide base gives room for the water sprays and lets lots of air in. The narrow waist speeds up the rising air, and the flared top helps the plume mix with the outside air. One shape, solving the structure and the airflow at the same time.""",
   "natural draft cooling tower", "ONE SHAPE, TWO JOBS")

# ---------- 3. NO TOWERS ----------
part(3, "The plant without towers", "WHY DO SOME PLANTS HAVE NO TOWERS?", "Why Do Some Nuclear Plants Have No Cooling Towers?",
     """Why do some nuclear plants have no cooling towers at all? Because they use the sea, a lake or a big river instead. They pump huge amounts of water in, pass it through the condenser to cool the steam, and send it back a few degrees warmer. Plants on the coast, like many in France, Japan and the United Kingdom, often work this way.""",
     "nuclear plant water intake")
sc("""It is cheaper and more efficient, but it has limits. In very hot summers, river water can get too warm to cool the plant properly, and environmental rules limit how much warmer the river may become. Some plants in Europe have had to reduce power during heat waves for exactly this reason.""",
   "nuclear power plant", "HEAT WAVES")
sc("""Sea intakes have their own surprise enemy, jellyfish. Large swarms have been sucked into intake screens and clogged them, forcing plants in Scotland, Sweden and elsewhere to shut down for a while. A nuclear reactor, stopped by jellyfish.""",
   "nuclear plant water intake", "STOPPED BY JELLYFISH")

# ---------- 4. CONTAINMENT ----------
part(4, "The concrete dome", "WHY DOES THE REACTOR LIVE IN A DOME?", "Why Do Nuclear Reactors Live Inside a Dome?",
     """Why does the reactor sit inside a huge concrete dome or cylinder? It is the containment building, the last barrier between the reactor and the outside world. Its walls are reinforced concrete, often around a meter thick, lined with steel. If something breaks inside, and radioactive steam escapes from the pipes, the containment is designed to hold it in.""",
     "containment building")
sc("""The round shape is strong against pressure from inside, like a balloon or a pressure cooker. It also resists things from outside, like storms, earthquakes and even, in many designs, the impact of a crashing airplane.""",
   "containment building", "STRONG LIKE A BALLOON")
sc("""In nineteen seventy nine, at Three Mile Island in Pennsylvania, part of the reactor core melted. But the containment building did its job, and only small amounts of radioactivity escaped. At Chernobyl in nineteen eighty six, the reactor had no containment of this kind, and the explosion threw radioactive material straight into the sky.""",
   "Three Mile Island", "THE LAST BARRIER")

# ---------- 5. CONTROL RODS ----------
part(5, "The rods that stop the reaction", "WHY CAN THESE RODS STOP A REACTOR?", "Why Can Control Rods Stop a Nuclear Reactor?",
     """How do you turn off a nuclear reactor? You push rods into it. Uranium splits when it is hit by neutrons, and each split releases more neutrons, which split more atoms. Control rods are made of materials like boron or cadmium that soak up neutrons. Push them in, and the chain reaction slows down or stops. Pull them out a little, and it speeds up.""",
     "nuclear reactor control rods")
sc("""In an emergency, all the rods drop in at once, often in a couple of seconds. This is called a scram. In many reactors, the rods are held up by electromagnets, so if the power fails, they simply fall in by gravity. The safe position is the one they reach on their own.""",
   "nuclear reactor control rods", "THE SCRAM")
sc("""But stopping the chain reaction does not stop all the heat. The radioactive fuel keeps producing heat for days and weeks, at first several percent of full power. That is why a stopped reactor still needs cooling, and why losing that cooling is so dangerous.""",
   "nuclear reactor", "THE HEAT DOES NOT STOP")

# ---------- 6. FUEL ----------
part(6, "The pellet the size of a fingertip", "WHY IS THIS TINY PELLET SO POWERFUL?", "Why Is a Tiny Uranium Pellet So Powerful?",
     """How much energy is in nuclear fuel? It comes as small ceramic pellets of uranium oxide, about the size of a fingertip. According to the nuclear industry, one pellet can produce about as much energy as a tonne of coal. Splitting an atom releases millions of times more energy than burning one.""",
     "nuclear fuel assembly")
sc("""The pellets are stacked inside long metal tubes, called fuel rods, and the rods are grouped into square bundles called fuel assemblies, several meters long. A large reactor holds a few hundred assemblies, and around a third of them are replaced every year or two.""",
   "nuclear fuel assembly", "BUNDLES OF RODS")
sc("""The pellets are made of ceramic for a reason. Ceramic stays solid at very high temperatures and traps most of the radioactive products inside it. The metal tube around it is another barrier. Nuclear safety is built in layers, starting with a pellet you could hold in your fingers.""",
   "nuclear fuel assembly", "LAYERS OF BARRIERS")

# ---------- 7. SPENT FUEL POOL ----------
part(7, "The pool of glowing blue water", "WHY DOES THIS WATER GLOW BLUE?", "Why Does Water Around Nuclear Fuel Glow Blue?",
     """Why does the water around nuclear fuel sometimes glow blue? It is called Cherenkov radiation. Particles from the fuel travel through the water faster than light travels in water. They do not break the speed of light in a vacuum, but in water, light is slower. The result is a kind of optical shock wave, like a sonic boom, but made of blue light.""",
     "Cherenkov radiation")
sc("""Used fuel is stored in deep pools of water for years after it leaves the reactor. The water does two jobs. It cools the fuel, which is still producing heat, and it blocks the radiation. A few meters of water above the fuel make it safe for workers to stand at the edge of the pool.""",
   "spent fuel pool", "WATER AS A SHIELD")
sc("""After several years, when the fuel has cooled down, it can be moved into dry casks, thick containers of steel and concrete that sit outside on concrete pads. A pool of water and a steel can, keeping some of the most radioactive material on Earth safe.""",
   "spent fuel pool", "DRY CASKS")

# ---------- 8. PRESSURE VESSEL ----------
part(8, "The thick steel pot", "WHY IS THE REACTOR IN A GIANT STEEL POT?", "Why Does a Nuclear Reactor Need Such a Thick Steel Pot?",
     """Why is a nuclear reactor core held inside a giant steel pot? It is the reactor pressure vessel. In the most common type of reactor, the water around the core is heated to around three hundred degrees, but kept from boiling by enormous pressure, more than a hundred and fifty times the pressure of the air. Holding that takes steel walls around twenty centimeters thick.""",
     "reactor pressure vessel")
sc("""The hot pressurized water then flows to steam generators, where it heats a second loop of water that boils into steam for the turbine. The water that touches the fuel never leaves the containment. That separation keeps radioactivity away from the turbine and the outside world.""",
   "steam generator nuclear", "TWO LOOPS OF WATER")
sc("""The pressure vessel cannot be replaced. Over decades, neutrons slowly make its steel more brittle. So small samples of the same steel are placed inside the vessel when it is built, and taken out over the years to test. They tell engineers how the real vessel is aging.""",
   "reactor pressure vessel", "SAMPLES THAT AGE WITH IT")

# ---------- 9. CONTROL ROOM ----------
part(9, "The control room", "WHY DID THIS CONTROL ROOM CHANGE AFTER 1979?", "Why Did Nuclear Control Rooms Change After 1979?",
     """Why do nuclear control rooms look the way they do, and why do operators train in an exact copy of them? Because of Three Mile Island. In March nineteen seventy nine, a valve stuck open and let cooling water escape. A light on the control panel showed that the valve had been told to close, not that it actually had. Operators believed it was closed for hours.""",
     "nuclear power plant control room")
sc("""Hundreds of alarms went off at once, and the most important information was hard to find. Investigators found that the control room design and operator training were major causes of the accident. After that, control rooms were redesigned to make critical information clear, and every plant in the United States was required to have a full scale simulator.""",
   "nuclear power plant control room", "HUNDREDS OF ALARMS")
sc("""Operators now spend weeks every year in these simulators, practicing accidents that will probably never happen. The simulator is an exact copy, down to the color of the switches. When something goes wrong in the real room, their hands already know what to do.""",
   "nuclear power plant control room", "PRACTICE FOR THE WORST")

# ---------- 10. DIESEL GENERATORS ----------
part(10, "The emergency generators", "WHY DOES A POWER PLANT NEED GENERATORS?", "Why Does a Nuclear Plant Need Emergency Generators?",
     """Why does a power plant, which makes electricity, need emergency diesel generators? Because when the reactor stops, it cannot power itself. The pumps that keep cooling the fuel need electricity. If the connection to the grid is lost, the diesel generators must start within seconds and keep the pumps running.""",
     "emergency diesel generator")
sc("""In March two thousand eleven, at Fukushima Daiichi in Japan, the earthquake cut the plant off from the grid, and the diesel generators started as designed. Then the tsunami arrived. It flooded the generators and the electrical rooms, many of them in low parts of the buildings. With no power to cool the cores, three reactors melted down.""",
   "emergency diesel generator", "FUKUSHIMA, 2011")
sc("""After Fukushima, plants around the world added more backup power, placed higher or in protected buildings, plus portable pumps and generators stored away from the site. The lesson was simple. A backup is only a backup if the same disaster cannot destroy it too.""",
   "nuclear power plant", "A REAL BACKUP")

# ---------- 11. STEAM PLUMES ----------
part(11, "The cloud on the horizon", "WHY CAN YOU SEE THIS PLANT FROM SO FAR?", "Why Can You See a Nuclear Plant From Miles Away?",
     """Why can you see the cloud from a big power plant from tens of kilometers away? Because a large cooling tower evaporates an enormous amount of water. A big plant can release hundreds of liters of water every second as vapor. On a cold, humid day, the plume can rise high into the sky and even make its own clouds downwind.""",
     "cooling tower")
sc("""That water must be replaced, so plants with towers still need a river or lake nearby. They just take much less water than plants that cool directly with river water, because evaporation carries away heat very efficiently. Every liter that evaporates takes a large amount of heat with it.""",
   "natural draft cooling tower", "EVAPORATION CARRIES HEAT")
sc("""So the famous image of a nuclear plant is really an image of water. Water cooling the core, water shielding the fuel, water turning the turbine, and water rising into the sky as a cloud. The atom heats it. Everything else is plumbing.""",
   "natural draft cooling tower", "EVERYTHING ELSE IS PLUMBING")

# ---------- VERDICT ----------
sc("""So here are the eleven. A giant tower that throws away heat, shaped to be both strong and thin. Plants with no towers at all, a concrete dome around the reactor, and rods that stop the reaction. A pellet the size of a fingertip, a pool of glowing blue water, a thick steel pot, a control room rebuilt after an accident, generators that must never fail, and a cloud you can see for miles.""",
   "nuclear power plant", "11 PARTS. 0 SMOKE.", chapter="The verdict", cuts=6)
sc("""Next time you see those towers on the horizon, you will know the cloud is just water. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "cooling tower", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:De Molen (windmill) and the nuclear power plant cooling tower in Doel, Belgium (DSCF3859).jpg", 0.65, 0.45),
    2: ("File:Godorf Cologne Rhineland-Refinery-Cooling-Towers-during-demolition-02.jpg", 0.8, 0.6),
    3: ("File:Neckarwestheim Nuclear Power Plant September 2013.jpg", 0.45, 0.55),
    4: ("File:NPP containment building construction.jpg", 0.45, 0.15),
    5: ("File:Reactor Vessel head.jpg", 0.6, 0.45),
    6: ("File:Nuclear fuel pellets at the Greifswald Nuclear Power Plant information center.jpg", 0.5, 0.45),
    7: ("File:Cerenkov Effect.jpg", 0.5, 0.6),
    8: ("File:Interior of the VVER-440 reactor pressure vessel at Greifswald NPP.jpg", 0.45, 0.5),
    9: ("File:Shearon Harris Nuclear Power Plant control room.jpg", 0.5, 0.4),
    10: ("File:Emergency power system in water purification plant Germany.jpg", 0.55, 0.5),
    11: ("File:De Molen (windmill) and the nuclear power plant cooling tower in Doel, Belgium (DSCF3859).jpg", 0.4, 0.15),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video59", "title": "Why Do Nuclear Plants Have Those Giant Towers?",
           "length_scale": 1.6, "scenes": S}, open("videos/video59/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
