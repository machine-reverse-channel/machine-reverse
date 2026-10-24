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
sc("""The wheels of the Mars rover Curiosity are covered in holes. Some of those holes were put there on purpose, by engineers in California. Others were made by rocks on Mars, and they are a very different story. Each of the six wheels is fifty centimeters across, forty centimeters wide, and was machined from a single block of aluminum. Today, ten parts of a Mars rover, and why each one exists.""",
   "Curiosity rover wheel", "WHY THE HOLES IN THE WHEELS?", cuts=8, chapter="Intro")
sc("""Curiosity landed on Mars on the sixth of August, two thousand twelve, and weighs about nine hundred kilograms. Everything it does is slow, careful and planned from millions of kilometers away, because there is no mechanic on Mars. So every part has to earn its place.""",
   "Curiosity rover Mars", "NO MECHANIC ON MARS")
sc("""As always, every fact here comes from a named source, NASA and the Jet Propulsion Laboratory, all listed in the description. Let's start with the holes.""",
   "Curiosity rover wheels track", "WHY DOES THIS EXIST?")

# ---------- 1. MORSE CODE ----------
part(1, "The Morse code holes", "WHY ARE THERE HOLES IN THIS WHEEL?", "Why Do Mars Rover Wheels Have Holes?",
     """Why do the wheels of Curiosity have holes? Some of them spell a message. The holes are arranged in Morse code, and the tracks they leave in the soil repeat the pattern. It reads J, P, L, the initials of the Jet Propulsion Laboratory, which built the rover. But the real reason is not decoration. The pattern leaves features in the sand that the rover can use to measure how far it has really traveled.""",
     "Curiosity rover wheel Morse code JPL")
sc("""That method is called visual odometry. After a drive, the rover takes pictures and compares them with the marks left behind, to see if the wheels slipped. On steep slopes, in loose soil, or in a sandy field with nothing to look at, a high contrast pattern is like a landmark that the rover carries with it.""",
   "Curiosity rover tracks sand", "A LANDMARK IT CARRIES")
sc("""The rover can not read the message. The engineers can. And it is a small bit of fun inside a serious tool, because the team could not have the letters JPL printed on the wheels as text. So they wrote them in dots and dashes.""",
   "Curiosity rover wheel tracks Mars", "WRITTEN IN DOTS AND DASHES")

# ---------- 2. THIN SKIN ----------
part(2, "The thin wheel skin", "WHY IS THIS WHEEL SO THIN?", "Why Are the Mars Rover's Wheels So Thin?",
     """Why are the wheels of Curiosity so thin? Because every gram has to be flown to Mars. The skin of each wheel is only seventy-five hundredths of a millimeter thick, described as the thinnest that could be machined. Adding just one millimeter of thickness to the wheels would have added about ten kilograms to the whole rover.""",
     "Curiosity rover wheel skin thin aluminum")
sc("""The wheels also had to survive the landing, when the rover was lowered to the ground on its own suspension. Lighter wheels meant lighter forces during that moment. The engineers did not expect to find so many sharp, pointed rocks at the landing site in Gale crater.""",
   "Curiosity rover landing sky crane", "A WEIGHT BUDGET")
sc("""It is the oldest trade-off in spaceflight. Stronger means heavier, and heavier means more rocket. The wheels are the place where that trade-off turned into holes.""",
   "Curiosity rover wheel Mars rock", "STRONGER MEANS HEAVIER")

# ---------- 3. GROUSERS ----------
part(3, "The zigzag treads", "WHY DOES THE WHEEL HAVE ZIGZAG RIDGES?", "Why Do Mars Rover Wheels Have Zigzag Treads?",
     """Why do the wheels have zigzag ridges? They are called grousers, and they grip the ground. Each one sticks out about seven and a half millimeters from the skin of the wheel, they are spaced fifteen degrees apart, and they have a chevron shape, a bit like arrows. They bite into sand and loose soil, so the wheel can push the rover forward without just spinning.""",
     "Curiosity rover wheel grousers chevron")
sc("""The grousers do a second job. They are also the stiffest part of the wheel, so they carry the load of the whole rover. The stress is highest near the tips of the chevrons, and that is where the metal later began to tear on Mars.""",
   "Curiosity rover wheel tear", "WHERE THE METAL TEARS")
