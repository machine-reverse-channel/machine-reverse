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
sc("""Some freight trains in North America are longer than three kilometers, almost two miles of steel boxes. And if you watch one pass, something strange happens. Halfway through, there is another locomotive. Sometimes there is one at the very end too, pushing. No crew inside. It is being driven by radio from the front. Today, ten parts of a giant freight train, and why each one exists.""",
   "freight train locomotives middle", "AN ENGINE IN THE MIDDLE", cuts=8, chapter="Intro")
sc("""Freight trains are the quiet giants of transport. One train can carry the load of hundreds of trucks, using a fraction of the fuel per ton. But the longer and heavier a train gets, the more it fights itself. The front pulls, the back pushes, every coupling stretches and squeezes, and a mistake can tear the train apart. Almost every strange part of a freight train exists to control those forces.""",
   "coal train", "A TRAIN THAT FIGHTS ITSELF")
sc("""As always, every fact comes from a named source, the Federal Railroad Administration, railway companies, and railway history, all listed in the description. Let's start with that engine in the middle.""",
   "distributed power locomotive mid train", "WHY DOES THIS EXIST?")

# ---------- 1. DPU ----------
part(1, "The engine in the middle", "WHY IS THERE AN ENGINE IN THE MIDDLE?", "Why Do Freight Trains Have Engines in the Middle?",
     """Why do long freight trains have locomotives in the middle? It is called distributed power. If all the locomotives are at the front, the couplers at the front have to pull the weight of the entire train. On a very long, heavy train, that force can break a coupler. Putting some locomotives in the middle or at the end splits the train into sections, and each group of engines pulls or pushes only part of the load.""",
     "distributed power locomotive mid train")
sc("""The remote locomotives have no crew. The engineer at the front controls them by radio, and they copy the commands, or can be set to work independently. Systems like this were developed in the nineteen sixties, and today they are common on long trains. In curves, they help too. A long train pulled only from the front tends to straighten itself across the inside of the curve, which can pull cars off the track.""",
   "freight train curve", "DRIVEN BY RADIO")
sc("""Braking is also better. On a long train, the air brake signal travels along the pipe from the front, and it takes time to reach the last car. With locomotives in the middle and at the end, the brakes can be applied from several points at once, so the whole train slows down more evenly. More engines in more places means a calmer train.""",
   "freight train locomotives", "A CALMER TRAIN")

# ---------- 2. SLACK ----------
part(2, "The slack between cars", "WHY DO FREIGHT CARS CRASH INTO EACH OTHER?", "Why Do Freight Train Cars Bang Into Each Other?",
     """Why do you hear a chain of bangs when a freight train starts? Every coupling between two cars has a little slack, a few centimeters of free movement. When the locomotive starts, it first pulls the first car, then the slack runs out, then the second car starts, then the third. With more than one hundred cars, those few centimeters add up to several meters, and you hear a wave of bangs running down the train.""",
     "freight train coupler slack")
sc("""The slack is not a mistake. It actually helps a locomotive start a heavy train, because it does not have to move all the cars at the same instant. Behind each coupler there is a spring and friction system called draft gear, which cushions those impacts. Without it, every start and stop would hammer the cars and the cargo.""",
   "draft gear railroad", "THE CUSHION")
sc("""But slack can also be dangerous. If the front of a train slows down while the back is still pushing, the slack runs in, and the cars slam together. Then if the front speeds up, the slack runs out and the couplers snap tight. Engineers on long freight trains are trained to manage slack carefully, especially on hills. Driving a two mile train is a lot like managing an accordion.""",
   "freight train hill", "AN ACCORDION")

# ---------- 3. KNUCKLE ----------
part(3, "The weak link", "WHY IS THIS PART DESIGNED TO BREAK?", "Why Is This Train Part Designed to Break?",
     """Why is one part of a freight train coupler designed to be the weak point? It is the knuckle, the curled piece that locks two couplers together. If the force on a train becomes too high, something has to give. Railways would much rather that it be a small, cheap, replaceable part than the frame of a car or the coupler shank itself. So the knuckle is often the part that breaks.""",
     "knuckle coupler")
sc("""When a knuckle breaks, the train separates. The air brake hose pulls apart, the pressure drops, and every car brakes automatically, so both halves stop. Then a crew member has to walk back, sometimes a long way, carrying a spare knuckle. A spare knuckle weighs about eighty pounds, around thirty-six kilograms, and locomotives often carry one for exactly this reason.""",
   "freight train couplers", "80 POUNDS OF SPARE")
sc("""The idea of a planned weak point appears everywhere in engineering. Fuses in electrical systems, shear pins in machines, and the knuckle in a train. When something must fail, you choose what fails. It is better to replace a small piece of steel by the tracks than to repair a broken car or clean up a derailment.""",
   "railroad knuckle", "CHOOSE WHAT FAILS")

