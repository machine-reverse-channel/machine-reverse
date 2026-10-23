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
sc("""Every time Concorde landed, its whole nose bent down, like a bird lowering its beak. It looked strange, almost alive, and it was not for show. Without that bend, the pilots could not have seen the runway. Concorde was full of parts like that, a glass shield over the windows, a wheel under the tail, fuel that moved around in flight. Today, ten parts of the fastest airliner ever to carry passengers in regular service, and why each one exists.""",
   "Concorde landing", "WHY DID IT DROP ITS NOSE?", cuts=8, chapter="Intro")
sc("""Concorde first flew on the second of March nineteen sixty-nine, entered airline service in nineteen seventy-six, and flew passengers at twice the speed of sound, at about sixty thousand feet, until two thousand three. At that speed, almost every normal airliner solution stops working. Air gets hot, the airplane grows, and even the windows have to change. So the engineers had to invent new ones.""",
   "Concorde British Airways", "TWICE THE SPEED OF SOUND")
sc("""As always, every fact here comes from a named source, museums, aviation references and official reports, all listed in the description. Let's start with the most famous part of all, the nose.""",
   "Concorde nose", "WHY DOES THIS EXIST?")

# ---------- 1. DROOP NOSE ----------
part(1, "The nose that bends", "WHY DOES THIS NOSE BEND DOWN?", "Why Did the Concorde Drop Its Nose?",
     """Why did Concorde's nose bend down? Because of its wing. A delta wing like Concorde's has no flaps, so to fly slowly it has to point its nose high into the air. On landing, Concorde came in with its nose so high that, with a straight nose, the pilots would have seen only sky. So the whole nose was hinged. It drooped to about five degrees for takeoff and taxi, and twelve and a half degrees for landing.""",
     "Concorde droop nose")
sc("""Why not just give Concorde a short, round nose like a normal airliner? Because at twice the speed of sound, a blunt nose makes a huge amount of drag. A supersonic airplane needs a long, sharp, pointed nose. That is perfect at Mach two, and terrible for seeing the runway. The droop nose was the compromise, sharp in the sky, and bent down near the ground.""",
   "Concorde nose up", "SHARP IN THE SKY")
sc("""The nose moved with hydraulic power, controlled by a lever in the cockpit. And the engineers planned for failure. If the hydraulics or the electrics failed, the locks could be released by hand, and the nose would fall to five degrees by gravity and the airflow. A part this important could never be allowed to get stuck in the wrong position.""",
   "Concorde cockpit", "IT COULD NEVER GET STUCK")

# ---------- 2. VISOR ----------
part(2, "The glass shield", "WHY IS THERE A SECOND WINDSHIELD HERE?", "Why Did the Concorde Have a Second Windshield?",
     """Why did Concorde have a second windshield in front of the first one? It is called the visor. In cruise, it slid up over the real windshield and made the nose one smooth, sharp shape. It protected the windshield from heat and air pressure at Mach two, and it made the cockpit very quiet. Pilots said that the first time they raised it, they thought the engines had stopped.""",
     "Concorde visor")
sc("""The first prototypes had a metal visor with tiny windows and a periscope. One test pilot said that flying it was like flying inside a letter box. The American Federal Aviation Administration wanted better forward vision, so the engineers developed a glass visor that could survive the heat and the force of Mach two. It was about one and a half inches thick, with a heated gold film to keep it clear.""",
   "Concorde prototype", "LIKE FLYING IN A LETTER BOX")
sc("""There was a clever safety lock too. With the visor up, the landing gear circuits were isolated, so nobody could lower the gear at twice the speed of sound by mistake. Visor down and nose down meant slow flight. Visor up and nose up meant Mach two. Just by looking at the nose, you could tell what Concorde was doing.""",
   "Concorde in flight", "READ THE NOSE")

