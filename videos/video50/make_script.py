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
sc("""Stand next to the wheel of a Caterpillar seven nine seven and you will not reach the top of the tire. You will not even reach the middle. Each tire is about four meters tall and weighs around five tonnes, as much as two family cars. The truck carries more than three hundred and sixty tonnes of rock in one trip. Today, eleven parts of a giant mining truck, and why each one exists.""",
   "Caterpillar 797", "TALLER THAN A PERSON", cuts=8, chapter="Intro")
sc("""These trucks never drive on public roads. They live inside open pit mines, climbing out of holes hundreds of meters deep, all day and all night, loaded to the limit. A mine can run a fleet of dozens of them, and every minute one stands still costs money. So every part on them exists for a reason.""",
   "open pit mine haul truck", "THEY NEVER STOP")
sc("""As always, every fact comes from a named source, manufacturers, mining safety agencies, and engineering references, all listed in the description. Let's start with the part that gives this video its name, the tire.""",
   "mining truck tire", "WHY DOES THIS EXIST?")

# ---------- 1. TIRE ----------
part(1, "The tire taller than a person", "WHY IS THIS TIRE TALLER THAN A PERSON?", "Why Are Mining Truck Tires Taller Than a Person?",
     """Why is this tire taller than the man standing next to the truck? Because the tire is what carries the load to the ground, and the ground in a mine is soft, broken rock. A Caterpillar seven nine seven, loaded, weighs more than six hundred tonnes. Spread that over six tires, and each one carries around a hundred tonnes. A small tire would sink into the haul road, cut itself on rock, and overheat. A big tire spreads the weight over a bigger patch of ground.""",
     "Caterpillar 797")
sc("""The tire size used on the biggest trucks is called fifty nine eighty R sixty three. The last number means the rim is sixty three inches across, about one point six meters. Just the rim is taller than many people. Around it sits a rubber casing with steel cords inside, built in layers, so it can bend over rocks thousands of times a day without tearing apart.""",
   "haul truck tire", "THE RIM ALONE: 1.6 M")
sc("""Only a few companies in the world can make these tires, among them Michelin, Bridgestone and Goodyear. Each one takes days to build and cure, and costs tens of thousands of dollars. In the mid two thousands, when mining boomed, the world ran short of giant tires, and some mines had to park trucks because they had nothing to put under them.""",
   "mining truck tire", "THE GREAT TIRE SHORTAGE")

# ---------- 2. NITROGEN ----------
part(2, "The tire filled with nitrogen", "WHY ARE THESE TIRES FILLED WITH NITROGEN?", "Why Are Mining Truck Tires Filled With Nitrogen?",
     """Why do many mines fill these tires with nitrogen instead of air? Because a giant tire can explode. If the tire gets very hot, from a brake fire, a lightning strike, or someone welding on the rim, the rubber inside can start to break down into flammable gases. Mixed with the oxygen in normal air, those gases can ignite inside the tire. Nitrogen has no oxygen to feed that reaction.""",
     "haul truck tire")
sc("""These explosions are not small. Mining safety agencies in the United States and Australia have warned that an overheated giant tire can burst with enough force to throw the rim and pieces of the truck dozens of meters, and to kill people nearby. That is why, when a tire is overheated, the rule is to clear the area and keep people far away for many hours, sometimes a full day.""",
   "Mont Wright Mine haul truck", "KEEP AWAY FOR 24 HOURS")
sc("""Nitrogen also helps the tire itself. With less oxygen inside, the rubber and steel cords age more slowly, and the pressure stays more stable as the tire heats up and cools down. For a tire that costs as much as a car, every extra hour of life matters. It is a simple gas doing a very serious job.""",
   "mining truck tire", "NO OXYGEN, NO FIRE")

# ---------- 3. HEAT LIMIT ----------
part(3, "The tire's speed limit", "WHY DO THESE TIRES HAVE A SPEED LIMIT?", "Why Can't Mining Trucks Drive Faster?",
     """Why can't a mining truck simply drive faster to move more rock? Because the tire would cook itself. Every time a loaded tire rolls, the rubber squeezes and relaxes, and that bending turns into heat. Rubber is a poor conductor, so the heat stays inside. Drive too fast, or too far without a break, and the inside of the tire gets hot enough to separate the layers and destroy it.""",
     "Tire Transport Truck")
