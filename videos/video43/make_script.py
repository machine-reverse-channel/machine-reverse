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
sc("""Some oil platforms stand in water deeper than the Grand Canyon. They are as heavy as a city block, they face waves taller than a house, and they must stay in almost exactly the same spot for decades, because a pipe connects them to a hole in the sea floor. If they drift too far, the pipe breaks. So how do they stay put? Today, ten parts of offshore platforms, and why each one exists.""",
   "offshore oil platform", "10 PARTS. 0 METERS OF DRIFT.", cuts=8, chapter="Intro")
sc("""The first platforms were built in shallow water, on simple steel legs, like a pier in the middle of the sea. But the oil kept moving deeper, from tens of meters of water to hundreds, and then to thousands. At each step, engineers had to invent a new way to hold a giant structure still on a moving ocean. That is why offshore platforms come in so many strange shapes.""",
   "oil platform North Sea", "DEEPER AND DEEPER")
sc("""As always, every fact comes from a named source, official accident reports, energy companies, and engineering references, all listed in the description. Let's start with a platform that stands up on its own legs.""",
   "jack-up rig legs", "WHY DOES THIS EXIST?")

# ---------- 1. JACK-UP ----------
part(1, "The legs that climb", "WHY DOES THIS RIG LIFT ITSELF UP?", "Why Do Some Oil Rigs Lift Themselves Out of the Water?",
     """Why do some oil rigs lift themselves out of the water? They are called jack-ups. The rig floats to the site like a barge, with its long legs pointing to the sky. Then motors walk the legs down to the sea floor, and keep pushing until the whole hull rises out of the sea. Now the rig stands on the bottom like a table, high enough that the biggest waves pass underneath it.""",
     "jack-up rig legs")
sc("""At the bottom of each leg is a big foot called a spud can, shaped a bit like an upside down cone. Before drilling, the crew fills tanks with seawater to make the rig much heavier than normal. This is called preloading. It pushes the feet deep into the seabed and tests the soil. If the ground is going to give way, it is much better to find out now, slowly, than later in a storm.""",
   "jackup rig leg spud can", "TEST THE GROUND FIRST")
sc("""Jack-ups have a limit. Their legs can only be so long, so they work in relatively shallow water, typically up to around one hundred fifty meters. When the job is done, the legs climb back up, the rig floats again and is towed to the next location. A building that walks down to the sea floor and climbs back up when it wants to leave.""",
   "jack-up rig towed", "A BUILDING THAT WALKS")

# ---------- 2. TLP ----------
part(2, "The cables pulling down", "WHY IS THIS PLATFORM PULLED DOWN?", "Why Are Some Oil Platforms Pulled Underwater?",
     """Why do some floating platforms pull themselves down instead of floating up? A tension leg platform has a hull that wants to float much higher than it does. But it is tied to the sea floor by vertical steel tubes called tendons, pulled extremely tight. The buoyancy pulls up, the tendons pull down. The platform can slide a little sideways in waves, but it barely moves up and down at all.""",
     "tension leg platform")
sc("""That vertical stillness is the whole point. On a platform that does not bob, the wells can be controlled from the deck, almost like on land. The first tension leg platform to produce oil was Hutton, in the British North Sea, in nineteen eighty-four. Later ones in the Gulf of Mexico went into water more than a kilometer deep.""",
   "tension leg platform tendons", "STILL AS LAND")
sc("""The tendons are a bit like the strings of a guitar, tight enough that they never go slack, even when a big wave passes. If a tendon ever went slack and then snapped tight again, the shock could damage it. So engineers design the platform with so much extra buoyancy that the tendons stay tight in any storm they expect. Tension is the safety.""",
   "offshore platform storm waves", "TENSION IS SAFETY")

