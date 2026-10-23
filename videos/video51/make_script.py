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
sc("""Under the sea between England and France, there is a machine that will never see daylight again. It dug part of the Channel Tunnel, and when the job was done, the workers did not bring it back. They steered it down into the rock, out of the way, and left it there. Today, eleven parts of a tunnel boring machine, and why each one exists, starting with the strange reason so many of them stay underground.""",
   "tunnel boring machine", "BURIED FOREVER", cuts=8, chapter="Intro")
sc("""A tunnel boring machine is a factory on the move. The front is a spinning wheel of steel that grinds through rock or soil. Behind it, the machine builds the tunnel walls as it goes, and behind that, a train of trailers up to hundreds of meters long carries everything the crew needs. Some of these machines are wider than a four story building is tall.""",
   "tunnel boring machine cutterhead", "A FACTORY ON THE MOVE")
sc("""As always, every fact comes from a named source, tunnel builders, engineering references, and official project reports, all listed in the description. Let's start with the question in the title.""",
   "tunnel boring machine", "WHY DOES THIS EXIST?")

# ---------- 1. LEFT BEHIND ----------
part(1, "The machine left in the ground", "WHY IS THIS MACHINE LEFT UNDERGROUND?", "Why Are Tunnel Boring Machines Left Underground?",
     """Why would anyone bury a machine worth millions? Because it cannot go back the way it came. The front of a tunnel boring machine, called the shield, is a little wider than the finished tunnel behind it, because the tunnel walls are built inside the shield. So the machine cannot reverse through the tunnel it just dug. It can only go forward, or be cut into pieces where it stands.""",
     "Channel Tunnel boring machine")
sc("""Cutting it up underground is slow and expensive. Workers need weeks or months to take the machine apart in a narrow tunnel and carry the pieces out. Often the used machine is worth less than that work. So when the end of the tunnel is not near a shaft, builders sometimes do the cheaper thing. They strip out the useful parts, drive the shield into a side pocket, and fill it with concrete.""",
   "tunnel boring machine", "CHEAPER TO BURY")
sc("""That is what happened under the English Channel. The British and French machines met in nineteen ninety. The British ones turned down into the rock and were buried, so the French ones could break through and be taken out. Years later, one Channel Tunnel machine was even put up for sale online. Many machines today are refurbished and reused, but some still end their lives as part of the tunnel they built.""",
   "Channel Tunnel", "SOLD ONLINE")

# ---------- 2. DISC CUTTERS ----------
part(2, "The steel discs on the cutterhead", "WHY IS THIS WHEEL COVERED IN DISCS?", "Why Does a Tunnel Boring Machine Have Steel Discs?",
     """Why is the front of a tunnel boring machine covered in little steel wheels? Because they do not cut the rock like a saw. Each disc rolls in a circle on the rock face, pressed against it with tonnes of force. The pressure crushes the rock under the disc and cracks it sideways, so chips flake off between neighboring tracks. The rock breaks itself.""",
     "TBM cutter disc")
sc("""A big hard rock machine can carry dozens of these discs, each about forty centimeters across. The cutterhead turns a few times per minute, pushed forward by hydraulic rams. In very hard rock, like granite, the discs wear out fast, and the crew stops regularly to inspect them and change the worn ones.""",
   "tunnel boring machine cutterhead", "THE ROCK BREAKS ITSELF")
sc("""Changing them is one of the hardest jobs in tunneling. Workers climb through the cutterhead to the face of the tunnel. In soft ground under water, the chamber behind the cutterhead is under pressure, so the workers breathe compressed air and need decompression afterwards, like deep sea divers. Some new machines change discs with robots for exactly that reason.""",
   "tunnel boring machine", "DIVERS UNDERGROUND")

# ---------- 3. SEGMENTS ----------
part(3, "The concrete puzzle pieces", "WHY IS THE TUNNEL MADE OF PUZZLE PIECES?", "Why Are Tunnels Built From Concrete Puzzle Pieces?",
     """Why is the wall of the tunnel made of curved concrete pieces? Because the machine builds the tunnel as it digs. The pieces, called segments, are made in a factory and brought in by train. Inside the shield, a rotating arm called the erector picks up each segment and places it, forming a ring. Usually six or seven segments plus a small key piece close one ring.""",
     "tunnel lining segments")
