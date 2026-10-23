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
sc("""In nineteen eighty-six, a Boeing seven twenty-seven took off from Mexico City. Minutes later, one of its tires exploded inside the wheel well, and the plane was lost with everyone on board. The tire was filled with ordinary air. Today, the tires on every big airliner are filled with something else. Why? And why don't airplane tires explode when they slam into the runway at more than one hundred fifty miles an hour? Today, ten landing gear secrets hidden in plain sight.""",
   "airliner landing gear touchdown", "10 LANDING GEAR SECRETS", cuts=8, chapter="Intro")
sc("""The landing gear is the only part of an airplane that has to work as a car, a shock absorber, a brake, and a crash structure, sometimes in the same second. It is folded away for the whole flight, frozen at altitude, and then it has to unfold, lock, and catch a machine that can weigh hundreds of tons. Almost every strange detail on it exists because something, at some point, went wrong.""",
   "Boeing 777 main landing gear", "THE HARDEST JOB ON THE PLANE")
sc("""As always, every number in this video comes from a named source, the Federal Aviation Administration rules, official accident reports, and the manufacturers, and all of them are listed in the description. Let's start with the question in the title, and with what is really inside an airplane tire.""",
   "aircraft tire close up", "WHY DOES THIS EXIST?")

# ---------- 1. NITROGEN ----------
part(1, "The gas inside the tires", "WHY IS THIS TIRE FULL OF NITROGEN?", "Why Are Airplane Tires Filled With Nitrogen?",
     """Why are airliner tires filled with nitrogen instead of air? Because air contains oxygen, and oxygen can turn an overheated tire into a bomb. When brakes get extremely hot, the rubber inside the tire can release flammable gases. Mix those with oxygen under high pressure and heat, and the tire can explode. Nitrogen is inert. It does not feed a fire. So under United States certification rules, the tires on braked wheels of airliners heavier than seventy-five thousand pounds must be filled with dry nitrogen, or a gas with no more than five percent oxygen.""",
     "aircraft tire nitrogen")
sc("""That rule was written after Mexicana Flight nine forty. On March thirty-first, nineteen eighty-six, a brake on the left main gear of the Boeing seven twenty-seven was dragging during takeoff. It overheated one tire, which had been filled with ordinary air. The tire exploded in the wheel well, cut fuel and hydraulic lines, and started a fire that destroyed the airplane in flight. One hundred sixty-seven people died. About a year later, the Federal Aviation Administration required nitrogen in airliner tires.""",
   "Boeing 727 Mexicana", "167 LIVES. ONE GAS.")
sc("""Nitrogen has a second advantage. Dry nitrogen carries no moisture, so it does not freeze into ice inside the tire at minus fifty degrees at cruising altitude, and it does not corrode the wheel from the inside. So the gas in an airplane tire is chosen for fire, for cold, and for rust, all at once.""",
   "aircraft wheel tire maintenance", "FIRE, ICE AND RUST")

# ---------- 2. FUSIBLE PLUGS ----------
part(2, "The plugs that melt", "WHY DOES THIS WHEEL HAVE PLUGS THAT MELT?", "Why Do Airplane Wheels Have Plugs That Melt?",
     """Why do airplane wheels have small metal plugs designed to melt? Because the most dangerous moment for a tire is not the landing. It is a few minutes after a hard stop, when all the heat from the brakes soaks into the wheel. The gas inside heats up, the pressure climbs, and the tire can burst. So the wheel has fusible plugs, small threaded plugs with a core of low melting point metal. If the wheel gets too hot, the core melts and the tire deflates slowly instead of exploding.""",
     "aircraft wheel fusible plug")
sc("""A flat tire after an emergency stop is not a failure. It is the system working. Ground crews know that after a rejected takeoff, they should approach the wheels from the front or the back, never from the side, in case a tire or a wheel lets go. And the escaping nitrogen even helps cool the brakes. Some heavy jets also have brake temperature sensors, so the pilots can see the heat building up before it becomes a problem.""",
   "airport fire truck aircraft brakes", "A FLAT TIRE ON PURPOSE")

sc("""The numbers are extreme. An airliner tire is inflated to around two hundred pounds per square inch, roughly six times the pressure of a car tire, and it has to carry many tons each. The main tires of a Boeing seven thirty-seven next generation are rated for two hundred twenty-five miles an hour. And yet the same tire might do a few hundred landings before it needs a new tread.""",
   "aircraft main gear tires", "6 TIMES A CAR TIRE")

