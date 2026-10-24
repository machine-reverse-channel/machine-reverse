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
sc("""The International Space Station weighs about four hundred fifty thousand kilograms, and it floats about four hundred kilometers above your head. It is bigger than a football field, and it never lands. So why doesn't it fall down? It does fall, all the time. It just keeps missing the ground. Today, ten parts of the space station, and the reason each one is there.""",
   "International Space Station", "WHY DOESN'T IT FALL?", cuts=8, chapter="Intro")
sc("""There is no magic up there, and no escape from gravity. At the height of the station, gravity is still almost as strong as on the ground. What the station has is speed, and a long list of machines that keep it alive in a place with no air, no shade and no help.""",
   "International Space Station Earth", "SPEED, NOT ESCAPE")
sc("""As always, every fact here comes from a named source, NASA documents and spaceflight references, all listed in the description. Let's start with the biggest question of all.""",
   "International Space Station orbit", "WHY DOES THIS EXIST?")

# ---------- 1. THE STATION ----------
part(1, "The station that never lands", "WHY DOESN'T THIS FALL DOWN?", "Why Doesn't the Space Station Fall Down?",
     """Why doesn't the space station fall down? Because it is moving sideways at about seven point six seven kilometers every second, twenty-seven thousand six hundred kilometers an hour. It does fall toward Earth, but the Earth's surface curves away as fast as the station drops. So it falls around the planet, over and over, completing a lap in about ninety-three minutes, fifteen and a half orbits every day.""",
     "International Space Station orbit Earth")
sc("""Think of throwing a ball. The harder you throw, the farther it lands. Throw it hard enough, and the ground curves away beneath it before it lands. That is an orbit. The astronauts feel weightless not because gravity is gone, but because they and the station are falling together.""",
   "astronaut floating International Space Station", "FALLING AND MISSING")
sc("""And this was done with an enormous machine, built in pieces, in orbit, by many countries. Humans have lived aboard continuously since the second of November, two thousand. Everything we will look at today is part of keeping that going.""",
   "International Space Station crew", "LIVED IN SINCE 2000")

# ---------- 2. SOLAR ARRAYS ----------
part(2, "The giant solar wings", "WHY ARE THESE WINGS SO HUGE?", "Why Does the Space Station Have Such Giant Solar Wings?",
     """Why does the station have such enormous wings? They are solar arrays, and there are eight of them. Each one is thirty-five meters long and twelve meters wide, and each makes close to thirty-one kilowatts in direct sunlight. All eight together make about two hundred forty kilowatts in the sun, and on average, a bit less than half of that, because of the shade.""",
     "International Space Station solar array")
sc("""Every ninety minute lap, the station spends about thirty-five minutes in the Earth's shadow. During that time, batteries take over. The battery system goes through sixteen charge and discharge cycles every day, which is why the batteries are one of the parts the crew has to replace over the years.""",
   "International Space Station eclipse night", "35 MINUTES IN THE DARK")
sc("""Folded for launch, each wing fits in a box just fifty-one centimeters high. In space, it unfolds into a field of solar cells bigger than a tennis court. It is a power plant, delivered in a shoebox, that has to work in vacuum for decades.""",
   "International Space Station solar panels", "A POWER PLANT IN A BOX")

# ---------- 3. ROTATING JOINTS ----------
part(3, "The rotating joints", "WHY DO THE SOLAR WINGS KEEP TURNING?", "Why Do the Space Station's Solar Wings Keep Turning?",
     """Why do the solar wings keep turning? To follow the Sun. The station circles the Earth every ninety minutes, so the Sun appears to move across the sky very fast. A rotating joint called the alpha gimbal turns the arrays to face it, and a second joint, the beta gimbal, adjusts for the angle of the orbit. A solar panel that does not face the Sun makes much less power.""",
     "International Space Station solar array rotary joint")
sc("""The station keeps its body pointed at the Earth, while its wings turn to follow the Sun. Those two jobs need different directions, so the joints do the work of a sunflower, all day, every day.""",
   "International Space Station Sun", "A SUNFLOWER IN SPACE")
sc("""Each of those joints is a moving part in a machine that is almost impossible to repair, which is why they are among the most watched parts of the station. A joint that sticks means a wing that stops making full power.""",
   "International Space Station spacewalk solar", "ALWAYS WATCHED")

