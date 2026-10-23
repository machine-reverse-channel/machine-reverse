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
sc("""Drive near an airport or across a big river valley and you may see giant colored balls hanging on power lines, orange, white and yellow, high above the ground. They look like toys someone threw up there. They are not. Each one may be saving a pilot's life. Today, eleven parts of a high voltage power line, and why each one exists, starting with those balls.""",
   "aerial marker ball", "WHY ARE THERE BALLS UP THERE?", cuts=8, chapter="Intro")
sc("""Power lines carry electricity from power plants to cities, sometimes over hundreds of kilometers, at hundreds of thousands of volts. They cross mountains, rivers and forests. They are hit by wind, ice, lightning and birds. And almost nothing on them is decoration. Every strange object you see on a power line is there to solve a problem.""",
   "transmission tower", "NOTHING IS DECORATION")
sc("""As always, every fact comes from a named source, power companies, aviation authorities, and official investigation reports, all listed in the description. Let's start with the balls.""",
   "power line marker ball", "WHY DOES THIS EXIST?")

# ---------- 1. MARKER BALLS ----------
part(1, "The colored balls", "WHY ARE THERE BALLS ON POWER LINES?", "Why Are There Balls on Power Lines?",
     """Why are there big colored balls on some power lines? Because pilots cannot see the wires. A thin cable stretched across a valley is almost invisible from the air, even in good weather. Low flying aircraft, like helicopters, crop dusters and small planes, have crashed into power lines they never saw. The balls make the wires visible from far away.""",
     "aerial marker ball")
sc("""They are called aerial marker balls, and aviation rules say where they must go. Usually near airports, across rivers and canyons, and on very high spans. In the United States, they can be up to about ninety centimeters across, in orange, white or yellow, and the colors alternate along the line so they stand out against the sky and the ground.""",
   "power line marker ball", "ORANGE, WHITE, YELLOW")
sc("""The balls are hollow, made of light plastic or fiberglass, so they add little weight to the line. They are clamped on by line workers, often from a helicopter. A few kilograms of plastic make a deadly cable impossible to miss.""",
   "aerial marker ball", "HOLLOW BUT LIFE SAVING")

# ---------- 2. STOCKBRIDGE DAMPER ----------
part(2, "The little dumbbells", "WHY ARE THERE DUMBBELLS ON THESE WIRES?", "Why Do Power Lines Have Little Dumbbells on Them?",
     """Why do power lines have small dumbbell shaped weights hanging near the towers? They are Stockbridge dampers, invented in the nineteen twenties by an engineer named George Stockbridge. They stop the wires from vibrating themselves to death. A steady breeze blowing across a cable sheds tiny swirls of air, which make the cable vibrate up and down very fast, with small movements.""",
     "Stockbridge damper")
sc("""This is called aeolian vibration, after the Greek god of the wind. It is too small to see easily, but it never stops. Over months and years, the bending at the clamps tires the metal strands, and they can break one by one. A broken conductor can drop a live wire to the ground.""",
   "Stockbridge damper", "VIBRATING TO DEATH")
sc("""The two weights hang on a short piece of flexible steel cable. When the wire vibrates, the weights swing and flex that cable, turning the vibration energy into a little heat. It is one of the simplest and most successful inventions in power engineering, and it is still used all over the world.""",
   "Stockbridge damper", "SIMPLE AND STILL USED")

# ---------- 3. SPACERS ----------
part(3, "The spacers between wires", "WHY ARE THESE WIRES IN BUNDLES?", "Why Do Power Lines Use Bundles of Wires?",
     """Why do the biggest power lines use groups of two, three or four wires, held apart by metal frames? Because one thick wire would waste energy into the air. At very high voltages, the electric field around a single wire is so strong that it rips electrons off the air molecules. That is called corona discharge. It wastes power, makes noise, and causes radio interference.""",
     "power line spacer")
sc("""Splitting each phase into a bundle of smaller wires spreads the electric field out, like making the wire act thicker without the weight. The bundle also carries more current. The metal frames, called spacers, keep the wires at the right distance, so they do not slap together in the wind or when a short circuit pulls them toward each other.""",
   "power line spacer", "ACTING THICKER")
sc("""On a damp day, you can sometimes hear a crackling buzz under high voltage lines. That is corona, the air itself conducting a tiny bit. The bundles and spacers keep it small. Without them, the buzz would be much louder and the losses much higher.""",
   "transmission tower", "THE BUZZ")

