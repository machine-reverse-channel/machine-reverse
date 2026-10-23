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
sc("""The Rimac Nevera weighs more than two tonnes, as much as a big family SUV. It has no engine sound, no gear changes and no exhaust. And it can reach one hundred kilometres per hour in under two seconds, faster than almost any petrol supercar ever built. How? Today, ten parts of an electric hypercar, and why each one makes it so fast.""",
   "Rimac Nevera", "WHY SO FAST?", cuts=8, chapter="Intro")
sc("""For a century, the fastest cars were built around bigger and louder engines. Then electric motors changed the rules. They work in a completely different way from a petrol engine, and almost every advantage of an electric hypercar comes from that difference, and from the battery that feeds it.""",
   "electric hypercar", "NEW RULES")
sc("""As always, every fact here comes from a named source, the car makers and automotive references, all listed in the description. Let's start with the motor.""",
   "electric motor", "WHY DOES THIS EXIST?")

# ---------- 1. INSTANT TORQUE ----------
part(1, "The electric motor", "WHY DOES THIS MOTOR PULL SO HARD?", "Why Do Electric Cars Accelerate So Fast?",
     """Why does an electric motor pull so hard from a standstill? A petrol engine makes its best force only at higher engine speeds. It has to rev up first. An electric motor makes its full pulling force, called torque, from the very first moment it turns. There is no waiting, no build up. Press the pedal, and all of it arrives at once.""",
     "electric car motor")
sc("""This is why even ordinary electric cars feel quick away from traffic lights. In a petrol car, the engine, the clutch and the gearbox have to work together, and every gear change interrupts the push. In an electric car, the force is smooth and constant, all the way from zero.""",
   "electric car acceleration", "NO WAITING")
sc("""The motor itself is surprisingly simple. Magnets and coils of copper wire, with one moving part that spins. No pistons, no valves, no explosions. A motor the size of a large watermelon can produce hundreds of horsepower. Simple, compact and brutally strong, it is the heart of every electric hypercar.""",
   "electric motor cutaway", "ONE MOVING PART")

# ---------- 2. FOUR MOTORS ----------
part(2, "The four motors", "WHY DOES THIS CAR HAVE FOUR MOTORS?", "Why Does an Electric Hypercar Have 4 Motors?",
     """Why does the Rimac Nevera have four electric motors? One for each wheel. Together, they produce close to two thousand horsepower. But the real reason is control. Each wheel can be given exactly the right amount of force at every moment, independently of the others.""",
     "Rimac Nevera")
sc("""This is called torque vectoring. In a corner, the car can push the outside wheels harder than the inside wheels, helping the car turn. On a slippery surface, it can reduce the force on a wheel that is about to spin. A petrol car needs complex differentials to do some of this. Four motors do it directly.""",
   "Rimac Nevera rear", "TORQUE VECTORING")
sc("""Electric motors can change their force far faster than any petrol engine. The car's computer adjusts each wheel many times per second. At launch, that means the tyres stay at the very edge of grip, without spinning. The four motors are not just about power. They are about using every bit of it.""",
   "Rimac Nevera front", "EVERY BIT OF POWER")

# ---------- 3. BATTERY FLOOR ----------
part(3, "The battery floor", "WHY IS THE BATTERY UNDER THE FLOOR?", "Why Is an Electric Car's Battery in the Floor?",
     """Why is the battery of an electric hypercar under the floor? Because it is the heaviest part of the car, and the lower the weight, the better the car handles. Putting hundreds of kilograms of battery at the very bottom of the car gives it a very low centre of gravity, lower than most petrol supercars.""",
     "electric car battery pack")
sc("""A low centre of gravity means the car leans less in corners and stays more stable when braking and accelerating. In the Nevera, the battery is shaped like an H, and runs through the middle of the car, behind and under the seats. It is also part of the structure, making the whole car stiffer.""",
   "Rimac battery", "LOW AND STIFF")
sc("""That is how a car that weighs over two tonnes can still corner like a much lighter car. The weight is there, but it is in the best possible place. In a petrol car, the engine sits high. In an electric car, the heaviest part lies flat, right where engineers want it.""",
   "electric car chassis", "THE BEST PLACE FOR WEIGHT")

