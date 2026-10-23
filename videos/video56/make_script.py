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
sc("""Some of the tallest dams in the world are thinner than you would believe. A wall of concrete can hold back a lake billions of tonnes heavy, while being only a few meters thick at the top. The secret is the curve. Bend a dam the right way, and the water pushes it tighter against the mountains instead of knocking it over. Today, eleven parts of a dam, and why each one exists.""",
   "arch dam", "WHY IS IT CURVED?", cuts=8, chapter="Intro")
sc("""Dams hold back rivers for drinking water, farms, flood control and electricity. Behind each one sits a huge weight of water, pressing harder the deeper it gets. If a big dam fails, the flood downstream can be one of the deadliest disasters humans can cause. So every part of a dam exists for a reason.""",
   "Hoover Dam", "A LAKE ON YOUR SHOULDERS")
sc("""As always, every fact comes from a named source, dam operators, government agencies, and official investigation reports, all listed in the description. Let's start with the curve.""",
   "arch dam", "WHY DOES THIS EXIST?")

# ---------- 1. ARCH ----------
part(1, "The curve", "WHY IS THIS DAM CURVED?", "Why Are Dams Curved?",
     """Why are so many dams curved, with the bulge pointing toward the lake? Because the curve turns the push of the water into squeezing. A straight wall would be bent by the water like a ruler. An arch, curved upstream, sends that force sideways along the curve into the rock walls of the canyon. Concrete is very strong when squeezed, so the arch can be surprisingly thin.""",
     "arch dam")
sc("""It is the same idea as a stone arch in an old bridge or church. Push on the outside of an arch, and every block is pressed against its neighbors, holding the whole shape together. An arch dam is just an arch lying on its side, with the canyon walls as its supports.""",
   "arch dam", "AN ARCH ON ITS SIDE")
sc("""That is why arch dams are built in narrow canyons with strong rock, like the Contra Dam in Switzerland, two hundred and twenty meters tall, where James Bond made his famous bungee jump in GoldenEye. In a wide valley with weak rock, the arch would have nothing solid to push against.""",
   "Contra Dam", "THE BOND JUMP")

# ---------- 2. GRAVITY ----------
part(2, "The thick wall", "WHY IS THIS DAM SO THICK?", "Why Are Some Dams So Thick?",
     """Why are some dams straight and enormously thick instead of curved and thin? Because they use a different trick, weight. A gravity dam simply stands in the way of the water and is so heavy that the water cannot push it over or slide it along the ground. It is shaped like a triangle, thin at the top and very wide at the base, where the water pressure is greatest.""",
     "gravity dam")
sc("""Gravity dams work in wide valleys where an arch would not fit. China's Three Gorges Dam is one, more than two kilometers long and about one hundred and eighty meters tall, built with tens of millions of cubic meters of concrete. It is also the largest power station on Earth.""",
   "Three Gorges Dam", "TWO KILOMETERS LONG")
sc("""Many dams combine both ideas. Hoover Dam, on the Colorado River, is an arch gravity dam. It is curved, so part of the water's force goes into the canyon walls, and it is very thick, about two hundred meters at the base, so its weight holds the rest.""",
   "Hoover Dam", "BOTH AT ONCE")

# ---------- 3. COOLING PIPES ----------
part(3, "The pipes hidden in the concrete", "WHY ARE THERE PIPES INSIDE THIS DAM?", "Why Was Hoover Dam Built With Pipes Inside?",
     """Why is Hoover Dam full of pipes buried in its concrete? Because concrete gets hot as it hardens. The chemical reaction between cement and water releases heat. In a small slab, that heat escapes quickly. But engineers calculated that if Hoover Dam had been poured as one solid block, it would have taken more than a hundred years to cool down, and it would have cracked as it shrank.""",
     "Hoover Dam")
sc("""So the dam was built as many separate columns, poured in blocks, with about a thousand kilometers of steel pipes inside. River water and then chilled water from a refrigeration plant was pumped through the pipes, cooling the concrete in months instead of a century. Afterwards, the pipes were filled with grout.""",
   "Hoover Dam", "A THOUSAND KILOMETERS OF PIPE")
sc("""The same problem exists in every big concrete pour today. Large dams, bridge foundations and building cores are still cooled with pipes, ice in the mix, or poured in layers. Hidden inside, a dam is as much a cooling system as a wall.""",
   "concrete dam cooling pipes", "A WALL THAT HAD TO COOL")

# ---------- 4. SPILLWAY ----------
part(4, "The spillway", "WHY DOES THIS DAM HAVE A GIANT SLIDE?", "Why Do Dams Have a Giant Concrete Slide?",
     """Why does a dam have a huge concrete channel down its side, like a water slide? Because the most dangerous thing for a dam is water going over the top where it should not. In a big flood, the lake fills faster than the turbines can use it. The spillway lets the extra water out safely, around or over the dam, without washing away its foundations.""",
     "dam spillway")