# ---------- 4. FRED ----------
part(4, "The box at the end", "WHY IS THERE A BLINKING BOX ON THE LAST CAR?", "Why Is There a Blinking Box at the End of Freight Trains?",
     """Why is there a small box with a blinking red light on the last car of many freight trains? It is an end of train device, nicknamed FRED, flashing rear end device. It hangs on the rear coupler and connects to the brake pipe. It measures the air pressure at the back of the train and sends it by radio to the locomotive, and its light marks the end of the train for anyone behind it.""",
     "end of train device")
sc("""Many of these devices also work in the other direction. If the engineer needs an emergency stop, the rear device can open the brake pipe at the back too, so the emergency brake starts from both ends of the train. That matters if something blocks the air in the middle. In the United States, rules require two-way devices on many heavy freight trains.""",
   "FRED railroad", "BRAKING FROM BOTH ENDS")
sc("""This little box replaced something much bigger. For more than a century, the end of a train was marked by a whole car with people inside. A box with a battery, a light and a radio took over its job. It is one of the reasons a freight train that once needed five crew members can now run with two.""",
   "freight train last car", "IT REPLACED A CAR")

# ---------- 5. CABOOSE ----------
part(5, "The caboose", "WHY DID THE CABOOSE DISAPPEAR?", "Why Did the Caboose Disappear?",
     """Why did the caboose disappear from freight trains? The caboose was the crew's car at the end of the train. Conductors and brakemen rode in it, did paperwork, ate and even slept on long trips. Many had a raised window on the roof, called a cupola, so the crew could watch the whole train for smoke from overheated bearings, shifting loads, or dragging equipment.""",
     "caboose")
sc("""Then technology took over its jobs. Detectors beside the tracks started to check bearings and dragging equipment. End of train devices replaced the lights and the brake monitoring. Radios replaced hand signals. In the nineteen eighties, railways and unions in North America agreed to run most trains without cabooses, and they disappeared from most main lines.""",
   "caboose cupola", "REPLACED BY SENSORS")
sc("""Cabooses still exist in a few places, for example on some local trains that need a place for crew to ride while switching cars. Many old ones became museums, cafes, or even small hotels. The caboose is a nice example of how one machine can be replaced not by another machine, but by a group of small sensors spread along the railway.""",
   "caboose museum", "FROM CAR TO CAFE")

# ---------- 6. DYNAMIC BRAKE ----------
part(6, "The grids on the roof", "WHY DOES THIS LOCOMOTIVE HAVE A HEATER ON TOP?", "Why Do Locomotives Have Giant Heaters on Their Roofs?",
     """Why do many diesel locomotives have big fans and grids on the roof? They are for braking. A diesel locomotive is actually electric. The diesel engine drives a generator, and electric motors turn the wheels. When going downhill, those motors can be switched to work as generators, which slows the train. But the electricity has to go somewhere. It is sent to big resistor grids on the roof, which turn it into heat, and fans blow the heat away.""",
     "dynamic brake grid locomotive")
sc("""This is called dynamic braking, and it is essential on long hills. If a heavy train used only its air brakes on a long downhill grade, the brake shoes could overheat and lose their grip, a dangerous condition called brake fade. Dynamic braking holds the train back without wearing the brakes at all, so the air brakes stay cool and ready.""",
   "freight train downhill mountain", "NO BRAKE FADE")
sc("""Electric locomotives can go one step further, sending the energy back into the overhead wire for other trains to use, which is called regenerative braking. Diesel locomotives usually cannot, so they burn it as heat. On a cold winter day in the mountains, a locomotive using dynamic brakes is literally heating the sky.""",
   "electric locomotive freight", "HEATING THE SKY")

# ---------- 7. DOUBLE STACK ----------
part(7, "The double stack", "WHY ARE THESE CONTAINERS STACKED TWO HIGH?", "Why Are Train Containers Stacked Two High?",
     """Why are containers on many North American trains stacked two high? Because it almost doubles the cargo per train, using the same locomotives and the same crew. To make it possible, the cars have a low floor between the wheels, called a well. The bottom container sits in the well, almost touching the rails, and the second one sits on top, locked with fittings at the corners.""",
     "double stack container train")
sc("""Double stack trains became popular in the United States in the nineteen eighties. But they created a new problem. They are tall. Many old tunnels and bridges were too low. So railways spent large amounts of money raising tunnel roofs and lowering tracks to clear the way. Some lines were rebuilt only to make room for that second box.""",
   "well car double stack", "RAISE THE TUNNELS")
sc("""In Europe and many other places, double stack trains are rare, because of electric wires above the tracks and smaller tunnels and bridges. That is why American freight trains often look so much taller than European ones. The shape of a train is decided not only by engineering, but by the height of every bridge on its route.""",
   "European freight train containers", "THE HEIGHT OF EVERY BRIDGE")

# ---------- 8. HUMP YARD ----------
part(8, "The hill in the yard", "WHY DO RAILWAYS BUILD A HILL IN THE YARD?", "Why Do Train Yards Have a Hill in the Middle?",
     """Why do some railway yards have a small hill in the middle? It is a hump yard, a giant sorting machine that runs on gravity. A locomotive slowly pushes a long line of cars up the hump. At the top, cars are uncoupled one by one, and each rolls down the other side on its own. Switches send each car onto the right track, where it joins other cars going to the same destination.""",
     "hump yard")