# ---------- 3. GROOVES ----------
part(3, "The straight grooves", "WHY DON'T THESE TIRES HAVE TREAD?", "Why Don't Airplane Tires Have Tread Like Car Tires?",
     """Why does an airplane tire have only a few straight grooves, and no tread pattern like a car tire? Because an airplane tire does not need to grip in every direction. It mostly rolls straight, at very high speed, and its biggest enemy is water. The straight grooves around the tire give rain a channel to escape, so the tire stays in contact with the runway instead of riding on a film of water. That is called hydroplaning, and it is one of the main reasons planes slide off wet runways.""",
     "aircraft tire tread grooves")
sc("""The grooves are also a wear gauge. When the tire wears down to the bottom of a groove, it is replaced. And airliner tires are retreaded, meaning the worn rubber is removed and a new tread is bonded onto the old casing, often several times. The casing of an airliner tire is a heavily layered structure built to carry a huge load, so throwing it away after one tread would be a waste.""",
   "aircraft tires stack maintenance", "BUILT TO BE REBUILT")
sc("""Runways help too. Many runways are grooved across their width, with thin cuts in the concrete, so water drains out sideways. Between the tire grooves and the runway grooves, a heavy jet can stop on a wet runway that would make a car slide.""",
   "grooved runway", "THE RUNWAY HAS GROOVES TOO")

# ---------- 4. OLEO STRUT ----------
part(4, "The shiny piston", "WHY IS THIS LEG FULL OF OIL AND GAS?", "Why Is an Airplane's Landing Gear Full of Oil?",
     """Why is there a shiny chrome piston on every landing gear leg? Because that is the shock absorber, and it is filled with oil and nitrogen. It is called an oleo strut. When the airplane touches down, the piston is pushed up into the cylinder. The nitrogen is compressed and works as a spring. At the same time, oil is forced through a small hole, and that turns the energy of the landing into heat. A metal spring would bounce the plane back into the air. The oil does not.""",
     "oleo strut landing gear")
sc("""The basic design was patented by the British company Vickers in nineteen fifteen, borrowed from the recoil system of a gun. More than a hundred years later, the shock absorbers of the biggest airliners still work on the same principle. The shiny part you can see is the piston, and that is why mechanics keep it perfectly clean. A scratch on it can damage the seals and let the oil leak out.""",
   "aircraft landing gear strut chrome", "SAME IDEA SINCE 1915")

sc("""Big airliners take this idea further. A Boeing seven seventy-seven main gear has six wheels on a frame called a bogie, and the whole bogie can tilt as it touches the ground, so the load arrives gradually instead of all at once. Spreading the weight over more wheels also spreads it over more of the runway, so the pavement is not crushed. That is why the heaviest planes have the most wheels.""",
   "Boeing 777 six wheel bogie", "MORE WHEELS, LESS DAMAGE")

# ---------- 5. TORQUE LINK ----------
part(5, "The scissors on the gear", "WHY ARE THERE SCISSORS ON THE GEAR?", "Why Do Airplane Landing Gears Have Scissors?",
     """Why is there a strange folding arm, like a pair of scissors, on the front of the landing gear? Because the shock absorber is a piston sliding in a cylinder, and a round piston can also spin. Without something to stop it, the wheels could twist sideways as the gear moves up and down. The scissor link, also called the torque link, lets the piston slide in and out but stops it from rotating. It keeps the wheels pointing exactly where they should.""",
     "landing gear torque link")
sc("""On the nose gear, the scissors do one more job. The steering motor turns the upper part of the strut, and the torque link passes that rotation down to the wheels. On some airplanes, the ground crew disconnects the torque link before towing, so the tug can turn the nose wheel without fighting the steering system. On others, a bypass pin does the same job. That is why you sometimes see a mechanic putting a pin near the nose wheel before pushback.""",
   "aircraft nose gear pushback tug", "IT ALSO STEERS")

sc("""There is a reason the torque link matters so much. If a wheel turns even slightly off line at landing speed, the tire is dragged sideways and can be destroyed in a single landing. It can also start a violent vibration called shimmy, where the wheel shakes from side to side. Many nose gears have a damper just to stop it. A few metal links and a damper keep tons of airplane rolling in a straight line.""",
   "aircraft nose landing gear close up", "NO SHIMMY ALLOWED")