sc("""Tire makers give every tire a heat rating, measured in tonne kilometers per hour. Mines calculate it for each road. How heavy is the load, how far is the trip, how fast does the truck go, and how hot is the weather. If the number is too high, the mine slows the trucks down, shortens the route, or buys tougher rubber.""",
   "haul truck tire", "TONNE-KILOMETERS PER HOUR")
sc("""That is why a truck with a four thousand horsepower engine usually tops out at around sixty kilometers an hour. The limit is not the engine. It is the rubber. And moving a single new tire to the mine is a job of its own, often on a special trailer as an oversize load.""",
   "Big, big tires", "THE LIMIT IS THE RUBBER")

# ---------- 4. STAIRS ----------
part(4, "The staircase on the front", "WHY DOES THIS TRUCK HAVE A STAIRCASE?", "Why Do Mining Trucks Have a Staircase on the Front?",
     """Why does this truck have a staircase built across its front? Because the driver sits about as high as the second floor of a house. A normal ladder would be steep and dangerous, especially at night, in rain or snow, in heavy boots. So the big trucks have a diagonal stairway with handrails, climbing across the front of the radiator to a walkway that leads to the cab.""",
     "Caterpillar 797")
sc("""Falls are one of the most common injuries around heavy equipment. A person climbing down backward, missing a step, can fall several meters onto rock. Stairs let people face forward, with three points of contact, and some trucks even have a powered ladder that lowers itself to the ground and lifts up when the truck moves.""",
   "Giant Mining Truck", "FACE FORWARD, HOLD ON")
sc("""Most trucks also have a rule. The driver must not move the truck until the stairs or ladder are up, and lights or alarms in the cab warn if they are not. On a machine this size, even getting in and out is engineered.""",
   "mining truck cab", "EVEN GETTING IN IS ENGINEERED")

# ---------- 5. CANOPY ----------
part(5, "The roof over the cab", "WHY DOES THE DUMP BODY COVER THE CAB?", "Why Does a Mining Truck's Body Cover the Driver?",
     """Why does the dump body stretch forward over the driver's cab like a roof? Because the truck is loaded by a shovel that drops dozens of tonnes of rock from above, a few bucketfuls at a time. The operator aims for the middle of the body, but rocks bounce and spill. A rock the size of a fridge falling onto an unprotected cab could crush it. The canopy takes the hit instead.""",
     "Komatsu 930E")
sc("""This extension is called the canopy, and it is part of the steel dump body. It also protects the engine, the radiator and the cooling fans at the front. On many trucks, the cab itself has a rollover protective structure, a steel cage tested to survive if the truck tips over.""",
   "mining dump truck body", "A STEEL ROOF")
sc("""The dump body is a wear part too. Rock sliding out of it scrapes the steel like sandpaper, so the floor is made of hard, wear resistant plate, and some mines add liners of rubber or steel that can be replaced. A body can weigh more than thirty tonnes empty, and it still needs repairs.""",
   "haul truck dump body", "STEEL LIKE SANDPAPER")

# ---------- 6. WHEEL MOTORS ----------
part(6, "The electric motors in the wheels", "WHY ARE THERE ELECTRIC MOTORS IN THESE WHEELS?", "Why Do Some Mining Trucks Have Electric Wheels?",
     """Why does this diesel truck have electric motors inside its rear wheels? Because a normal gearbox has a hard time handling this much power and weight. On a diesel electric truck like the Komatsu nine thirty E, the diesel engine does not turn the wheels. It turns a generator. The electricity goes through cables to motors inside the rear wheel hubs, with gears that multiply the force.""",
     "Komatsu 930E")
sc("""There is no clutch and no gear shift. The motors give strong, smooth force even at a crawl, which is exactly what a loaded truck needs when it climbs a steep ramp out of a pit. The idea is old. In the nineteen sixties, a company called Unit Rig built the Lectra Haul, one of the first big diesel electric mining trucks.""",
   "Lectra Haul", "NO GEARBOX")