# ---------- 4. INSULATORS ----------
part(4, "The stack of discs", "WHY DO THESE INSULATORS LOOK LIKE PLATES?", "Why Do Power Line Insulators Look Like Stacks of Plates?",
     """Why do power line insulators look like stacks of glass or ceramic plates? Because they must keep hundreds of thousands of volts away from the steel tower. Each disc can hold back a certain voltage, so the higher the voltage of the line, the more discs in the string. You can roughly guess a line's voltage by counting them.""",
     "high voltage insulator string")
sc("""The wavy shape is important. Dirt, salt and rain can form a wet path on the surface, and electricity can creep along it. The ridges under each disc make the path along the surface much longer, and keep part of it dry in the rain, so the current cannot sneak across.""",
   "power line insulator", "A LONGER PATH")
sc("""Glass discs have a clever safety feature. If one is damaged by a bullet or a power surge, it shatters completely and visibly, while the metal parts keep holding the line. Inspectors flying by can see the missing disc right away. Many new lines use long rubber polymer insulators, which are lighter and resist vandalism better.""",
   "high voltage insulator string", "GLASS THAT SHATTERS ON PURPOSE")

# ---------- 5. CORONA RINGS ----------
part(5, "The metal rings at the ends", "WHY ARE THERE RINGS ON THESE INSULATORS?", "Why Do High Voltage Lines Have Metal Rings?",
     """Why do some insulators have shiny metal rings around their ends? They are corona rings, also called grading rings. At the end of an insulator, the electric field gets concentrated on sharp edges and small metal parts. That concentrated field causes corona discharge, which slowly damages the insulator and wastes energy.""",
     "power line corona ring")
sc("""A smooth, round ring spreads the field out over a larger surface, the same way the bundles do for the wires. On polymer insulators, this protects the rubber, which can be burned by constant tiny discharges. On the highest voltage lines, you will see rings at both ends of every insulator.""",
   "power line corona ring", "SPREADING THE FIELD")
sc("""It is a rule you see all over high voltage equipment. Sharp points are bad, smooth curves are good. That is why substations are full of round tubes, domes and rings. Electricity at these voltages leaks from anything pointy.""",
   "power line corona ring", "NO SHARP POINTS")

# ---------- 6. GROUND WIRE ----------
part(6, "The wire on the very top", "WHY IS THERE A WIRE ABOVE THE OTHERS?", "Why Is There an Extra Wire on Top of Power Towers?",
     """Why do many power towers have one or two thin wires running along their very tops, above the main wires? They are shield wires, or ground wires. They are connected to the steel towers and to the earth, and they catch lightning. A strike on the shield wire flows down the towers into the ground instead of hitting the live wires below.""",
     "overhead ground wire")
sc("""Without them, a lightning strike on a power wire would send a huge surge along the line, damaging equipment and tripping the power off. The shield wires create a kind of protective tent above the conductors, like an umbrella against lightning.""",
   "transmission tower", "AN UMBRELLA FOR LIGHTNING")
sc("""Many modern shield wires have a hidden second job. Inside, they carry optical fibers. Power companies use them to send control signals, and some rent the extra fibers to telecom companies. A wire meant to catch lightning also carries internet traffic.""",
   "overhead ground wire", "INTERNET INSIDE")

# ---------- 7. BIRD DIVERTERS ----------
part(7, "The spirals for birds", "WHY ARE THERE SPIRALS ON THIS WIRE?", "Why Do Power Lines Have Spirals for Birds?",
     """Why do some power lines have small spirals or flapping tags clipped on them? They are bird diverters. Large birds, like cranes, swans, storks and bustards, often cannot see thin wires until it is too late, especially in fog or at dusk. Collisions with power lines kill huge numbers of birds every year.""",
     "bird diverter power line")
sc("""The diverters make the wires thicker and more visible, and some flap, glow or reflect light. Studies have found that marking lines can greatly reduce bird collisions, often cutting them by half or more, depending on the species and the place.""",
   "bird diverter power line", "HALF THE COLLISIONS")
sc("""Power companies also design towers so that birds landing on them cannot touch two wires at once, which would electrocute them. Some even build nest platforms on towers for storks and ospreys, giving them a safe place away from the live wires.""",
   "bird nest transmission tower", "SAFE NESTS")

# ---------- 8. ANTI-CLIMB ----------
part(8, "The barbed panels on the legs", "WHY DO THESE TOWERS HAVE BARBED WIRE?", "Why Do Power Towers Have Barbed Wire on Their Legs?",
     """Why do many power towers have barbed wire or spiked panels on their legs, a few meters above the ground? Because people climb them. Children, thrill seekers and thieves have climbed towers, and some have been killed. You do not have to touch a high voltage wire to be electrocuted. At these voltages, the current can jump through the air if you get close.""",
     "transmission tower anti-climbing")
