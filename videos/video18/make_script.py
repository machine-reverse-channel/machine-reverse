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
sc("""For sixty years, rockets were thrown away after one flight. Then one day a booster came back down from space, slowed itself with its own engine, and landed upright on a pad, on its tail, like a rocket in an old science fiction movie. The first time it worked was in December two thousand fifteen. A rocket that lands itself is covered in strange parts, and every one has a reason. Today, ten parts of a landing rocket, and why each one exists.""",
   "Falcon 9 booster landing", "WHY DOES IT LAND ON ITS TAIL?", cuts=8, chapter="Intro")
sc("""The Falcon nine first stage is about forty-one meters tall, and its nine engines push with about seven thousand six hundred kilonewtons. It has to fly to the edge of space, turn around, fall back through the atmosphere, and touch down on a pad. Nothing on it is there by accident.""",
   "Falcon 9 first stage", "41 METERS ON A TARGET")
sc("""As always, every fact here comes from a named source, reference works and company information, all listed in the description. Let's start with the part that looks like a waffle iron.""",
   "Falcon 9 grid fins", "WHY DOES THIS EXIST?")

# ---------- 1. GRID FINS ----------
part(1, "The grid fins", "WHY DOES THIS ROCKET HAVE WAFFLE IRONS ON TOP?", "Why Does a Falcon 9 Have Waffle-Shaped Fins?",
     """Why does the booster have fins that look like waffle irons? They are grid fins, and they steer the booster as it falls through the air. They fold against the body during launch, and deploy moments after stage separation. A rocket falling tail first has no wings, so the fins are its only way to guide itself to the landing spot.""",
     "Falcon 9 grid fins")
sc("""A grid fin folds flat against the body, which saves space during the climb. And on the way down, the heat is intense. The newer fins are cast and cut from a single piece of titanium, in place of the earlier aluminum ones, so they survive the heat of reentry and can be reused almost indefinitely.""",
   "grid fin titanium Falcon 9", "ONE PIECE OF TITANIUM")
sc("""So the strangest-looking part of the booster is also one of the most important. Without the fins, a falling rocket would tumble, and no engine in the world could aim it at a landing pad.""",
   "Falcon 9 booster descent", "NO FINS, NO LANDING")

# ---------- 2. LANDING LEGS ----------
part(2, "The landing legs", "WHY DOES A ROCKET HAVE LEGS?", "Why Does a Falcon 9 Have Folding Legs?",
     """Why does a rocket have legs? Because it lands on them. A recoverable Falcon nine has four landing legs, made of carbon fiber and aluminum honeycomb, folded against the base during flight and extended just before touchdown. Boosters that are meant to be thrown away have no legs and no fins, because they would only add weight.""",
     "Falcon 9 landing legs")
sc("""The legs have to be light, since every kilogram on the booster is a kilogram that can't be carried to orbit. But they also have to be strong enough to absorb the final contact of a very tall, nearly empty rocket. The honeycomb design is a way to get both.""",
   "Falcon 9 landing legs deployed", "LIGHT, BUT STRONG")
sc("""There is a kind of beauty in them. A part that spends the whole flight folded away and unused, and is needed for the last two seconds. If it fails, the whole mission is lost, even if everything else went right.""",
   "Falcon 9 landing touchdown", "NEEDED FOR TWO SECONDS")

# ---------- 3. COLD GAS THRUSTERS ----------
part(3, "The nitrogen thrusters", "WHY DOES THE ROCKET HAVE TINY GAS JETS?", "Why Does the Falcon 9 Have Tiny Nitrogen Thrusters?",
     """Why does the rocket have tiny gas jets, when it has such big engines? The big engines are off while the booster coasts through the thin air at the edge of space, and it still needs to point the right way. So the booster uses nitrogen gas thrusters, small puffs of cold gas, together with the grid fins, to control its position as it coasts and falls. They also control the roll during the climb.""",
     "Falcon 9 cold gas thrusters")
sc("""There is a famous test of their limits. On the sixth Falcon nine flight, the thrusters could not overcome a spin caused by the airflow, during the final landing burn. The engine shut down early, and the booster hit the water hard. It was a lesson, and later boosters were better.""",
   "Falcon 9 booster spin splashdown", "THE LIMITS OF A PUFF OF GAS")
sc("""It is a good reminder that control is not only power. A big engine moves a rocket, but it is the small nozzles that point it in the right direction.""",
   "Falcon 9 attitude control", "SMALL JETS, BIG CONTROL")

# ---------- 4. OCTAWEB ----------
part(4, "The nine engines", "WHY DOES THE BOTTOM HAVE NINE ENGINES?", "Why Does the Falcon 9 Have Nine Engines?",
     """Why does the booster have nine engines on the bottom? They are Merlin engines, each making about eight hundred fifty-four kilonewtons, arranged in an octagonal pattern that the company calls Octaweb, with one in the middle. Together, they make about seven thousand six hundred kilonewtons at sea level. The arrangement is meant to simplify and streamline building the rocket.""",
     "Falcon 9 Octaweb engines")
sc("""Nine small engines give something better than one huge one. The rocket can lose up to two engines during the climb and still complete the mission, by burning the others a bit longer. That kind of backup was not possible with a single engine.""",
   "Falcon 9 engines firing", "LOSE TWO AND KEEP GOING")
sc("""The Merlin engine can also swivel its thrust, which is how the rocket steers during the climb. The same machine that lifts a satellite is the one that sets itself down.""",
   "Falcon 9 landing burn", "THE SAME ENGINES LAND IT")

