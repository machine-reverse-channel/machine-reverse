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
sc("""The steering wheel of a Formula One car has more than twenty buttons, dials and switches, a screen in the middle and paddles behind it. And the driver uses them at three hundred kilometres per hour, with one thumb, between corners. It is not a steering wheel. It is the control room of the car. Today, ten parts of the F1 cockpit, and why each one exists, starting with the wheel.""",
   "Formula One steering wheel", "WHY SO MANY BUTTONS?", cuts=8, chapter="Intro")
sc("""The cockpit of a Formula One car is a tiny carbon fibre tub. The driver lies almost flat, with the feet higher than the hips, wrapped in a seat shaped to his body. There is no room for anything that does not have a job. Every button, every strap and every piece of clothing in there was designed for speed, or written into the rules after someone got hurt.""",
   "Formula One cockpit", "NO ROOM FOR ANYTHING USELESS")
sc("""As always, every fact here comes from a named source, the FIA, Formula One and motorsport references, all listed in the description. Let's take the wheel off and look closer.""",
   "Formula One car driver", "WHY DOES THIS EXIST?")

# ---------- 1. STEERING WHEEL ----------
part(1, "The steering wheel", "WHY DOES THIS WHEEL HAVE SO MANY BUTTONS?", "Why Does an F1 Steering Wheel Have So Many Buttons?",
     """Why does an F1 steering wheel have so many buttons? Because the driver is also the engineer on board. A modern Formula One car is a hybrid, with a turbo engine, electric motors and a battery. The driver can change how the engine delivers power, how the battery is used, how the brakes are balanced and how the differential behaves, corner by corner. All of that is done from the wheel.""",
     "Formula One steering wheel buttons")
sc("""Some buttons are simple. One for the radio, one for the pit lane speed limiter, one to confirm a message, one for neutral. Others change whole maps of settings with a single click. Every team designs its own wheel, and each driver can ask for buttons in different places, for his own thumbs. Each wheel is a handmade carbon fibre computer, reported to cost tens of thousands of dollars.""",
   "Formula One steering wheel display", "A COMPUTER YOU STEER")
sc("""Drivers spend hours in the simulator learning the wheel, until the movements are automatic. During the race, the engineer on the radio may say a code, like a mode number, and the driver changes it without looking down. The most important skill is not knowing every button. It is knowing which one to press, at three hundred kilometres per hour, without losing a tenth.""",
   "Formula One simulator", "WITHOUT LOOKING DOWN")

# ---------- 2. DIALS ----------
part(2, "The rotary dials", "WHY DOES THE DRIVER TURN THESE DIALS?", "Why Do F1 Drivers Keep Turning Dials on the Wheel?",
     """Why do F1 drivers keep turning small dials on the wheel during a lap? One of the most used is brake balance. It decides how much braking goes to the front wheels and how much to the rear. As the fuel burns and the tyres wear, the car changes. A balance that was perfect on lap one can lock the front wheels on lap forty. So the driver adjusts it, sometimes for a single corner.""",
     "Formula One steering wheel rotary switch")
sc("""Another dial controls the differential, the part that lets the two rear wheels turn at different speeds in a corner. More locked helps traction out of slow corners. More open helps the car turn in. Drivers change it between corners, and on some cars the setting even changes automatically at different points of the corner, entry, middle and exit.""",
   "Formula One car corner exit", "ONE SETTING PER CORNER")
sc("""Other dials manage the hybrid system, how much energy the electric motor gives and how much it takes back under braking. Watch an onboard camera closely, and you will see the driver's thumbs moving on almost every straight. They are not playing. They are tuning a race car while racing it.""",
   "Formula One onboard camera", "TUNING WHILE RACING")

# ---------- 3. PADDLES ----------
part(3, "The paddles", "WHY ARE THERE PADDLES BEHIND THE WHEEL?", "Why Does an F1 Car Have Two Clutch Paddles?",
     """Why are there paddles behind an F1 steering wheel? The top ones change gear. Right paddle up, left paddle down, through eight forward gears. A modern F1 gearbox changes gear in a few thousandths of a second, so fast that there is almost no gap in the power. The driver never takes his hands off the wheel, and there is no gear lever in the cockpit at all.""",
     "Formula One steering wheel paddles")
sc("""The lower paddles are the clutch, and there are often two of them. The clutch is only used to start, at the race start and leaving a pit stop. Before the lights go out, the driver holds one paddle at the perfect bite point and the other fully in. When the lights go out, he lets go of the second paddle, and the car launches from the bite point.""",
   "Formula One race start grid", "TWO CLUTCHES, ONE START")
sc("""Getting that bite point right is one of the hardest skills in the sport. Too much and the wheels spin. Too little and the engine bogs down. The rules banned electronic launch control, so the start depends on the driver's fingers. Races have been won and lost in the first two seconds, on a paddle behind the wheel.""",
   "Formula One start lights", "WON IN TWO SECONDS")