# ---------- 6. BRAKES ----------
part(6, "The brakes that glow", "WHY DO THESE BRAKES GLOW RED?", "Why Do Airplane Brakes Glow Red in Tests?",
     """Why are the brakes of an airliner tested until they glow red? Because they have to stop the airplane in the worst possible case, a rejected takeoff at full weight, at the last moment. Before Boeing could certify the seven forty-seven eight, test pilots loaded it to nine hundred seventy-five thousand pounds, accelerated to takeoff speed, and stopped it with brakes that had been worn down to their limit. The wheels glowed red. Then nobody was allowed to touch them for five minutes.""",
     "rejected takeoff test brakes")
sc("""Those five minutes simulate the time it might take for airport fire trucks to arrive. The airplane has to get through that wait without the fire spreading beyond the wheels. In those tests, the fusible plugs we saw earlier usually melt and the tires go flat. That is expected. The airplane passed. And modern airliners use carbon brakes, stacks of carbon discs that are lighter than steel and can absorb enormous amounts of heat.""",
   "Boeing 747-8 brakes", "5 MINUTES. NO FIREFIGHTERS.")

sc("""Carbon brakes have a strange habit. They wear more from the number of times they are used than from how hard they are used. So pilots and airlines often use the brakes in fewer, firmer applications instead of many small touches. On the ground, after a long taxi or a heavy landing, the brakes can stay hot for a long time, and airlines track brake temperature before the next takeoff.""",
   "carbon brake disc aircraft", "FEWER, FIRMER STOPS")

# ---------- 7. ANTI-SKID ----------
part(7, "The anti-skid", "WHY DON'T THESE WHEELS LOCK UP?", "Why Don't Airplane Wheels Lock Up When Braking?",
     """Why don't airplane wheels lock up and skid when the pilots brake hard? Because airplanes had anti-lock brakes long before cars. In the early nineteen fifties, Dunlop in Britain introduced a system called Maxaret. It sensed when a wheel was starting to slow down too fast, which means it was about to lock, and released the brake for a moment. In tests, it cut stopping distances by about thirty percent, and it let jets land safely on icy runways.""",
     "Dunlop Maxaret anti-skid")
sc("""A locked wheel is a disaster on an airplane. The tire scrubs against the runway at high speed, wears through in seconds, and bursts. Maxaret also eliminated tire bursts from skids. Every airliner today has an anti-skid system, monitoring each wheel separately. And the technology went on to cars. One of the first cars with anti-lock brakes, the Jensen F F, used the Maxaret system from airplanes.""",
   "Jensen FF car", "FROM JETS TO CARS")

sc("""On a modern airliner, the anti-skid works together with the autobrake. Before landing, pilots select how hard they want to stop. After touchdown, the system applies the brakes by itself, and the anti-skid adjusts each wheel many times per second. On a wet or icy runway, this is what keeps the airplane straight. The pilots feel smooth deceleration. Underneath, the brakes are pulsing on and off.""",
   "airliner landing wet runway spray", "PULSING MANY TIMES A SECOND")

# ---------- 8. SMOKE ----------
part(8, "The puff of smoke", "WHY DO TIRES SMOKE ON LANDING?", "Why Do Airplane Tires Smoke When They Land?",
     """Why is there a puff of smoke every time an airliner touches down? Because the wheels are not spinning when they hit the runway. The airplane is moving at more than one hundred fifty miles an hour, but the tires are standing still. In a fraction of a second, friction has to spin them up to full speed. During that moment, the rubber slides against the concrete and a thin layer burns off. That is the smoke, and the black marks you see at the start of every runway.""",
     "airplane landing tire smoke")
sc("""So why not spin the wheels before landing? Engineers have tried the idea many times, with small fins or motors on the wheels. But it adds weight and complexity to every flight, and the rubber is cheap compared to that. Tires are simply designed to lose a little tread every landing. The black rubber is later removed from runways with high pressure water, because too much of it makes the runway slippery when wet.""",
   "runway rubber deposits touchdown zone", "A LITTLE RUBBER EVERY LANDING")

sc("""That spin-up moment is also the biggest test for the tire structure. The sudden twist from standing still to full speed pulls hard on the rubber and the casing. Engineers design tires and wheels for it, and the landing gear itself has to handle the backward drag force as the wheels grab the runway. Watch the gear in slow motion and you can see the whole leg flex backward for an instant.""",
   "aircraft touchdown slow motion gear", "THE WHOLE LEG FLEXES")