# ---------- 4. RADIATORS ----------
part(4, "The white radiator panels", "WHY ARE THESE WHITE PANELS HERE?", "Why Does the Space Station Have Giant White Panels?",
     """Why does the station have giant white panels next to its solar wings? They are radiators. Every computer, light and astronaut makes heat, and in space there is no air to carry it away. The only way to get rid of heat in a vacuum is to radiate it as infrared light, so the station circulates liquid through pipes to the panels, which shine the heat out into space.""",
     "International Space Station radiator panels")
sc("""The truss that carries the solar arrays also carries the radiators. Together, the two sets of panels are the station's lungs and its power supply, one bringing energy in and the other letting energy out.""",
   "International Space Station truss radiator", "ENERGY IN, ENERGY OUT")
sc("""It is a strange problem. The danger in space is not only the cold. A station full of equipment, parked in sunlight, can get too hot to work. Keeping cool is as hard as keeping warm.""",
   "International Space Station thermal", "TOO HOT IN SPACE")

# ---------- 5. TRUSS ----------
part(5, "The long truss", "WHY IS THERE A GIANT SPINE?", "Why Does the Space Station Have a Giant Metal Spine?",
     """Why does the station have a giant metal spine? It is called the Integrated Truss Structure, built of ten segments, about one hundred eight meters long. It is the backbone that holds the solar arrays and radiators, far enough from the living modules so the wings do not shade the crew, or each other.""",
     "International Space Station integrated truss structure")
sc("""A truss is a very light way to be very long. It is made of simple bars, with mostly empty space between them. That lets the station carry large wings and panels without the weight of a solid beam, which matters when every kilogram has to be launched on a rocket.""",
   "International Space Station truss assembly", "LONG BUT LIGHT")
sc("""The truss was assembled piece by piece, over years of shuttle flights, by astronauts doing spacewalks. It is one of the largest structures humans have ever built outside the Earth.""",
   "International Space Station assembly spacewalk", "BUILT BY SPACEWALKERS")

# ---------- 6. CUPOLA ----------
part(6, "The Cupola", "WHY DOES THE STATION HAVE A GLASS DOME?", "Why Does the Space Station Have a Glass Dome?",
     """Why does the station have a dome made of windows? It is called the Cupola, and it has seven windows, with a round one in the middle about eighty centimeters across. It is the control room for the robotic arm, a place from which astronauts can see the outside of the station and the spacecraft arriving to dock.""",
     "International Space Station Cupola")
sc("""Moving a robot arm, or catching a cargo ship with it, is much easier when you can look at it with your own eyes. Cameras help, but a window gives the view and the depth that screens can not. It is also where astronauts go to look at the Earth.""",
   "International Space Station Cupola window astronaut", "WORK WITH YOUR EYES")
sc("""The windows are protected by shutters, closed when they are not in use, against dust and tiny impacts. A big window on a spacecraft is a risk, so it needs good reasons. The view of the arm and the planet was one.""",
   "Cupola shutters International Space Station", "A WINDOW WITH A SHUTTER")

# ---------- 7. GYROSCOPES ----------
part(7, "The control gyroscopes", "WHY DOES THE STATION HAVE GIANT SPINNING WHEELS?", "How Does the Space Station Turn Without Using Fuel?",
     """How does the station keep itself pointed the right way without burning fuel? With four giant spinning wheels, called control moment gyroscopes, mounted on the truss. Tilt a spinning wheel and it pushes back on the station, turning it. They keep the station at a steady angle to the Earth, and they use only electricity from the solar arrays.""",
     "International Space Station control moment gyroscope")
sc("""Rocket thrusters can do the same job, but they burn propellant that has to be launched from Earth. Over the years, using the gyroscopes for turns, including turns before Soyuz capsules undock, has saved a lot of propellant.""",
   "International Space Station thrusters attitude", "SAVES PROPELLANT")
sc("""The gyroscopes have a limit. If they keep absorbing push, they eventually saturate, and then the station has to use another way to get rid of the extra momentum, like thrusters or the pull of gravity itself. Even a machine without fuel has a limit.""",
   "International Space Station gyroscope saturation", "EVEN THEY HAVE LIMITS")

# ---------- 8. DEBRIS SHIELD ----------
part(8, "The debris shields", "WHY ARE THERE BLANKET SHIELDS ON THE WALLS?", "How Does the Space Station Survive Space Junk?",
     """How does the station survive the pieces of space junk flying around it? With shields. The walls of many modules have an aluminum outer bumper, and behind it a blanket of Nextel ceramic fabric and Kevlar, with the real wall behind. The design is meant to stop an aluminum ball about one centimeter wide, at speeds of several kilometers a second.""",
     "International Space Station debris shield Whipple")
