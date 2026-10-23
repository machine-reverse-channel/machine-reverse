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
sc("""On the back of almost every Le Mans prototype from the last fifteen years, there is a tall, thin fin, like the fin of a shark. It does not make the car faster. It was added because racing cars were flying, literally, lifting off the ground at over three hundred kilometres per hour and somersaulting through the air. Today, ten parts of the cars that race for twenty-four hours at Le Mans, and why each one exists.""",
   "Le Mans prototype", "WHY THE SHARK FIN?", cuts=8, chapter="Intro")
sc("""The twenty-four hours of Le Mans is the oldest endurance race in the world, first run in nineteen twenty-three. Three drivers share one car, day and night, rain or dry, for a full day. The cars must be fast like a Formula One car and tough like a truck. Many ideas that are now in your road car were tested there first, from disc brakes to hybrid systems.""",
   "24 Hours of Le Mans night", "24 HOURS, ONE CAR")
sc("""As always, every fact here comes from a named source, the organisers of Le Mans, the World Endurance Championship and motorsport references, all listed in the description. Let's start with the fin.""",
   "Le Mans pit lane", "WHY DOES THIS EXIST?")

# ---------- 1. FIN ----------
part(1, "The shark fin", "WHY IS THERE A FIN ON THE BACK?", "Why Do Le Mans Cars Have a Fin on Their Back?",
     """Why do Le Mans cars have a fin on their back? To stop them from flying. A modern prototype has a very flat, wide body that works like a wing turned upside down. When the car goes straight, the air pushes it down. But if the car spins and slides sideways or backwards at high speed, the same body can start to work like a real wing, and lift the car off the ground.""",
     "Le Mans prototype shark fin")
sc("""The most famous case happened in nineteen ninety-nine. The Mercedes CLR lifted off three times that weekend. Mark Webber's car flipped over twice, in practice and in the warm up. Then in the race, Peter Dumbreck's car took off on a straight, somersaulted and landed in the trees beside the track. Amazingly, every driver survived. Mercedes withdrew its last car and left sports car racing.""",
   "Mercedes-Benz CLR", "THE CAR THAT FLEW")
sc("""The fin works like the feathers on an arrow. When the car starts to turn sideways, the air hits the fin and pushes the tail back into line, so the car keeps pointing forward and the body keeps pressing down. After more flying accidents, the rules made fins compulsory on prototypes from twenty eleven. It is a safety part that looks like a style choice.""",
   "Audi R18 Le Mans", "FEATHERS ON AN ARROW")

# ---------- 2. LOUVRES ----------
part(2, "The holes above the wheels", "WHY ARE THERE HOLES ABOVE THE WHEELS?", "Why Do Race Cars Have Holes Above the Wheels?",
     """Why do Le Mans cars have holes and slats on top of the wheel arches? Because the spinning wheels pump air into the wheel wells. A tyre turning at high speed drags air around with it, and that air gets trapped inside the bodywork. Trapped air means high pressure, and high pressure under the body pushes the car up, the opposite of what you want.""",
     "Le Mans prototype wheel arch louvres")
sc("""The louvres, those slats cut in the top of the wheel arch, let that air escape upwards. Less pressure inside, less lift and less drag. You will also see the same trick on some fast road cars and in many racing series. The holes look aggressive, but they are simply a pressure valve shaped by the wind tunnel.""",
   "race car wheel arch vents", "A PRESSURE VALVE")
sc("""They also help with safety. If the car spins backwards, air can rush under the front of the body. The openings above the wheels let some of that air out before it builds enough pressure to lift the car. Together with the fin, the holes are part of the same lesson the sport learned in nineteen ninety-nine. A race car must never become a wing.""",
   "Le Mans hypercar", "NEVER BECOME A WING")