# ---------- 4. QUICK RELEASE ----------
part(4, "The quick release", "WHY DOES THE WHEEL COME OFF?", "Why Do F1 Drivers Take the Steering Wheel Off?",
     """Why do F1 drivers pull the steering wheel off when they get out? Because the cockpit is so tight that a driver cannot climb out with the wheel in place. Behind the wheel there is a quick release hub. The driver pulls a collar, and the wheel slides off the column. The rules require a driver to be able to get out of the car in five seconds.""",
     "Formula One steering wheel quick release")
sc("""The five second test is done with full racing gear, helmet, gloves and belts. It exists for fire and for crashes. A driver who is trapped in a burning car has seconds, not minutes. The wheel comes off, the six point harness opens with one twist of the buckle, and the driver jumps out over the sides of the cockpit.""",
   "Formula One driver getting out of car", "FIVE SECONDS TO GET OUT")
sc("""When drivers stop their car on the track, you will often see them put the wheel back on before walking away. That is because marshals may need to push or steer the car off the track, and the car cannot be steered without the wheel. A small habit, but it is in the rules too.""",
   "Formula One marshals pushing car", "PUT IT BACK")

# ---------- 5. SHIFT LIGHTS ----------
part(5, "The lights on the wheel", "WHY DO THESE LIGHTS FLASH?", "Why Do Lights Flash on an F1 Steering Wheel?",
     """Why does a row of coloured lights flash at the top of the F1 steering wheel? These are the shift lights. As the engine revs climb, the lights fill up from one side to the other, and when they all flash, it is the perfect moment to change gear. The driver does not look at a number. His eyes stay on the track and he sees the colours in his peripheral vision.""",
     "Formula One steering wheel shift lights")
sc("""The car also has lights for the race officials. Small panels in the cockpit light up yellow, blue, red, or the colour of the safety car, at the same moment the flags are shown on the side of the track. A driver might miss a flag waved by a marshal in a fast corner, so the flag comes into the cockpit too.""",
   "Formula One marshal flag", "THE FLAG IN THE COCKPIT")
sc("""And on the screen in the middle of the wheel, the driver can see lap times, the gap to other cars, tyre temperatures and warnings. Teams customise the screen pages, so each driver sees what he wants, where he wants it. All this information has to be readable in one glance, at the end of a straight, with a vibrating helmet.""",
   "Formula One steering wheel screen", "ONE GLANCE")

# ---------- 6. DRINK BUTTON ----------
part(6, "The drink button", "WHY IS THERE A DRINK BUTTON?", "Why Is There a Drink Button in an F1 Car?",
     """Why is there a drink button on an F1 steering wheel? Because drivers lose a lot of water. In a hot race like Singapore, with high humidity and almost two hours of driving, a driver can lose around three kilograms of body weight, mostly sweat. A bottle sits inside the car, and a tube runs into the helmet. Press the button, and a pump sends a sip of drink to the driver's mouth.""",
     "Formula One driver helmet")
sc("""The system does not always work. Sometimes the pump fails, and the driver has nothing to drink for the whole race. And the drink is often hot, because the bottle sits in a cockpit that can be well above forty degrees in a hot race. Drivers describe it as drinking hot tea while running a marathon.""",
   "Singapore Grand Prix night", "HOT TEA, FULL SPEED")
sc("""Dehydration is dangerous in a race car. A small loss of water can slow reactions and focus, and in Formula One a tenth of a second of reaction is several metres of track. So the teams weigh drivers before and after races, and plan exactly how much they should drink before the start. Even water has a strategy in Formula One.""",
   "Formula One driver podium", "EVEN WATER HAS A STRATEGY")

# ---------- 7. SEAT ----------
part(7, "The extraction seat", "WHY DOES THE SEAT COME OUT WITH THE DRIVER?", "Why Does an F1 Seat Come Out With the Driver in It?",
     """Why does an F1 seat come out of the car with the driver still in it? Each seat is a hard carbon fibre shell, moulded to the exact shape of one driver's body. And it is designed to be lifted out in one piece. If a driver is injured in a crash, the medical team can take him out still strapped into the seat, without bending his back or neck.""",
     "Formula One seat")
sc("""Back and neck injuries are the biggest fear after a heavy crash, because a wrong movement can turn a fracture into paralysis. With the extraction seat, the seat itself becomes the stretcher. Medical teams practice this procedure at every race, on real cars, so they can do it in minutes on any track.""",
   "Formula One medical car", "THE SEAT IS THE STRETCHER")
sc("""Making the seat is a ritual for every new driver. He sits in a bag of liquid foam inside the car, in his racing position, until the foam hardens around his body. That shape becomes the mould for the carbon seat. It fits so closely that the driver feels every bump of the track through it, which is exactly what he needs to feel the car.""",
   "Formula One driver seat fitting", "MOULDED TO ONE BODY")

# ---------- 8. HANS ----------
part(8, "The HANS device", "WHY DO DRIVERS WEAR THIS COLLAR?", "Why Do Race Drivers Wear This Collar?",
     """Why do race car drivers wear this carbon collar on their shoulders? It is the HANS device, short for head and neck support. Two straps connect the back of the helmet to the collar, which sits under the shoulder belts. In a sudden stop, the body is held by the belts, but the head keeps moving forward. HANS holds the head back with the body.""",
     "HANS device")
