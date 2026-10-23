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
sc("""When a giant ship sits in dry dock, you can see something strange below the waterline. At the very front, a huge rounded bulb sticks out, like the nose of a dolphin. You never see it when the ship is sailing. But it saves enormous amounts of fuel on every trip. Today, ten parts of a ship, and why each one exists.""",
   "bulbous bow dry dock", "WHY THE BULB?", cuts=8, chapter="Intro")
sc("""A big ship is one of the most efficient machines ever built. It can carry thousands of containers across an ocean, burning less fuel per tonne than a truck or a train. That efficiency comes from parts most people never see, many of them hidden under the water.""",
   "container ship at sea", "HIDDEN UNDER THE WATER")
sc("""As always, every fact here comes from a named source, maritime organisations, shipbuilders and naval references, all listed in the description. Let's start with the bulb.""",
   "ship bow", "WHY DOES THIS EXIST?")

# ---------- 1. BULB ----------
part(1, "The bulbous bow", "WHY DOES THIS SHIP HAVE A BULB?", "Why Do Ships Have a Bulb Under the Front?",
     """Why do ships have a big bulb under the front? To fight waves. As a ship moves, it pushes water aside and creates a large wave at the bow. Making that wave costs energy, a lot of it. The bulb, sitting just below the surface, creates its own small wave, slightly ahead of the main one.""",
     "bulbous bow")
sc("""If the bulb is shaped and placed correctly, its wave meets the main bow wave out of step, with a crest meeting a trough. The two partly cancel each other. The ship makes a smaller wave, and needs less power to move. On large ships at their design speed, the saving can be well over ten percent of the fuel.""",
   "bow wave ship", "WAVES THAT CANCEL")
sc("""There is a catch. The bulb works best at one speed and one depth in the water. When shipping companies started sailing slower to save fuel, some found that the old bulbs no longer helped, and even added drag. Some ships had their bows cut off and rebuilt with a new shape, just to match the new speed.""",
   "ship in dry dock", "ONE SPEED")

# ---------- 2. PROPELLER ----------
part(2, "The giant propeller", "WHY IS THIS PROPELLER SO HUGE?", "Why Are Ship Propellers So Huge?",
     """Why are ship propellers so huge? Because a big, slow propeller is more efficient than a small, fast one. It pushes a large amount of water backwards, gently, rather than a small amount very fast. The propeller of a large container ship can be almost ten metres across and weigh over one hundred tonnes.""",
     "ship propeller")
sc("""Spinning slowly also avoids a problem called cavitation. When a propeller blade spins too fast, the pressure on the back of the blade drops so low that the water boils into tiny bubbles, even in cold sea water. When those bubbles collapse, they hit the metal like tiny hammers, and they can eat holes in the blades.""",
   "propeller cavitation", "TINY HAMMERS")
sc("""That is why giant propellers turn at around one hundred revolutions per minute, slower than a washing machine. Each one is cast in one piece from a bronze alloy and polished by hand. A small scratch or bend can cost fuel on every trip, for the life of the ship.""",
   "bronze ship propeller", "SLOWER THAN A WASHING MACHINE")

# ---------- 3. BOW THRUSTER ----------
part(3, "The bow thruster", "WHY IS THERE A TUNNEL IN THE BOW?", "Why Do Ships Have a Tunnel in the Bow?",
     """Why do many ships have a round tunnel going straight through the front of the hull? It holds a bow thruster, a propeller that pushes sideways. A big ship's main propeller and rudder only work well when the ship is moving forward. At very low speed, in a harbour, they cannot turn the front of the ship.""",
     "bow thruster")
sc("""The bow thruster solves that. By pushing water to the left or right, it swings the bow sideways, without the ship moving forward. Many ships have thrusters at the stern too. Together, they let a ship slide sideways into a berth, without needing tugboats every time.""",
   "bow thruster tunnel", "SIDEWAYS")
sc("""The thruster tunnel is usually marked on the side of the hull with a sign, a circle with an arrow or the letters for thruster. It warns small boats and tugboats to stay clear, because the thruster can create a strong current that pulls or pushes them. A small sign for a powerful hidden part.""",
   "bow thruster sign", "STAY CLEAR")

# ---------- 4. PLIMSOLL ----------
part(4, "The load line", "WHY IS THERE A CIRCLE ON THE SIDE?", "Why Do Ships Have a Circle With a Line on the Side?",
     """Why is there a circle with a line through it painted on the side of ships? It is the load line, also called the Plimsoll line. It shows how deep a ship can safely sit in the water. If the water rises above the line, the ship is overloaded, and it could sink in a storm.""",
     "Plimsoll line")
