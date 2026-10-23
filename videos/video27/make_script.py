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
sc("""A set of tyres for a Bugatti Veyron has been reported to cost more than many new cars. An oil change, around twenty thousand dollars. One supercar has its engine bay lined with real gold. Another needs its engine rebuilt like a Formula One car. It sounds like pure luxury. But almost every crazy price has an engineering reason behind it. Today, ten supercar parts that cost more than your car, and why each one exists.""",
   "Bugatti Veyron", "MORE THAN YOUR CAR?", cuts=8, chapter="Intro")
sc("""A normal car is built by the hundreds of thousands. Every part is designed to be cheap to make, by machines, on huge production lines. A supercar is built by the dozens or hundreds, often by hand. Its parts must survive speeds and temperatures no normal car will ever see. Few parts made, extreme demands, and no shortcuts. That is the formula for a crazy price.""",
   "supercar factory", "FEW PARTS, EXTREME DEMANDS")
sc("""As always, every fact here comes from a named source, the manufacturers and automotive references, all listed in the description. And remember, prices are as reported, and they change. Let's start with the tyres.""",
   "supercar wheel", "WHY DOES THIS EXIST?")

# ---------- 1. TYRES ----------
part(1, "The Veyron tyres", "WHY DO THESE TYRES COST SO MUCH?", "Why Do Supercar Parts Cost More Than Your Car?",
     """Why do supercar parts cost more than your car? Start with the tyres of the Bugatti Veyron. The Veyron could go over four hundred kilometres per hour. At that speed, each tyre turns about fifty times per second, and the forces try to tear the rubber apart. No ordinary tyre could survive. Michelin developed special tyres just for this car, and a set of four has been reported to cost tens of thousands of dollars.""",
     "Bugatti Veyron wheel tyre")
sc("""The tyres for the later Bugatti Chiron went even further. To test them at speeds above four hundred kilometres per hour, Michelin reportedly used a test machine originally built for the tyres of the Space Shuttle. Every tyre is checked and certified. At top speed, the Bugatti manual says the tyres last only around fifteen minutes, and the fuel tank empties even faster.""",
   "Bugatti Chiron", "SPACE SHUTTLE TESTED")
sc("""So the price is not just rubber. It is research, testing and a tiny production run, spread over very few cars. A normal tyre is made by the millions, and the development cost almost disappears. A Bugatti tyre is made for a few hundred cars in the world. You are paying for the knowledge that keeps the car on the road at four hundred kilometres per hour.""",
   "Michelin tyre", "YOU PAY FOR THE KNOWLEDGE")

# ---------- 2. OIL CHANGE ----------
part(2, "The oil change", "WHY DOES AN OIL CHANGE COST $20,000?", "Why Does a Bugatti Oil Change Cost $20,000?",
     """Why does an oil change on a Bugatti Veyron reportedly cost around twenty thousand dollars? Because the engine is buried. The Veyron has a sixteen cylinder engine with four turbochargers, packed tightly into the middle of the car. To change the oil, mechanics have to remove the rear wheels, parts of the bodywork and the underbody panels, just to reach the drain plugs.""",
     "Bugatti Veyron engine")
sc("""The engine uses a dry sump lubrication system, like a race car. Instead of a simple pan under the engine, oil is kept in a separate tank and pumped around, so it never runs away from the pump in hard corners. That means more lines, more plugs and more work. The job takes many hours of a specialist technician's time, using special tools and a lot of oil.""",
   "dry sump engine", "A RACE CAR SYSTEM")
sc("""It is the same story for almost every service on a hypercar. Parts are packed so tightly that simple jobs become surgery. Engineers design for speed, cooling and weight first. Ease of repair comes last. When you buy a hypercar, you also buy a relationship with a very expensive service department.""",
   "supercar service workshop", "SPEED FIRST, REPAIRS LAST")

# ---------- 3. GOLD FOIL ----------
part(3, "The gold engine bay", "WHY IS THIS ENGINE BAY LINED WITH GOLD?", "Why Is the McLaren F1 Engine Bay Lined With Gold?",
     """Why is the engine bay of the McLaren F one lined with real gold? Because gold is one of the best materials for reflecting heat. The F one's BMW V twelve engine runs very hot, and it sits right behind the carbon fibre body. Carbon fibre does not like heat. So designer Gordon Murray lined the engine bay with gold foil, to reflect the heat radiating from the engine.""",
     "McLaren F1 engine gold")
sc("""The amount of gold is small, reported at about sixteen grams. But its effect is big. Gold reflects infrared radiation very well, and it does not corrode or tarnish, so it keeps working for decades. The same idea is used in space, where satellites are wrapped in gold coloured foils and astronauts' visors are coated with a thin layer of gold.""",
   "BMW S70 engine", "A TRICK FROM SPACE")
