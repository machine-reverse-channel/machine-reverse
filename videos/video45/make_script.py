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
sc("""The nose of a Japanese bullet train can be longer than a whole subway car. On some trains, a big part of the first car is just nose, with no seats inside. That looks like a waste of space on the most crowded railway in the world. But without that nose, every time the train entered a tunnel, people living near the exit would hear a bang like a cannon. Today, ten parts of the bullet train, and why each one exists.""",
   "Shinkansen E5 nose", "THE NOSE IS NOT FOR LOOKS", cuts=8, chapter="Intro")
sc("""Japan opened the first Shinkansen line, between Tokyo and Osaka, on October first, nineteen sixty-four, just before the Tokyo Olympics. It was the first high speed railway in the world. Since then, the Shinkansen has carried billions of passengers, and it is famous for two numbers. An average delay of under a minute per train, and no passenger deaths from derailments or collisions in normal operation.""",
   "Shinkansen 0 series", "THE FIRST BULLET TRAIN")
sc("""As always, every fact comes from a named source, Japanese railway companies, engineering papers, and railway references, all listed in the description. Let's start with the most famous part, the nose.""",
   "Shinkansen N700 nose", "WHY DOES THIS EXIST?")

# ---------- 1. NOSE ----------
part(1, "The long nose", "WHY IS THIS NOSE SO LONG?", "Why Do Bullet Trains Have Such Long Noses?",
     """Why do bullet trains have such long noses? The main reason is not speed. It is tunnels. When a fast train enters a tunnel, it pushes the air ahead of it like a piston. That creates a pressure wave that races through the tunnel at the speed of sound. When it reaches the other end, part of it bursts out as a loud boom, called a tunnel boom, which can rattle windows of houses near the exit.""",
     "Shinkansen E5 nose")
sc("""A long, slowly tapering nose pushes the air more gently, so the pressure rises more slowly and the boom becomes much weaker. That is why the noses got longer as the trains got faster. The newest test train, the ALFA-X, has a nose about twenty-two meters long on one end, almost as long as an entire normal train car.""",
   "ALFA-X Shinkansen", "22 METERS OF NOSE")
sc("""The most famous nose was inspired by a bird. In the nineteen nineties, Eiji Nakatsu, an engineer at JR West and a bird watcher, noticed that the kingfisher dives from air into water with almost no splash, thanks to its long, pointed beak. The nose of the five hundred series was shaped like it. Reports say the new train was quieter, used about fifteen percent less electricity, and ran faster than the old one.""",
   "kingfisher", "COPIED FROM A BIRD")

# ---------- 2. TUNNEL HOOD ----------
part(2, "The tunnel hood", "WHY DO THESE TUNNELS HAVE HOODS?", "Why Do Bullet Train Tunnels Have Hoods?",
     """Why do many Shinkansen tunnel entrances have a strange box sticking out of the mountain, often with holes in its sides? It is a tunnel hood, also called a buffer. It works together with the long nose. When the train enters the hood, some of the air escapes through the openings, so the pressure in the tunnel rises in steps instead of all at once. The pressure wave is softer, and the boom at the far end is quieter.""",
     "tunnel portal hood Shinkansen")
sc("""Japan needed this more than most countries, because its high speed lines cross mountains and are full of tunnels, and many tunnels are close to homes. Japanese rules limit the noise and pressure that a train can cause near the line, so engineers attack the problem from both sides, the train and the tunnel.""",
   "Shinkansen tunnel entrance", "ATTACK FROM BOTH SIDES")
sc("""Even the inside of the tunnel matters. Some tunnels were built with a larger cross section so the air has more room to move around the train. A bigger tunnel costs much more to dig, but a smaller one makes the boom louder and the ride less comfortable. In high speed rail, air is the enemy you have to design around.""",
   "Shinkansen tunnel", "AIR IS THE ENEMY")

