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
sc("""In many London Underground stations, if you look down from the platform, the space between the rails is not flat. There is a deep trench, almost a meter deep, running under the track. It is there for drainage and for workers. But it has another, darker job. It has saved the lives of people who fell, or jumped, in front of a train. Today, eleven parts of a subway, and why each one exists.""",
   "London Underground platform track", "THE PIT UNDER THE TRACK", cuts=8, chapter="Intro")
sc("""The London Underground opened in eighteen sixty-three, the first underground railway in the world. Since then, cities from New York to Tokyo have built their own. A subway is a strange machine. Millions of people, thousands of volts, and trains running every two minutes, all inside narrow tunnels. Almost every detail you see in a station exists because something went wrong somewhere.""",
   "deep level tube platform", "THOUSANDS OF VOLTS, MILLIONS OF PEOPLE")
sc("""As always, every fact comes from a named source, transport authorities, medical studies, and railway history, all listed in the description. Let's start with the pit.""",
   "tube station track pit", "WHY DOES THIS EXIST?")

# ---------- 1. PIT ----------
part(1, "The pit under the track", "WHY IS THERE A PIT UNDER THE TRACK?", "Why Is There a Pit Under Subway Tracks?",
     """Why is there a deep pit between the rails at many subway stations? Officially, it is mostly a drainage pit. Water collects in tunnels, and the pit carries it away. It also gives maintenance workers access to the underside of trains. But it has a famous nickname in London, the suicide pit. If a person falls or jumps onto the track, they can sometimes drop into the pit, and the train passes over them.""",
     "tube station track pit")
sc("""Does it work? A study published in the British Medical Journal in nineteen ninety-nine looked at people hit by trains on the London Underground. At stations with pits, about forty-four percent died. At stations without pits, about sixty-six percent died. The pit does not prevent the accident. But it gives a person a place to survive it.""",
   "London Underground train platform", "44% VS 66%")
sc("""Many of these pits were built in the early twentieth century, as the deep tube lines expanded. Today, the best protection is to stop people from reaching the track at all, with doors on the platform edge. But on lines built a hundred years ago, the pit is still there, quietly doing a job most passengers never notice.""",
   "London Underground station old", "A QUIET JOB")

# ---------- 2. THIRD RAIL ----------
part(2, "The covered rail", "WHY DOES THIS RAIL HAVE A ROOF?", "Why Does the Subway Third Rail Have a Cover?",
     """Why does one rail in the New York subway have a little roof over it? That is the third rail, and it carries the electricity that powers the trains, around six hundred volts. Trains collect the power with a metal shoe that slides along it. The cover board on top protects people and workers from touching it by accident, and it also keeps snow and ice off in outdoor sections.""",
     "NYC subway third rail")
sc("""Touching the third rail can kill. That is why subway workers are trained to never step on it, and why the rail is mounted on insulators slightly to the side of the running rails. Six hundred volts does not sound like much compared with the twenty-five thousand volts of some overhead wires, but the current available is enormous. Every year, people are killed on third rails around the world.""",
   "New York City Transit Third Rail Operations Sign", "NEVER STEP ON IT")
sc("""Why not use overhead wires, like most modern trains? In tunnels, there is very little space above the train. A third rail lets tunnels be smaller and cheaper to dig. Many subways built in the late eighteen hundreds and early nineteen hundreds chose the third rail, and once a system is built, it is very hard to change.""",
   "third rail subway", "SMALLER TUNNELS")

# ---------- 3. FOURTH RAIL ----------
part(3, "The fourth rail", "WHY DOES LONDON NEED A 4TH RAIL?", "Why Does the London Underground Have Four Rails?",
     """Why does the London Underground have four rails instead of three? On most electric railways, the current comes in through a power rail, and returns through the running rails, the ones the wheels roll on. London's tube lines have a separate return rail in the middle, between the running rails. The power rail on the outside is positive, and the center rail is negative.""",
     "fourth rail London Underground")
