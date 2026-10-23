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
# ---------- HOOK ----------
sc("""Start the engine of a normal helicopter, take away one small part at the back, and the whole machine would spin around in circles the moment it tried to lift off. That small part is the tail rotor, and it is only the beginning. Helicopters are full of parts that look strange from the ground, a fan inside the tail, a nut with a nickname, blades that cut cables. Today, ten parts that keep a helicopter from spinning, shaking or falling, and why each one exists.""",
   "helicopter hovering", "WHY DOESN'T IT SPIN?", cuts=8, chapter="Intro")
sc("""A helicopter is one of the hardest machines to keep stable. Its wing is a set of blades turning hundreds of times a minute, its engine fights its own body, and it has to hover, climb, and land almost anywhere. Every part we will look at today solves one of those problems, and some of them were written into the design after people died.""",
   "helicopter rotor blades", "THE HARDEST MACHINE TO FLY")
sc("""As always, every fact comes from a named source, aviation handbooks, manufacturers and accident reports, all listed in the description. Let's start with the problem that every helicopter is born with.""",
   "helicopter tail", "WHY DOES THIS EXIST?")

# ---------- 1. TAIL ROTOR ----------
part(1, "The tail rotor", "WHY IS THERE A SMALL ROTOR HERE?", "Why Do Helicopters Have a Small Rotor on the Tail?",
     """Why is there a small rotor on the tail of a helicopter? Because of Newton's third law. When the engine pushes the big rotor around in one direction, the rotor pushes the body of the helicopter around in the other direction. Without something to stop it, the cabin would spin under the blades. The tail rotor pushes sideways against that spin, like a hand holding the tail still.""",
     "helicopter tail rotor")
sc("""This layout, one main rotor and one small rotor at the tail, was perfected by Igor Sikorsky with his VS-300 in the years around nineteen forty, and it is still the most common design in the world. It is not free. About ten percent of the engine power goes to the tail rotor, power that does nothing to lift the helicopter. The pilot controls it with two pedals that change the pitch of the tail blades, and that is how a helicopter turns its nose while hovering.""",
   "Sikorsky VS-300", "10% OF THE POWER")
sc("""The tail rotor spins so fast that it almost disappears. That is why tail rotor blades are painted with bright stripes, often red and white or black and white. A spinning tail rotor is a hazard to anyone walking near a running helicopter, and the stripes turn an invisible disc into something the eye can catch. On a helicopter, even the paint has a job.""",
   "tail rotor stripes", "EVEN THE PAINT HAS A JOB")

# ---------- 2. FENESTRON ----------
part(2, "The fan inside the tail", "WHY IS THE TAIL ROTOR INSIDE A HOLE?", "Why Do Some Helicopters Hide the Tail Rotor in a Hole?",
     """Why do some helicopters have their tail rotor hidden inside a round hole in the tail? It is called a Fenestron, a fan inside a duct. It first flew on the twelfth of April nineteen sixty-eight, on a prototype of the French Gazelle. The engineers' first goal was protection, of the people working on the ground and of the tail rotor itself, which can hit branches, wires or the ground.""",
     "Fenestron")
sc("""The duct around the fan does more than protect. It makes the tail rotor quieter, and on newer versions the blades are spaced unevenly on purpose, so the sound spreads across many tones instead of one loud buzz. Airbus introduced that uneven spacing on the H135 in the nineteen nineties. On the H160, the whole fan is tilted twelve degrees, so that it also helps with lift.""",
   "Eurocopter EC135 Fenestron", "UNEVEN ON PURPOSE")
sc("""Today the Fenestron is on many Airbus helicopters, like the H130, the H135, the H145 and the H160. It is heavier than an open tail rotor, which is why not every helicopter uses one. But when a helicopter lands next to people, in a hospital car park or a city rooftop, a fan inside a hole is a lot safer than blades spinning in the open.""",
   "Airbus H145 helicopter", "SAFER NEAR PEOPLE")

