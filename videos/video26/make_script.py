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
sc("""The small mirror above your windscreen was first made famous by a racing driver, at the very first Indianapolis five hundred, in nineteen eleven. Your brakes were proven at Le Mans. The paddles behind the steering wheel came from Formula One. Your everyday car is full of parts that were invented, tested or perfected in racing. Today, ten race car parts hiding in your road car, and why each one exists.""",
   "rear view mirror car", "RACE PARTS IN YOUR CAR", cuts=8, chapter="Intro")
sc("""Car makers have an old saying. Win on Sunday, sell on Monday. Racing is the harshest test a part can face. Brakes are used to their limit every lap, engines run at full power for hours, and every gram and every second matters. If an idea survives racing, it can survive your daily commute. And if it wins, the marketing department wants it in the showroom.""",
   "racing car vintage", "WIN ON SUNDAY")
sc("""As always, every fact here comes from a named source, car makers, motorsport history and engineering references, all listed in the description. Let's start with the oldest one, the mirror.""",
   "car interior dashboard", "WHY DOES THIS EXIST?")

# ---------- 1. MIRROR ----------
part(1, "The rear view mirror", "WHY IS THERE A MIRROR HERE?", "Why Does Your Car Have Race Car Parts?",
     """Why does your car have race car parts, starting with the rear view mirror? At the first Indianapolis five hundred, in nineteen eleven, drivers usually carried a riding mechanic, who looked back and warned them about cars coming from behind. Ray Harroun drove his Marmon Wasp alone, a single seater. Instead of a mechanic, he fitted a mirror on a frame above the car.""",
     "Marmon Wasp")
sc("""Harroun won the race, and he is often credited with the first use of a rear view mirror on a car. Other drivers complained that the single seat car was dangerous without a lookout. The mirror was his answer. The vibration on the brick track made the image shake, but it worked well enough to see who was coming.""",
   "Indianapolis 1911", "NO MECHANIC, ONE MIRROR")
sc("""Within a few years, mirrors were being sold as accessories for road cars, and later they became a legal requirement in many countries. Today, cars have three mirrors and often cameras too. But the basic idea is the same as in nineteen eleven. A driver who looks forward still needs to know what is behind.""",
   "car side mirror", "LOOK BEHIND, DRIVE FORWARD")

# ---------- 2. DISC BRAKES ----------
part(2, "The disc brakes", "WHY ARE THESE BRAKES DISCS?", "Why Does Your Car Have Disc Brakes?",
     """Why does your car have disc brakes? Old cars used drum brakes, with shoes pressing on the inside of a metal drum. They worked, but when they got hot from repeated braking, they lost power. Drivers called it brake fade. A disc brake squeezes a flat metal disc between pads, out in the open air, where it cools much better.""",
     "car disc brake")
sc("""Disc brakes were invented long before, but racing made them famous. At Le Mans in nineteen fifty-three, Jaguar raced its C-Type with disc brakes developed with Dunlop. The drivers could brake later and harder, lap after lap, without fade. Jaguar won the race, finishing first and second. Rivals could no longer ignore the discs.""",
   "Jaguar C-Type", "LE MANS 1953")
sc("""Within a few years, disc brakes appeared on road cars, first on fast sports cars and then on family cars. Today, almost every new car has discs at least on the front wheels, where most of the braking happens. When you stop at a red light, you are using an idea that won a twenty-four hour race.""",
   "car front brake disc caliper", "FROM LE MANS TO RED LIGHTS")

# ---------- 3. FUEL INJECTION ----------
part(3, "The fuel injectors", "WHY DOES THIS ENGINE SPRAY FUEL?", "Why Do Car Engines Spray Fuel Instead of Sucking It?",
     """Why do modern car engines spray their fuel instead of sucking it in? For decades, cars used carburettors, which mixed fuel and air using the suction of the engine. They were simple, but not precise. Fuel injection sprays a measured amount of fuel, giving more power, cleaner burning and better economy.""",
     "fuel injector engine")