# ---------- 3. SPAR ----------
part(3, "The giant fishing float", "WHY IS THIS PLATFORM A GIANT TUBE?", "Why Do Some Oil Platforms Float on a Giant Tube?",
     """Why do some platforms sit on one huge vertical tube? They are called spars, and they work like a fishing float. The tube is very long, most of it underwater, and its bottom is heavy, so the center of gravity sits far below the center of buoyancy. Like a float with a weight at the bottom, it always wants to stand upright. And because most of it is deep below the waves, the surface motion barely moves it.""",
     "spar platform offshore")
sc("""The first production spar, Neptune, was installed in the Gulf of Mexico in nineteen ninety-six. One of the most famous, Perdido, floats over water about two thousand four hundred fifty meters deep, around eight thousand feet. Its hull is about one hundred seventy meters long, taller than many skyscrapers, and it was towed to the site lying on its side, then flooded to flip upright.""",
   "Perdido spar platform", "TOWED LYING DOWN")
sc("""A spar is held in place by mooring lines spread out like the strings of a tent. In deep water, steel chain would be too heavy to hang that far, so the middle of each line is often made of polyester rope, strong, flexible, and much lighter in water. A platform in the deep ocean is often held by something closer to a giant rope than a chain.""",
   "offshore mooring polyester rope", "HELD BY ROPE")

# ---------- 4. GRAVITY BASE ----------
part(4, "The concrete giant", "WHY DOESN'T THIS PLATFORM NEED ANCHORS?", "Why Doesn't This Giant Platform Need Anchors?",
     """Why doesn't this platform need any anchors at all? Because it is simply too heavy to move. It is a gravity-based structure, a giant made of reinforced concrete that sits on the sea floor and is held down by its own weight. The most famous is Troll A in Norway. Its total height is about four hundred seventy-two meters, and in nineteen ninety-five it was towed out to sea, becoming one of the tallest structures ever moved by humans.""",
     "Troll A platform")
sc("""Troll A stands in about three hundred meters of water, so most of it is hidden below the surface. Concrete giants like this were built standing in deep, sheltered Norwegian fjords. The base was built first, then flooded to sink lower and lower while the walls grew taller. When finished, the whole thing was floated out using air in its big hollow cells, and then flooded again to settle on the seabed.""",
   "gravity based structure platform", "BUILT IN A FJORD")
sc("""In Canada, the Hibernia platform uses the same idea for another reason, icebergs. Its gravity base has an ice wall with teeth designed to resist the impact of an iceberg. It sits off Newfoundland, in the stretch of the North Atlantic called Iceberg Alley. When you cannot move out of the way, you become a wall.""",
   "iceberg Newfoundland", "BECOME A WALL")

# ---------- 5. ANCHOR LINES ----------
part(5, "The anchor lines", "WHY DO FLOATING RIGS NEED THESE CHAINS?", "Why Do Floating Oil Rigs Need So Many Anchors?",
     """Why do floating rigs need so many anchors? A semi-submersible rig floats on giant pontoons deep under the water, with columns rising up to the deck. Because the pontoons are below the waves, it moves much less than a ship. But it still floats, so it is held in place by eight, ten or more anchor lines spread around it. Each link of the chain can be the size of a person's torso.""",
     "semi-submersible drilling rig")
sc("""A floating rig is only as strong as its structure. In nineteen eighty, the semi-submersible Alexander L. Kielland, used as a floating hotel for oil workers in the North Sea, capsized in a storm. One of its bracing tubes broke. The investigation found a fatigue crack that had started at a poorly made weld around a small fitting. One hundred twenty-three people died.""",
   "Alexander L. Kielland", "ONE SMALL WELD", file="File:Alexander L Kielland and Edda 2-7C NOMF-02663-1-650.jpg")
sc("""That disaster changed the rules for offshore structures, with more redundancy so that one broken member cannot capsize a rig, and better lifeboats and evacuation. Offshore engineering is full of lessons like this. A platform is designed to survive the hundred-year wave. The real danger is often a small crack nobody saw.""",
   "offshore anchor chain", "THE CRACK NOBODY SAW")