sc("""The rings are bolted together and sealed with rubber gaskets, so water from the ground cannot get in. The machine digs a little more than one ring length, stops, builds the next ring, and moves on. Ring after ring, the tunnel appears behind the machine, already finished.""",
   "tunnel segment erector", "RING AFTER RING")
sc("""The last segment, the key, is shaped like a wedge. It slides in last and locks the whole ring, like the keystone of a stone arch. Without it, the ring is just a pile of curved concrete. With it, the ring can hold back the weight of the ground and the pressure of water for more than a hundred years.""",
   "tunnel lining segments", "THE KEY LOCKS IT")

# ---------- 4. THRUST JACKS ----------
part(4, "The jacks that push off the walls", "WHY DOES THE MACHINE PUSH ON ITS OWN TUNNEL?", "Why Does a Tunnel Boring Machine Push Off Its Own Walls?",
     """How does a machine without wheels move forward through solid rock? It pushes against the tunnel it just built. Around the back of the shield, a ring of powerful hydraulic jacks presses against the last concrete ring. When they extend, the whole machine slides forward and the cutterhead is pressed into the face. Then the jacks pull back, a new ring is built, and the cycle starts again.""",
     "tunnel boring machine")
sc("""The force can be enormous, tens of thousands of tonnes on the biggest machines. And the jacks also steer. Push harder on the left side, and the machine turns right. Push harder at the bottom, and it climbs. The operator does this constantly, guided by lasers and computers that know where the machine should be to within a few millimeters.""",
   "tunnel boring machine", "STEERING WITH JACKS")
sc("""In hard rock, some machines use a different trick. Instead of pushing on segments, they press big pads called grippers against the rock walls on both sides, lock themselves in place, and push the cutterhead forward from there. Then they release the grippers, pull the body forward, and grip again, like an inchworm.""",
   "Gotthard Base Tunnel", "LIKE AN INCHWORM")

# ---------- 5. GROUT ----------
part(5, "The grout behind the ring", "WHY IS GROUT PUMPED BEHIND THE WALLS?", "Why Do Tunnel Machines Pump Grout Behind the Walls?",
     """Why does a tunnel boring machine pump liquid grout behind the walls it builds? Because there is a gap. The cutterhead digs a hole slightly wider than the shield, and the segments are built inside the shield. When the shield moves on, a ring of empty space is left between the concrete and the ground. If nothing fills it, the ground above slowly sinks into it.""",
     "tunnel grout")
sc("""In a city, that matters a lot. A few centimeters of settlement can crack the buildings above, break water pipes, or tilt railway tracks. So the machine injects grout through the tail of the shield, at the same moment it moves forward, filling the gap before the ground can move.""",
   "tunnel boring machine Crossrail", "BUILDINGS ABOVE")
sc("""Engineers watch the surface the whole time. Under London, during the Crossrail project, thousands of sensors measured buildings above the tunnels. Under some historic buildings, they even pumped grout into the ground beforehand, ready to push it back up if it started to sink.""",
   "Crossrail", "THOUSANDS OF SENSORS")

# ---------- 6. PRESSURE CHAMBER ----------
part(6, "The chamber full of mud", "WHY IS THERE MUD BEHIND THE CUTTER?", "Why Do Tunnel Machines Keep Mud Behind the Cutter?",
     """Why do soft ground tunnel machines keep a chamber full of mud behind the cutterhead? Because in soft soil under water, the face of the tunnel wants to collapse. The soil and water push into the hole. An earth pressure balance machine fills the chamber behind the cutterhead with the dug soil itself, turned into a thick paste, and keeps it pressed against the face, at the same pressure as the ground outside.""",
     "earth pressure balance shield")
sc("""A long screw conveyor takes the paste out of the chamber, and its speed controls the pressure. Turn it faster, and pressure drops. Turn it slower, and pressure rises. If the pressure is too low, the ground above can collapse into the tunnel. If it is too high, the machine can push the ground up, and even blow mud out at the surface.""",
   "tunnel boring machine", "BALANCE THE PRESSURE")