sc("""One of the first production cars with fuel injection was the Mercedes three hundred SL of nineteen fifty-four, the famous Gullwing. The road car was born from a racing car, the three hundred SL that won Le Mans and the Carrera Panamericana in nineteen fifty-two. Its mechanical injection, made by Bosch, sprayed fuel directly into the cylinders, a technology learned from aircraft engines.""",
   "Mercedes-Benz 300 SL Gullwing", "BORN FROM A RACE CAR")
sc("""For years, injection stayed in expensive cars. Then emission rules arrived, and electronic injection replaced carburettors almost everywhere by the nineteen nineties. Direct injection, the same idea as the Gullwing, is now in millions of ordinary cars. A system for winning races became a system for passing emissions tests.""",
   "modern car engine bay", "FROM RACING TO EMISSIONS")

# ---------- 4. DOHC ----------
part(4, "The twin camshafts", "WHY ARE THERE TWO CAMSHAFTS?", "Why Do Car Engines Have Two Camshafts?",
     """Why do many car engines have two camshafts on top and four valves per cylinder? Because more valves let the engine breathe more air, and more air means more power. That layout was proven in racing more than a century ago, by Peugeot. Its nineteen twelve Grand Prix car had two overhead camshafts and four valves per cylinder.""",
     "double overhead camshaft engine")
sc("""The Peugeot won the French Grand Prix in nineteen twelve, and the Indianapolis five hundred in nineteen thirteen. Engineers around the world studied it. The design let the engine rev higher and breathe better than anything else at the time. Racing engines have used twin camshafts ever since, from Grand Prix cars to motorbikes.""",
   "Peugeot 1912 Grand Prix car", "PEUGEOT 1912")
sc("""In road cars, it took longer, because twin cam engines were more complex and expensive. But from the nineteen eighties, four valve, twin camshaft engines spread to normal family cars. If your car's engine says sixteen valves on the cover, that is a four cylinder engine with four valves each, a direct descendant of a racing car from before the First World War.""",
   "16 valve engine cover", "16 VALVES")

# ---------- 5. DUAL CLUTCH ----------
part(5, "The dual clutch gearbox", "WHY DOES THIS GEARBOX HAVE TWO CLUTCHES?", "Why Do Some Cars Have Two Clutches?",
     """Why do some modern gearboxes have two clutches? It is a dual clutch gearbox. One clutch handles the odd gears, one, three and five. The other handles the even gears, two, four and six. While you drive in one gear, the next one is already selected and waiting. The change is just one clutch opening while the other closes, in a fraction of a second.""",
     "dual clutch transmission")
sc("""The idea was developed for racing. In the nineteen eighties, Porsche used its PDK dual clutch gearbox on the nine five six and nine six two race cars, and Audi tried a dual clutch system on its rally cars. The goal was to keep the turbo spinning and never lose power during a gear change. The early systems were heavy and complex, but they proved the idea.""",
   "Porsche 962", "NO GAP IN THE POWER")
sc("""When electronics became fast and cheap enough, the dual clutch came to the road. Volkswagen launched its DSG gearbox in two thousand three, and Porsche brought PDK back in road cars a few years later. Today you find dual clutch gearboxes in hot hatches, supercars and even small family cars. The gearbox races, even when you are just going to work.""",
   "Volkswagen Golf R32", "IT RACES TO WORK")

# ---------- 6. PADDLES ----------
part(6, "The paddle shifters", "WHY ARE THERE PADDLES BEHIND THE WHEEL?", "Why Do Road Cars Have Paddles Behind the Wheel?",
     """Why do many road cars have paddles behind the steering wheel? They came from Formula One. In nineteen eighty-nine, Ferrari raced the six forty, designed by John Barnard, with a semi automatic gearbox controlled by two paddles behind the wheel. The driver no longer needed a clutch pedal or a gear lever, and could keep both hands on the wheel.""",
     "Ferrari 640")