# ---------- 3. LONG TAIL ----------
part(3, "The long tail", "WHY IS THIS CAR SO LONG AT THE BACK?", "Why Did Le Mans Cars Have Such Long Tails?",
     """Why did some old Le Mans cars have such long tails? Because of one straight. The Mulsanne, a public road closed for the race, was almost six kilometres long with no corner. Teams built special long tail versions of their cars, like the Porsche nine one seven LH, short for Langheck, long tail in German. A long, tapering tail lets the air close smoothly behind the car, and cuts drag.""",
     "Porsche 917 LH")
sc("""Less drag meant higher top speed on the straight, and the Porsche nine one seven long tails went well over three hundred fifty kilometres per hour in the early nineteen seventies, on tyres and brakes of that time. The price was stability. A long tail with little downforce could become nervous at speed, and drivers described the car as moving around on the straight.""",
   "Porsche 917 Le Mans 1970", "SPEED VS. STABILITY")
sc("""The idea came back again and again. In the late nineties and in the twenty tens, Le Mans cars still used special low drag bodywork for this one race, different from the rest of the season. Le Mans is so different from other tracks that teams design a separate car for it. The tail tells you which track the car is built for.""",
   "Le Mans prototype rear", "A CAR FOR ONE TRACK")

# ---------- 4. CHICANES ----------
part(4, "The chicanes on the straight", "WHY ARE THERE CORNERS ON THIS STRAIGHT?", "Why Did Le Mans Add Corners to Its Longest Straight?",
     """Why are there two tight chicanes in the middle of the Mulsanne straight? Because the cars became too fast. In nineteen eighty-eight, a WM Peugeot prototype driven by Roger Dorchy was clocked at four hundred five kilometres per hour on the straight. That is still the fastest speed ever recorded at Le Mans.""",
     "Mulsanne straight chicane")
sc("""At those speeds, a tyre failure or a small mistake could be fatal, and the brakes and tyres of the time were at their limit. In nineteen ninety, two chicanes were added to break the straight into three shorter parts. The governing body would no longer approve circuits with straights that long. Top speeds dropped by dozens of kilometres per hour.""",
   "Circuit de la Sarthe", "TOO FAST")
sc("""The chicanes also changed how the cars are built. With more braking zones, brakes and stability under braking became more important, and the special top speed cars disappeared. The famous straight still exists, and you can drive it on a normal day, because it is a public road. But the record of nineteen eighty-eight will probably never be broken there.""",
   "Mulsanne road France", "A RECORD THAT WILL STAND")

# ---------- 5. AIR JACKS ----------
part(5, "The air jacks", "WHY DOES THIS CAR LIFT ITSELF?", "Why Do Le Mans Cars Lift Themselves Up?",
     """Why do Le Mans cars lift themselves off the ground in the pit stop? They have air jacks built in. Small pneumatic legs are hidden inside the car. A mechanic plugs a high pressure air lance into a valve on the bodywork, and the legs shoot down and lift the whole car in a second. No separate jack is needed.""",
     "racing car air jack")
sc("""In endurance racing, the rules allow only a few mechanics to work on the car at the same time, and the car needs fuel, tyres and a driver change in the same stop. Carrying heavy jacks around the car would waste time. With air jacks, one person lifts the car with one movement, and the car drops to the ground the moment the lance is pulled out.""",
   "Le Mans pit stop", "ONE PERSON LIFTS THE CAR")
sc("""Air jacks add weight and complexity, and Formula One does not use them. But in endurance racing, where cars stop dozens of times in one race, they are worth it. Over twenty-four hours, a second saved in every stop adds up to a lap or more. Le Mans can be decided by less than a minute, after more than five thousand kilometres.""",
   "Le Mans finish", "SECONDS INTO LAPS")