sc("""The McLaren F one was built in the nineteen nineties, in tiny numbers, and was the fastest production car in the world for years. Today it sells for many millions of dollars. Part of its legend is that gold lining. It looks like a rich man's luxury, but it is a heat shield chosen because it was simply the best material for the job.""",
   "McLaren F1", "LUXURY? NO, PHYSICS")

# ---------- 4. CARBON WHEELS ----------
part(4, "The hollow carbon wheels", "WHY ARE THESE WHEELS MADE OF CARBON?", "Why Do Some Supercars Have Carbon Fibre Wheels?",
     """Why do some supercars have wheels made of carbon fibre? Because weight in the wheels is the most expensive weight on a car. Wheels are unsprung mass, weight the suspension has to control, and they also spin, so they resist every acceleration and braking. Koenigsegg makes one piece hollow carbon fibre wheels, much lighter than metal wheels of the same size.""",
     "Koenigsegg carbon wheel")
sc("""A lighter wheel lets the suspension react faster to bumps, so the tyre stays in contact with the road. It also takes less energy to spin up and slow down. Engineers say that a kilogram saved in the wheels is worth much more than a kilogram saved in the body. That is why racing cars always use the lightest wheels the rules allow.""",
   "supercar wheel close up", "THE MOST EXPENSIVE WEIGHT")
sc("""Making them is slow. Each wheel is made of carbon layers placed carefully around a mould, then cured under heat and pressure, and inspected for any hidden flaw. A crack in a wheel at three hundred kilometres per hour would be a disaster. Few cars, slow production and total quality control. That is why a set can cost as much as a family car.""",
   "Koenigsegg Agera", "NO HIDDEN FLAWS")

# ---------- 5. TITANIUM BOLTS ----------
part(5, "The titanium bolts", "WHY ARE THESE BOLTS ENGRAVED?", "Why Does a Pagani Use Titanium Bolts With Its Name?",
     """Why does a Pagani use titanium bolts with the company name engraved on them? Titanium is as strong as many steels, but much lighter, and it does not rust. On a car that is built around saving weight, a thousand small savings add up. Pagani is reported to use more than a thousand titanium bolts in a Huayra, each one engraved with the Pagani name.""",
     "Pagani Huayra")
sc("""Titanium is expensive to make and hard to machine. It wears out cutting tools and must be worked slowly. A titanium bolt can cost many times more than a steel one. Engraving each one adds even more work. For most cars, that would be crazy. For Pagani, it is a signature. The company says every part should be beautiful, even the ones you will never see.""",
   "titanium bolts", "EVEN THE HIDDEN PARTS")
sc("""Horacio Pagani worked on composite parts for Lamborghini before founding his own company, and his cars are built almost like sculpture. The result is a car where both the engineering and the art are paid for by the gram. When people ask why a Pagani costs millions, the answer is in a thousand small details like these bolts.""",
   "Pagani Zonda", "PAID BY THE GRAM")

# ---------- 6. ENGINE PLAQUE ----------
part(6, "The signed engine", "WHY IS THERE A SIGNATURE ON THIS ENGINE?", "Why Do AMG Engines Have a Signature on Them?",
     """Why is there a signature on the engine of a Mercedes AMG? It is the One Man, One Engine philosophy. At the AMG engine factory in Affalterbach, Germany, one technician builds a complete engine from start to finish, and then signs a plaque that is fixed on top of it. The owner can see exactly who built the heart of the car.""",
     "AMG engine plaque")
sc("""A mass production engine is assembled by robots and many workers along a line, each doing one small step. A hand built engine takes much longer, and every builder must be trained for every step. That is part of why these engines cost so much. The builder checks each part as it goes in, and his name on the plaque is a promise of quality.""",
   "Mercedes-AMG V8 engine", "ONE NAME, ONE PROMISE")
sc("""Other makers do similar things. Many supercar and luxury brands build engines by hand in small teams. The signature is also a smart idea for marketing. It turns an engine into a personal object, with a story. But behind it, there is a real reason. High performance engines have tight tolerances, and skilled hands are still one of the best ways to get them right.""",
   "engine assembly by hand", "SKILLED HANDS")

# ---------- 7. AMG ONE ----------
part(7, "The Formula One engine", "WHY DOES THIS ENGINE NEED A REBUILD?", "Why Does the Mercedes-AMG One Need an Engine Rebuild?",
     """Why does the Mercedes AMG One need its engine rebuilt after a set distance? Because it has a real Formula One engine. The AMG One uses a hybrid one point six litre V six derived from the Mercedes Formula One cars that won world championships. That engine revs extremely high and works with electric motors and a complex hybrid system.""",
     "Mercedes-AMG One")