sc("""Electric drive also helps the brakes. Going downhill, the motors work in reverse, as generators. They slow the truck and turn its energy into heat in big resistor grids, so the normal brakes stay cool. And some mines now go further. They put overhead power lines on the uphill ramps, and the trucks raise a pantograph like a tram, to climb on electricity from the grid.""",
   "Komatsu 930E", "MOTORS THAT BRAKE")

# ---------- 7. RADIATOR ----------
part(7, "The giant radiator", "WHY IS THIS RADIATOR SO BIG?", "Why Do Mining Trucks Have Such Huge Grilles?",
     """Why does the front of a mining truck look like a giant wall of grille? Because behind it is a radiator the size of a garage door. The engine in a Caterpillar seven nine seven F has twenty cylinders and a displacement of about one hundred and six liters, roughly fifty times a family car's. It makes around four thousand horsepower, and a lot of that energy comes out as heat, not motion.""",
     "Komatsu HD605")
sc("""In a mine, that heat has nowhere easy to go. Trucks work in deserts at more than forty degrees, climb ramps fully loaded at low speed, and run around the clock. A huge fan pulls air through the radiator, and the whole front of the truck is shaped around feeding that fan with cool air.""",
   "haul truck engine", "40 DEGREES, 24 HOURS")
sc("""Dust is the other enemy. The air is full of fine rock powder that clogs radiators and wears engines from the inside. So the trucks use large air filters, sometimes with pre-cleaners that spin the dust out before the air reaches the filter. Breathing is hard work for a machine this size.""",
   "mining truck", "DUST IS THE ENEMY")

# ---------- 8. AUTONOMOUS ----------
part(8, "The sensors on the mast", "WHY DOES THIS TRUCK HAVE NO DRIVER?", "Why Do Some Mining Trucks Drive Themselves?",
     """Why does this truck have sensors and antennas on a mast above the cab? Because some mining trucks drive themselves. The mast carries GPS antennas, radios and obstacle sensors. A control room tells each truck where to go, the truck follows a precise path on the haul road, and it stops if something gets in its way.""",
     "autonomous haul truck")
sc("""Autonomous haulage started in real mines around two thousand eight, in Chile and in the iron ore mines of Western Australia. Today, systems from Komatsu, Caterpillar and others run hundreds of driverless trucks. They can work every hour of the day, without breaks or shift changes, and the mines report fewer accidents and lower costs.""",
   "Pilbara iron ore mine", "NO BREAKS, NO SHIFTS")
sc("""Driverless does not mean nobody is in charge. People in the control room plan routes and watch every truck. And the trucks are fenced off from people. Anyone who enters the autonomous zone has to be tracked by the system, so the trucks know where they are. The robot still needs humans. They just sit somewhere else.""",
   "open pit mine", "THE HUMANS SIT ELSEWHERE")

# ---------- 9. BELAZ ----------
part(9, "The eight tires of the BelAZ", "WHY DOES THIS TRUCK HAVE 8 TIRES?", "Why Does the World's Biggest Truck Have 8 Tires?",
     """Why does the BelAZ seven five seven ten have eight tires instead of six? Because it is the largest dump truck ever built, and no tire in the world is big enough to carry its load with just six. Built in Belarus and launched in two thousand thirteen, it is rated for four hundred and fifty tonnes. In a test, it carried more than five hundred tonnes in one load.""",
     "BelAZ 75710")
sc("""Instead of inventing a bigger tire, the engineers used more of the existing giant ones, two axles with four tires each. Two diesel engines, together making more than four thousand five hundred horsepower, feed an electric drive. And unlike most trucks, both axles steer, so this giant can turn in a smaller circle.""",
   "BelAZ", "TWO ENGINES, BOTH AXLES STEER")
sc("""It shows a strange truth about mining trucks. Their size is not limited by engines or steel. It is limited by tires, by roads, and by the size of the shovels that load them. A truck that is too big for the shovel waits longer to fill, and that waiting costs more than the extra rock is worth.""",
   "BelAZ 75710", "LIMITED BY TIRES")