# ---------- 3. PANTOGRAPH ----------
part(3, "The owl pantograph", "WHY IS THIS PART COPIED FROM AN OWL?", "Why Is a Bullet Train Part Copied From an Owl?",
     """Why was part of a bullet train copied from an owl? The part is the pantograph, the arm on the roof that touches the overhead wire to collect electricity. At three hundred kilometers an hour, air rushing past it creates loud noise. Eiji Nakatsu looked at owls, which hunt in near silence. Their wing feathers have small comb-like edges that break the air into tiny swirls, making their flight quiet.""",
     "Shinkansen 500 series pantograph")
sc("""The pantograph of the five hundred series used a wing-shaped support with small serrations, inspired by those owl feathers. The serrations break the large noisy swirls of air into smaller, quieter ones. Combined with a smaller design and covers around the pantograph, the noise dropped enough to meet Japan's strict rules at high speed.""",
   "owl feather", "THE SILENT HUNTER")
sc("""Modern Shinkansen trains use fewer pantographs than older ones, often with streamlined covers or shields at their base, because each pantograph adds noise and drag. The goal is simple. Collect electricity from a wire at three hundred kilometers an hour, and do it so quietly that people living next to the line can sleep.""",
   "Shinkansen pantograph", "QUIET ENOUGH TO SLEEP")

# ---------- 4. SEALED BODY ----------
part(4, "The sealed body", "WHY ARE THESE TRAIN CARS SEALED LIKE PLANES?", "Why Are Bullet Trains Sealed Like Airplanes?",
     """Why are bullet train cars sealed almost like an airplane? Because of the same tunnel pressure. When a train enters a tunnel at high speed, the air pressure outside changes suddenly. In an ordinary train, that change would rush in through doors and gaps, and passengers would feel a painful pop in their ears, every tunnel. So Shinkansen cars are built to be airtight, with pressure-tight doors and controlled ventilation.""",
     "Shinkansen interior")
sc("""The ventilation system controls how quickly the air inside changes, so the pressure in the cabin moves slowly and gently. The car body must also be strong enough to handle the pressure pushing on it, again and again, every time the train enters or leaves a tunnel, or passes another train in a tunnel. It is a pressure vessel on wheels.""",
   "Shinkansen car body", "A PRESSURE VESSEL ON WHEELS")
sc("""Passing another train at high speed is also a pressure event. Two trains approaching each other at three hundred kilometers an hour each create a sudden push of air that hits the windows of the other train. That is one reason the space between tracks on high speed lines is wider than on old lines. The air needs room too.""",
   "Shinkansen trains passing", "THE AIR NEEDS ROOM")

# ---------- 5. TILTING ----------
part(5, "The tilting body", "WHY DOES THIS TRAIN LEAN IN CURVES?", "Why Do Some Bullet Trains Lean in Curves?",
     """Why do some bullet trains lean into curves? The old Tokaido Shinkansen line, built in the nineteen sixties, has many curves that are tighter than modern high speed lines. To go faster on it, the N seven hundred series uses air springs to tilt the car body by about one degree in curves. It is a small angle, but it lets the train take many curves at two hundred seventy kilometers an hour instead of slowing down to around two hundred fifty.""",
     "Shinkansen N700 nose")
sc("""The tilt is not for the train. It is for the passengers. In a fast curve, you are pushed sideways, and if the force is too strong, coffee spills and people lose balance. Tilting the body moves the force so that it feels more like it is pushing you into your seat. The train is not more stable when it tilts. It is more comfortable.""",
   "Shinkansen curve", "FOR THE COFFEE")
sc("""Saving a few seconds on every curve adds up. Along the busy route between Tokyo and Osaka, faster curves helped trains save several minutes. On a line that runs a train every few minutes, minutes matter. The fastest way to speed up an old railway is sometimes not a new line, but a train that leans.""",
   "Tokaido Shinkansen Mount Fuji", "MINUTES MATTER")

# ---------- 6. SNOW SPRINKLERS ----------
part(6, "The snow sprinklers", "WHY DO THEY SPRAY WATER ON THE SNOW?", "Why Does Japan Spray Water on Bullet Train Tracks?",
     """Why does Japan spray water on bullet train tracks when it snows? Because snow can stick to the bottom of the train at high speed and build up into heavy chunks of ice. Later, when the train reaches a warmer area, the chunks fall off, hit the stones of the track, and throw them up into the train, breaking windows and equipment. Wetting the snow makes it heavy and less likely to fly up and stick.""",
     "Shinkansen snow sprinkler")