# ---------- 6. LED PANELS ----------
part(6, "The glowing panels", "WHY DO THESE NUMBERS LIGHT UP?", "Why Do Le Mans Cars Have Glowing Numbers?",
     """Why do Le Mans cars have glowing panels on their sides? At night, the track is dark, and more than sixty cars of different classes share it. The lit number panels let the marshals, the timing team and the fans identify every car. The colours show the class. In the World Endurance Championship, red is for the top Hypercars, blue for LMP2, and orange for the GT cars.""",
     "Le Mans car number panel night")
sc("""Many cars also carry small LED displays that show their current position in the class. The leader carries a one, the second car a two, and so on, updated live during the race. For a driver coming up behind, it is useful information. Is the car in front fighting for a podium, or is it a back marker that will move aside?""",
   "Le Mans hypercar night", "WHO ARE YOU FIGHTING?")
sc("""Mixed classes are the heart of Le Mans. The fastest cars lap much quicker than the slowest, so they are always overtaking. A Hypercar driver might pass a hundred cars in a single stint. Lights, colours and numbers turn a dark track full of strangers into something every driver can read in a fraction of a second.""",
   "Le Mans night race traffic", "READ IN A SPLIT SECOND")

# ---------- 7. DRIVER CHANGE ----------
part(7, "The driver change", "WHY DO THREE DRIVERS SHARE ONE SEAT?", "Why Do Three Drivers Share One Le Mans Car?",
     """Why do three drivers share one Le Mans car? Because no human can drive at the limit for twenty-four hours. The rules set a maximum time for each driver, and a minimum time too. So during the pit stop, one driver jumps out and the next one jumps in, often in less than a minute, while the car is refuelled.""",
     "Le Mans driver change")
sc("""The drivers are often different heights, but there is only one seat. So each driver has a custom foam insert, moulded to his body, that slides into the seat. The pedals are often adjustable, and the belts are set so the outgoing driver can help strap in the next one. Teams practice driver changes as carefully as tyre changes.""",
   "racing car seat insert", "ONE SEAT, THREE BODIES")
sc("""It used to be even harder. In the early decades, some drivers raced most of the twenty-four hours alone, and in nineteen fifty-two Pierre Levegh tried to drive the whole race by himself. He led until about an hour before the end, when exhaustion led to a mistake and the car broke. Today, rest is part of the strategy.""",
   "Le Mans 1950s", "REST IS STRATEGY")

# ---------- 8. HYBRID ----------
part(8, "The hybrid front axle", "WHY CAN THIS MOTOR ONLY WORK AT HIGH SPEED?", "Why Can a Le Mans Hybrid Motor Only Work Above 190 km/h?",
     """Why can the electric motor of some Le Mans hybrids only push the car above a certain speed? Cars like the Toyota GR zero one zero hybrid have an electric motor on the front wheels. That gives four wheel drive when the motor is working. And four wheel drive is a huge advantage when accelerating out of slow corners, especially in the rain.""",
     "Toyota GR010 Hybrid")
sc("""To keep the racing fair against cars that only drive the rear wheels, the rules say the front motor can only work above a set speed, around one hundred ninety kilometres per hour in the dry. Below that speed, the hybrid car is rear wheel drive like the others. Above it, the electric motor adds its power on the straights.""",
   "Le Mans hypercar straight", "FAIRNESS BY SPEED")
sc("""It is one of the strangest rules in motor racing, and it shows how the class works. Very different cars, built by different manufacturers with different ideas, must be made equal. Engineers design the most efficient car they can. Then the rule makers decide how and when each part is allowed to help.""",
   "Le Mans hypercars", "DIFFERENT CARS, EQUAL CHANCES")

# ---------- 9. BALLAST ----------
part(9, "The hidden ballast", "WHY DO THESE CARS CARRY EXTRA WEIGHT?", "Why Do Le Mans Cars Carry Extra Weight on Purpose?",
     """Why do Le Mans cars carry extra weight on purpose? It is called balance of performance. Because the cars in the top class are so different, with different engines, hybrid systems and shapes, the organisers adjust them to bring them closer. A car that is too fast may get extra ballast, less power, or less energy per stint.""",
     "Le Mans hypercar pit")