sc("""The idea is called a Whipple shield. The outer bumper does not stop the piece. It breaks it up, melts it or turns it into a cloud of fine fragments, and the layers behind spread and absorb what is left. A thin plate with a gap works better than one thick plate.""",
   "Whipple shield impact test", "A THIN PLATE AND A GAP")
sc("""The faster the object, the better it works. At several kilometers a second, a small fragment vaporizes when it hits the bumper. It is a strange rule of space. A fast thing can be easier to stop than a slow one.""",
   "space debris impact", "FASTER IS EASIER TO STOP")

# ---------- 9. REBOOST ----------
part(9, "The reboost engines", "WHY DOES THE STATION NEED TO BE PUSHED UP?", "Why Does the Space Station Need to Be Pushed Higher?",
     """Why does a station need engines if it is already in orbit? Because there is still a very thin trace of air at four hundred kilometers, and it drags on the station. Without help, the station loses about two kilometers of altitude every month. So, from time to time, a visiting spacecraft, or the station's own engines, fire to lift it back up.""",
     "International Space Station reboost")
sc("""Without those pushes, the orbit would slowly shrink, and eventually the station would fall into the atmosphere and burn up. The station is not simply parked up there. It is slowly being held up, month after month, by people on the ground planning each burn.""",
   "International Space Station orbit decay", "HELD UP, MONTH AFTER MONTH")
sc("""So the answer to our title is a little more complicated. The station does not fall down because it is always moving sideways, very fast, and because someone keeps topping up its speed. Gravity never lets go. We just keep winning.""",
   "International Space Station orbit boost", "GRAVITY NEVER LETS GO")

# ---------- 10. ROBOT ARM ----------
part(10, "The robot arm", "WHY DOES THE STATION HAVE A ROBOT ARM?", "Why Does the Space Station Have a Giant Robot Arm?",
     """Why does the station have a giant robot arm? It is Canadarm two, and it is the station's crane. It moved the pieces of the station into place during assembly, and since then it has caught visiting cargo ships and moved astronauts to their work sites. The arm walks along the station, hand over hand, changing the end it holds on to.""",
     "Canadarm2 International Space Station")
sc("""Ships that bring supplies do not dock by themselves, many of them stop a short distance away, and wait to be grabbed by the arm. It is gentler and safer than trying to fly a spaceship into a docking port at that moment.""",
   "Canadarm2 captures cargo spacecraft", "THE STATION'S CRANE")
sc("""It is a simple idea, a robot arm built to work in zero gravity. And with it, the astronauts built a house in the sky, one room at a time, that has been lived in for more than twenty-five years.""",
   "International Space Station robotic arm assembly", "A HOUSE IN THE SKY")

# ---------- VERDICT ----------
sc("""So here are the ten. A station that falls around the Earth and misses, solar wings that follow the Sun, radiators that shine away the heat, a spine that holds them, a dome of windows. Spinning wheels that turn the station, shields against space junk, engines that lift it, and an arm that built it.""",
   "International Space Station sunrise", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see the station crossing the night sky, a bright dot that moves faster than any plane, you will know what is holding it up. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "International Space Station night sky", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:STS-134 International Space Station after undocking.jpg", 0.5, 0.5),
    2: ("File:Earth horizon and International Space Station solar panel array (Expedition 17 crew, August 2008).jpg", 0.55, 0.4),
    3: ("File:Portion of the International Space Station (4615081313).jpg", 0.33, 0.33),
    4: ("File:International Space Station radiators and solar arrays ESA21792677.jpeg", 0.45, 0.57),
    5: ("File:ISS Truss structure.jpg", 0.5, 0.5),
    6: ("File:Cupola ISS open shutters.jpg", 0.5, 0.5),
    7: ("File:ISS gyroscope.jpg", 0.5, 0.45),
    8: ("File:ATV shielding after impact test ESA313132.jpg", 0.5, 0.5),
    9: ("File:The Progress 91 resupply ship fires its thrusters to reboost the International Space Station (iss073e0429326).jpg", 0.85, 0.25),
    10: ("File:ISS-50 Canadarm2 with Dextre robot (ISS050-E-029710, crop).jpg", 0.2, 0.55),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video13", "title": "Why Doesn't the Space Station Fall Down?",
           "length_scale": 1.6, "scenes": S}, open("videos/video13/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