sc("""A wheel is more than a circle. On Mars, it is a tool for grip, for measuring distance and for carrying weight, all at once. And all of those jobs ask the same thin piece of aluminum for something different.""",
   "Curiosity rover wheel close", "MANY JOBS, ONE WHEEL")

# ---------- 4. DAMAGE ----------
part(4, "The punctured wheel", "WHY IS THIS WHEEL FULL OF HOLES?", "Why Did Curiosity's Wheels Get Holes in Them?",
     """Why did Curiosity's wheels get holes in them? The first large puncture appeared around the four hundred eleventh Martian day of the mission, and by day four hundred sixty-three, a big rip had been found in the left front wheel. There were two causes. Tears came from metal fatigue, the skin bending and straightening on hard bedrock until it cracked. Punctures came from sharp, buried rocks, pushed by the suspension into the front and middle wheels.""",
     "Curiosity rover wheel damage punctures")
sc("""The rear wheels had no punctures, because the front and middle wheels are the ones pushed into the rocks as the rover climbs. So the team changed how it drove. They avoided pointed rocks, used shorter drives on rough ground, and drove backwards in places, so the front wheels are dragged and not shoved.""",
   "Curiosity rover driving backwards", "DRIVE BACKWARDS")
sc("""Engineers also used satellite data to map the terrain before the rover got there, picking routes with sand instead of sharp bedrock. The wheel damage did not end the mission. It changed the way the rover is driven, and it is one of the best stories of how a machine is nursed along on another planet.""",
   "Mars terrain map Curiosity route", "NURSING A ROVER")

# ---------- 5. PERSEVERANCE WHEEL ----------
part(5, "The new wheel", "WHY ARE THE NEW WHEELS DIFFERENT?", "Why Are Perseverance's Wheels Different From Curiosity's?",
     """Why does the newer rover, Perseverance, have different wheels? Because Curiosity's were damaged. Perseverance's wheels are a bit larger, fifty-two and a half centimeters across, narrower, and made of thicker, more durable aluminum. Cleats cover them for traction, and curved titanium spokes give the wheel some spring.""",
     "Perseverance rover wheel")
sc("""Perseverance weighs about one thousand twenty-five kilograms, roughly fourteen percent more than Curiosity, and part of that is a tougher set of wheels. Every rover learns from the one before it. Curiosity's holes became Perseverance's thicker skin.""",
   "Perseverance rover Mars", "LEARNED FROM THE HOLES")
sc("""This is how a space program works in practice. A machine on Mars is a test for the next machine, and the damage you see in the photos is the lesson that fixed the next set of wheels.""",
   "Perseverance rover wheels", "ONE ROVER TEACHES THE NEXT")

# ---------- 6. ROCKER-BOGIE ----------
part(6, "The rocker-bogie suspension", "WHY ARE THE WHEELS ON LEGS?", "Why Does a Mars Rover Have Such a Strange Suspension?",
     """Why does the rover have such strange legs? It is a rocker-bogie suspension, a set of linked arms that lets all six wheels stay on the ground while the rover climbs over rocks. It can roll over obstacles up to sixty-five centimeters high, and it has sixty centimeters of ground clearance. The arms just pivot, and the wheels stay in contact.""",
     "Curiosity rover rocker-bogie suspension")
sc("""On Curiosity, the same suspension also acts as the landing gear. During the landing, the rover was lowered to the ground on a tether, with the wheels already down, and the suspension took the touch. The smaller rovers before it did not do this.""",
   "Curiosity rover landing wheels down", "THE SUSPENSION IS THE LANDING GEAR")
sc("""A simple mechanism, with few parts to break. On a planet where nothing can be repaired, the simplest design is the safest kind.""",
   "Mars rover suspension climbing rock", "FEW PARTS TO BREAK")

# ---------- 7. MASTCAM ----------
part(7, "The camera mast", "WHY DOES THE ROVER HAVE A HEAD?", "Why Does a Mars Rover Have a Camera Mast?",
     """Why does the rover have a head? It is a mast with cameras, so the rover can look around from higher up. Mastcam has two cameras, one with a wider view and one with a narrow, zoomed view. They take color pictures at sixteen hundred by twelve hundred pixels, and also video, at up to ten frames per second.""",
     "Curiosity rover Mastcam mast")