sc("""The ballast is usually heavy metal plates bolted low in the car, where they do the least harm to the handling. The numbers are published before each race and change during the season, based on data from every car. Teams spend a lot of time arguing about it, because a few kilograms can mean tenths of a second per lap.""",
   "race car ballast weight", "KILOGRAMS INTO TENTHS")
sc("""Critics say it punishes good engineering. Supporters say it is the only way to have many manufacturers fighting for the win at the same time. Either way, the result is visible. Le Mans now has more top class manufacturers than it has had in decades, Toyota, Ferrari, Porsche, Cadillac, Peugeot, BMW and more.""",
   "Le Mans 2024 hypercar class", "MANY BRANDS, ONE FIGHT")

# ---------- 10. LE MANS START ----------
part(10, "The old Le Mans start", "WHY DID DRIVERS RUN TO THEIR CARS?", "Why Did Le Mans Drivers Run to Their Cars?",
     """Why did Le Mans drivers once run across the track to their cars at the start? This was the famous Le Mans start. The cars were lined up at an angle on one side of the track, and the drivers stood on the other side. When the flag dropped, they ran, jumped in, started the engine and drove away. It was spectacular, and dangerous.""",
     "Le Mans start 1960s")
sc("""To save time, many drivers did not fasten their seat belts properly, planning to do it later on the straight. In nineteen sixty-nine, Jacky Ickx protested by walking slowly to his Ford, fastening his belts carefully, and starting last. On the first lap, driver John Woolfe crashed and was killed. Ickx went on to win the race.""",
   "Jacky Ickx Ford GT40", "HE WALKED")
sc("""The running start was dropped after that. In nineteen seventy, drivers started already strapped in their cars, and from nineteen seventy-one Le Mans used a rolling start behind a pace car. Today the only running at the start is done by the fans. One walk across a track was enough to change a tradition of almost fifty years.""",
   "Le Mans rolling start", "ONE WALK CHANGED IT")

# ---------- VERDICT ----------
sc("""So here are the ten. A shark fin that stops cars from flying. Holes above the wheels that release pressure. Long tails for a long straight, and chicanes to slow it down. Air jacks for fast stops, glowing panels for the night, one seat for three drivers, a hybrid that waits for high speed, hidden ballast for fairness, and a running start that ended with a walk.""",
   "24 Hours of Le Mans", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Le Mans is not only a race. It is a laboratory that runs for twenty-four hours, and every part of these cars has a story written by speed and by accidents. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Le Mans sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:2011 Peugeot 908 Donington Park 2023 01.jpg", 0.22, 0.34),
    2: ("File:Ferrari 499P - Hybrid, 2023.jpg", 0.47, 0.47),
    3: ("File:Porsche 917 LH (1971).jpg", 0.15, 0.35),
    4: ("File:The Mulsanne Straight (5847759679).jpg", 0.6, 0.45),
    5: ("File:United-autosports-le-mans-race-053.jpg", 0.33, 0.6),
    6: ("File:2011 Le Mans 24 Qualifying 03.jpg", 0.55, 0.68),
    7: ("File:Le Mans 1992 Olindo driver change.jpg", 0.55, 0.5),
    8: ("File:2023 6 Hours of Spa-Francorchamps Toyota Gazoo Racing Toyota GR010 Hybrid No.8 (DSC08663).jpg", 0.3, 0.68),
    9: ("File:51 Ferrari AF Corse Ferrari 499P Lone Star Le Mans.jpg", 0.5, 0.62),
    10: ("File:Sportwagenraces Zandvoort Le Mans start, Bestanddeelnr 910-4937.jpg", 0.38, 0.42),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video24", "title": "Why Do Le Mans Cars Have a Fin on Their Back?",
           "length_scale": 1.6, "scenes": S}, open("videos/video24/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