sc("""Other machines, called slurry shields, use bentonite clay mixed with water instead. The slurry holds the face and is pumped through pipes to a plant on the surface, where the soil is separated out and the slurry is reused. Either way, the idea is the same. Hold the ground with pressure until the concrete ring is in place.""",
   "slurry shield TBM", "SLURRY SHIELDS")

# ---------- 7. BACKUP ----------
part(7, "The train behind the machine", "WHY IS THERE A TRAIN BEHIND THE CUTTER?", "Why Do Tunnel Machines Drag a Train Behind Them?",
     """Why does a tunnel boring machine drag a long chain of trailers behind it? Because the cutterhead is only the tip. Behind it, on what is called the backup, are the electric transformers, hydraulic pumps, grout tanks, ventilation, a control cabin, toilets and a place for the crew to eat. The whole thing can be more than a hundred meters long.""",
     "TBM backup gantry")
sc("""The dug material has to leave too. On many machines, a conveyor belt carries the broken rock back through the tunnel, sometimes for kilometers, to the surface. On others, small trains carry it out in wagons, and bring segments back in on the return trip.""",
   "TBM conveyor belt tunnel", "KILOMETERS OF BELT")
sc("""The crew lives inside this moving factory. Work goes on day and night, in shifts, for years. On a good day, a modern machine can advance tens of meters. On a bad day, in broken rock or mud, it might not advance at all.""",
   "tunnel boring machine", "DAY AND NIGHT, FOR YEARS")

# ---------- 8. BERTHA ----------
part(8, "The seals that failed under Seattle", "WHY DID THIS GIANT MACHINE GET STUCK?", "Why Did the Biggest Tunnel Machine Get Stuck?",
     """Why did one of the biggest tunnel machines ever built stop under Seattle for two years? The machine, named Bertha, was more than seventeen meters across. In December two thousand thirteen, after about a thousand feet of digging, it overheated and stopped. Investigators later found damaged seals around the main bearing, the part that lets the cutterhead turn.""",
     "Bertha tunnel boring machine")
sc("""There was no way to reach the front of the machine from inside. So the builders dug a huge rescue pit from the surface, down to the cutterhead, and lifted the front end of the machine out with a giant crane. It was repaired, put back, and in late two thousand fifteen it started digging again.""",
   "Bertha tunnel boring machine", "A RESCUE PIT")
sc("""Bertha finished the tunnel in two thousand seventeen, and the new highway opened in two thousand nineteen, years late. Who was responsible became a long legal fight. The main bearing and its seals are the heart of the machine, and when the heart fails underground, there is no easy way to reach it.""",
   "Seattle tunnel", "THE HEART FAILED")

# ---------- 9. NAMES ----------
part(9, "The name on every machine", "WHY DOES EVERY TUNNEL MACHINE HAVE A NAME?", "Why Does Every Tunnel Machine Have a Woman's Name?",
     """Why do tunnel boring machines have names like Bertha, Phyllis or Elizabeth? It is a tradition. Miners and tunnelers have long believed a machine should not start digging without a name. The names are usually female, often in honor of Saint Barbara, the patron saint of miners and tunnelers, who is said to protect them from danger underground.""",
     "Saint Barbara statue tunnel")
sc("""On many projects, a small statue of Saint Barbara is placed at the entrance of the tunnel, and the machines are blessed before they start. On Crossrail in London, the eight machines were named after famous women from London's history, chosen by the public.""",
   "tunnel boring machine Crossrail", "BLESSED BEFORE DIGGING")
sc("""It sounds like superstition, and it is. But tunneling was one of the most dangerous jobs in the world for centuries. Collapses, floods and gas killed many workers. A name and a saint at the entrance are a reminder that the people inside are the most important part of the machine.""",
   "tunnel", "THE PEOPLE INSIDE")

# ---------- 10. LASER ----------
part(10, "The laser that steers", "WHY DOES THIS MACHINE NEED A LASER?", "Why Does a Tunnel Machine Need a Laser to Steer?",
     """How does a machine deep underground, with no GPS, know where it is going? It follows a laser. A survey station fixed to the tunnel wall behind the machine shoots a laser beam onto a target on the machine. Computers read the target and calculate the exact position and direction of the cutterhead, so the operator can correct the course.""",
     "tunnel boring machine")