sc("""Two lenses are better than one. The wide lens shows the landscape, and the narrow lens zooms in on a rock to decide if it is worth the trip. Most of the rover's decisions begin with a picture, taken from the mast.""",
   "Curiosity rover camera Mars rock", "FIND THE ROCK WORTH A TRIP")
sc("""And the pictures come home the long way, relayed by spacecraft that orbit Mars. Many of the pictures you have seen of the red planet were taken from a mast like this one.""",
   "Mars panorama Curiosity", "THE EYES OF MARS")

# ---------- 8. CHEMCAM ----------
part(8, "The laser", "WHY DOES THE ROVER HAVE A LASER?", "Why Does the Mars Rover Shoot Rocks With a Laser?",
     """Why does the rover shoot rocks with a laser? It is the ChemCam instrument, and the laser vaporizes a tiny spot on a rock, up to seven meters away. A telescope then looks at the flash of light it makes. Each element glows with its own colors, so the light tells scientists what the rock is made of. It fires about fifty to seventy-five short pulses at each target.""",
     "Curiosity rover ChemCam laser")
sc("""The point is speed. To know what a rock is made of without driving to it, and without touching it, saves days of work. The team expected about a dozen of these measurements on a typical day.""",
   "Curiosity ChemCam laser rock spark", "READ A ROCK FROM 7 METERS")
sc("""The newer rover has a successor, called SuperCam, with two lasers and four spectrometers. It is the same idea, but with more tools, and a lot more science from one single flash.""",
   "Perseverance SuperCam laser", "THE NEXT VERSION")

# ---------- 9. MMRTG ----------
part(9, "The nuclear battery", "WHY DOES THE ROVER HAVE A GIANT BLACK FINNED BOX?", "How Is a Mars Rover Powered Without Solar Panels?",
     """How does the rover get its power? Not from solar panels. At the back is a nuclear battery, a Multi-Mission Radioisotope Thermoelectric Generator. It holds about four point eight kilograms of plutonium-238 dioxide, and the heat from its natural decay is turned into electricity. It was designed to give one hundred ten watts at the start, and about one hundred watts after fourteen years.""",
     "Curiosity rover MMRTG radioisotope generator")
sc("""Solar panels would collect dust on Mars, and would struggle in winter and at night. A nuclear battery works day and night, in any season. It is not a reactor, and it does not run on fission. It is a heat source with a slow, steady output.""",
   "Curiosity rover back MMRTG fins", "DAY AND NIGHT, ANY SEASON")
sc("""The fins on the side are heat radiators. The generator makes more heat than electricity, and the extra heat has to go somewhere, or it would cook the rover. Even a nuclear battery needs a radiator.""",
   "MMRTG radioisotope generator fins", "THE FINS SHED HEAT")

# ---------- 10. ARM AND DRILL ----------
part(10, "The arm and drill", "WHY DOES THE ROVER HAVE A DRILL?", "Why Does a Mars Rover Carry a Drill?",
     """Why does the rover carry a drill? The surface of a rock can be changed by wind, dust and radiation. To find out what a rock is made of inside, the rover has to open it up. Its arm is two point one meters long, and its drill makes holes one point six centimeters wide and up to five centimeters deep, and it carries two spare bits.""",
     "Curiosity rover robotic arm drill")
sc("""The powder from the drill goes to instruments inside the rover. One of them found more than twenty organic molecules in clay-bearing sandstones. It is evidence about the chemistry of Mars, and that is the main reason that the rover was sent.""",
   "Curiosity rover drill hole powder", "THE SECRET INSIDE A ROCK")
sc("""And the drill itself has had its own troubles, including a short circuit in two thousand fifteen and a malfunction in two thousand sixteen. It resumed work in May two thousand eighteen. As with the wheels, the rover keeps working because the team on Earth keeps finding a way.""",
   "Curiosity rover drilling Mars", "FIXED FROM EARTH")

# ---------- VERDICT ----------
sc("""So here are the ten. Holes in the wheels that spell a message, and skin that is very thin. Zigzag treads, a wheel that was damaged by the rocks, and a new wheel that learned from it. Strange legs, a camera head, a laser, a nuclear battery, and a drill that opens up a rock.""",
   "Curiosity rover sunset Mars", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see tracks on Mars, look at the pattern. It is a rover's name written in the dust. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Curiosity rover selfie Mars", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video16", "title": "Why Do Mars Rover Wheels Have Holes?",
           "length_scale": 1.6, "scenes": S}, open("videos/video16/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