sc("""Without it, the neck can be stretched so violently that the base of the skull fractures. It is called a basilar skull fracture, and it killed several drivers. The device was developed in the nineteen eighties by Robert Hubbard, an engineering professor, and his brother in law Jim Downing, a racing driver. For years few drivers used it.""",
   "racing driver helmet HANS", "HELD BACK WITH THE BODY")
sc("""Then, in two thousand one, NASCAR legend Dale Earnhardt died of a basilar skull fracture at the Daytona five hundred. After that, series around the world made it mandatory. Formula One made HANS compulsory from two thousand three. Today no top racing driver starts a race without it. A collar on the shoulders is the reason many drivers walked away from crashes.""",
   "NASCAR Daytona 500", "A COLLAR THAT SAVES LIVES")

# ---------- 9. RACE SUIT ----------
part(9, "The race suit", "WHY DOESN'T THIS SUIT BURN?", "Why Don't F1 Race Suits Burn?",
     """Why don't F1 race suits catch fire? They are made of layers of a fire resistant fibre called Nomex, the same family of material used by firefighters. The suits are tested to protect against direct flame for several seconds, enough for a driver to escape. Underneath, drivers wear fireproof underwear, socks, a balaclava and gloves. Every layer is certified by the FIA.""",
     "Formula One race suit")
sc("""In twenty twenty, at the Bahrain Grand Prix, Romain Grosjean's car hit a barrier at more than two hundred kilometres per hour, split in two and exploded into flames. He was inside the fire for almost thirty seconds. He climbed out with burns on his hands. His suit, his helmet, the halo over his head and the fire marshals all did their job that day.""",
   "Romain Grosjean Haas", "28 SECONDS IN FIRE")
sc("""Every race suit also has two handles on the shoulders. They are there so that marshals and doctors can pull a driver out of the car, even if he is unconscious. The suits are surprisingly light, around a kilogram, because a heavier suit means more heat and more sweat. The race suit is a compromise between a furnace and a sauna.""",
   "Formula One driver race suit shoulders", "HANDLES TO PULL YOU OUT")

# ---------- 10. GLOVES ----------
part(10, "The biometric gloves", "WHY DO THESE GLOVES HAVE A SENSOR?", "Why Do F1 Gloves Measure the Driver's Pulse?",
     """Why do F1 drivers' gloves have a sensor inside? Since twenty eighteen, Formula One drivers wear biometric gloves. A small sensor, sewn into the glove, measures the driver's pulse and the oxygen in his blood, and sends it by radio to the medical team. After a big crash, before anyone reaches the car, the doctors already know if the driver's heart is working.""",
     "Formula One driver gloves")
sc("""It is a reaction to a simple problem. After a crash, the car may be upside down or in a barrier, and the driver may not be able to speak on the radio. With the glove sensor, the medical car can decide how urgent it is while it is still driving to the scene. And the data are also used to study how drivers' bodies react to crashes and to the stress of racing.""",
   "Formula One medical car track", "THE DOCTOR KNOWS FIRST")
sc("""The gloves still have to be perfect for driving. They are thin, so the driver can feel the buttons on the wheel, and fireproof, like the rest of his clothes. The sensor is the size of a coin and almost weightless. In Formula One, even the gloves are connected to the internet of the race.""",
   "Formula One driver hands steering wheel", "EVEN THE GLOVES ARE CONNECTED")

# ---------- VERDICT ----------
sc("""So here are the ten. A wheel full of buttons because the driver is also the engineer. Dials for brake balance and the differential. Paddles for gears and two clutches for the start. A wheel that comes off in seconds. Lights that say when to shift, a drink button, a seat that becomes a stretcher, a collar for the neck, a suit that does not burn, and gloves that check your heart.""",
   "Formula One cockpit driver", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""In the cockpit of a Formula One car, every object has two jobs, to make the driver faster and to bring him home. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Formula One car race", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Caterham steering wheel at Goodwood 2012.jpg", 0.5, 0.45),
    2: ("File:Toyota F1 steering wheel (3649850169).jpg", 0.47, 0.55),
    3: ("File:Toyota 86 GT - Paddle shifter.jpg", 0.48, 0.42),
    4: ("File:Geneva Motor Show 2011 - Renault RB7 F1 Car Steering Wheel (5577393685).jpg", 0.3, 0.45),
    5: ("File:Alpine F1 steering wheel.jpg", 0.5, 0.18),
    6: ("File:Toyota steering wheel 1.jpg", 0.63, 0.81),
    7: ("File:Ferrari F1 (5356124552).jpg", 0.3, 0.5),
    8: ("File:Ken SchraderHANSdevice.jpg", 0.85, 0.45),
    9: ("File:Andy Priaulx 2007 Curitiba qualify.jpg", 0.35, 0.65),
    10: ("File:Puma Furio Nomex Racing Gloves.JPG", 0.55, 0.45),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video22", "title": "Why Does an F1 Steering Wheel Have So Many Buttons?",
           "length_scale": 1.6, "scenes": S}, open("videos/video22/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
