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
sc("""A rally car can fly through the air for more than forty metres, land nose first on a gravel road, and keep going flat out to the next corner, as if nothing happened. Your road car would leave its wheels behind. The difference is not luck or magic. It is a list of parts built for the worst roads in the world. Today, ten parts of a rally car, and why each one exists.""",
   "rally car jump", "WHY DON'T THEY BREAK?", cuts=8, chapter="Intro")
sc("""Rally is motorsport on real roads. Gravel in Finland, snow in Sweden, mud in Kenya, tarmac in the Alps, often in the same season. The roads are closed for the stage, but they are not prepared like a race track. Rocks, ruts, crests and jumps are part of the course. And the cars race one at a time, against the clock, with a co-driver reading the road ahead.""",
   "rally car gravel", "REAL ROADS, FULL SPEED")
sc("""As always, every fact here comes from a named source, the FIA, the World Rally Championship and motorsport references, all listed in the description. Let's look under the car first.""",
   "rally car service park", "WHY DOES THIS EXIST?")

# ---------- 1. SUSPENSION ----------
part(1, "The long suspension", "WHY DOESN'T THIS CAR BREAK WHEN IT FLIES?", "Why Don't Rally Cars Break When They Fly?",
     """Why don't rally cars break when they land a jump? Because of the suspension. A gravel rally car has far more suspension travel than a road car, often more than twenty centimetres. When it lands, the wheels can move up a long way into the body before anything hits. The springs and dampers absorb the energy of a landing that would bend a normal car.""",
     "rally car suspension")
sc("""The dampers are the secret. They are big, adjustable units, often costing thousands of dollars each, with separate settings for slow movements, like the body rolling in a corner, and fast movements, like a wheel hitting a rock. Teams change the settings for every rally, and sometimes during the day. A rally car on gravel rides high, soft and long legged, almost like an off road truck.""",
   "rally car damper", "SOFT AND LONG LEGGED")
sc("""The same car on tarmac is a different machine. For asphalt rallies, the teams fit shorter, stiffer suspension, lower the car and fit wider wheels. Engineers can turn a gravel car into a tarmac car in the service park. The jumps in Finland are where the gravel setup earns its money. Some crests send the cars flying for more than forty metres.""",
   "Rally Finland jump", "FLYING IN FINLAND")

# ---------- 2. ROLL CAGE ----------
part(2, "The roll cage", "WHY IS THE INSIDE FULL OF PIPES?", "Why Are Rally Cars Full of Metal Pipes Inside?",
     """Why is the inside of a rally car full of metal pipes? This is the roll cage, steel tubes welded to the body, running around the doors, over the heads of the crew and down to the floor. When a rally car rolls over, and many do, the cage keeps the roof from collapsing onto the driver and co-driver. It also makes the whole body much stiffer.""",
     "rally car roll cage")
sc("""The cage is built to strict FIA rules. The tubes have minimum sizes and thicknesses, and the design is tested and approved. In modern cars, there are extra bars inside the doors, because side impacts against trees are one of the most dangerous accidents in rally. A road car is designed to crumple and absorb a crash. A rally car is designed to survive many crashes in a single season.""",
   "rally car crash roll", "BUILT TO ROLL")
sc("""Safety in rally changed forever in nineteen eighty-six. That year, Henri Toivonen and his co-driver Sergio Cresto died when their Lancia Delta S four left the road in Corsica and caught fire. The extreme Group B cars were banned at the end of that season. Since then, cages, fuel tanks and seats have become stronger with every new set of rules.""",
   "Lancia Delta S4", "THE END OF GROUP B")

# ---------- 3. SUMP GUARD ----------
part(3, "The underbody shield", "WHY IS THERE ARMOUR UNDER THIS CAR?", "Why Do Rally Cars Have Armour Underneath?",
     """Why do rally cars have a metal plate underneath? It is the sump guard, also called the skid plate. A thick plate of aluminium or composite covers the engine, the gearbox and the important pipes under the car. On a gravel road, a rally car hits rocks, ruts and the ground itself after jumps. Without the guard, one rock could punch a hole in the engine.""",
     "rally car underbody protection")
sc("""The plate is designed to slide. When the car lands hard or scrapes over a crest, the guard takes the hit and lets the car glide over the obstacle instead of catching on it. After each stage, mechanics often find deep scratches in the plate, and sometimes they replace it completely in the service park. It is the part that sacrifices itself so the engine does not have to.""",
   "rally car service park mechanics", "IT SACRIFICES ITSELF")
sc("""Even the fuel tank is protected. In a modern rally car, the fuel sits in a safety cell, a flexible bag inside a strong box, placed where it is least likely to be hit. Fire was the great danger in the past. Today the most important parts of the car are hidden behind layers of armour, from the floor to the roof.""",
   "rally car fuel tank", "ARMOUR EVERYWHERE")