sc("""The Tokaido Shinkansen passes near Sekigahara, an area known for heavy snow, and it uses sprinklers to keep the snow damp. On lines in the snowiest parts of Japan, some sprinklers spray warmed water to melt the snow. Trains in snowy regions also have plows and special shapes to throw snow away from the train.""",
   "Shinkansen snow", "SEKIGAHARA")
sc("""And at some stations, workers remove ice from the bottom of trains by hand during short stops, sometimes with high pressure water. In winter, keeping a bullet train on time is not only about engines and signals. It is about a crew with hoses fighting the snow, one train at a time.""",
   "Shinkansen winter station", "HOSES VS SNOW")

# ---------- 7. SLAB TRACK ----------
part(7, "The track without stones", "WHY DOES THIS TRACK HAVE NO STONES?", "Why Does Bullet Train Track Have No Stones?",
     """Why does much of the Shinkansen track have no stones? Most railways lay their track on a bed of crushed rock called ballast. It works well, but trains shake the stones, the track slowly moves, and crews have to fix it constantly. Many Shinkansen lines use slab track instead, rails fixed on concrete slabs, with a layer of special mortar underneath. It stays in place much better, and needs far less maintenance.""",
     "Shinkansen slab track")
sc("""Slab track also has another advantage. At high speed, the air under a train can lift small stones of ballast and throw them, a problem sometimes called ballast flight. Concrete slabs do not fly. The downside is cost. Slab track is more expensive to build, and once laid, it is harder to adjust if the ground moves.""",
   "ballast railway track", "STONES CAN FLY")
sc("""Japan began using slab track widely on the Sanyo Shinkansen in the nineteen seventies, and many later lines followed. For a railway that runs hundreds of trains a day with only a few hours at night for maintenance, a track that does not need constant fixing is worth its higher price.""",
   "Shinkansen track night maintenance", "FEW HOURS AT NIGHT")

# ---------- 8. EARTHQUAKE ----------
part(8, "The earthquake detectors", "WHY DO THESE SENSORS STOP THE TRAIN?", "Why Can Bullet Trains Stop Before an Earthquake Hits?",
     """Why can a bullet train start braking before an earthquake shaking arrives? Japan has seismometers along the coast and along the lines. An earthquake sends two main waves. The fast P wave arrives first and is weaker. The slower S wave carries the strong shaking. When the sensors detect the first wave, the system can cut power to trains automatically, and their emergency brakes start working, sometimes seconds before the strong shaking arrives. Japan even places seismometers like this one on the ocean floor, to catch offshore earthquakes earlier.""",
     "seismometer")
sc("""In two thousand four, during the Chuetsu earthquake, a Shinkansen train traveling at about two hundred kilometers an hour derailed. It was the first derailment of a Shinkansen in passenger service. Nobody was killed. After that, railways added devices that keep a derailed train close to the rails, so it slides along them instead of tipping over.""",
   "Joetsu Shinkansen", "2004: THE FIRST DERAILMENT", file="File:Joetsu Shinkansen derailed by the 2004 Chuetsu Earthquake 01.jpg")
sc("""In March twenty eleven, the huge Tohoku earthquake struck while Shinkansen trains were running on the Tohoku line. The warning system cut power, and the trains in service stopped without any passenger being hurt in a derailment. In twenty twenty-two, another strong earthquake derailed a Tohoku Shinkansen near Shiroishi, and again nobody was killed. A few seconds of warning, used by machines instead of humans, can be the difference between a stop and a disaster.""",
   "Tohoku Shinkansen", "SECONDS OF WARNING")

# ---------- 9. DOCTOR YELLOW ----------
part(9, "The yellow train", "WHY IS THIS BULLET TRAIN YELLOW?", "Why Is This Bullet Train Yellow?",
     """Why is one Japanese bullet train painted bright yellow? It is called Doctor Yellow, and it is not for passengers. It is an inspection train that runs at full speed while measuring the track and the overhead wire, checking for tiny problems before they become dangerous. Its sensors can measure the track's alignment and the condition of the electric wire while running at high speed.""",
     "Doctor Yellow Shinkansen")
