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
sc("""Look under almost any railway track in the world and you will see the same thing. Rocks. Millions of sharp, gray stones, piled under and around the rails. They look like leftovers from construction, but they are one of the most carefully designed parts of the railway. Without them, a track would sink, flood, and twist out of shape in a few months. Today, ten parts of a railway track, and why each one exists.""",
   "railway ballast", "THE ROCKS ARE NOT AN ACCIDENT", cuts=8, chapter="Intro")
sc("""A railway track looks simple. Two steel rails, some blocks under them, and stones. But every train that passes hits it with enormous force, again and again, in rain, heat and frost. A loaded freight car can weigh more than one hundred tons, all carried by just eight wheels, and a train can have more than one hundred cars. The track has to take that punishment every day and stay accurate to a few millimeters.""",
   "freight train track", "ACCURATE TO MILLIMETERS")
sc("""As always, every fact comes from a named source, railway engineering references, infrastructure managers, and railway history, all listed in the description. Let's start with the rocks.""",
   "track ballast close up", "WHY DOES THIS EXIST?")

# ---------- 1. BALLAST ----------
part(1, "The rocks", "WHY ARE THERE ROCKS UNDER RAILWAY TRACKS?", "Why Are There Rocks Under Railway Tracks?",
     """Why are there rocks under railway tracks? They are called ballast, and they do three jobs at once. First, they spread the weight of the train over the soft ground below, like snowshoes. Second, they lock the sleepers in place, so the track cannot slide sideways or along its length. And third, they let rain drain away instantly. Water is the enemy of a railway, because wet ground turns soft and the track sinks.""",
     "railway ballast")
sc("""The stones are not random. They are crushed rock, usually hard stone like granite or basalt, broken into pieces of a few centimeters with sharp edges. Sharp edges matter. Angular stones lock together like a puzzle when they are pressed. Round river pebbles would roll like marbles, and the track would move every time a train passed.""",
   "crushed stone granite", "SHARP, NOT ROUND")
sc("""Ballast also keeps plants away. Grass and weeds hold water and fill the gaps between stones, so railways regularly send weed control trains to spray the track. And the layer is deep, often around a quarter of a meter or more under the sleepers. Those gray rocks are a foundation, a drain and a clamp, all in one.""",
   "weed spraying train", "A FOUNDATION, A DRAIN, A CLAMP")

# ---------- 2. SLEEPERS ----------
part(2, "The sleepers", "WHY ARE THERE BLOCKS UNDER THE RAILS?", "Why Do Railway Tracks Need Sleepers?",
     """Why are there blocks across the track under the rails? They are called sleepers in Britain and ties in America. Their job is to hold the two rails at exactly the right distance apart, called the gauge, and to pass the load from the rails into the ballast. A main line has well over a thousand of them in every kilometer. If the gauge opens even a few centimeters, a wheel can drop between the rails.""",
     "concrete sleepers")
sc("""For more than a century, sleepers were mostly wood, often soaked in creosote, a dark tar-like preservative that protects against rot and insects. That smell of a railway on a hot day is often creosote. Many modern main lines use concrete sleepers instead. They are heavier, around a quarter of a ton or more each, so they hold the track more firmly, and they can last for decades.""",
   "wooden railway sleepers", "THE SMELL OF A RAILWAY")
sc("""Wood is still everywhere, though. In North America, most ties are still wood, because wood is easy to cut, handles impacts well, and is simple to replace one by one. Some railways now use sleepers made of recycled plastic or composite materials. The block under the rail is one of the most replaced parts in the whole railway.""",
   "railroad ties stack", "STILL MOSTLY WOOD")

# ---------- 3. CLIPS ----------
part(3, "The rail clip", "WHY IS THE RAIL HELD BY THIS CLIP?", "Why Are Rails Held Down by Springs?",
     """Why are modern rails held down by small curled pieces of steel instead of big nails? Those clips are springs. On wooden sleepers, rails were traditionally held by spikes, like giant nails. But spikes slowly loosen as trains shake them. A spring clip presses down on the rail with a constant force, and if the rail moves or vibrates, the clip moves with it and keeps pushing.""",
     "Pandrol clip")
sc("""One of the most famous designs is the Pandrol clip, developed in the nineteen fifties from an idea by a Norwegian engineer, Per Pande-Rolfsen. The name combines parts of his name. It became one of the most widely used rail fastenings in the world. Workers can install and remove these clips quickly, which matters on a railway that has millions of them.""",
   "rail fastening clip", "MILLIONS OF SPRINGS")
sc("""Under the rail, there is often a thin rubber pad. It cushions the impact of the wheels, reduces vibration and noise, and protects the concrete sleeper. So a modern track is not just steel on concrete. It is steel, a spring, a cushion and concrete, each one absorbing a little of the hammering that every train delivers.""",
   "rail pad concrete sleeper", "A SPRING AND A CUSHION")