# ---------- 5. FIRST LANDING ----------
part(5, "The first landing", "WHY WAS THIS LANDING SUCH A BIG DEAL?", "Why Was the First Rocket Landing So Important?",
     """Why was the first rocket landing such a big deal? Because nobody had ever landed an orbital-class booster upright before. It happened in December two thousand fifteen, on the Orbcomm mission, when a Falcon nine came back and landed on a pad on the ground. Until then, a rocket was a machine that was thrown away, and the most expensive part of a launch was lost every time.""",
     "Falcon 9 first landing Landing Zone 1")
sc("""The booster is one of the biggest and most expensive parts of the rocket. If it can be flown again, the price of each launch falls. Landing it was the first step, and every flight after that was a step toward turning a rocket into something more like an aircraft.""",
   "Falcon 9 landing zone", "THROWING AWAY A JET EVERY FLIGHT")
sc("""And the feat looks even stranger on a calm day. A tall white tube comes down out of the sky on a pillar of flame, slows to a stop, and stands still on four legs. It is a sight that still stops people in their tracks.""",
   "Falcon 9 booster touchdown", "A PILLAR OF FLAME")

# ---------- 6. DRONE SHIP ----------
part(6, "The drone ship", "WHY IS THERE A SHIP WITH NO CREW?", "Why Do Rockets Land on a Ship in the Ocean?",
     """Why does a rocket land on a ship in the ocean? Because some missions fly too far to come back to land. The first drone ship landing was in April two thousand sixteen, on the ship called Of Course I Still Love You, after the CRS-8 mission. A rocket that carries a heavy satellite to a high orbit has no fuel left to fly back to the coast, so the ship waits for it at sea.""",
     "Of Course I Still Love You drone ship Falcon 9")
sc("""The ship has no crew while the rocket lands. It is a big flat platform that holds its position in the sea with thrusters. The booster aims at the center, and the landing is a precise act, on a deck that moves with the waves.""",
   "SpaceX drone ship landing", "A PLATFORM THAT HOLDS STILL")
sc("""So the ocean became part of the launch pad. A rocket launches from the coast, flies across the sea, and lands on a ship that is waiting in the middle of nowhere.""",
   "drone ship at sea Falcon 9", "THE SEA IS THE LAUNCH PAD")

# ---------- 7. REUSE ----------
part(7, "The reused booster", "WHY CAN THIS ROCKET FLY AGAIN?", "Why Can a Rocket Fly More Than Once?",
     """Why is a rocket that flies twice such a big change? The first booster to be flown again was B1021, which first flew in April two thousand sixteen, and flew again in March two thousand seventeen. Both flights ended in a landing. After that, it was retired and put on display. A rocket that is flown again, and not rebuilt, was a new thing.""",
     "Falcon 9 B1021 reused booster")
sc("""Since then, the numbers have grown. One booster has now flown thirty-five times, as of June two thousand twenty-six. Each flight is cheaper than building a new rocket, and the savings change what can be launched, and how often.""",
   "Falcon 9 booster flight record", "35 FLIGHTS ON ONE BOOSTER")
sc("""This is the real revolution. Not the landing, but what comes after it. A rocket that can be reused is a machine that can be improved, tested and trusted, like an airplane.""",
   "Falcon 9 booster reuse", "FROM LANDING TO ROUTINE")

# ---------- 8. SECOND STAGE ----------
part(8, "The expendable second stage", "WHY DOESN'T THE UPPER STAGE LAND TOO?", "Why Doesn't the Falcon 9's Upper Stage Land Too?",
     """Why does only the first stage come back? Because the second stage is going much faster. It carries the satellite all the way to orbit, and to come back it would need a heat shield, landing engines and other equipment. SpaceX concluded that the mass of that equipment was prohibitive, so the second stage is still thrown away.""",
     "Falcon 9 second stage")
sc("""Every kilogram on the second stage is a kilogram less for the satellite. Adding a heat shield and engines for the landing would take a big share of what the rocket can carry. So it is a trade, and the company chose to save the first stage, where the savings are largest.""",
   "Falcon 9 stage separation", "EVERY KILO COMES OUT OF THE PAYLOAD")
sc("""It shows that reuse is not all or nothing. The best machine is the one that saves the most money for the least added weight, and that is the first stage.""",
   "Falcon 9 upper stage", "SAVE THE EXPENSIVE PART")

# ---------- 9. FAIRING ----------
part(9, "The recovered nose cone", "WHY DOES THE ROCKET'S NOSE COME BACK TOO?", "Why Does the Falcon 9's Nose Cone Come Back Too?",
     """Why is the nose cone recovered too? It is called the fairing, the two-part shell that protects the satellite during the climb. After the fairing is released, it falls back and re-enters the atmosphere, and since twenty nineteen, these halves have been recovered and reused. It is another expensive part that does not need to be thrown away.""",
     "Falcon 9 fairing recovery")
sc("""The fairing is built to protect something delicate, so it is made of light, strong material, and it is not cheap. Bringing it back, and using it again, saves money in the same way as the booster, one part at a time.""",
   "Falcon 9 fairing halves", "SAVE EVERY EXPENSIVE PIECE")
sc("""So the whole idea is simple. Wherever the rocket has something valuable that falls back to Earth, find a way to catch it and fly it again.""",
   "Falcon 9 fairing ship", "CATCH WHAT FALLS")

# ---------- VERDICT ----------
sc("""So here are the nine. Waffle-shaped fins that steer a falling rocket, legs that unfold for two seconds, gas jets for small turns, and nine engines that can lose two. A first landing that changed everything, a ship waiting at sea, a booster that flew again, an upper stage that still gets thrown away, and a nose cone that returns.""",
   "Falcon 9 landing sunrise", "9 PARTS. 9 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see a rocket land on its tail, you will know what each part is doing. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Falcon 9 landing night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video18", "title": "Why Do Rockets Land on Their Tails Now?",
           "length_scale": 1.6, "scenes": S}, open("videos/video18/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