sc("""It is named after Samuel Plimsoll, a British politician who campaigned in the eighteen seventies against overloaded ships, which owners sometimes sent to sea knowing they might sink. The law made the mark mandatory. Next to the circle, a ladder of short lines shows different limits for different waters and seasons.""",
   "load line marks", "SAMUEL PLIMSOLL")
sc("""The ladder exists because water is not all the same. Fresh water is less dense than sea water, so a ship sinks deeper in a river. Cold water is denser than warm water. And winter seas are rougher, so ships must carry less. One painted mark keeps all these rules in one place.""",
   "ship load line", "NOT ALL WATER IS THE SAME")

# ---------- 5. RUDDER ----------
part(5, "The rudder", "WHY IS THE RUDDER BEHIND THE PROPELLER?", "Why Is a Ship's Rudder Behind the Propeller?",
     """Why is a ship's rudder placed right behind the propeller? Because the propeller blows a fast stream of water straight onto it. A rudder works by turning that flowing water, pushing the stern sideways. The faster the water, the stronger the push. Behind the propeller, the rudder gets the fastest water on the ship.""",
     "ship rudder")
sc("""This matters most at low speed. When the ship is moving slowly, the water around the hull is almost still, and a rudder in still water does nothing. But if the propeller is turning, it still blows water over the rudder, and the ship can steer. Captains use short bursts of power to turn in tight spaces.""",
   "ship rudder dry dock", "STEERING AT LOW SPEED")
sc("""A large ship's rudder is the size of a house wall, and it is moved by powerful hydraulic machines. Even so, a giant ship turns slowly. It can take several kilometres to stop or make a full turn. That is why ships have to plan every move long before a harbour or a narrow channel.""",
   "ship steering gear", "THE SIZE OF A WALL")

# ---------- 6. KORT NOZZLE ----------
part(6, "The propeller nozzle", "WHY IS THIS PROPELLER INSIDE A RING?", "Why Do Tugboat Propellers Spin Inside a Ring?",
     """Why do some ship propellers spin inside a ring? The ring is called a nozzle, or Kort nozzle, after the German engineer Ludwig Kort, who developed it. It is shaped like a short, thick tube, with a curved inside, like the cross section of a wing.""",
     "Kort nozzle")
sc("""At low speed and high power, a propeller loses a lot of energy at the tips of its blades, where water slips around them. The ring stops that, and guides more water through the propeller. The ring itself is also shaped to produce extra thrust. Together, they can push much harder than an open propeller.""",
   "ducted propeller", "MORE PUSH")
sc("""That is why you see nozzles on tugboats, fishing trawlers and other ships that need to pull heavy loads at low speed. A tugboat is not built to go fast. It is built to push and pull a giant ship, and the nozzle gives it extra pulling power for its size.""",
   "tugboat", "BUILT TO PULL")

# ---------- 7. ANCHOR ----------
part(7, "The anchor chain", "WHY IS THE CHAIN MORE IMPORTANT THAN THE ANCHOR?", "Why Is the Anchor Chain More Important Than the Anchor?",
     """Why is the anchor chain more important than the anchor itself? Because most of the holding comes from the chain. A ship lets out much more chain than the depth of the water. The heavy chain lies along the sea floor, and it pulls on the anchor horizontally, so the anchor digs in instead of being lifted out.""",
     "anchor chain")
sc("""The weight of the chain also acts like a spring. When a wave or the wind pulls the ship, the chain lifts off the seabed a little, absorbing the shock, and then settles back down. If the chain were short and straight, every pull would yank the anchor out of the sea floor.""",
   "ship anchor", "A HEAVY SPRING")
sc("""A large ship's anchor chain is made of links that can weigh more than a hundred kilograms each. The chain runs into a locker deep inside the bow. When the anchor is dropped, it roars out in a cloud of rust and dust. One of the oldest tricks in shipping is still all about weight.""",
   "anchor windlass", "IT'S ALL ABOUT WEIGHT")

# ---------- 8. ANODES ----------
part(8, "The sacrificial anodes", "WHY ARE THERE METAL BLOCKS ON THE HULL?", "Why Do Ships Have Metal Blocks on the Hull?",
     """Why are there small metal blocks fixed to the hull of a ship? They are sacrificial anodes, usually made of zinc or aluminium. Steel in salt water rusts, through a slow electrical process. Two different metals in sea water act like a battery, and the more active metal corrodes first.""",
     "sacrificial anode ship")