# ---------- 3. DELTA WING ----------
part(3, "The wing with no flaps", "WHY DOES THIS WING HAVE NO FLAPS?", "Why Didn't the Concorde Need Flaps?",
     """Why did Concorde's wing have no flaps? Normal airliners have flaps and slats that slide out to make the wing bigger for landing. Concorde's thin delta wing had none. Instead, at high angles, the sharp front edge of the wing creates two huge spinning vortices of air above the wing. Those swirls create low pressure, and that low pressure keeps the wing lifting at low speed.""",
     "Concorde delta wing")
sc("""This is called vortex lift, and on a humid day you could actually see it, as white swirls of condensation over the wings on takeoff and landing. The wing was not a simple triangle. It had a gentle curve, called an ogee shape, refined over about five thousand hours of wind tunnel testing, so that one wing could work at two hundred miles an hour and at one thousand three hundred fifty.""",
   "Concorde vortex condensation", "5,000 HOURS IN THE TUNNEL")
sc("""The price of vortex lift is that high nose up angle. And that is the link between all the first parts of this video. The wing needs a high angle, so the nose has to droop, so the visor has to move. One design decision created three moving parts. That is how airplanes are built. Every solution creates the next problem.""",
   "Concorde takeoff", "ONE DECISION, THREE PARTS")

# ---------- 4. TAIL WHEEL ----------
part(4, "The wheel under the tail", "WHY IS THERE A WHEEL UNDER THE TAIL?", "Why Did the Concorde Have Wheels Under Its Tail?",
     """Why did Concorde have a small set of wheels under its tail? Because of that high angle again. Concorde lifted off with its nose pointing about eighteen degrees up, far more than a normal airliner. With such a long body, a pilot pulling up a little too much could scrape the tail on the runway. The tail wheels were there to touch first and protect the airplane.""",
     "Concorde tail wheel")
sc("""To reach that angle, Concorde also needed very tall landing gear, so the main legs were long and had to fold into a thin wing. The legs even shortened as they retracted, to fit into the space available. Takeoff speed was about two hundred fifty miles an hour, and landing speed about one hundred eighty-seven, much faster than a normal airliner.""",
   "Concorde landing gear", "250 MPH TAKEOFF")
sc("""A tail bumper sounds like a small detail, but a tailstrike can damage the pressure bulkhead and the structure at the back of an airliner. On Concorde, with its long thin body and steep angles, the engineers decided it was simpler to give the tail its own wheels than to trust every takeoff to be perfect.""",
   "Concorde rear fuselage", "DON'T TRUST PERFECT")

# ---------- 5. INTAKES ----------
part(5, "The engine intakes", "WHY ARE THESE INTAKES SO LONG?", "Why Were the Concorde's Engine Intakes So Long?",
     """Why were Concorde's engine intakes so long and rectangular? Because a jet engine cannot swallow air at twice the speed of sound. The air must be slowed down to below the speed of sound before it reaches the fan. Inside each intake there were movable ramps, which created shock waves in exactly the right places, slowing the air down and squeezing it at the same time.""",
     "Concorde engine intakes")
sc("""The ramps moved all the time, depending on speed, altitude and temperature, and they were controlled by a digital computer. According to aviation historians, it was the first time a digital computer had full authority over an essential system on a passenger airplane. At Mach two, the intake was doing a huge share of the work of compressing the air.""",
   "Rolls-Royce Olympus 593", "A COMPUTER IN CHARGE")
sc("""If an engine failed at Mach two, the intake had to react instantly, or the shock waves could disturb the engine next to it. So spill doors opened and the ramps moved fully to protect the airflow. On Concorde, the engine was not just the part that burned fuel. The whole channel in front of it was part of the machine.""",
   "Concorde engine nacelle", "THE INTAKE IS THE ENGINE")