# ---------- 9. PINS ----------
part(9, "The red flags", "WHY ARE THERE RED FLAGS ON THE GEAR?", "Why Are There Red Flags on Airplane Landing Gear?",
     """Why are there red ribbons hanging from the landing gear of a parked airplane? They are attached to gear pins, steel pins pushed into the gear mechanism to lock it physically in the down position. A parked airplane has no hydraulic pressure, and someone could accidentally move the gear lever in the cockpit, or a mechanic could trigger a system. The pin makes it mechanically impossible for the gear to fold up and drop the airplane on its belly.""",
     "remove before flight landing gear pin")
sc("""The red flag says remove before flight, and that is exactly the point. A pin left in place means the gear cannot retract after takeoff. So the ribbon is bright, long, and impossible to miss during the walk around inspection. The same red flags are used on pitot covers, engine covers, and weapons on military jets. It is one of the simplest safety devices in aviation, a piece of cloth that says, in big letters, don't forget me.""",
   "remove before flight tag", "DON'T FORGET ME")

sc("""Gear pins are part of a bigger culture. Before every flight, a pilot or mechanic walks around the airplane looking for anything that should not be there, covers, pins, leaks, damage. It sounds old fashioned, but it catches problems that no sensor sees. The red flags exist because the walk around exists. One makes the other work.""",
   "pilot walk around inspection airliner", "THE WALK AROUND")

# ---------- 10. GRAVITY ----------
part(10, "The backup that uses gravity", "WHAT IF THE GEAR WON'T COME DOWN?", "Why Can Pilots Drop the Landing Gear Without Power?",
     """What happens if the hydraulic system fails and the landing gear will not come down? Pilots have a backup that needs almost no power, gravity. On most airliners, a handle or switch in the cockpit releases the locks that hold the gear up. The heavy gear simply falls out of the wheel wells, pushed by its own weight and by the air rushing past, until it locks in the down position. It is called a gravity extension, or free fall.""",
     "landing gear extension airliner")
sc("""It is tested on certification flights, and pilots practice it in the simulator. It works so well that true belly landings of airliners are very rare. When the gear really will not come down, it is usually because something has jammed, not because of a power failure. Simple physics, gravity and airflow, is the last line of defense, because it is the one thing that never runs out on an airplane in flight.""",
   "airliner final approach gear down", "GRAVITY NEVER FAILS")

sc("""The gear also has a way to tell the pilots it is really down. Three green lights in the cockpit, one for each gear leg, light up only when each one is locked. If a light stays red or dark, pilots can fly past the control tower so controllers can look, or use cameras on some airplanes. Three green is one of the most reassuring sights in aviation.""",
   "airliner cockpit landing gear lever", "THREE GREEN")

# ---------- VERDICT ----------
sc("""So here are the ten. Nitrogen in the tires, because of a tire that exploded with air. Plugs that melt so the tire goes flat instead of bursting. Straight grooves for water. A shock absorber full of oil and gas. Scissors that keep the wheels straight. Brakes tested until they glow. Anti-lock brakes that were invented for jets. A puff of smoke at every touchdown, red flags that must be removed, and gravity as the final backup.""",
   "airliner landing gear runway", "10 SECRETS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Landing gear looks like a few wheels on sticks. It is really one of the most tested parts of an airplane, shaped by decades of lessons. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "airplane landing at sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Two man replace a main landing gear tire of a plane.jpg", 0.22, 0.55),
    2: ("File:Concorde - Undercarriage and cooling fans embedded in the wheel rims (7181588076).jpg", 0.66, 0.5),
    3: ("File:Nose landing gear of a Sukhoi Superjet 100.jpg", 0.46, 0.58),
    4: ("File:Oleo trailing link main landing gear.JPG", 0.6, 0.35),
    5: ("File:Oleo torque link main landing gear.JPG", 0.43, 0.45),
    6: ("File:Boeing 737 Next-Generation Carbon Brake PAS 2013.jpg", 0.62, 0.45),
    7: ("File:American Airlines Boeing 777-200ER N788AN landing gear and flaps.jpg", 0.6, 0.7),
    8: ("File:Touchdown! FedEx MD-11 main gear making contact.jpg", 0.36, 0.76),
    9: ("File:'Remove before flight' tag on Concorde F-BVFA.jpg", 0.52, 0.45),
    10: ("File:44 Hercules main landing gear manual emergency extension - IMG 6279 RIAT 2025 - Friday 18 July.jpg", 0.5, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video04", "title": "Why Don't Airplane Tires Explode on Landing?",
           "length_scale": 1.6, "scenes": S}, open("videos/video04/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