sc("""Many people expected the system to break, and at first it often did. But Nigel Mansell won the very first race with it, in Brazil. Within a few years, every Formula One team used paddles. Ferrari then brought the idea to the road in nineteen ninety-seven, in the F three five five F one, the name telling buyers exactly where it came from.""",
   "Ferrari F355", "FROM GRID TO SHOWROOM")
sc("""Today, paddles are in cars of every price. In most of them, they control an automatic gearbox, letting the driver choose the gear. They are not always faster than letting the computer decide. But the feeling of clicking a paddle, like a Formula One driver, sells cars. Win on Sunday, sell on Monday.""",
   "steering wheel paddle shifter", "THE FEELING SELLS")

# ---------- 7. CARBON FIBRE ----------
part(7, "The carbon fibre", "WHY IS THIS CAR MADE OF CARBON?", "Why Are Supercars Made of Carbon Fibre?",
     """Why are many supercars built around a carbon fibre shell? Because carbon fibre is extremely stiff and strong for its weight. In nineteen eighty-one, McLaren raced the MP four slash one, the first Formula One car with a chassis made entirely of carbon fibre composite. Rivals worried it would shatter in a crash. Instead, it proved incredibly strong.""",
     "McLaren MP4/1")
sc("""At Monza that year, John Watson crashed heavily and the car broke apart, but the carbon tub around him held, and he walked away. Within a few years, every Formula One car had a carbon fibre chassis. It became one of the biggest safety improvements in the history of the sport, because the survival cell around the driver no longer folded in a crash.""",
   "McLaren Formula One 1980s", "HE WALKED AWAY")
sc("""In nineteen ninety-two, McLaren built the F one road car, one of the first road cars with a full carbon fibre chassis. Today, supercars from McLaren, Ferrari and others use carbon tubs, and carbon panels appear on many sports cars. It is still expensive, because each part is laid by hand and baked. But the material that saved Formula One drivers now holds supercar owners too.""",
   "McLaren F1", "FROM F1 TO THE ROAD")

# ---------- 8. SPOILER ----------
part(8, "The rear spoiler", "WHY DOES THIS CAR HAVE A DUCK TAIL?", "Why Do Some Road Cars Have a Spoiler?",
     """Why do some road cars have a spoiler on the back? On a fast car, air flowing over the curved roof creates lift at the rear, making the back end light and nervous at high speed. A spoiler disturbs that flow and cuts the lift. In nineteen seventy-three, Porsche gave the nine eleven Carrera RS two point seven a famous spoiler called the ducktail.""",
     "Porsche 911 Carrera RS 2.7")
sc("""The Carrera RS was built because of racing rules. To race a car in certain classes, a manufacturer had to sell a minimum number of road versions. It is called homologation. Porsche built the RS with the ducktail so the racing version could use it. The road car sold out, and the ducktail became one of the most famous shapes in car history.""",
   "Porsche 911 ducktail", "BUILT FOR THE RULES")
sc("""Homologation is the reason many legendary road cars exist, from rally specials to race cars with number plates. Today, most spoilers on family cars are small, and some are mostly for style. But on fast cars, they still do the job they were designed for in racing, keeping the rear tyres pressed onto the road.""",
   "car rear spoiler", "THE RULES MADE LEGENDS")

# ---------- 9. ACTIVE SUSPENSION ----------
part(9, "The smart suspension", "WHY CAN THIS SUSPENSION THINK?", "Why Can Modern Car Suspension Think?",
     """Why can the suspension of some modern cars change itself, hundreds of times per second? In the nineteen eighties, Lotus developed active suspension for Formula One, with computers and hydraulic actuators controlling each wheel. The idea was to keep the car at the perfect height and angle, whatever the bumps and corners.""",
     "Lotus 99T")