# ---------- 4. GEARBOX ----------
part(4, "The single gear", "WHY DOES THIS CAR HAVE ONLY ONE GEAR?", "Why Do Electric Cars Have Only One Gear?",
     """Why do most electric cars have only one gear? Because an electric motor can spin very fast and still make strong force across a huge range of speeds. A petrol engine works well only in a narrow band, so it needs many gears to stay in that band. An electric motor does not.""",
     "electric car gearbox")
sc("""A single gear means no gear changes, and no interruption in the push. The acceleration is one smooth, unbroken surge from zero to very high speed. It also means fewer moving parts, less weight and less to go wrong. For acceleration, one gear is often the best gear.""",
   "electric drive unit", "ONE SMOOTH SURGE")
sc("""There are exceptions. The Porsche Taycan has a two speed gearbox on its rear motor. The first gear gives a stronger launch, and the second lets the motor spin slower at high speed, which helps efficiency and top speed. Engineers still debate which approach is better. But for most electric cars, one gear is enough.""",
   "Porsche Taycan", "THE TWO GEAR EXCEPTION")

# ---------- 5. INVERTER ----------
part(5, "The inverter", "WHY IS THIS BOX SO IMPORTANT?", "Why Is the Inverter the Brain of an Electric Car?",
     """Why is a small metal box called the inverter one of the most important parts of an electric car? The battery stores electricity as direct current, flowing in one direction. Most electric car motors need alternating current, which changes direction many times per second. The inverter converts one into the other.""",
     "electric car inverter")
sc("""By changing how fast and how strongly the current alternates, the inverter controls the speed and the force of the motor. It is the part that turns your foot on the pedal into motion. In a hypercar, it handles enormous currents, hundreds of amperes, switching them on and off thousands of times per second.""",
   "power electronics", "THE FOOT ON THE PEDAL")
sc("""Modern inverters use a material called silicon carbide, which wastes less energy as heat and can handle higher voltages. Tesla was one of the first to use it in a mass production car. Less wasted heat means more power reaches the wheels, and more range from the same battery.""",
   "silicon carbide", "LESS WASTED HEAT")

# ---------- 6. BATTERY POWER ----------
part(6, "The power cells", "WHY CAN THIS BATTERY DELIVER SO MUCH POWER?", "Why Can Hypercar Batteries Deliver So Much Power?",
     """Why can a hypercar battery deliver so much power at once? Because it is designed for power, not just range. A battery is made of thousands of cells. Some cells are built to store as much energy as possible. Others are built to release energy very fast. Hypercars use cells that can do both, at a high cost.""",
     "lithium-ion battery cells")
sc("""Releasing more than a megawatt from a battery is a huge challenge. The cells heat up quickly, and every connection between them must handle a large current. The Nevera's battery is designed to deliver the power of about two thousand horsepower, enough to supply many homes at once.""",
   "battery pack cells", "MORE THAN A MEGAWATT")
sc("""This is the real secret of electric speed. A powerful motor is easy to build. Feeding it with enough electricity, for long enough, without overheating, is the hard part. The battery is not just a fuel tank. It is the part that decides how fast the car can really go.""",
   "electric car battery", "THE REAL SECRET")

# ---------- 7. COOLING ----------
part(7, "The battery cooling", "WHY DOES THIS BATTERY NEED SO MUCH COOLING?", "Why Do Electric Hypercars Need So Much Cooling?",
     """Why does an electric hypercar need so much cooling? Because batteries and motors do not like heat. When a battery delivers a huge amount of power, it warms up fast. Too hot, and the cells age quickly or can even become dangerous. So the car limits its power before the battery gets too hot.""",
     "electric car cooling system")
sc("""That is why hypercars have liquid cooling running between the battery cells, around the motors and through the inverters, with radiators in the front of the car. On a race track, the cooling decides how many fast laps the car can do before it has to reduce power.""",
   "Rimac Nevera radiator", "HOW MANY FAST LAPS?")