sc("""One important reason is the tunnels. Many old London tunnels are lined with cast iron rings. If the return current flowed through the running rails, some of it could leak into the ground and into those iron linings and pipes, and slowly eat them away by electrolytic corrosion. A separate insulated return rail keeps the current where it belongs.""",
   "London Underground tunnel", "SAVING THE IRON TUNNELS")
sc("""The fourth rail also makes signaling easier, because the running rails are free to carry the signaling circuits. It is a choice made more than a century ago that still shapes how the system works today. When you look down at a London track and count four rails, you are looking at an engineering decision from the early nineteen hundreds.""",
   "London Underground track fourth rail", "COUNT THE RAILS")

# ---------- 4. TRIP COCK ----------
part(4, "The arm that stops trains", "WHY DOES THIS ARM POP UP NEXT TO THE TRACK?", "Why Does This Arm Pop Up Beside Subway Tracks?",
     """Why is there a small arm beside the track next to subway signals? It is a train stop. When the signal is red, the arm rises. If a train tries to pass the red signal, the arm hits a valve under the train, called a trip cock, which opens the brake pipe and puts the train into emergency braking. When the signal turns green, the arm drops down out of the way.""",
     "train stop arm signal")
sc("""This system is very old, but very effective. It was used on the New York subway and the London Underground in the early nineteen hundreds. It does not depend on the driver seeing the signal, or even being awake. It is purely mechanical. If the train passes a red light, it stops.""",
   "tripcock", "PURELY MECHANICAL")
sc("""The weakness is that it only acts after the train has passed the signal, so there must be enough space beyond the signal for the train to stop safely. Modern systems use computers and continuous communication to control the speed all the time. But in many tunnels, that little mechanical arm is still standing guard next to every signal.""",
   "London Underground signal", "STANDING GUARD")

# ---------- 5. PLATFORM DOORS ----------
part(5, "The glass wall", "WHY IS THERE A GLASS WALL ON THIS PLATFORM?", "Why Do Some Subway Platforms Have Glass Walls?",
     """Why do some subway platforms have a wall of glass doors? They are platform screen doors. The doors line up exactly with the train doors and only open when the train is stopped. Nobody can fall onto the track, nobody can be pushed, and nobody can jump. They also stop litter from reaching the rails, which can start fires.""",
     "platform screen doors")
sc("""One of the earliest versions opened in nineteen sixty-one, at Park Pobedy station in Leningrad, now Saint Petersburg. Its platform has a solid wall with doors, and passengers see the train only when the doors open. Today, platform doors are standard on many new lines, especially driverless ones, because no driver is watching the platform.""",
   "Metro SPB Line2 Park Pobedy", "SINCE 1961")
sc("""Full height doors also help with air. They separate the station from the tunnel, so the station can be air conditioned without cooling the tunnels, and the wind from trains does not blast through the platform. The downside is cost, and the trains must stop at exactly the right spot, often within a few centimeters.""",
   "platform edge doors metro", "STOP WITHIN CENTIMETERS")

# ---------- 6. TACTILE PAVING ----------
part(6, "The bumpy tiles", "WHY ARE THESE TILES BUMPY?", "Why Are There Bumpy Tiles at the Platform Edge?",
     """Why are there bumpy yellow tiles near the edge of many train platforms? They are tactile paving, designed for people who are blind or have low vision. Feet and canes can feel the bumps. Rows of dots mean stop, danger ahead, like the edge of a platform. Long raised lines mean this is the path, follow it. The bright color helps people with partial sight.""",
     "tactile paving platform edge")
sc("""Tactile paving was invented in Japan by Seiichi Miyake, who created it to help a friend who was losing his sight. The first tiles were installed in nineteen sixty-seven near a school for the blind in Okayama. Today, they are used all over the world, in train stations, at crosswalks, and at the top of stairs.""",
   "tactile paving Japan", "INVENTED FOR A FRIEND")