# ---------- 10. BLIND SPOT ----------
part(10, "The car that disappears", "WHY CAN'T THE DRIVER SEE THIS CAR?", "Why Can't a Mining Truck Driver See a Car?",
     """Why can a mining truck driver not see a car parked right in front of them? Because from a cab this high, the ground near the truck is hidden by the truck itself. The blind area in front and on the right side can be big enough to hide a pickup truck completely. Mining safety agencies have recorded many cases of haul trucks driving over smaller vehicles, often killing the people inside.""",
     "Logan Lake mining truck")
sc("""So the mines fight blindness with rules and gadgets. Light vehicles carry tall flags on a pole, sometimes called buggy whips, with a light on top, so the driver can see them over the truck's nose. Trucks have cameras, mirrors and radar that beep when something is close. And small vehicles must ask by radio before they come near a haul truck.""",
   "haul truck", "FLAGS ON A POLE")
sc("""Another rule is called the berm. Haul roads have walls of rock along the edges, at least as tall as half a truck tire, so a truck that drifts off the road hits the berm instead of going over the edge. On a machine this size, safety is not a feature you add. It is designed into the road too.""",
   "open pit mine haul road", "THE ROAD IS PART OF IT")

# ---------- 11. HEATED BODY ----------
part(11, "The heated dump body", "WHY DO SOME DUMP BODIES GET HEATED?", "Why Do Some Mining Trucks Heat Their Dump Body?",
     """Why do some mining trucks send their hot exhaust through the dump body? Because in cold climates, wet rock freezes to the steel. When the truck tips its body, part of the load stays stuck inside, frozen to the floor. That is called carryback. The truck drives back to the shovel still carrying tonnes of rock it was supposed to dump.""",
     "Lectra Haul")
sc("""Carryback is pure waste. The truck burns fuel to haul the same rock twice, and it has less room for the next load. So trucks working in places like Canada, Russia and Scandinavia can be fitted with body heating. Exhaust gas is routed through channels under the floor of the body, warming the steel so the rock slides out.""",
   "mining dump truck", "HAULING ROCK TWICE")
sc("""It is a clever reuse of heat the engine would throw away anyway. And it shows the whole philosophy of these machines. When a truck moves hundreds of tonnes every few minutes, small losses add up to millions of dollars a year. Every part is there to remove one.""",
   "Komatsu 930E", "SMALL LOSSES, MILLIONS")

# ---------- VERDICT ----------
sc("""So here are the eleven. A tire taller than a person, filled with nitrogen so it cannot explode, with a speed limit set by heat. A staircase instead of a ladder, a roof over the driver, and electric motors in the wheels. A radiator the size of a garage door, a mast that lets the truck drive itself, eight tires on the biggest truck ever built, a blind spot that can hide a car, and a dump body heated by its own exhaust.""",
   "Caterpillar 797", "11 PARTS. 360 TONNES PER TRIP.", chapter="The verdict", cuts=6)
sc("""A mining truck looks like a toy blown up to giant size, but at this scale, nothing works the way it does on a normal truck. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "mining truck", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:CAT 797 SDB BHPBilliton Escondida Chile 2 HR.jpg", 0.18, 0.5),
    2: ("File:Mont Wright Mine haul truck in for maintenance - see the maintenance crew?.jpg", 0.66, 0.62),
    3: ("File:Big, big tires (8093997590).jpg", 0.5, 0.3),
    4: ("File:Caterpillar 797 Truck2.jpg", 0.45, 0.6),
    5: ("File:KOMATSU 930E-2.JPG", 0.3, 0.15),
    6: ("File:Komatsu 930E Monster truck.jpg", 0.68, 0.62),
    7: ("File:Komatsu HD605 Dump Truck (12716020333).jpg", 0.55, 0.62),
    8: ("File:Ferrexpo autonomous truck.jpg", 0.27, 0.3),
    9: ("File:BelAZ 75710 1.png", 0.42, 0.72),
    10: ("File:Logan Lake Mining Dump Truck 1.jpg", 0.75, 0.78),
    11: ("File:Lectra Haul giant mining truck in Asbestos, Quebec.jpg", 0.55, 0.3),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video50", "title": "Why Are Mining Truck Tires Taller Than a Person?",
           "length_scale": 1.6, "scenes": S}, open("videos/video50/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