sc("""The anti climbing devices make the first few meters very hard to climb, and danger signs warn of death. Line workers who need to go up use special access points and switch off or work with strict safety distances.""",
   "transmission tower", "DANGER OF DEATH")
sc("""Even kites and drones are dangerous near power lines. A wet kite string can conduct electricity, and a drone touching a wire can short it out. The safest rule is the simple one. Stay well away from anything attached to a power line.""",
   "transmission tower", "STAY AWAY")

# ---------- 9. HELICOPTER LINEMEN ----------
part(9, "The man on the live wire", "WHY IS THIS MAN TOUCHING A LIVE WIRE?", "Why Can This Man Touch a Live Power Line?",
     """How can a line worker touch a power line carrying hundreds of thousands of volts and survive? Because current only flows when there is a difference in voltage. Workers on a platform hanging from a helicopter wear suits woven with metal threads. They first touch the wire with a metal wand, so that they, the suit and the helicopter rise to the same voltage as the line.""",
     "transmission line helicopter")
sc("""Once they are at the same voltage, no current flows through their bodies, the same reason birds can sit on a single wire. The metal suit acts like a Faraday cage, keeping the electric field around them. They can then repair spacers, replace insulators or fix damaged strands, without switching off the power to a whole region.""",
   "power line live line work", "SAME VOLTAGE, NO CURRENT")
sc("""The dangerous moment is the connection, when a bright arc jumps between the wand and the wire. After that, the worker can sit on the line as if it were a bench. It is one of the most extreme jobs in the world, and it only works because the physics is exactly right.""",
   "power line live line work", "SITTING ON THE LINE")

# ---------- 10. SAG ----------
part(10, "The wire that sags", "WHY DO POWER LINES SAG?", "Why Do Power Lines Sag More on Hot Days?",
     """Why do power lines hang in a curve instead of being pulled tight? Because a perfectly tight wire would need enormous force, and it would snap when it shrank in the cold. So lines are hung with a planned sag. But that sag changes. When a line carries a lot of current, it heats up, the metal expands, and the wire droops lower.""",
     "transmission tower")
sc("""On the fourteenth of August two thousand three, in Ohio, hot heavily loaded lines sagged into trees that had not been trimmed. They shorted out one after another. Alarm software had failed, so operators did not see what was happening. The failure spread into the largest blackout in North American history, cutting power to about fifty million people.""",
   "transmission tower", "THE 2003 BLACKOUT")
sc("""That is why power companies keep wide clear strips under their lines, cutting trees and bushes. The space under a power line is not empty by accident. It is the room the wire needs on its hottest day.""",
   "transmission tower", "ROOM TO SAG")

# ---------- 11. HIGH VOLTAGE ----------
part(11, "The giant towers", "WHY DOES POWER TRAVEL AT SUCH HIGH VOLTAGE?", "Why Does Electricity Travel at Such High Voltage?",
     """Why do power lines run at such dangerous voltages, hundreds of thousands of volts? Because it saves energy. The power lost in a wire depends on the current squared. If you raise the voltage ten times, you can send the same power with a tenth of the current, and the losses drop to about a hundredth.""",
     "transmission tower")
sc("""That is why electricity leaves the power plant through a transformer that raises the voltage, travels across the country on tall towers, and is then stepped down again in substations near the city, and once more on the pole outside your house. The giant towers exist because the voltage needs big distances from the ground and between the wires.""",
   "transmission tower", "UP, ACROSS, DOWN")
sc("""Most lines carry three wires, or three bundles, because the grid uses three phase power, three currents that rise and fall one after the other. It is the most efficient way to move large amounts of power, and it is why many towers have their wires in groups of three.""",
   "transmission tower", "GROUPS OF THREE")

# ---------- VERDICT ----------
sc("""So here are the eleven. Colored balls for pilots, and little dumbbells that stop the vibration. Bundles of wires with spacers, insulators like stacks of plates, and metal rings that spread the field. A wire on top that catches lightning, spirals for birds, barbed wire against climbers, a man on a live wire, a sag that caused a blackout, and voltages high enough to save the energy.""",
   "transmission tower", "11 PARTS. 500,000 VOLTS.", chapter="The verdict", cuts=6)
sc("""Next time you drive under a power line, look up, and you will know what everything up there is for. If you want more machines and structures explained part by part, subscribe to Machine Reverse. And tell us in the comments what you want us to take apart next.""",
   "transmission tower", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video58", "title": "Why Are There Balls on Power Lines?",
           "length_scale": 1.6, "scenes": S}, open("videos/video58/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