sc("""For an earth dam, made of soil and rock, water flowing over the top is fatal. It erodes the dam from the top down within hours. So spillways are designed for floods far bigger than any recorded, sometimes the largest flood thought possible at that river.""",
   "dam spillway", "THE BIGGEST FLOOD POSSIBLE")
sc("""In February two thousand seventeen, the main spillway of California's Oroville Dam, the tallest dam in the United States, broke apart during heavy rains. Water then began flowing down the emergency spillway, which started eroding. Nearly two hundred thousand people were evacuated. The dam held, but the spillway had to be rebuilt.""",
   "Oroville Dam spillway", "OROVILLE, 2017")

# ---------- 5. AIR SLOTS ----------
part(5, "The air slots in the tunnel", "WHY DOES THIS SPILLWAY NEED AIR?", "Why Do Dam Spillways Need Air Holes?",
     """Why do some spillway tunnels have slots that suck air into the water? Because fast water can eat concrete. When water flows very fast over a small bump, the pressure drops so low that tiny bubbles of vapor form, and then collapse violently. This is called cavitation. Each collapse is a tiny hammer blow, and millions of them can tear holes in solid concrete.""",
     "Glen Canyon Dam spillway")
sc("""In nineteen eighty three, a huge snowmelt flood forced Glen Canyon Dam, in Arizona, to use its spillway tunnels for weeks. Cavitation tore out concrete, steel and even rock, and the tunnels shook and spat out debris. Workers even added plywood boards on top of the spillway gates to hold back a little more water.""",
   "Glen Canyon Dam", "GLEN CANYON, 1983")
sc("""After the flood, engineers added aeration slots. Air mixed into the water acts as a cushion, so the collapsing bubbles cannot hit the concrete so hard. It is an elegant fix. To protect the tunnel from water, you let air in.""",
   "dam spillway", "AIR AS A CUSHION")

# ---------- 6. INTAKE TOWERS ----------
part(6, "The towers in the lake", "WHY ARE THERE TOWERS IN THIS LAKE?", "Why Are There Towers Standing in Front of Hoover Dam?",
     """Why are there tall towers standing in the lake in front of Hoover Dam? They are intake towers. They let water into the dam's power plant, through gates at different heights. Taking water from the right depth matters. Water near the bottom may be colder and carry more silt, while water near the surface may be warmer.""",
     "Hoover Dam intake towers")
sc("""Hoover Dam has four of these towers, each one taller than a twenty five story building, with huge cylinder gates that can be opened or closed. Water flows from them through tunnels in the canyon walls to the turbines below. Screens on the towers stop logs and debris from going in.""",
   "Hoover Dam intake towers", "FOUR TOWERS")
sc("""Many dams have intake structures like these, but few are as beautiful. Hoover Dam was built in the nineteen thirties with art deco details, and even its clocks on the towers show two different times. One for Nevada and one for Arizona, the two states on either side of the dam.""",
   "Hoover Dam", "TWO TIME ZONES")

# ---------- 7. PENSTOCKS ----------
part(7, "The giant pipes", "WHY ARE THESE PIPES SO HUGE?", "Why Are Dam Pipes Big Enough to Drive Through?",
     """Why are the pipes that carry water to a dam's turbines so huge? They are called penstocks, and they have to carry enormous amounts of water under high pressure. At Hoover Dam, the main penstocks are about nine meters across, big enough to drive a truck through. The bigger the pipe, the slower the water flows for the same amount, and the less energy is lost to friction.""",
     "dam penstock")
sc("""The weight of the lake behind the dam is what makes the electricity. The deeper the turbines sit below the surface, the more pressure pushes the water through them. At the bottom, the water spins the turbines, which turn generators, and then flows out into the river below.""",
   "dam penstock", "THE WEIGHT MAKES POWER")
sc("""Closing a penstock gate suddenly would be dangerous. All that moving water would slam to a stop, creating a pressure shock called water hammer, strong enough to burst the pipe. So gates close slowly, and many plants have surge tanks that let the water rise and fall to absorb the shock.""",
   "dam penstock", "WATER HAMMER")

# ---------- 8. GALLERIES ----------
part(8, "The tunnels inside the dam", "WHY ARE THERE TUNNELS INSIDE THIS DAM?", "Why Are There Tunnels Inside a Dam?",
     """Why are there tunnels running through the inside of a concrete dam? They are inspection galleries. Engineers walk through them to check the dam from the inside. They measure cracks, temperature, movement, and especially water that seeps through the concrete and the rock below. A dam is not supposed to be perfectly watertight, but leaks must be watched.""",
     "dam inspection gallery")