# ---------- 4. RAIL SHAPE ----------
part(4, "The rail's shape", "WHY IS A RAIL SHAPED LIKE THIS?", "Why Are Rails Shaped Like an Upside Down T?",
     """Why does a rail have that strange shape when you cut it? Look at the end of a rail. It has a rounded head on top, a thin vertical web in the middle, and a wide flat foot at the bottom. It is like a steel beam. The head is thick because the wheels wear it away. The tall web makes the rail very stiff, so it can bridge the gap between sleepers. And the wide foot sits flat and stable on the sleepers.""",
     "rail profile cross section")
sc("""This flat-bottom design was promoted in Britain by the engineer Charles Vignoles in the eighteen thirties, and something similar was developed in America by Robert Stevens around the same time. Earlier rails came in many shapes, and some broke easily. The flat-bottom rail won because it puts the steel exactly where it does the most work.""",
   "old railway rails", "STEEL WHERE IT WORKS")
sc("""Rails are measured by weight per length. A typical heavy main line rail today weighs around sixty kilograms per meter. Every meter of track has two of them. Rails are also made of special steel, hard enough to resist wear but tough enough not to crack. They do not last forever. On busy lines, the head slowly wears down, and rails are ground and eventually replaced.""",
   "rail grinding train", "60 KILOS PER METER")

# ---------- 5. TAMPING MACHINE ----------
part(5, "The tamping machine", "WHY DOES THIS MACHINE SHAKE THE ROCKS?", "Why Do Machines Shake the Rocks Under Railway Tracks?",
     """Why do giant yellow machines drive along tracks shaking the rocks? They are tampers. Over time, trains push the ballast around, and the track sinks a little more in some places than others. The tamper measures the track, lifts it to the correct height, and then drives vibrating steel fingers into the ballast on each side of a sleeper. They squeeze the stones together under the sleeper, so it stays at the new height.""",
     "tamping machine")
sc("""This is the big advantage of ballast. A track on stones can be adjusted. Raise it a little here, shift it a little there, then pack the stones tightly. A modern tamping machine uses lasers and computers, and it can work through hundreds of sleepers in an hour. The Austrian company Plasser and Theurer has been building these machines since the nineteen fifties.""",
   "Plasser tamping", "LASERS AND STONES")
sc("""After tamping, other machines shape the stone shoulder along the sides, and some even shake the whole track to settle it faster. Then the line can go back to full speed. To passengers, it is invisible. They only notice that the ride is smooth again. The comfort of your train trip depends on stones being squeezed every few years.""",
   "ballast regulator", "INVISIBLE COMFORT")

# ---------- 6. BALLAST CLEANER ----------
part(6, "The stone washing machine", "WHY DOES THIS MACHINE EAT THE ROCKS?", "Why Do Railways Dig Up and Wash Their Rocks?",
     """Why do some railway machines dig up all the stones under a track? Because ballast slowly dies. Every train crushes the stones a little. Sharp edges become round, small pieces become dust, and dirt from the ground and from trains fills the gaps. Railway engineers call this fouling. Fouled ballast cannot drain water, and it no longer locks the sleepers in place.""",
     "ballast cleaning machine")
sc("""A ballast cleaner digs the stones out from under the track with a moving chain, without removing the rails. It shakes them through screens, keeps the good stones, throws away the dust and small pieces, and puts the clean stones back, with fresh stone added. It is like a giant sieve rolling along the railway.""",
   "ballast cleaner chain", "A GIANT SIEVE")
sc("""If fouling is ignored, the result is something called mud pumping. Every time a train passes, the sleepers push down into wet mud, and the mud squirts up through the stones like toothpaste. You can sometimes see it as gray stains around the sleepers. That spot will keep sinking, so the speed must be reduced until the track is fixed.""",
   "railway track mud", "MUD PUMPING")

# ---------- 7. GUARD RAILS ----------
part(7, "The extra rails on bridges", "WHY DOES THIS BRIDGE HAVE EXTRA RAILS?", "Why Do Railway Bridges Have Extra Rails?",
     """Why do some railway bridges have extra rails inside the normal ones? They are guard rails. They do nothing when the train runs normally. But if a wheel derails on the bridge, the guard rail catches it and keeps the train running in a straight line along the track, instead of veering sideways and falling off the bridge or hitting the structure.""",
     "guard rail railway bridge")
sc("""The same idea is used in other risky places, like sharp curves and next to important structures. On switches, short check rails help guide the wheels through the gap where two rails cross. These extra rails are a backup for the moment something has already gone wrong. They turn a derailment into a controlled slide.""",
   "railway switch check rail", "A CONTROLLED SLIDE")