# ---------- 3. NOTAR ----------
part(3, "The tail with no rotor", "WHY IS THERE NO TAIL ROTOR?", "Why Does This Helicopter Have No Tail Rotor?",
     """Why do some helicopters have no tail rotor at all? This is NOTAR, short for no tail rotor. Inside the tail boom, a fan blows low pressure air out of two long slots on the side. The air coming down from the main rotor hugs the curved boom, and that bends the flow and creates a sideways force, just like a wing. The tail boom itself becomes the anti-torque device.""",
     "MD 600N helicopter")
sc("""At the very end of the tail, a rotating nozzle called a direct jet thruster pushes out more air, and the pilot uses it to steer, with the same pedals as any other helicopter. A NOTAR test aircraft, a modified OH-6A, first flew on the seventeenth of December nineteen eighty-one. The production MD five twenty N followed in nineteen ninety, built by McDonnell Douglas, later MD Helicopters.""",
   "MD 520N helicopter", "THE BOOM BECOMES A WING")
sc("""The reasons are safety and noise. With no blades spinning at the back, nobody can walk into the tail rotor, and the tail cannot hit a tree or a wire. Tail rotors also make a large part of a helicopter's noise, which is why NOTAR helicopters are among the quietest certified by the Federal Aviation Administration. That is why you often see them with police and news crews flying over cities.""",
   "MD 902 Explorer police helicopter", "AMONG THE QUIETEST")

# ---------- 4. COAXIAL ----------
part(4, "The two rotors on top", "WHY ARE THERE TWO ROTORS ON TOP?", "Why Do Some Helicopters Have Two Rotors on Top?",
     """Why do some helicopters have two rotors stacked on top of each other? Because if two rotors turn in opposite directions, their torque cancels out, and the helicopter needs no tail rotor. This is called a coaxial design, and the Russian company Kamov made it its trademark, on helicopters like the Ka-27 and the Ka-52 attack helicopter.""",
     "Kamov Ka-52 rotor")
sc("""There is a bonus. Every bit of engine power goes into lift instead of ten percent going to a tail rotor, and the helicopter can be shorter, which matters on the small deck of a ship. Coaxial helicopters also handle crosswinds well, because there is no tail rotor to fight the wind. The price is a tall and complex rotor head, with two sets of blades and controls on one mast.""",
   "Kamov Ka-27 ship", "NO POWER WASTED")
sc("""The two rotors must also never touch. When a blade flexes, it bends toward the other rotor, so coaxial designs keep a careful gap between the two discs. The same idea is now used on new high speed designs like the Sikorsky X2 family, where stiff rotors and a pusher propeller let a helicopter fly much faster than a normal one.""",
   "Sikorsky X2 coaxial", "NEVER TOUCH")

# ---------- 5. TANDEM ----------
part(5, "The rotor at each end", "WHY DOES THIS HELICOPTER HAVE TWO ROTORS?", "Why Does the Chinook Have Two Rotors?",
     """Why does the Chinook have a rotor at each end? Same trick, different place. The two rotors turn in opposite directions, so their torque cancels and there is no tail rotor. The Chinook first flew in September nineteen sixty-one, and more than six decades later it is still one of the best known helicopters in the world.""",
     "CH-47 Chinook rotors")
sc("""Two big rotors mean the Chinook can lift heavy loads, and because all the power goes into lift, nothing is wasted on a tail rotor. It also has a very long cabin that can be loaded from the back through a ramp, with vehicles, cargo or dozens of troops. The two rotors overlap in the middle, so a shaft along the top of the cabin keeps them perfectly in time. If they ever got out of step, the blades would collide.""",
   "Chinook tandem rotor", "ALWAYS IN TIME")
sc("""Steering is clever too. To turn, the pilot tilts the front rotor one way and the rear rotor the other way, so the helicopter swings around its middle. To fly forward, the rotors tilt forward together. The front rotor sits lower than the rear one, so the rear rotor does not fly through the disturbed air from the front.""",
   "Boeing CH-47 Chinook flying", "TILT ONE WAY, TILT THE OTHER")