sc("""Formula One engines are built to run at the limit for a limited distance. So the AMG One comes with a strict maintenance plan, including a major engine overhaul after fifty thousand kilometres, done by specialists. Even starting the car is a process, because the engine must warm up before it can run properly. Mercedes needed years to make a race engine work on public roads.""",
   "Formula One hybrid engine", "A RACE ENGINE ON THE ROAD")
sc("""Bringing a Formula One engine to the road was so hard that the project was delayed for years, mostly because of emission rules and idling. A racing engine never has to wait at a red light. The result is one of the most complex road cars ever made, and its servicing is part of what you pay for.""",
   "Mercedes-AMG One rear", "NEVER WAITS AT A RED LIGHT")

# ---------- 8. SPEED KEY ----------
part(8, "The speed key", "WHY DOES THIS CAR NEED A SECOND KEY?", "Why Does a Bugatti Need a Second Key for Top Speed?",
     """Why does a Bugatti need a second key to reach its top speed? Bugatti cars have a special speed key. Without it, the car is limited to a lower top speed. Before reaching the very top, the driver stops, turns the second key in a slot near the seat, and the car checks itself. It lowers its body, changes the rear wing and tells the driver if everything is ready.""",
     "Bugatti Chiron interior")
sc("""The car is changing its shape. At the highest speeds, the Bugatti needs less drag and just the right amount of downforce to stay stable. Running in the wrong mode at those speeds could make the car unstable. So the second key makes the driver think before entering a speed that only a handful of road cars in the world can reach.""",
   "Bugatti Veyron rear wing", "THINK BEFORE YOU GO")
sc("""The key is a symbol too. It tells the owner that the full speed of the car is something special, almost like a vault you open. But the engineering is real. Tyres, aerodynamics and cooling are all at their limits there. A key is the simplest way to make sure the car, and the driver, are ready before going that fast.""",
   "Bugatti Chiron road", "A VAULT OF SPEED")

# ---------- 9. TITANIUM EXHAUST ----------
part(9, "The titanium exhaust", "WHY IS THIS EXHAUST MADE OF TITANIUM?", "Why Do Supercars Have Titanium Exhausts?",
     """Why do many supercars have exhausts made of titanium? Because titanium is light, strong and handles heat well. An exhaust system is a long set of pipes that gets extremely hot, and on a big engine it can be heavy. Switching from steel to titanium can save many kilograms, often at the very back of the car, where weight hurts the handling the most.""",
     "titanium exhaust")
sc("""Titanium is hard to work with. It must be welded in a protected atmosphere, often with inert gas, because hot titanium reacts with the air and becomes weak. Every weld must be done carefully by a skilled welder. That is why a titanium exhaust can cost many thousands of dollars, sometimes more than a used family car.""",
   "titanium welding", "WELDED WITH CARE")
sc("""There is another reason owners love them. Titanium exhausts have a distinctive sound, and they turn blue, purple and gold as they heat up, a colour pattern that fans love to see. It is a part where engineering and emotion meet. Lighter, stronger, louder, and beautiful when it is hot.""",
   "titanium exhaust colour", "LIGHTER AND LOUDER")

# ---------- 10. LASER LIGHTS ----------
part(10, "The laser headlights", "WHY DOES THIS CAR HAVE LASER LIGHTS?", "Why Do Some Cars Have Laser Headlights?",
     """Why do some cars have laser headlights? Because they can light the road much further ahead. In laser headlights, blue lasers shine onto a material that converts the light into intense white light. The light source is tiny and very bright, so the beam can reach several hundred metres, about twice as far as many normal high beams.""",
     "BMW i8 headlight")
sc("""BMW was the first to put laser high beams into a production car, the i eight hybrid sports car, in twenty fourteen. Audi used them on sports cars and luxury models too. The lasers never shine directly out of the car. They are used only inside the headlight to create the white light, which is then shaped into a safe beam.""",
   "BMW i8", "NEVER POINTED AT YOU")
sc("""Headlights are now one of the most expensive parts to replace on a modern car. LED matrix lights with cameras, motors and computers can cost thousands of dollars each. A small crash at the front can cost more than an old car. Better light saves lives at night, but on supercars, even a scratch on the headlight is a costly lesson.""",
   "car LED headlight", "EVEN A SCRATCH IS COSTLY")

# ---------- VERDICT ----------
sc("""So here are the ten. Tyres built for four hundred kilometres per hour. An oil change that needs surgery. A heat shield made of gold. Hollow carbon wheels, titanium bolts with a name, an engine signed by its builder, a Formula One engine that needs a rebuild, a second key for top speed, a titanium exhaust and lasers that light the night.""",
   "hypercars lineup", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""The price of a supercar part is the price of extreme demands, tiny numbers and no shortcuts. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "supercar night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video27", "title": "Why Do Supercar Parts Cost More Than Your Car?",
           "length_scale": 1.6, "scenes": S}, open("videos/video27/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