# ---------- 6. THRUSTERS ----------
part(6, "The propellers that hold still", "WHY 6 PROPELLERS TO STAND STILL?", "Why Do Drillships Have Propellers Pointing Everywhere?",
     """Why do some drilling ships have propellers pointing in every direction, when they never go anywhere? Because in very deep water, anchors become impractical. So these ships use dynamic positioning. Satellite navigation, motion sensors and wind sensors feed a computer, which constantly adjusts six or more thrusters to push against the wind, waves and current. The ship can hold its position over a well within a few meters, without touching the bottom.""",
     "dynamic positioning thruster")
sc("""The idea started early. In nineteen sixty-one, the drilling vessel CUSS One drilled into the sea floor off Mexico for Project Mohole, holding position with steerable propellers while operators watched buoys and radar. Today, the system is fully automated and has backups for its backups, because a drillship that drifts off position while connected to a well is an emergency.""",
   "drillship", "BACKUPS FOR BACKUPS")
sc("""Dynamic positioning is now used by many kinds of ships, from cable layers to cruise ships waiting near a port where anchoring is not allowed. The ship is not parked. It is driving very hard to stay exactly where it is. Standing still, it turns out, burns a lot of fuel.""",
   "drillship thrusters drydock", "DRIVING TO STAND STILL")

# ---------- 7. MOONPOOL ----------
part(7, "The hole in the middle", "WHY IS THERE A HOLE IN THIS SHIP?", "Why Do Drillships Have a Hole in the Middle?",
     """Why is there a big hole in the middle of a drilling ship? It is called the moonpool, an opening straight through the hull, from the deck down to the sea. The drill pipe, the riser and the equipment go down through it, protected from the waves at the sides of the ship. Supposedly the name comes from the moonlight reflecting on the water inside it at night.""",
     "drillship moonpool")
sc("""But there is another problem. The ship rises and falls with the waves, sometimes by several meters, while the drill bit is kilometers below, trying to press on the rock with a steady force. So the drill string hangs from a heave compensator, a system of giant cylinders and pressurized gas that works like a shock absorber, letting the ship move up and down while the pipe stays steady.""",
   "drill string derrick offshore", "THE SHIP MOVES, THE DRILL DOESN'T")
sc("""The pipe that connects the ship to the well is called the riser, and in ultra-deep water it can be more than three kilometers long, hanging from the ship like a giant steel straw. Currents push on it, the ship pulls it, and it must not bend too much. That is the real reason a rig cannot float away. It is attached to the sea floor by a long, fragile straw.""",
   "offshore riser", "A 3 KM STRAW")

# ---------- 8. BOP ----------
part(8, "The giant valve", "WHY DOES THIS VALVE SIT ON THE SEA FLOOR?", "Why Is There a Giant Valve on the Sea Floor?",
     """Why does every offshore well have a building-sized valve sitting on the sea floor? It is the blowout preventer. If gas or oil rushes up the well uncontrolled, the crew can close it. Some of its parts squeeze rubber around the pipe, and the strongest, called shear rams, are designed to cut straight through the drill pipe and seal the well completely. It is the last line of defense.""",
     "blowout preventer")
sc("""On April twentieth, twenty ten, the Deepwater Horizon rig in the Gulf of Mexico suffered a blowout. Gas reached the rig and exploded, and eleven workers died. The blowout preventer was activated but failed to seal the well. Investigators found that the drill pipe had been pushed off center, so the shear rams could not cut and seal it properly. Oil flowed into the Gulf for eighty-seven days.""",
   "Deepwater Horizon", "87 DAYS")
sc("""After the disaster, rules for blowout preventers became stricter in the United States, with more testing and requirements for equipment that can cut pipe in more conditions. The giant valve is a perfect example of offshore engineering. It works silently for years at the bottom of the sea, and it must work perfectly on the one day it is needed.""",
   "blowout preventer stack", "THE ONE DAY")