# ---------- 6. SWASHPLATE ----------
part(6, "The plates under the rotor", "WHY IS THERE A RING UNDER THE ROTOR?", "Why Is There a Tilting Ring Under Helicopter Rotors?",
     """Why is there a strange tilting ring under the main rotor? It is called the swashplate, and it is how the pilot talks to the blades. It has two parts. The bottom plate does not spin and is moved by the pilot's controls. The top plate spins with the rotor and is connected to each blade with rods. When the bottom plate moves, the top plate follows, and the blades change their angle.""",
     "helicopter swashplate")
sc("""The collective lever, at the pilot's left hand, raises the whole swashplate. Every blade takes a bigger bite of air at the same time, and the helicopter climbs. The cyclic stick, between the pilot's knees, tilts the swashplate. Now each blade changes its angle as it goes around, more bite on one side, less on the other, and the whole rotor disc tilts in that direction.""",
   "swashplate rotor head", "COLLECTIVE AND CYCLIC")
sc("""A helicopter does not fly in a direction by pointing its nose. It tilts its rotor. Tilt the disc forward and part of the lift pushes forward. Tilt it left and the helicopter slides left. All of that happens through one tilting ring, a few rods, and blades that twist a little every single turn, many times per second.""",
   "Robinson R44 rotor", "IT TILTS ITS ROTOR")

# ---------- 7. JESUS NUT ----------
part(7, "The nut on top", "WHY IS THIS NUT CALLED THE JESUS NUT?", "Why Is This Helicopter Part Called the Jesus Nut?",
     """Why is the nut at the very top of some helicopter rotors called the Jesus nut? It is the main rotor retaining nut, the part that holds the rotor onto the mast. If it ever came off in flight, the rotor would leave the helicopter, and the crew would have nothing left to do but pray. The nickname appeared in print in nineteen sixty-seven, and it became famous through books about helicopter pilots in Vietnam.""",
     "helicopter rotor head mast nut")
sc("""Real failures are rare, because the nut and its locking pin are checked before every flight. But it can happen. In two thousand, a Bell two oh six crashed about ten minutes after takeoff, killing both people on board. The mast nut had been removed for repainting and had not been properly put back and checked.""",
   "Bell 206 helicopter", "CHECKED BEFORE EVERY FLIGHT")
sc("""Today engineers use Jesus nut to describe any single part whose failure would bring down the whole system. Most of aviation is designed to avoid single points of failure, with two of everything. A helicopter rotor is one of the few places where one part simply has to hold, so it is made to be strong, simple and inspected again and again.""",
   "Bell UH-1 rotor hub", "ONE PART THAT MUST HOLD")

# ---------- 8. DAMPERS ----------
part(8, "The dampers on the blades", "WHY ARE THERE SHOCK ABSORBERS HERE?", "Why Do Helicopter Blades Have Shock Absorbers?",
     """Why are there small shock absorbers at the root of helicopter blades? They prevent something called ground resonance. On many rotors, the blades are hinged so they can move a little forward and back as they turn. If those blade movements fall out of step and match the rocking of the helicopter on its landing gear, the vibration can grow violently in seconds.""",
     "helicopter lead-lag damper")
sc("""In the worst cases, a helicopter sitting on the ground starts to shake, then rock, and then literally tears itself apart while the engine is still running. That is ground resonance. It was first seen on early gyroplanes and became a serious problem for helicopters during the Second World War. The cure is damping, lag dampers on the blades, either hydraulic or made of elastic material, plus carefully tuned landing gear.""",
   "helicopter rotor hub damper", "IT TEARS ITSELF APART")
sc("""Military helicopters must pass ground resonance tests on slopes, with a flat tire, and even with a failed damper. And pilots learn the escape. If it starts, the best option is often to lift off. Once the helicopter is no longer touching the ground, the rocking stops feeding the vibration, and the machine settles down.""",
   "helicopter landing gear skids", "THE ESCAPE IS UP")

# ---------- 9. WIRE CUTTERS ----------
part(9, "The blades above the cockpit", "WHY ARE THERE BLADES ON THE NOSE?", "Why Do Some Helicopters Have Knives on the Nose?",
     """Why do some helicopters have sharp blades sticking up from the roof and down from the belly? They are wire cutters, part of a wire strike protection system. Helicopters fly low, and power lines and cables are almost invisible from the cockpit. If the helicopter flies into a wire, it slides up or down the windshield into the cutters, and the cutters slice it.""",
     "wire strike protection system")