# ---------- 4. MUD FLAPS ----------
part(4, "The mud flaps", "WHY DO RALLY CARS HAVE THESE FLAPS?", "Why Do Rally Cars Have Big Mud Flaps?",
     """Why do rally cars have big flaps behind the wheels? Because spinning tyres on gravel throw stones like a machine gun. A rally car accelerating on a loose surface fires rocks backwards at high speed. The mud flaps catch them. The rules require them on gravel, to protect the car's own body, and everyone standing near the road.""",
     "rally car mud flaps")
sc("""Rally fans often stand very close to the stages, and the cars pass at full speed. A stone thrown from a wheel can be dangerous. The flaps are thick, flexible and long enough to stop most of the gravel. They also stop the car from blasting its own rear bodywork and windows with stones, which would break parts of the car during a stage.""",
   "rally car gravel spray", "A MACHINE GUN OF STONES")
sc("""The flaps are also a canvas. Teams put sponsor names and the car's number on them, because they are big flat surfaces right at the height of the cameras. On a muddy rally, they are often the only part of the car you can still read. A strip of rubber with two jobs, safety first and advertising second.""",
   "rally car mud", "SAFETY, THEN ADVERTISING")

# ---------- 5. LIGHT POD ----------
part(5, "The light pod", "WHY DOES THIS CAR HAVE EXTRA LIGHTS?", "Why Do Rally Cars Have Giant Lights on the Front?",
     """Why do some rally cars have a giant set of lights on the bonnet? Because some stages are run at night, on narrow roads in forests or mountains, with no street lights. A normal car's headlights are not enough at more than one hundred fifty kilometres per hour. The light pod carries several powerful lamps, aimed at different angles, to light the road far ahead and the edges of the corners.""",
     "rally car night lights")
sc("""Each lamp has a job. Some throw a long, narrow beam to see far down a straight. Others are wide, to light the inside of the corner the car is turning into. The pod is bolted onto the front for night stages and removed for day stages, to save weight and air resistance. Modern pods use LEDs, which are lighter and brighter than the old lamps.""",
   "rally car light pod", "EACH LAMP HAS A JOB")
sc("""Night stages are some of the most dramatic in rally. At the Monte Carlo rally, crews may face snow and ice in the mountains, in the dark. Fans line the roads with torches and campfires. The drivers say the hardest part is not seeing far enough. The light pod is their only way to see the next corner before they reach it.""",
   "Rallye Monte Carlo night", "SEE THE NEXT CORNER")

# ---------- 6. ROOF SCOOP ----------
part(6, "The roof scoop", "WHY IS THERE A SCOOP ON THE ROOF?", "Why Is There an Air Scoop on a Rally Car's Roof?",
     """Why is there an air scoop on the roof of a rally car? To keep the crew from cooking. The windows of a rally car stay closed on the stages, because open windows let in dust, stones and branches. The engine, the gearbox and the exhaust are all close to the cabin, and on a hot rally the temperature inside can be extremely high. The scoop forces fresh air into the cabin.""",
     "rally car roof scoop")
sc("""The roof is the best place for it. The air there is clean and fast, away from the dust thrown up by the wheels. The scoop pushes the air down through a vent into the cockpit, where it blows over the driver and co-driver. In rallies like Mexico, Kenya or Greece, where the heat is intense, that flow of air helps them stay focused through long stages.""",
   "rally car roof vent", "CLEAN AIR FROM ABOVE")
sc("""A tired, overheated driver makes mistakes, and on a rally road a mistake can mean a tree. So the cooling of the crew is treated almost as seriously as the cooling of the engine. A small scoop on the roof is there to cool the most important part of the car, the people inside.""",
   "rally crew helmets cockpit", "COOL THE HUMANS")

# ---------- 7. HANDBRAKE ----------
part(7, "The tall handbrake", "WHY IS THIS HANDBRAKE SO TALL?", "Why Do Rally Cars Have a Giant Handbrake?",
     """Why do rally cars have a tall handbrake lever next to the driver? It is a hydraulic handbrake, used to turn the car, not to park it. In a tight hairpin, the driver pulls the lever, the rear wheels lock for an instant, and the back of the car swings around. The car rotates much faster than it would by steering alone.""",
     "rally car hydraulic handbrake")
sc("""The lever is tall so the driver can grab it quickly, without looking, while the other hand stays on the wheel. In a four wheel drive rally car, pulling it also disconnects the drive to the rear wheels for a moment, so they can lock without fighting the engine. Let go, and the drive comes back as the car points to the exit.""",
   "rally car hairpin", "ROTATE, THEN GO")