sc("""The survey station itself must be moved forward as the tunnel grows, and every move adds a tiny error. Surveyors check the line again and again, using points measured from the surface down through shafts. In a tunnel kilometers long, being off by a fraction of a degree would mean missing the target by meters.""",
   "tunnel", "A FRACTION OF A DEGREE")
sc("""Under the Channel, the British and French tunnels started more than thirty kilometers apart. When they met in December nineteen ninety, the difference was about thirty five centimeters sideways and less than six centimeters up and down. Two tunnels dug from two countries, under the sea, met almost perfectly.""",
   "Channel Tunnel", "OFF BY 35 CM")

# ---------- 11. GRIPPERS ----------
part(11, "The longest tunnel's machines", "WHY DID THE LONGEST TUNNEL NEED 4 GIANTS?", "Why Did the World's Longest Tunnel Need Four Giant Machines?",
     """Why did the Gotthard Base Tunnel in Switzerland need four giant machines working at the same time? Because it is fifty seven kilometers long, the longest railway tunnel in the world. One machine would have taken far too long. So the builders dug access shafts and tunnels into the mountain, and the machines started from several points at once, digging toward each other.""",
     "Gotthard Base Tunnel")
sc("""Under the Alps, up to two thousand three hundred meters of rock sit above the tunnel. The rock there is hot, sometimes above forty degrees, and it can squeeze in on the tunnel or burst out from the walls. The machines had to dig through granite and gneiss, and some sections were dug with explosives instead.""",
   "Gotthard Base Tunnel", "2,300 METERS OF ROCK ABOVE")
sc("""The tunnel opened in two thousand sixteen, after seventeen years of construction. Freight trains now cross the Alps almost flat, without climbing over the mountains. And the machines? They were taken apart and carried out, piece by piece, to dig again somewhere else.""",
   "Gotthard Base Tunnel", "17 YEARS")

# ---------- VERDICT ----------
sc("""So here are the eleven. A machine that cannot reverse, so it is sometimes buried. Steel discs that let the rock break itself. Concrete puzzle pieces locked by a key, jacks that push off the tunnel, and grout that holds up the city above. A chamber of mud that balances the ground, a train of trailers behind the cutter, a bearing that stopped Bertha, a name and a saint, a laser that steers, and four giants under the Alps.""",
   "tunnel boring machine", "11 PARTS. 0 DAYLIGHT.", chapter="The verdict", cuts=6)
sc("""Next time you ride a subway or drive through a tunnel, remember that a machine like this built it, ring by ring, and might still be down there. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "tunnel boring machine", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:2012 Eurotunnel tunnel boring machine 02.JPG", 0.5, 0.45),
    2: ("File:Hallandsåstunneln TBM disc cutter - 01.jpg", 0.45, 0.45),
    3: ("File:Wewelsfleth SuedLink ElbX Tunnelsegment 20241224.jpg", 0.42, 0.3),
    4: ("File:Tunnel Boring Machine Rachel.jpg", 0.45, 0.4),
    5: ("File:Rondout pressure tunnel. Section of tunnel with finished concrete lining in place. Note grout hole in arch key. Contract 12. October 6, 1910 (NYPL b13814376-435474).jpg", 0.6, 0.45),
    6: ("File:Greenwich Crossrail TBM Tunnel Boring Machines.jpg", 0.62, 0.45),
    7: ("File:Bertha TBM model at Milepost 31.jpg", 0.6, 0.5),
    8: ("File:Bertha TBM retrieval site.jpg", 0.3, 0.4),
    9: ("File:Sainte Barbe tunnel de Cointe.jpg", 0.43, 0.65),
    10: ("File:People welding inside the tunnel boring machine (8903739087).jpg", 0.5, 0.35),
    11: ("File:20141120 gotthard-basistunnel02-wikipedia-hannes-ortlieb.jpg", 0.55, 0.4),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video51", "title": "Why Are Tunnel Boring Machines Left Underground?",
           "length_scale": 1.6, "scenes": S}, open("videos/video51/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