sc("""Each car rolls at a different speed, depending on its weight, its bearings, and the wind. So the tracks have retarders, big steel jaws next to the rails that squeeze the wheels to slow the cars down. That loud screeching sound you hear near a hump yard is the retarders at work. Computers measure each car and decide how hard to squeeze it.""",
   "car retarder", "THE SCREECH")
sc("""The goal is for each car to reach the other cars on its track gently, fast enough to couple, but not so fast that it damages anything. Big hump yards can sort thousands of cars a day. Gravity does most of the work, and steel jaws and computers keep it under control.""",
   "railroad classification yard", "GRAVITY SORTS")

# ---------- 9. HELPERS ----------
part(9, "The loop", "WHY DOES THIS TRAIN CROSS OVER ITSELF?", "Why Does This Train Track Cross Over Itself?",
     """Why does one railway in California make a full loop and pass over itself? It is the Tehachapi Loop, built in the eighteen seventies to climb a steep mountain pass. Instead of going straight up a slope too steep for trains, the track spirals around a hill and gains height gradually. A long freight train crossing it passes over its own end, in one of the most famous sights in railroading.""",
     "Tehachapi Loop")
sc("""Even with the loop, the climb is hard, so heavy trains often need extra power. In the past, railways added helper locomotives, often at the back, to push trains up the grade, and then sent them back down to help the next train. Today, distributed power locomotives often do the same job, already placed in the middle and at the end.""",
   "helper locomotive pusher", "PUSH FROM BEHIND")
sc("""Grades matter enormously for trains. Steel wheels on steel rails have low friction, which makes trains efficient but also limits how steep a line can be. Main lines usually stay very gentle, often a slope of around one or two percent. Climbing a mountain with a train is not about power. It is about patience and distance.""",
   "railroad mountain pass", "PATIENCE AND DISTANCE")

# ---------- 10. DITCH LIGHTS ----------
part(10, "The triangle of lights", "WHY DO LOCOMOTIVES HAVE 3 LIGHTS LIKE THIS?", "Why Do Train Lights Form a Triangle?",
     """Why do many locomotives have lights arranged in a triangle? The headlight is on top, and two extra lights, called ditch lights, are lower down on each side. The triangle helps drivers at a crossing judge how far away the train is and how fast it is coming, because the lights seem to spread apart as the train gets closer. A single light is very hard to judge in the dark.""",
     "ditch lights locomotive")
sc("""In the United States, rules adopted in the nineteen nineties require these auxiliary lights on lead locomotives on many main lines. At crossings, the ditch lights often flash, along with the horn, to grab attention. Many accidents at crossings happen because drivers underestimate the speed of the train, so making speed visible saves lives.""",
   "railroad crossing train", "MAKE SPEED VISIBLE")
sc("""That is also why a freight train cannot stop quickly. A heavy train at full speed can need more than a mile, more than one and a half kilometers, to stop. By the time the engineer sees a car on the tracks, it is usually too late. The lights and the horn are not a courtesy. They are the only brakes that work fast enough, the ones in the minds of the people watching.""",
   "freight train headlight night", "MORE THAN A MILE TO STOP")

# ---------- VERDICT ----------
sc("""So here are the ten. Engines in the middle to share the load. Slack that works like an accordion, and a knuckle designed to break. A blinking box that replaced the caboose. Grids that turn braking into heat, cars that carry two boxes high, a hill that sorts trains with gravity, a track that loops over itself, and a triangle of lights that shows you how fast the train is coming.""",
   "coal train", "10 PARTS. 2 MILES OF TRAIN.", chapter="The verdict", cuts=6)
sc("""A freight train looks like the simplest machine on Earth. It is actually a two mile long system fighting its own weight. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "freight train sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:CN Freight. Helper Engine in Mid-train 6082 (6775062342).jpg", 0.65, 0.4),
    2: ("File:Long freight train in Newport station - geograph.org.uk - 6254833.jpg", 0.83, 0.6),
    3: ("File:AAR knuckle coupler connection.jpg", 0.5, 0.5),
    4: ("File:Rear of CSX train L005 awaiting departure from Framingham October 2025.jpg", 0.49, 0.69),
    5: ("File:Antique Caboose at La Crosse, Virginia.jpg", 0.62, 0.22),
    6: ("File:DGVR40 Staunton WJGrimes.JPG", 0.55, 0.3),
    7: ("File:DTTX 724681 20050529 IL Rochelle.jpg", 0.5, 0.5),
    8: ("File:Tinsley Hump Marshalling Yard 1981 - geograph.org.uk - 2308273.jpg", 0.45, 0.6),
    9: ("File:Tehachapi Loop Aerial.jpg", 0.5, 0.5),
    10: ("File:Illinois Central 101 (4593757527).jpg", 0.42, 0.62),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video47", "title": "Why Do Freight Trains Have Engines in the Middle?",
           "length_scale": 1.6, "scenes": S}, open("videos/video47/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
