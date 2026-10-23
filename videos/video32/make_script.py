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
sc("""Behind the wheels of many supercars, the brake discs are not shiny steel. They are dark grey, with a strange speckled surface, and they cost more than a used car. They are made of ceramic, the same family of materials as a coffee cup. Today, ten parts of a car's brakes, and why each one exists.""",
   "carbon ceramic brake disc", "WHY CERAMIC?", cuts=8, chapter="Intro")
sc("""Brakes have one job that sounds simple. Turn the speed of the car into heat, and get rid of that heat. A heavy car stopping from high speed produces enough heat to make the discs glow. Every clever part of a modern brake is about handling that heat, without losing grip, weight or control.""",
   "brake disc glowing", "SPEED BECOMES HEAT")
sc("""As always, every fact here comes from a named source, the car makers, brake makers and automotive references, all listed in the description. Let's start with the ceramic disc.""",
   "supercar brakes", "WHY DOES THIS EXIST?")

# ---------- 1. CERAMIC ----------
part(1, "The ceramic disc", "WHY IS THIS BRAKE DISC MADE OF CERAMIC?", "Why Are Supercar Brakes Made of Ceramic?",
     """Why are supercar brake discs made of ceramic? Because they handle heat better and weigh much less. A carbon ceramic disc is made of carbon fibres mixed into a ceramic material called silicon carbide. It stays strong at temperatures that would make an iron disc lose its grip, and it weighs about half as much as an iron disc of the same size.""",
     "carbon ceramic brake disc")
sc("""When iron brakes get too hot after repeated hard stops, they start to fade. The pedal goes soft and the car takes longer to stop. Carbon ceramic discs resist fade much better, so the brakes feel the same on the tenth hard stop as on the first. On a race track, that is the difference between confidence and fear.""",
   "Porsche ceramic brakes", "NO FADE")
sc("""The lower weight matters too. The discs are part of the unsprung weight, the weight that the suspension has to control as the wheel moves up and down. Lighter discs help the wheels follow the road. Porsche marks its ceramic brakes with yellow calipers, so you can spot them from the street.""",
   "Porsche yellow brake caliper", "YELLOW MEANS CERAMIC")

# ---------- 2. DRILLED ----------
part(2, "The holes in the disc", "WHY DOES THIS BRAKE DISC HAVE HOLES?", "Why Do Some Brake Discs Have Holes?",
     """Why do some brake discs have holes drilled in them? In the past, brake pads could release gas when they got very hot. That gas formed a thin layer between the pad and the disc, like a cushion, and reduced the grip. The holes gave the gas, and also water, a place to escape.""",
     "drilled brake disc")
sc("""Modern pads release much less gas, but the holes still help. They let water escape in the rain, they clean the surface of the pad, and they save a little weight. Some discs use slots instead of holes, curved grooves that sweep the pad clean with every turn.""",
   "slotted brake disc", "HOLES OR SLOTS")
sc("""Holes also have a downside. Each hole is a weak point, and under extreme heat, small cracks can start around them. That is why many race cars use slotted discs rather than drilled ones. On a road car, the holes are often there because they work well enough and look fast.""",
   "brake disc", "A WEAK POINT")

# ---------- 3. CALIPER ----------
part(3, "The six piston caliper", "WHY DOES THIS BRAKE HAVE SIX PISTONS?", "Why Do Supercar Brakes Have So Many Pistons?",
     """Why does a supercar brake caliper have six or more pistons? The caliper is the part that squeezes the pads against the disc. A basic car has one piston pushing on one side. A big supercar pad is long, and one piston would push hard in the middle and weakly at the ends.""",
     "brake caliper six piston")
sc("""Several smaller pistons spread the force evenly along the whole pad. The pad wears more evenly and grips with its full surface. The pistons can even be different sizes, smaller at the front of the pad and larger at the back, because the front edge of a pad tends to wear faster.""",
   "Brembo brake caliper", "EVEN PRESSURE")
sc("""High performance calipers are often made from one solid block of aluminium, called a monoblock. Without a joint in the middle, the caliper bends less under huge forces, so the pedal feels firm and precise. Less flex means the driver feels exactly how hard the car is braking.""",
   "monoblock caliper", "ONE SOLID BLOCK")