sc("""Doctor Yellow did not follow a public timetable, so seeing one became a small legend in Japan. People said it brings good luck. JR Central retired its Doctor Yellow in January twenty twenty-five, and JR West planned to retire its own later. Their job is moving to sensors fitted on regular passenger trains, which measure the line every day.""",
   "Doctor Yellow train", "A LUCKY TRAIN")
sc("""That change shows the philosophy of the Shinkansen. Instead of waiting for something to break, measure everything, all the time. The goal is to find a problem when it is a millimeter, not when it is a meter. That is how you run a railway at three hundred kilometers an hour for decades with almost no accidents.""",
   "Shinkansen maintenance", "A MILLIMETER, NOT A METER")

# ---------- 10. GAUGE ----------
part(10, "The wider track", "WHY DID JAPAN BUILD A NEW TRACK?", "Why Couldn't Bullet Trains Use Japan's Old Tracks?",
     """Why couldn't the bullet train simply use Japan's existing railway tracks? Because most old Japanese lines use a narrow gauge, about one point oh six seven meters between the rails, which limits speed and stability. The Shinkansen was built from the start on separate lines with standard gauge, one point four three five meters, the same width used by most of Europe and North America. A wider track allows bigger, more stable trains at high speed.""",
     "rail gauge measurement")
sc("""The new lines were also built without level crossings. No cars, no people, no animals crossing the tracks at street level. Bridges and tunnels carry the line over and under everything. That alone removes one of the most common causes of railway accidents. A bullet train never has to worry about a truck stuck on the tracks.""",
   "Shinkansen viaduct", "NO LEVEL CROSSINGS")
sc("""Some lines, called mini-Shinkansen, use a different trick. They widened old narrow gauge lines to standard gauge, so bullet trains could continue from the high speed line onto them at lower speed. But on its own dedicated lines, the Shinkansen lives in its own world, which is why it can be so fast and so safe.""",
   "Shinkansen E6 nose", "ITS OWN WORLD")

# ---------- VERDICT ----------
sc("""So here are the ten. A long nose against the tunnel boom, and hoods at the tunnel doors. A pantograph copied from an owl, and cars sealed like airplanes. A body that leans for your coffee, sprinklers against the snow, track without stones, sensors that feel earthquakes first, a yellow train that checks everything, and a wider track built just for speed.""",
   "Shinkansen N700 nose", "10 PARTS. 300 KM/H.", chapter="The verdict", cuts=6)
sc("""The bullet train does not look like that to look fast. Every curve has a reason. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Shinkansen Mount Fuji", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Class E956 ALFA-X Shinkansen EMU.jpg", 0.75, 0.62),
    2: ("File:Nakayama tunnel north entrance of the Joetsu Shinkansen A.jpg", 0.55, 0.35),
    3: ("File:JRW Shinkansen Series 500 V3 Pantograph.jpg", 0.62, 0.35),
    4: ("File:Kyushu Shinkansen N700-8000 series interior 20110315.jpg", 0.9, 0.42),
    5: ("File:JRCentralSeriesN700Nose.JPG", 0.5, 0.55),
    6: ("File:Shinkansen snow melting sprinkler water pipe ２.jpg", 0.4, 0.85),
    7: ("File:Tokaido Shinkansen Tokyo station Slab tracks 01.jpg", 0.55, 0.6),
    8: ("File:Ocean Bottom Seismometer made by ERI, U-Tokyo.jpg", 0.5, 0.4),
    9: ("File:Doctor Yellow inspection running on Tokaido Shinkansen.jpg", 0.42, 0.55),
    10: ("File:Nakayama tunnel north entrance of the Joetsu Shinkansen C.jpg", 0.48, 0.8),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video45", "title": "Why Do Bullet Trains Have Such Long Noses?",
           "length_scale": 1.6, "scenes": S}, open("videos/video45/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