sc("""The system was developed in Canada by Bristol Aerospace, and in May nineteen seventy-nine it was qualified on the Bell Kiowa for the Canadian Armed Forces. It is designed to cut a steel cable three eighths of an inch thick. The United States Army tested it on the Kiowa, the Huey and the Cobra, and it was fitted to its small and medium helicopters.""",
   "OH-58 Kiowa wire cutter", "IT CUTS STEEL CABLE")
sc("""The reason was blood. Between nineteen seventy-four and nineteen seventy-nine, wire strikes caused sixteen percent of US Army aircraft related deaths. Today you see these cutters on military, rescue and agricultural helicopters, all the machines that work close to the ground. Two small knives, and one of the most invisible dangers in aviation becomes survivable.""",
   "agricultural helicopter spraying", "16% OF THE DEATHS")

# ---------- 10. FREEWHEEL ----------
part(10, "The clutch that lets go", "WHY DOES THE ROTOR KEEP SPINNING?", "Why Doesn't a Helicopter Fall When the Engine Dies?",
     """What happens if a helicopter's engine stops? It does not fall like a stone. Between the engine and the rotor, there is a freewheeling unit, a clutch that lets go automatically when the engine turns slower than the rotor. The rotor keeps spinning freely, and as the helicopter descends, air flowing up through the blades keeps them turning. It is called autorotation, the helicopter version of a glide.""",
     "helicopter autorotation")
sc("""The pilot has to act fast. The collective must go down immediately, so the blades keep their speed. Then the helicopter glides down at a steep angle, and at about fifty to one hundred feet the pilot raises the nose and pulls the collective, using the energy stored in the spinning rotor to slow down and land softly. Every single engine helicopter must show it can do this to be certified.""",
   "helicopter rotor", "THE ROTOR STORES ENERGY")
sc("""The most famous autorotation happened on the twenty-first of June nineteen seventy-two. Test pilot Jean Boulet flew a small Lama helicopter to about forty thousand eight hundred feet, a world record. Up there, in the extreme cold, the engine flamed out and could not be restarted. Boulet came all the way down with no engine, in the longest autorotation ever, and landed safely. His altitude record still stands.""",
   "Aerospatiale SA 315B Lama", "40,800 FT. NO ENGINE.")

# ---------- VERDICT ----------
sc("""So here are the ten. A tail rotor that stops the spin, a fan hidden in a hole, a tail with no rotor at all. Two rotors on top, or one at each end. A tilting ring that steers the blades, a nut that must never fail, dampers that stop a helicopter from shaking itself apart, knives for invisible wires, and a clutch that lets the rotor keep spinning when the engine dies.""",
   "helicopter sunset", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A helicopter looks like it is fighting the air, and in a way it is. Every one of these parts is there because something went wrong once, or could go wrong. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "helicopter takeoff", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Tail rotor Sea Lynx.jpg", 0.48, 0.42),
    2: ("File:Shrouded tail of an H135 (5).jpg", 0.42, 0.55),
    3: ("File:MD600N (14825938382).jpg", 0.78, 0.42),
    4: ("File:Ka-52 at an air show in Voronezh 2014.jpg", 0.47, 0.32),
    5: ("File:ZK558 Boeing Chinook HC.6 RAF Corris Corner 2018 01.jpg", 0.28, 0.5),
    6: ("File:Swashplate by Kamov Ka-26. Central House of Aviation and Cosmonautics.jpg", 0.5, 0.45),
    7: ("File:JMSDF SH-60J (8295) main rotor head at Tokushima Air Base October 1, 2022.jpg", 0.5, 0.25),
    8: ("File:Rotor head CH-53.jpg", 0.45, 0.55),
    9: ("File:Coupe cable gazelle 16321.jpg", 0.76, 0.3),
    10: ("File:NATC pilots train with A-Star Helicopter (20250207612).jpg", 0.47, 0.33),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video07", "title": "Why Doesn't a Helicopter Spin Out of Control?",
           "length_scale": 1.6, "scenes": S}, open("videos/video07/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