sc("""Water seeping under a dam can push upward on it, like the dam is trying to float. This is called uplift, and it reduces the dam's grip on the ground. So drains are drilled from the galleries into the rock below, letting that water escape and lowering the pressure.""",
   "dam inspection gallery", "THE DAM TRIES TO FLOAT")
sc("""Inside many dams, there are also hanging wires called plumb lines, which show if the dam leans a few millimeters more in summer or under a full lake. Big dams bend a little with the water level and the temperature, and engineers have records of those movements going back decades.""",
   "concrete dam", "PLUMB LINES")

# ---------- 9. FISH LADDER ----------
part(9, "The fish ladder", "WHY DOES THIS DAM HAVE STAIRS FOR FISH?", "Why Do Some Dams Have Stairs for Fish?",
     """Why do some dams have a staircase of small pools beside them? It is a fish ladder. Salmon and other fish swim upstream to lay their eggs where they were born. A dam blocks their path completely. A fish ladder gives them a route of small steps, each one a pool, that they can jump or swim up, one level at a time.""",
     "fish ladder")
sc("""On the Columbia River, in the United States, big dams like Bonneville have fish ladders with windows where visitors can watch salmon pass and staff count them. Some dams even use fish elevators, or trucks, to carry fish over the wall.""",
   "fish ladder", "COUNTING SALMON")
sc("""Getting young fish back downstream is just as hard, because the turbines and spillways can hurt them. So modern dams use screens, bypass channels, and fish friendly turbines. A dam is not just a wall for water. It is a wall in the middle of an ecosystem.""",
   "fish ladder", "A WALL IN AN ECOSYSTEM")

# ---------- 10. VAJONT ----------
part(10, "The mountain that fell into the lake", "WHY DID THIS DAM SURVIVE BUT THE TOWN DIE?", "Why Did This Dam Survive but the Town Below Didn't?",
     """Why is the Vajont Dam in Italy still standing, even though nearly two thousand people died below it? Because the dam did not fail. In October nineteen sixty three, a huge landslide, more than two hundred and fifty million cubic meters of rock, slid from a mountain into the lake behind it. It pushed a wave of water over the top of the dam.""",
     "Vajont Dam")
sc("""The wave rose far above the dam and fell into the narrow valley below, destroying the town of Longarone and nearby villages in minutes. The dam, a thin arch, was barely damaged. Warning signs of the moving mountain had been seen for years, and the investigation found that the risk had been underestimated.""",
   "Vajont Dam", "LONGARONE, 1963")
sc("""Vajont changed dam engineering forever. Engineers now study the whole valley, not just the dam. The slopes around the lake, the geology, and how the rock behaves when the water rises and falls. The strongest dam in the world is useless if the mountain next to it is not stable.""",
   "Vajont Dam", "STUDY THE WHOLE VALLEY")

# ---------- 11. ITAIPU ----------
part(11, "The dam shared by two countries", "WHY IS THIS DAM SPLIT BETWEEN 2 COUNTRIES?", "Why Is This Giant Dam Split Between Two Countries?",
     """Why is the Itaipu Dam split exactly between Brazil and Paraguay? Because it sits on the Parana River, the border between them. The two countries built it together and own it fifty fifty. It has twenty generating units, half of them running on Brazil's electrical frequency and half on Paraguay's.""",
     "Itaipu Dam")
sc("""Brazil uses sixty hertz electricity and Paraguay uses fifty, so the two halves of the plant produce power at different frequencies. Paraguay uses only a part of its share and sells most of the rest to Brazil. For years, Itaipu produced more electricity in a single year than any other plant on Earth.""",
   "Itaipu Dam", "50 AND 60 HERTZ")
sc("""It shows that a dam is not only an engineering problem. It is a political one, a legal one, and a human one. Every curve, pipe and tunnel you have seen today exists because a whole country is downstream, trusting that the wall will hold.""",
   "Itaipu Dam", "A COUNTRY DOWNSTREAM")

# ---------- VERDICT ----------
sc("""So here are the eleven. A curve that squeezes instead of bends, and a thick wall that wins by weight. Pipes that cooled the concrete, a giant slide for floods, and air slots that stop the water eating the tunnels. Towers in the lake, pipes big enough to drive through, tunnels inside the dam, stairs for fish, a mountain that fell into the lake, and a dam shared by two countries.""",
   "arch dam", "11 PARTS. BILLIONS OF TONNES.", chapter="The verdict", cuts=6)
sc("""Next time you see a dam, look at its shape, and you will know which trick it uses to hold the water back. If you want more machines and structures explained part by part, subscribe to Machine Reverse. And tell us in the comments what you want us to take apart next.""",
   "Hoover Dam", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video56", "title": "Why Are Dams Curved?",
           "length_scale": 1.6, "scenes": S}, open("videos/video56/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