sc("""Railways also use the opposite idea. In some places, special devices called derails or catch points are designed to deliberately push a runaway wagon off the track, onto the ground, in a safe place, before it can roll onto a main line. Sometimes the safest thing for a train is to stay on the rails. Sometimes it is to leave them on purpose.""",
   "railway derail device", "LEAVE ON PURPOSE")

# ---------- 8. TRACK CIRCUIT ----------
part(8, "The box that counts axles", "WHY IS THIS BOX ON THE RAIL?", "Why Is There a Box Bolted to the Rail?",
     """Why are there small boxes bolted to the side of railway rails? Many of them are axle counters. Each one counts the wheels entering and leaving a section of track. If the same number goes out as came in, the section is empty and the signal can turn green. If not, it stays red. Signals do not see trains. They count them.""",
     "axle counter")
sc("""The older method is even more clever. In eighteen seventy-two, the American William Robinson created the closed track circuit. A small electric current runs through the rails. When a train enters, its steel wheels and axles connect the two rails and short the circuit, and the signal turns red. If a wire breaks or the power fails, the signal also turns red. The failure is safe.""",
   "railway signal red", "THE WHEELS CLOSE THE CIRCUIT")
sc("""That is also why railway workers sometimes carry a simple wire with two clips, called a track circuit operating clip. If there is a danger, clipping it across the two rails makes the signal behind think there is a train and turn red. A piece of wire, two clips, and the signal protects you. Simple systems save lives.""",
   "railway signal box", "TWO CLIPS, ONE RED LIGHT")

# ---------- 9. BALISE ----------
part(9, "The yellow box between the rails", "WHY IS THIS YELLOW BOX BETWEEN THE RAILS?", "Why Is There a Yellow Box Between the Rails?",
     """Why are there flat yellow boxes lying between the rails on many modern railways? They are balises, and they talk to trains. When a train passes over one, an antenna under the train sends energy down, and the balise wakes up and sends back data, like the exact location, the speed limit ahead, or the distance to the next signal. The balise has no battery. It is powered by the train itself.""",
     "Eurobalise")
sc("""In Europe, these are part of the European Train Control System, which is replacing dozens of different national systems. The computer on the train uses the information to calculate a safe speed, and if the driver goes too fast, the train brakes automatically. The train does not just obey signals. It knows the rules of the track ahead.""",
   "balise track", "THE TRAIN KNOWS THE RULES")
sc("""Balises also tell the train exactly where it is, which is surprisingly hard on a railway. Wheels slip and slide, so counting turns gives errors over long distances. A balise is a fixed point that resets the train's position. In a tunnel, without satellite signals, a simple yellow box on the ground can be the most reliable map in the world.""",
   "railway tunnel tracks", "A FIXED POINT")

# ---------- 10. HOT BOX DETECTOR ----------
part(10, "The heat detector", "WHY DOES THIS SENSOR WATCH WHEELS?", "Why Do Railways Measure the Temperature of Every Wheel?",
     """Why do some railways have sensors beside the track pointing at the wheels? They are hot box detectors. As a train passes, infrared sensors measure the temperature of every wheel bearing. A bearing that is failing gets very hot, and if nothing is done, it can seize, the axle can break, and the train can derail. The detector finds it minutes or hours before it fails.""",
     "hot box detector")
sc("""On many North American railways, these detectors talk to the crew by radio. After the train passes, a robotic voice announces the result, often something like no defects. If there is a problem, it tells the crew which axle, counted from the front, so they can stop and inspect it. Other detectors along the line check for dragging equipment, high loads, and flat spots on wheels.""",
   "freight train detector", "NO DEFECTS")
sc("""The name comes from the old days, when axles ran in boxes of grease or oil called journal boxes. If the lubrication failed, the box overheated, sometimes smoking or even catching fire. Railway workers called it a hot box. The technology changed, but the danger is the same. A tiny bearing can stop a train of ten thousand tons.""",
   "railway journal box", "THE HOT BOX")

# ---------- VERDICT ----------
sc("""So here are the ten. Sharp rocks that spread, lock and drain. Sleepers that hold the gauge, and spring clips that never let go. A rail shaped like a beam. A machine that squeezes the stones, and one that washes them. Extra rails on bridges, boxes that count axles, yellow boxes that talk to trains, and sensors that check every wheel for heat.""",
   "railway track perspective", "10 PARTS UNDER YOUR TRAIN", chapter="The verdict", cuts=6)
sc("""Next time you see rocks under a railway, you will know they are doing three jobs at once. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "train sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video46", "title": "Why Are There Rocks Under Railway Tracks?",
           "length_scale": 1.6, "scenes": S}, open("videos/video46/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