# ---------- 9. FLARE ----------
part(9, "The flame on the boom", "WHY DOES THIS PLATFORM BURN A FLAME?", "Why Do Oil Platforms Have a Burning Flame?",
     """Why do many oil platforms have a long arm with a flame burning at the end? It is the flare. The most important reason is safety. If pressure builds up somewhere in the process, or if there is an emergency, gas has to go somewhere. Releasing it unburned near a platform full of people and engines could create an explosive cloud. So it is sent to the end of the boom, far from the deck, and burned.""",
     "oil platform flare stack")
sc("""The boom sticks out far from the platform, and it is often placed so that the wind usually blows the heat away. In an emergency, a platform can send large amounts of gas to the flare in minutes, called blowdown, to empty dangerous equipment quickly. A small pilot flame often burns all the time, so the flare is always ready to light.""",
   "offshore flare boom", "ALWAYS READY")
sc("""In the past, many fields also flared gas simply because there was no pipeline to sell it. That is wasteful and polluting, and today many countries limit routine flaring and push companies to capture the gas instead. But the safety flare stays. On a platform, the most dangerous gas is the gas with nowhere to go.""",
   "gas flaring", "NOWHERE TO GO")

# ---------- 10. FREE FALL LIFEBOAT ----------
part(10, "The lifeboat that falls", "WHY IS THIS LIFEBOAT POINTING DOWN?", "Why Do Oil Rig Lifeboats Drop Into the Sea?",
     """Why are some lifeboats on oil platforms pointing down at the sea, like a ride at an amusement park? They are free-fall lifeboats. Instead of being lowered slowly by ropes, they slide off a ramp and drop straight into the water, sometimes from more than twenty or thirty meters. They hit the water nose first, dive, and come up already moving away from the platform.""",
     "free fall lifeboat")
sc("""Why drop people from that height? Because on a burning or capsizing platform, slow lowering can be deadly. Ropes can jam, the boat can swing into the structure, and waves can smash it against the legs. A free-fall boat leaves in seconds and gets away from the danger. The seats face backward with strong harnesses, so the crew can survive the impact.""",
   "free fall lifeboat launch", "OUT IN SECONDS")
sc("""The North Sea learned this the hard way. After the Alexander Kielland disaster, and later Piper Alpha in nineteen eighty-eight, where an explosion and fire on a platform killed one hundred sixty-seven people, offshore safety rules changed deeply. Free-fall lifeboats became common, especially in Norway. A boat that falls on purpose is safer than one that might fall by accident.""",
   "Piper Alpha", "FALL ON PURPOSE")

# ---------- VERDICT ----------
sc("""So here are the ten. Legs that walk down to the sea floor. Cables that pull a floating hull down. A giant fishing float, and a concrete tower too heavy to move. Anchor lines, and propellers that drive just to stand still. A hole in the middle of a ship, a valve on the sea floor, a flame on a long arm, and a lifeboat that falls on purpose.""",
   "offshore oil platform", "10 PARTS. NO DRIFT.", chapter="The verdict", cuts=6)
sc("""An oil platform does not stay in place by accident. Every shape fights the sea in a different way. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "oil platform sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Jackup Rig - Galveston TX.jpg", 0.22, 0.35),
    3: ("File:Shell Perdido deepwater offshore production platform (51115227891).jpg", 0.31, 0.72),
    4: ("File:Troll A Platform.jpg", 0.48, 0.8),
    5: ("File:Ramnäs bruk AB 5.jpg", 0.35, 0.65),
    6: ("File:Siemens Schottel Propulsor.jpg", 0.42, 0.4),
    7: ("File:2025 07 24 Océan Arctique équipage en action David Monmarché plongée Moon Pool P1005493.jpg", 0.5, 0.45),
    8: ("File:Blowout Preventer (BOP).jpg", 0.35, 0.45),
    9: ("File:Gullfaks Alpha.jpg", 0.15, 0.25),
    10: ("File:Freefall lifeboat.JPG", 0.62, 0.45),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video43", "title": "Why Don't Oil Rigs Float Away?",
           "length_scale": 1.6, "scenes": S}, open("videos/video43/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