sc("""The tiles also remind everyone else to keep back. That is why many platforms combine bumps with a painted line and announcements. A subway platform is one of the few places where millions of people stand a step away from a machine that can kill them, and every one of these details exists to keep that step from being taken.""",
   "platform edge warning", "ONE STEP AWAY")

# ---------- 7. RUBBER TYRES ----------
part(7, "The rubber tyres", "WHY DOES THIS SUBWAY HAVE RUBBER TYRES?", "Why Do Paris Metro Trains Have Rubber Tyres?",
     """Why do some Paris Metro trains run on rubber tyres, like a bus? Rubber grips much better than steel. That means trains can accelerate and brake faster, climb steeper slopes, and run more quietly. On a metro line where stations are close together, faster acceleration and braking save time on every trip. Paris began using rubber tyred trains on line eleven in nineteen fifty-six.""",
     "Paris Metro rubber tyres")
sc("""The trains run on concrete or steel tracks under the tyres, and small horizontal wheels press against guide bars on the sides to steer them. And hidden behind the rubber tyres are normal steel wheels with flanges. If a tyre goes flat, the steel wheel drops onto a normal rail and the train can continue. The French system was copied by Montreal, Mexico City, Santiago, and others.""",
   "Metro de Paris bogie MP", "STEEL WHEELS HIDDEN INSIDE")
sc("""Rubber also has downsides. It wears out and must be replaced, it uses more energy than steel on steel, and it creates more heat in tunnels. That is why most new metros still use steel wheels. The rubber tyre is a tool for specific lines, with steep hills and closely spaced stations.""",
   "Paris Metro line 1", "A TOOL, NOT A RULE")

# ---------- 8. HUMPED STATIONS ----------
part(8, "The station on a hill", "WHY IS THIS STATION HIGHER THAN THE TUNNEL?", "Why Are Some Subway Stations Built on a Hill?",
     """Why are some subway stations built higher than the tunnels around them? It saves energy. On several London lines, including the Central line and the Victoria line, the track climbs slightly into each station and slopes down when leaving it. A train arriving uses the uphill to help it slow down, and when it leaves, the downhill helps it speed up.""",
     "Central line platform")
sc("""It sounds small, but a metro train stops and starts dozens of times on every trip. Gravity doing part of the braking and part of the acceleration adds up to real savings in energy and brake wear. The Central line opened in nineteen hundred with this design, and the Victoria line, opened in the late nineteen sixties, used it again.""",
   "Victoria line train", "LET GRAVITY HELP")
sc("""Modern trains can do something similar with regenerative braking, sending energy back to the power rail when they slow down. But humped stations need no electronics at all. It is a design that was smart in nineteen hundred and is still smart today. The track itself is part of the machine.""",
   "London Underground tunnel train", "THE TRACK IS THE MACHINE")

# ---------- 9. THE GAP ----------
part(9, "The gap", "WHY IS THERE A GAP HERE?", "Why Do Subways Say Mind the Gap?",
     """Why is there a gap between the train and the platform? Because many old platforms are curved, and trains are straight. When a straight train car stops at a curved platform, the middle or the ends of the car are farther from the edge, leaving a gap. Platforms also cannot be too close, or a train swaying slightly would hit them.""",
     "mind the gap")
sc("""That is why London made mind the gap one of the most famous phrases in the world. The recorded announcement was introduced in the late nineteen sixties. At Embankment station, an old recording by actor Oswald Laurence played for years. After he died, his widow used to visit the station just to hear his voice. When the recording was replaced, the Underground brought his announcement back at that station for her.""",
   "Mind the gap platform", "HIS VOICE")
sc("""New platforms are built straight wherever possible, with gap fillers or platform doors. But in old tunnels, the gap is part of the architecture. A simple warning, repeated millions of times a day, is the cheapest safety device on the entire network.""",
   "London Underground curved platform", "THE CHEAPEST SAFETY DEVICE")