sc("""Zinc and aluminium are more active than steel. So when they are attached to the hull, they corrode instead of the steel. They slowly dissolve, giving up their metal, while the hull stays protected. That is why they are called sacrificial. They die so the ship does not.""",
   "zinc anode", "THEY DIE SO THE SHIP DOESN'T")
sc("""Anodes are placed near the propeller, the rudder and other parts where different metals meet, like the bronze propeller and the steel hull. They are checked and replaced in dry dock. A few cheap blocks of zinc protect a ship worth tens of millions.""",
   "ship hull dry dock", "CHEAP BLOCKS, EXPENSIVE SHIP")

# ---------- 9. BRIDGE WINGS ----------
part(9, "The bridge wings", "WHY DOES THE BRIDGE STICK OUT TO THE SIDES?", "Why Does a Ship's Bridge Stick Out to the Sides?",
     """Why does the bridge of a ship stick out past the sides of the hull? These extensions are called bridge wings. From the middle of the bridge, the officers cannot see the side of their own ship, or how close it is to the dock. From the end of a bridge wing, they can look straight down along the hull.""",
     "ship bridge wing")
sc("""During docking, the captain and the pilot walk out onto the wing to see the gap between the ship and the quay. Many bridge wings have a small control station with the thrusters and engines, so the ship can be steered right from there. Some even have a glass floor to look straight down.""",
   "ship bridge", "LOOKING DOWN")
sc("""On a giant container ship, the bridge can be hundreds of metres from the bow, and the view forward is partly blocked by containers. That is why the rules limit how much of the sea in front of the ship can be hidden. The bridge wings are the captain's eyes when the ship is closest to danger.""",
   "container ship bridge", "THE CAPTAIN'S EYES")

# ---------- 10. DOUBLE HULL ----------
part(10, "The double hull", "WHY DOES THIS TANKER HAVE TWO HULLS?", "Why Do Oil Tankers Have Two Hulls?",
     """Why do oil tankers have two hulls, one inside the other? To stop oil spills. A single hull is only one layer of steel between the oil and the sea. If the ship hits a rock, the hull can tear open, and the oil flows straight out. With a double hull, there is a space between the outer skin and the tanks.""",
     "double hull tanker")
sc("""In nineteen eighty-nine, the tanker Exxon Valdez ran aground in Alaska and spilled a huge amount of crude oil, one of the worst environmental disasters of its time. After that, the United States passed laws requiring double hulls, and international rules soon followed for new tankers.""",
   "Exxon Valdez", "AFTER EXXON VALDEZ")
sc("""In a minor grounding, the outer hull can be damaged while the inner hull stays intact. The space between them can also hold ballast water when the ship is empty. A double hull does not make spills impossible, but it has made them much less common. Sometimes one disaster changes how every ship is built.""",
   "oil tanker", "ONE DISASTER CHANGED EVERY SHIP")

# ---------- VERDICT ----------
sc("""So here are the ten. A bulb that cancels the bow wave. A giant slow propeller. A sideways thruster for docking. A painted line against overloading. A rudder in the propeller's stream. A ring that adds pulling power. A chain that holds more than the anchor. Blocks of zinc that sacrifice themselves. Bridge wings for the captain's eyes. And a double hull against oil spills.""",
   "container ship", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""The biggest machines on Earth hide their cleverest parts under the water. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which ship you want us to take apart next.""",
   "ship at night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Bulbous bow container feeder.jpg', 0.5, 0.55),
    2: ('File:Ship-propeller 2000.jpg', 0.5, 0.33),
    3: ('File:Brosen bowthruster pharos.jpg', 0.47, 0.45),
    4: ('File:Plimsoll mark.jpg', 0.62, 0.62),
    5: ('File:Rudder and propeller Beached fishing vessel Nørre Vorupør Denmark 2017-04-14.jpg', 0.3, 0.45),
    6: ('File:Union Sapphire close up of the propellor 11-Jan-2005.jpg', 0.27, 0.5),
    7: ('File:Anchor chain (cable). (9769053784).jpg', 0.5, 0.5),
    8: ('File:2022-01-18 sacrificial galvanic anode.jpg', 0.45, 0.5),
    9: ('File:Nipponmaru bridge wing 20170929.jpg', 0.4, 0.68),
    10: ('File:Polar Endeavour 31930.JPG', 0.45, 0.6),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video35", "title": "Why Do Ships Have a Bulb Under the Front?",
           "length_scale": 1.6, "scenes": S}, open("videos/video35/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