# ---------- 6. AFTERBURNERS ----------
part(6, "The afterburners", "WHY DID AN AIRLINER HAVE AFTERBURNERS?", "Why Did the Concorde Have Afterburners?",
     """Why did a passenger airliner have afterburners like a fighter jet? Afterburners spray extra fuel into the hot exhaust and burn it, for a big boost of thrust. Concorde's four Rolls-Royce Olympus engines used them only twice in a normal flight, for takeoff, and to push through the sound barrier, between about Mach zero point nine five and Mach one point seven.""",
     "Concorde afterburner")
sc("""The sound barrier is where drag rises the most, and Concorde needed extra push to get through it quickly. Once above Mach one point seven, the afterburners were switched off, and Concorde cruised at twice the speed of sound without them. That is called supercruise, something very few airplanes have ever done, even military ones.""",
   "Concorde supersonic", "SUPERCRUISE")
sc("""Afterburners burn fuel very fast, and Concorde was already thirsty, using more than five thousand six hundred gallons per hour. That is why, from London or Paris, it could cross the Atlantic to New York, but not the Pacific. The fastest east to west crossing took three hours and six minutes.""",
   "Concorde New York", "3 HOURS 6 MINUTES")

# ---------- 7. FUEL TRIM ----------
part(7, "The fuel that moved", "WHY DID THE FUEL MOVE IN FLIGHT?", "Why Did the Concorde Move Its Fuel Around in Flight?",
     """Why did Concorde pump its fuel from one end of the airplane to the other during flight? Because when an airplane goes supersonic, the point where the wing's lift acts moves backward, by about two meters on Concorde. That would make the nose want to pitch down. Normally you fix that with the tail controls, but on Concorde that would have created too much drag.""",
     "Concorde fuel tanks")
sc("""So the flight engineer moved the weight instead. During acceleration, fuel was pumped toward the back of the airplane, moving the center of gravity backward to follow the lift. When slowing down before landing, fuel was pumped forward again. The fuel was not only energy for the engines. It was also a moving weight that balanced the whole airplane.""",
   "Concorde flight engineer panel", "FUEL AS BALLAST")
sc("""This trick is now used on other long range airliners too, with trim tanks in the tail, to reduce drag and save fuel. But Concorde did it on a much bigger scale, because at supersonic speeds the change was so large. A simple idea, move the weight instead of fighting it, made Mach two possible.""",
   "Concorde in flight sky", "MOVE THE WEIGHT")

# ---------- 8. SMALL WINDOWS ----------
part(8, "The tiny windows", "WHY ARE THESE WINDOWS SO SMALL?", "Why Did the Concorde Have Such Tiny Windows?",
     """Why did Concorde have such tiny passenger windows, about the size of a hand? Because it flew at around sixty thousand feet, almost twice as high as a normal airliner. Up there, if a window broke, the cabin would lose its air very fast, and the air outside is too thin to stay conscious for long. Small windows slow down the rate of pressure loss if the cabin is breached.""",
     "Concorde cabin windows")
sc("""From that height, passengers could see the curve of the Earth and a dark blue sky above them. The cabin was pressurized to about six thousand feet, similar to a normal airliner. The cabin itself was narrow, about nine feet wide, with four seats per row. Speed was the luxury, not space.""",
   "Concorde cabin interior", "THE CURVE OF THE EARTH")
sc("""Passengers also noticed that the windows felt warm. At Mach two, friction with the air heated the outer skin to around one hundred twenty degrees Celsius. Which brings us to the next part. That heat changed the shape of the whole airplane.""",
   "Concorde passenger window", "WARM WINDOWS")

# ---------- 9. WHITE PAINT ----------
part(9, "The white paint", "WHY WAS CONCORDE ALWAYS WHITE?", "Why Was the Concorde Always White?",
     """Why was Concorde almost always painted white? Because white reflects heat. At Mach two, the skin got so hot that the aluminum airframe expanded, and Concorde grew between six and eight inches longer in flight. A special white paint kept the temperature as low as possible, because aluminum loses strength if it gets too hot for too long.""",
     "Concorde Air France")