# ---------- 10. ESCALATOR ----------
part(10, "The metal escalator", "WHY ARE THESE ESCALATORS MADE OF METAL?", "Why Did the Subway Get Rid of Wooden Escalators?",
     """Why are subway escalators today made of metal, when old ones were made of wood? Because of one night in London. On November eighteenth, nineteen eighty-seven, a fire started under a wooden escalator at King's Cross St. Pancras station, probably from a dropped match. Grease and fluff had built up underneath for years. The fire grew slowly at first, then suddenly exploded up the escalator shaft into the ticket hall. Thirty-one people died.""",
     "London Underground escalator")
sc("""Investigators were shocked by how fast the fire spread, so scientists recreated it with computer models and a scale model. They discovered something new, called the trench effect. In the sloped, narrow shaft of an escalator, the flames lie down along the steps, heat the wood ahead of them, and race upward. Nobody had predicted it before King's Cross.""",
   "escalator shaft", "THE TRENCH EFFECT")
sc("""After the fire, the Underground banned smoking in all stations, began replacing wooden escalators with metal ones, installed heat detectors and sprinklers, and trained staff in fire safety. The last wooden escalator on the network was removed years later. Every metal step you ride today is part of the lesson of that night.""",
   "metal escalator steps", "EVERY METAL STEP")

# ---------- 11. VENTILATION ----------
part(11, "The vent shaft", "WHY IS THERE A WIND IN THE SUBWAY?", "Why Is There Always Wind in the Subway?",
     """Why do you feel a strong wind on the platform just before the train arrives? It is the piston effect. A train in a tunnel works like a piston in a cylinder. It pushes a column of air ahead of it and pulls air behind it. That moving air is the wind you feel, and it can be strong enough to blow hats away. Vent shafts to the surface let the pushed air escape.""",
     "metro ventilation shaft")
sc("""Ventilation is also about heat and smoke. Trains, brakes and passengers produce enormous heat, and some old tunnels have warmed up over the decades. Big fans and shafts move air through the system. In a fire, the fans are used to push smoke away from people and toward the shafts, giving passengers clean air to escape.""",
   "subway ventilation tower", "SMOKE CONTROL")
sc("""Those mysterious grates on city sidewalks, sometimes blowing warm air, are often subway vents. In winter, the air coming out of them can be warmer than the street above. Next time you stand over one, you are standing on the breathing system of a giant underground machine.""",
   "subway grate sidewalk", "THE CITY BREATHES")

# ---------- VERDICT ----------
sc("""So here are the eleven. A pit that gives people a place to survive. A rail with a roof, and a fourth rail that protects iron tunnels. An arm that stops trains at red lights. Glass walls, and bumpy tiles for those who cannot see the edge. Rubber tyres, stations built on hills, a gap you must mind, escalators made of metal, and a wind that tells you the train is coming.""",
   "London Underground platform", "11 PARTS UNDERGROUND", chapter="The verdict", cuts=6)
sc("""A subway station looks like a simple room with a train passing through. It is actually a carefully designed machine for keeping millions of people alive. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "metro train tunnel", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Bounds Green Underground Station (Piccadilly Line) - 52809713604.jpg", 0.62, 0.75),
    2: ("File:NYC subway third rail.agr.jpg", 0.5, 0.42),
    3: ("File:Cockfosters station centre track platform 2 and 3 look west.JPG", 0.72, 0.62),
    4: ("File:Train stop.jpg", 0.5, 0.6),
    5: ("File:Metro SPB Line2 Park Pobedy.jpg", 0.3, 0.55),
    6: ("File:Tactile Ground Surface Indicators at Corinda railway station along platform edge.jpg", 0.45, 0.6),
    7: ("File:Gummibereifung der metro.JPG", 0.42, 0.55),
    8: ("File:Southgate station southbound look north tunnel.JPG", 0.52, 0.45),
    9: ("File:Bournemouth (9453245033).jpg", 0.45, 0.15),
    11: ("File:Novatorskaya - south-east ventilation shaft 2.jpg", 0.47, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video48", "title": "Why Is There a Pit Under Subway Tracks?",
           "length_scale": 1.6, "scenes": S}, open("videos/video48/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