# ---------- 4. VENTED ----------
part(4, "The vented disc", "WHY IS THIS BRAKE DISC HOLLOW?", "Why Are Brake Discs Hollow Inside?",
     """Why is a brake disc hollow inside? Look at the edge of most front discs, and you will see two plates with gaps between them. Inside are curved walls called vanes. As the disc spins, the vanes act like a fan, pulling air from the centre and throwing it out of the edge.""",
     "ventilated brake disc")
sc("""That moving air carries heat away from the inside of the disc, so it cools much faster than a solid disc. Front brakes do most of the stopping work, because the car's weight moves forward when it brakes. That is why many cars have vented discs at the front and simpler solid discs at the back.""",
   "brake disc vanes", "A FAN INSIDE")
sc("""On high performance discs, the vanes can be curved in one direction, which means the left and right discs are different parts. Fit them on the wrong side, and the fan blows the wrong way. It is a small reminder that even the inside of a disc is carefully designed.""",
   "directional brake disc", "LEFT AND RIGHT")

# ---------- 5. BRAKE DUCTS ----------
part(5, "The brake ducts", "WHY DOES THIS BUMPER HAVE A HOLE?", "Why Do Fast Cars Have Holes for the Brakes?",
     """Why do many fast cars have openings in the front bumper that lead to the wheels? They are brake ducts. They catch cool air at the front of the car and blow it straight at the brakes. On a race track, the brakes can get so hot that the extra air makes a real difference.""",
     "brake cooling duct")
sc("""The duct sends air into the centre of the vented disc, where the vanes pull it through. Too little air and the brakes overheat. Too much air and the brakes may run too cold to grip properly, and the duct adds drag. Race teams change the size of the ducts for each track.""",
   "race car brake duct", "NOT TOO HOT, NOT TOO COLD")
sc("""On road cars, the ducts are usually smaller, but the idea is the same. Some cars even open and close flaps to change the cooling. The brakes are one of the most important things the front of the car has to feed with air.""",
   "front bumper air intake", "FEEDING THE BRAKES")

# ---------- 6. SQUEALER ----------
part(6, "The squealer tab", "WHY DO WORN BRAKES SQUEAL?", "Why Do Brakes Squeal When They Are Worn?",
     """Why do brakes squeal when the pads are worn out? Often, it is on purpose. Many brake pads have a small metal tab on the back plate. When the pad wears down close to its limit, the tab touches the disc and makes a high pitched squeal. It is an alarm that does not need any electronics.""",
     "brake pad wear indicator")
sc("""If the driver ignored it and kept driving, the pad would wear down to its metal backing, which would grind into the disc and damage it. The squeal gives the driver time to replace the pads before that happens. Many modern cars also use an electrical sensor that lights a warning on the dashboard.""",
   "worn brake pad", "AN ALARM WITHOUT ELECTRONICS")
sc("""Not every squeal means worn pads. Brakes can also squeal from vibration, dust or moisture, especially on a cold morning. But if a high pitched sound appears and does not go away, the little tab may be doing its job. It is a very cheap part that saves very expensive ones.""",
   "brake pads", "A CHEAP PART SAVES EXPENSIVE ONES")

# ---------- 7. ABS ----------
part(7, "The ABS ring", "WHY DOES THIS RING HAVE TEETH?", "Why Do Cars Have ABS Rings With Teeth?",
     """Why is there a ring with teeth near each wheel of your car? It is part of the anti lock braking system. A sensor counts the teeth as they pass, and that tells the car how fast each wheel is turning. If one wheel suddenly slows much faster than the others, it is about to lock.""",
     "ABS sensor ring")
sc("""A locked wheel slides instead of rolling, and a sliding tyre cannot steer. In an emergency stop, the car would go straight even if you turned the wheel. The anti lock system releases and reapplies the pressure on that wheel many times per second, keeping it at the edge of grip. That is the buzzing you feel in the pedal.""",
   "anti-lock braking system", "STEER WHILE YOU BRAKE")