sc("""In nineteen ninety-six, Air France painted one Concorde in dark blue for a Pepsi promotion. Because dark paint absorbs more heat, that Concorde was allowed to fly at Mach two for no more than twenty minutes at a time. Below Mach one point seven, there was no limit. It is one of the few airplanes where the paint color changed the speed limit.""",
   "Pepsi Concorde", "20 MINUTES AT MACH 2")
sc("""The expansion was visible inside too. Crews told stories of a gap opening near the flight engineer's panel at cruise, which closed again after landing. Concorde's engineers chose an aluminum alloy that could live with that heat for decades. At Mach three, the skin would have been around three hundred fifty degrees, too hot for aluminum. That is one reason Concorde stopped at Mach two.""",
   "Concorde museum", "IT GREW IN FLIGHT")

# ---------- 10. CARBON BRAKES ----------
part(10, "The carbon brakes", "WHY ARE THESE BRAKES MADE OF CARBON?", "Why Did the Concorde Have Carbon Brakes?",
     """Why did Concorde have brakes made of carbon? Because it landed fast and heavy, and steel brakes would have been too heavy for the job. Concorde was the first airliner with carbon brakes, developed by Dunlop. They saved about one thousand two hundred pounds compared with steel brakes, and they could survive temperatures of three hundred to four hundred degrees Celsius after landing.""",
     "Concorde brakes")
sc("""Carbon brakes are now standard on most large airliners, from the Boeing seven forty-seven to the Airbus A three fifty. Like many Concorde ideas, they were too early and too expensive at first, and then became normal. Fly-by-wire controls, digital engine computers, carbon brakes, Concorde tested them in airline service before almost anyone else.""",
   "aircraft carbon brakes", "TOO EARLY, THEN NORMAL")
sc("""The wheels and tires also played a part in Concorde's darkest day. On the twenty-fifth of July two thousand, Air France flight forty-five ninety ran over a metal strip on the runway in Paris. A tire burst, debris struck a fuel tank, and a fire started. One hundred thirteen people died. Afterwards, Concorde got Kevlar linings inside its fuel tanks and new burst-resistant tires, and flew again in two thousand one.""",
   "Concorde museum Paris", "KEVLAR INSIDE THE TANKS")

# ---------- VERDICT ----------
sc("""So here are the ten. A nose that bends to see the runway, and a visor to make it sharp again. A wing that lifts with swirls instead of flaps, and a wheel under the tail for the steep angle. Intakes that slow the air down, afterburners for the sound barrier, fuel that moves to balance the airplane, tiny windows for the altitude, white paint for the heat, and carbon brakes for the landing.""",
   "Concorde sunset", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Concorde was retired in two thousand three, and no passenger airplane has flown that fast since. Every strange part was the price of speed. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Concorde museum", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:British Airways Concorde G-BOAC 03.jpg", 0.14, 0.2),
    2: ("File:Concorde Air France Musee du Bourget P1020006.JPG", 0.84, 0.25),
    3: ("File:Concorde - Delta wing and Rolls-Royce-Snecma Olympus 593 engine (7181594822).jpg", 0.5, 0.3),
    4: ("File:Concorde - Tail bumper wheel (7181575152).jpg", 0.58, 0.67),
    5: ("File:Concorde engine intake.jpg", 0.5, 0.45),
    6: ("File:Aerospatiale Concorde (42935940412).jpg", 0.35, 0.5),
    7: ("File:Concorde Fueling Control (7946110800).jpg", 0.5, 0.45),
    8: ("File:Concorde G-BBDG Windows.JPG", 0.53, 0.45),
    9: ("File:Air France Concorde at CDG.jpg", 0.3, 0.43),
    10: ("File:Concorde brake discs.jpg", 0.4, 0.45),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video08", "title": "Why Did the Concorde Drop Its Nose?",
           "length_scale": 1.6, "scenes": S}, open("videos/video08/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