sc("""A petrol supercar can run at full speed until the tank is empty. Many electric cars can deliver full power in short bursts, but not for long. Better cooling is what separates an electric hypercar that only wins drag races from one that can survive a whole track day.""",
   "electric car race track", "SHORT BURSTS")

# ---------- 8. AXIAL FLUX ----------
part(8, "The flat motor", "WHY IS THIS MOTOR SHAPED LIKE A PANCAKE?", "Why Are Some Electric Motors Shaped Like a Pancake?",
     """Why are some new electric motors flat, like a pancake? They are called axial flux motors. In a normal motor, the magnetic field crosses the gap between a spinning cylinder and a ring around it. In an axial flux motor, the field runs along the axis, between flat discs placed side by side.""",
     "axial flux motor")
sc("""That layout puts the magnets further from the centre, where they have more leverage, so the motor can produce more force for its size and weight. A flat motor can also fit between an engine and a gearbox, where a long cylinder would not. Ferrari uses one in its hybrid SF90.""",
   "Ferrari SF90", "MORE FORCE, LESS SIZE")
sc("""Axial flux motors are harder to build and cool, which is why they appeared first in expensive cars. But as production grows, they may spread to everyday electric cars. In engineering, the most exotic parts of today's hypercars often become the normal parts of tomorrow's family cars.""",
   "electric motor", "FROM HYPERCAR TO FAMILY CAR")

# ---------- 9. TYRES ----------
part(9, "The tyres", "WHY ARE THE TYRES THE REAL LIMIT?", "Why Are Tires the Limit for Electric Hypercars?",
     """Why are the tyres the real limit of an electric hypercar? Because the motors can deliver more force than the tyres can put on the road. At a standing start, two thousand horsepower would simply spin the wheels. The car is only as fast as the grip of four small patches of rubber, each about the size of a hand.""",
     "Michelin Pilot Sport Cup 2")
sc("""That is why hypercars use special soft tyres, sometimes developed just for that car. Soft rubber grips better, but wears out faster. On a cold road, even the best tyres grip less. The record runs of electric hypercars are done on prepared, warm surfaces, to get every bit of grip.""",
   "supercar tyre", "SOFT RUBBER")
sc("""It is a funny problem for engineers. For a century, the challenge was making enough power. Now the challenge is putting it down. An electric hypercar has more power than its tyres can use at low speed, and the computer holds it back to keep the tyres right at their limit.""",
   "tyre", "TOO MUCH POWER")

# ---------- 10. WEIGHT ----------
part(10, "The heavy weight", "WHY IS THIS CAR SO HEAVY?", "Why Are Electric Hypercars So Heavy?",
     """Why is an electric hypercar so heavy, and still so fast? The battery is heavy. A battery stores much less energy per kilogram than petrol does. To travel a useful distance at hypercar power, the car needs hundreds of kilograms of cells. The Nevera weighs over two tonnes, much more than a petrol supercar.""",
     "Rimac Nevera side")
sc("""In a straight line, the huge power and the instant torque more than make up for the weight. But weight hurts in corners, in braking and in tyre wear. That is why electric hypercars still use carbon fibre bodies, light materials and clever suspension to fight every extra kilogram.""",
   "carbon fibre chassis", "FIGHTING EVERY KILOGRAM")
sc("""Engineers are working on batteries that store more energy in less weight, such as solid state cells. If they succeed, electric hypercars will become lighter and even faster. Today, they are fast in spite of their weight. Tomorrow, they may be fast and light at the same time.""",
   "solid-state battery", "LIGHTER TOMORROW")

# ---------- VERDICT ----------
sc("""So here are the ten. A motor that gives all its force at once. Four motors that control each wheel. A battery in the floor for a low centre of gravity. One gear for one smooth surge. An inverter that turns your foot into motion. Cells built for power. Cooling that decides how long it lasts. Flat motors that pack more force. Tyres that set the real limit. And a heavy battery that the car has to fight.""",
   "electric hypercar", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Electric hypercars are fast because the rules of the motor changed. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments, electric or petrol, which hypercar would you choose?""",
   "Rimac Nevera night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video33", "title": "Why Are Electric Hypercars So Fast?",
           "length_scale": 1.6, "scenes": S}, open("videos/video33/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