sc("""Drivers use it differently. Some use it in many corners, some only in the tightest hairpins. On the narrowest mountain roads, it can be the only way to turn the car without stopping and reversing. A parking brake on your car holds you still. On a rally car, the same idea is used to make the car dance.""",
   "rally car drifting", "MAKE THE CAR DANCE")

# ---------- 8. ANTI-LAG ----------
part(8, "The anti-lag system", "WHY DOES THIS CAR BANG AND POP?", "Why Do Rally Cars Bang and Shoot Flames?",
     """Why do rally cars bang, pop and shoot flames from the exhaust? It is the anti-lag system. A turbo engine has a delay. When the driver lifts off the throttle, the turbo slows down, and when he accelerates again, it takes a moment to spin back up. On a twisty rally road, with constant braking and accelerating, that delay would cost a lot of time.""",
     "rally car exhaust flames")
sc("""Anti-lag keeps the turbo spinning even when the driver is off the throttle. The engine lets a little air through and adds fuel late, so it burns in the exhaust before the turbo. The explosions keep the turbo turning at high speed. When the driver touches the throttle again, the boost is there immediately. The bangs you hear in the forest are those explosions.""",
   "rally car turbo", "EXPLOSIONS ON PURPOSE")
sc("""It is brutal for the hardware. The exhaust and the turbo get extremely hot, and parts wear much faster than in a road car. That is why anti-lag is turned off on the road sections between stages, where rally cars drive in normal traffic. It is a system built for a few minutes of total attack, not for a long life.""",
   "rally car road section", "OFF BETWEEN STAGES")

# ---------- 9. STUDDED TYRES ----------
part(9, "The studded tyres", "WHY DO THESE TYRES HAVE SPIKES?", "Why Do Rally Tyres Have Metal Spikes?",
     """Why do rally tyres have metal spikes? These are the studded tyres used on snow and ice, especially at Rally Sweden. Hundreds of small metal studs stick out of each tyre. On ice, a normal tyre has almost no grip. The studs dig into the ice like the claws of an animal, giving the car grip in places where you could barely stand.""",
     "rally studded tyre")
sc("""With studs, rally cars race on frozen roads at speeds above one hundred eighty kilometres per hour. In Sweden, the roads are lined with snow banks, and drivers lean the car against them in corners, using the snow as a wall. The studs wear down during a stage, and the tyre rules limit how many studs each tyre can have and how far they may stick out.""",
   "Rally Sweden snow", "CLAWS IN THE ICE")
sc("""Tyres are the only contact between the car and the road, so rally teams carry different tyres for every surface. Soft and hard compounds for gravel, slicks and grooved tyres for tarmac, narrow tyres for snow, and studs for ice. On a mixed rally, choosing the wrong tyre in the morning can decide the whole day.""",
   "rally tyres service park", "THE WRONG TYRE COSTS THE DAY")

# ---------- 10. PACE NOTES ----------
part(10, "The pace notes", "WHY IS THE PASSENGER READING A BOOK?", "Why Does the Rally Co-Driver Read a Notebook?",
     """Why is the passenger in a rally car reading a notebook at full speed? These are the pace notes, and the passenger is the co-driver. Before the rally, the crew drives each stage slowly, writing a description of every corner, crest and jump. During the stage, the co-driver reads the notes out loud, a few seconds ahead, so the driver knows what is coming before he can see it.""",
     "rally co-driver pace notes")
sc("""The notes are written in a code. Many crews use numbers for how tight each corner is, along with words like crest, don't cut, or over jump, and the distance to the next instruction. A sentence like six left, into four right, don't cut, describes a corner sequence in two seconds. The driver trusts the voice so completely that he drives flat out over crests he cannot see beyond.""",
   "rally car crest", "TRUST THE VOICE")
sc("""A mistake in the notes or in the timing of the reading can put the car off the road. That is why the co-driver is as important as the driver, and why crews often stay together for years. The fastest part of a rally car is not the engine or the suspension. It is the conversation inside the cockpit.""",
   "rally driver co-driver", "THE FASTEST PART")

# ---------- VERDICT ----------
sc("""So here are the ten. Long suspension that swallows jumps. A roll cage for when the car rolls. Armour under the car, flaps for the stones, lights for the night and a scoop on the roof for the crew. A handbrake to turn, an anti-lag system that bangs, spikes for the ice, and a notebook that lets the driver see around corners.""",
   "World Rally Championship car", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A rally car looks like a normal car with stickers. Underneath, almost every part has been rebuilt to survive the roughest roads on Earth. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "rally car forest", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video25", "title": "Why Don't Rally Cars Break When They Fly?",
           "length_scale": 1.6, "scenes": S}, open("videos/video25/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