sc("""Electronic anti lock brakes arrived on a production car in nineteen seventy-eight, on the Mercedes S Class, developed with Bosch. Today they are standard, and the same wheel sensors feed stability control, which can brake single wheels to keep the car from spinning. A ring of teeth became the base of modern car safety.""",
   "Mercedes-Benz W116", "THE BASE OF MODERN SAFETY")

# ---------- 8. BRAKE FLUID ----------
part(8, "The brake fluid", "WHY DOES THIS FLUID NEED CHANGING?", "Why Does Brake Fluid Need Changing?",
     """Why does brake fluid need to be changed every few years? The fluid carries the force of your foot to the brakes. It can do that because liquids do not compress. But brake fluid slowly absorbs water from the air, through the hoses and seals, even when the system is closed.""",
     "brake fluid reservoir")
sc("""Water lowers the boiling point of the fluid. Fresh fluid boils at well over two hundred degrees, but with some water in it, the boiling point can drop a lot. During hard braking, the heat from the brakes travels into the fluid. If it boils, it forms gas bubbles, and gas does compress.""",
   "brake fluid", "BUBBLES COMPRESS")
sc("""The result is a pedal that suddenly goes soft and sinks towards the floor, exactly when you need the brakes most. That is why car makers recommend changing the fluid on a schedule, often every two years. A cheap liquid, quietly protecting the most important system in the car.""",
   "brake pedal", "A SOFT PEDAL")

# ---------- 9. F1 BRAKES ----------
part(9, "The glowing F1 brakes", "WHY DO THESE BRAKES GLOW RED?", "Why Do Formula 1 Brakes Glow Red?",
     """Why do Formula One brakes glow red when the car slows down? Because they are made of carbon carbon, a material that works best when it is extremely hot. The discs can reach around one thousand degrees during hard braking. At that temperature, they shine like the coils in a toaster.""",
     "F1 brake disc glowing")
sc("""Carbon carbon brakes have a strange problem. When they are cold, they barely grip. Drivers have to warm them up, and the cars use ducts and covers to keep them in the right temperature window. Each disc is drilled with hundreds of tiny holes to cool it from the inside.""",
   "Formula One brakes", "TOO COLD TO GRIP")
sc("""When they are hot, the deceleration is brutal. A Formula One car can slow down with a force of around five times its own weight, pushing the driver into the belts. It is why carbon ceramic road brakes exist, a version of the same idea that also works when cold.""",
   "Formula One car braking", "FIVE TIMES ITS WEIGHT")

# ---------- 10. REGEN ----------
part(10, "The motor that brakes", "WHY DO ELECTRIC CARS BARELY USE THEIR BRAKES?", "Why Do Electric Cars Barely Use Their Brakes?",
     """Why do electric cars barely use their brake discs? Because the electric motor can work in reverse. When you lift your foot, the motor becomes a generator. The wheels turn it, and it makes electricity that goes back into the battery. That resistance slows the car down, without touching the discs.""",
     "regenerative braking")
sc("""Instead of turning the car's speed into wasted heat, regenerative braking turns part of it back into energy. In city traffic, with many stops, this can add a lot of range. Many drivers learn to drive with one pedal, slowing down just by lifting off the accelerator.""",
   "electric car", "ENERGY BACK INTO THE BATTERY")
sc("""The irony is that the brakes can now suffer from being used too little. Iron discs that rarely get hot can rust and lose their smooth surface. Some electric cars use the brakes on purpose from time to time, just to keep them clean. After a century of fighting heat, brakes now sometimes need a little more of it.""",
   "rusty brake disc", "USED TOO LITTLE")

# ---------- VERDICT ----------
sc("""So here are the ten. Ceramic discs that resist heat and weigh half as much. Holes and slots that let gas and water escape. Many pistons for even pressure. Hollow discs with fans inside. Ducts that feed them air. A tab that squeals when the pad is worn. A toothed ring that stops wheels from locking. Fluid that must stay dry. Carbon brakes that glow. And motors that brake by charging the battery.""",
   "brake disc", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Speed is easy. Stopping is the real engineering. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which car has the best brakes you have ever felt.""",
   "supercar night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video32", "title": "Why Are Supercar Brakes Made of Ceramic?",
           "length_scale": 1.6, "scenes": S}, open("videos/video32/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