sc("""In nineteen ninety-two, Williams perfected it on the FW fourteen B, and Nigel Mansell dominated the season. The system worked so well that rival teams could not keep up, and the rules banned active suspension from nineteen ninety-four. Formula One decided that the drivers, not the computers, should control the car.""",
   "Williams FW14B", "TOO GOOD FOR F1")
sc("""On the road, there was no ban. Today, many cars have adaptive dampers that adjust in milliseconds, and some luxury cars use cameras to read the road and prepare the suspension for a bump before it arrives. The ideas that were too good for Formula One are now there to make your ride more comfortable.""",
   "luxury car suspension", "BANNED IN F1, COMFORT FOR YOU")

# ---------- 10. HYBRID ----------
part(10, "The energy recovery", "WHY DOES THIS CAR CHARGE WHEN IT BRAKES?", "Why Do Hybrid Cars Charge When They Brake?",
     """Why do hybrid cars charge their battery when they brake? Braking normally turns the car's energy into heat, wasted in the brakes. A hybrid uses an electric motor as a generator, slowing the car while sending energy back to the battery. Racing turned this idea into a weapon. Formula One introduced its kinetic energy recovery system in two thousand nine.""",
     "hybrid car regenerative braking")
sc("""At Le Mans, hybrid race cars from Audi, Toyota and Porsche won every year from two thousand twelve to twenty twenty-two. The Porsche nine one nine Hybrid won three times in a row. Racing pushed batteries, motors and energy management to extremes, recovering energy at every braking zone and releasing it on every straight.""",
   "Porsche 919 Hybrid", "HYBRIDS WON LE MANS")
sc("""Road cars had regenerative braking before, but racing showed that hybrids could be fast, not just economical. Porsche built the nine one eight Spyder hypercar alongside its Le Mans program. Today, many performance cars are hybrids. The energy you lose every time you stop at a light is now saved, thanks partly to cars that raced through the night.""",
   "Porsche 918 Spyder", "FAST, NOT JUST GREEN")

# ---------- VERDICT ----------
sc("""So here are the ten. A mirror from the first Indianapolis five hundred. Disc brakes that won Le Mans. Fuel injection from a racing Mercedes. Twin camshafts from a Peugeot of nineteen twelve. Two clutches from Porsche race cars, paddles from Ferrari, carbon fibre from McLaren, a ducktail for the rules, a suspension too clever for Formula One, and hybrids that won Le Mans.""",
   "classic racing cars", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Every time you drive, you are using the results of more than a hundred years of racing. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "car highway sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Indianapolis Motor Speedway Museum May 2026 29 (Ray Harroun's 1911 Marmon Wasp).jpg", 0.42, 0.28),
    2: ("File:Disc brakes.jpg", 0.8, 0.35),
    3: ("File:Mercedes 300 SL Engine EMS.jpg", 0.45, 0.35),
    4: ("File:Alfa Romeo 1300 Twin Cam engine.jpg", 0.5, 0.4),
    5: ("File:VW DSG transmission DTMB.jpg", 0.45, 0.45),
    6: ("File:Ferrari 640 front-left Museo Ferrari.jpg", 0.62, 0.3),
    7: ("File:McLaren MP4-1 Carbon Fibre-Kevlar Monocoque Chassis at Formula 1 Exhibition, London.jpg", 0.4, 0.6),
    8: ("File:1973 Porsche 911 Carrera RS 2.7 CHP.jpg", 0.1, 0.45),
    9: ("File:1992 Williams FW14B (49379465223).jpg", 0.33, 0.68),
    10: ("File:FIA WEC Porsche 919 hybrid and 911 RSR , GIMS 2014 (Ank Kumar) 02.jpg", 0.5, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video26", "title": "Why Does Your Road Car Have Race Car Parts?",
           "length_scale": 1.6, "scenes": S}, open("videos/video26/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
