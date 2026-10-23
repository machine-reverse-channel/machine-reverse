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
sc("""The biggest cruise ships rise more than sixty metres above the water, as tall as a twenty storey building. Yet below the water, the hull goes down only about nine metres. It looks impossible. A tall, thin tower floating on a shallow base should simply fall over in the first strong wind. It does not. Today, ten parts of a cruise ship, and why each one exists.""",
   "cruise ship", "WHY DON'T THEY TIP?", cuts=8, chapter="Intro")
sc("""The secret is not what you see above the water. It is where the weight is, how wide the hull is, and a long list of systems that fight every wave, every gust of wind and every turn. A cruise ship is a balancing act, engineered down to the last tonne.""",
   "cruise ship at sea", "A BALANCING ACT")
sc("""As always, every fact here comes from a named source, maritime safety rules, shipbuilders and naval references, all listed in the description. Let's start with the weight.""",
   "cruise ship side", "WHY DOES THIS EXIST?")

# ---------- 1. LOW WEIGHT ----------
part(1, "The heavy bottom", "WHY DOESN'T THIS TALL SHIP FALL OVER?", "Why Don't Cruise Ships Tip Over?",
     """Why doesn't a tall cruise ship tip over? Because almost all of its heavy parts are at the very bottom. The engines, generators, fuel, fresh water tanks and the thick steel of the hull all sit low, below the waterline. The decks above are full of cabins, theatres and pools, which are big but relatively light.""",
     "cruise ship hull dry dock")
sc("""The result is a low centre of gravity. When the ship leans, the heavy bottom swings back like the weight in a toy that always stands up. Designers often use lighter materials like aluminium high up, to keep the top as light as possible. Every tonne added on a top deck has to be balanced by weight down below.""",
   "cruise ship engine room", "LIKE A TOY THAT STANDS UP")
sc("""Naval architects describe this with a number called the metacentric height. It measures how strongly a ship pushes itself back upright when it tilts. Too small, and the ship rolls over easily. Too large, and the ship snaps back so fast that passengers feel sick. Cruise ships are tuned for a gentle, comfortable middle.""",
   "cruise ship design", "NOT TOO STIFF, NOT TOO SOFT")

# ---------- 2. WIDE HULL ----------
part(2, "The wide hull", "WHY IS THIS SHIP SO WIDE AND FLAT?", "Why Are Cruise Ships So Wide and Flat?",
     """Why are cruise ships so wide and flat underneath? Because width gives stability. When a wide ship tilts, the side going down pushes deep into the water, and the water pushes back up hard on that side. A wide, boxy hull resists tilting much more strongly than a narrow, rounded one.""",
     "cruise ship hull")
sc("""The tall sides of a cruise ship also catch the wind like a sail. A strong side wind can push the ship over a few degrees. Designers calculate the wind force on the whole side area, and make sure the hull is wide enough and the weight low enough to resist it with a large safety margin.""",
   "cruise ship wind", "A GIANT SAIL")
sc("""The wide hull also creates more space for cabins with balconies, which customers love. But the width is limited by the canals and ports a ship needs to use. Ships built to pass the Panama Canal had a maximum width. The newest giants were designed for the larger, newer locks, or to skip the canal entirely.""",
   "Panama Canal cruise ship", "LIMITED BY CANALS")

# ---------- 3. STABILISERS ----------
part(3, "The stabiliser fins", "WHY DOES THIS SHIP HAVE HIDDEN WINGS?", "Why Do Cruise Ships Have Hidden Wings?",
     """Why do cruise ships have hidden wings under the water? They are stabiliser fins. Each side of the hull has a fin that slides out below the waterline. When a wave starts to roll the ship to one side, the fins tilt, like the wings of a plane, and the flowing water pushes the ship back level.""",
     "ship stabilizer fin")
sc("""Sensors measure the roll many times per second, and a computer moves the fins to fight it before passengers feel it. The fins need the ship to be moving to work, because they depend on the water flowing past. Newer designs can also work at very low speed, by flapping like the fins of a fish.""",
   "stabilizer fins ship dry dock", "FIGHTING THE ROLL")
sc("""The fins fold back into the hull when they are not needed, to reduce drag and protect them in port. Stabilisers do not stop a ship from tipping over. The hull and the low weight do that. The fins are there for comfort, so a dinner does not slide off the table in rough seas.""",
   "cruise ship dining room", "FOR COMFORT")

# ---------- 4. ANTI-HEELING ----------
part(4, "The anti-heeling tanks", "WHY DOES THIS SHIP PUMP WATER SIDEWAYS?", "Why Do Cruise Ships Pump Water From Side to Side?",
     """Why do ships pump water from one side to the other? To stay upright. When a ship turns, it leans outward. When thousands of passengers gather on one side to watch a view, or cargo is loaded unevenly, it leans too. Anti heeling tanks on each side move water across the ship to cancel that lean.""",
     "ship ballast tanks")
sc("""The system is automatic. Sensors measure the tilt, and pumps move hundreds of tonnes of water to the opposite side in minutes. On ferries, where trucks drive on and off one side, the tanks work constantly. On cruise ships, they keep the decks level in port and during turns.""",
   "ferry loading", "HUNDREDS OF TONNES OF WATER")
sc("""The same tanks are part of the ship's ballast system, which also adds or removes weight low down to keep the ship at the right depth as fuel and water are used during the voyage. A cruise ship is constantly adjusting itself, like a person balancing on one foot.""",
   "cruise ship port", "CONSTANTLY ADJUSTING")

# ---------- 5. WATERTIGHT COMPARTMENTS ----------
part(5, "The watertight doors", "WHY DOES THIS SHIP HAVE HEAVY DOORS INSIDE?", "Why Do Cruise Ships Have Heavy Steel Doors Inside?",
     """Why do cruise ships have heavy sliding steel doors deep inside the hull? They are watertight doors. The lower hull is divided into compartments by steel walls called bulkheads. If the hull is damaged, the doors close, and the water is trapped in only a few compartments, instead of flooding the whole ship.""",
     "watertight door ship")
sc("""The rules for this come largely from the sinking of the Titanic in nineteen twelve. Its compartments were not tall enough, and water spilled over from one to the next. The first international convention on the safety of life at sea, known as SOLAS, was agreed soon after, and it is still updated today.""",
   "Titanic", "LESSONS FROM THE TITANIC")
sc("""Modern rules require a passenger ship to stay afloat and upright even with several compartments flooded. The doors can be closed from the bridge in seconds. When they slide shut, they are strong enough to crush anything in their way, which is why crew are trained never to pass through them carelessly.""",
   "bulkhead ship", "STAY AFLOAT WHEN FLOODED")

# ---------- 6. AZIPODS ----------
part(6, "The pods", "WHY DO THESE PROPELLERS TURN AROUND?", "Why Do Cruise Ship Propellers Turn Around?",
     """Why do the propellers of many cruise ships hang in pods that can turn all the way around? They are azimuth pods, often called azipods. Each pod holds an electric motor and a propeller, and the whole pod can rotate in any direction. There is no need for a separate rudder.""",
     "azipod")
sc("""Turning the pod points the thrust exactly where the captain wants it, forwards, sideways or backwards. Combined with bow thrusters, a giant cruise ship can slide sideways into a dock, spin on the spot, or stop much faster. Many cruise ships can dock without tugboats, saving time and money in every port.""",
   "cruise ship propulsion", "SPIN ON THE SPOT")
sc("""The motors are electric, powered by generators deep in the hull. That means the engines do not have to be connected to the propellers by long shafts, so designers can place them wherever the weight and space work best, usually low, which also helps stability. Cruise ships began using pods in the late nineteen nineties.""",
   "ship generator", "NO LONG SHAFTS")

# ---------- 7. SAFE RETURN ----------
part(7, "The double engine rooms", "WHY DOES THIS SHIP HAVE TWO ENGINE ROOMS?", "Why Do Cruise Ships Have Two Engine Rooms?",
     """Why do modern cruise ships have two separate engine rooms? Because of a rule called safe return to port. For large passenger ships built since two thousand ten, a fire or flood in one area must not leave the ship helpless. The ship must be able to sail back to port on its own, with essential systems still working.""",
     "cruise ship engine room")
sc("""To do that, the ship is designed with doubled systems in separate spaces. Two or more engine rooms, separate switchboards, backup steering, and areas where passengers can stay safely with food, water, toilets and light. If one side is lost, the other keeps the ship moving.""",
   "ship engine control room", "EVERYTHING DOUBLED")
sc("""The idea is simple. On the open ocean, the safest place for thousands of people is often the ship itself. Evacuating a giant ship into lifeboats is a last resort. So engineers design the ship to be its own lifeboat, able to bring everyone home even after a serious accident.""",
   "cruise ship ocean", "ITS OWN LIFEBOAT")

# ---------- 8. LIFEBOATS ----------
part(8, "The orange lifeboats", "WHY ARE LIFEBOATS ALWAYS ORANGE?", "Why Are Lifeboats Always Orange?",
     """Why are lifeboats almost always bright orange? So they can be seen. In a grey, rough sea, a small boat is very hard to spot from a ship or a helicopter. A strong orange colour stands out against water, sky and fog better than almost any other colour, which is why it is used for lifeboats, life jackets and rescue equipment.""",
     "lifeboat cruise ship")
sc("""On cruise ships, the lifeboats hang on the sides, a few decks above the water, on davits, the cranes that lower them. They are fully enclosed, with engines, food, water and seats. The largest modern lifeboats can carry over three hundred and fifty people each.""",
   "cruise ship lifeboat davit", "FULLY ENCLOSED")
sc("""The rules require enough lifeboat and life raft space for everyone on board, plus extra. Every passenger takes part in a safety drill before the ship leaves port, and the crew practises launching the boats regularly. They are the part of the ship everyone hopes will never be used.""",
   "lifeboat drill", "HOPEFULLY NEVER USED")

# ---------- 9. INCLINING TEST ----------
part(9, "The inclining test", "WHY DO ENGINEERS TILT A NEW SHIP ON PURPOSE?", "Why Do Engineers Tilt a New Ship on Purpose?",
     """Why do engineers tilt a brand new ship on purpose before it sails? It is called the inclining experiment. Known heavy weights are moved from one side of the deck to the other, and the engineers measure exactly how far the ship leans, using long pendulums hanging inside the ship.""",
     "inclining experiment ship")
sc("""From the size of the weights, the distance they moved, and the angle of the tilt, the engineers calculate where the ship's real centre of gravity is. Computers can predict it, but a real ship always ends up slightly different from the drawings, with extra cables, furniture and paint.""",
   "ship pendulum", "MEASURING THE REAL SHIP")
sc("""The result decides how much weight the ship can carry, and where. It becomes part of the ship's official stability book, which the officers use every day. A simple experiment with weights and a pendulum is still the final check before thousands of people step on board.""",
   "new cruise ship shipyard", "THE FINAL CHECK")

# ---------- 10. HEEL IN TURNS ----------
part(10, "The lean in turns", "WHY DOES THIS SHIP LEAN OUT IN TURNS?", "Why Do Ships Lean Outward When Turning?",
     """Why does a ship lean outward when it turns, while a bicycle leans inward? Because of where the forces act. When a ship turns, the water pushes sideways on the hull, low down. The ship's weight, higher up, wants to keep going straight. That pair of forces tips the ship toward the outside of the turn.""",
     "ship turning")
sc("""On a fast turn, a large ship can lean noticeably, and objects on board can slide. That is why big ships turn gently, and why the captain plans turns in advance. The stability rules require ships to stay safe even in a hard turn at full speed, with a margin for wind and waves.""",
   "cruise ship wake turning", "TURN GENTLY")
sc("""Stability is never just one part. It is the low weight, the wide hull, the fins, the tanks, the compartments and the careful habits of the crew, all working together. A cruise ship stays upright because hundreds of engineers made sure every tonne is exactly where it should be.""",
   "cruise ship bow", "ALL WORKING TOGETHER")

# ---------- VERDICT ----------
sc("""So here are the ten. Heavy machinery at the bottom. A wide hull that pushes back. Hidden fins that fight the roll. Tanks that move water across the ship. Steel doors that trap a flood. Pods that turn all the way around. Two engine rooms to bring everyone home. Orange lifeboats that can be seen. A test that tilts the ship on purpose. And the physics of leaning out in a turn.""",
   "cruise ship", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A cruise ship looks top heavy, but it is really a carefully weighted keel with a hotel on top. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments, would you rather sail on a giant cruise ship or a small one?""",
   "cruise ship sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ('File:Vasco da Gama (ship, 1993) at Liverpool Cruise Terminal 1.jpg', 0.5, 0.72),
    2: ('File:Viking Sky (ship, 2017) - Sète - December 2018 - 02.jpg', 0.6, 0.5),
    3: ('File:Polarstern stabilizer hg.jpg', 0.45, 0.45),
    4: ('File:Inside SS Rotterdam, foto Smiths Stabiliser fin angle indicator.JPG', 0.5, 0.4),
    5: ('File:USS Pampanito watertight door.JPG', 0.5, 0.55),
    6: ('File:Mackinaw WLBB-30 Azipod thruster.jpg', 0.6, 0.5),
    7: ('File:Engine control room, Explorer of the Seas 03.jpg', 0.5, 0.45),
    8: ('File:A lifeboat on the cruise ship Scarlet Lady.jpg', 0.4, 0.5),
    9: ('File:USS Tennessee (ACR-10)- Inclining Experiment - Ship at Time of Inclining Experiment., Sheet 1 - NARA - 122414678.jpg', 0.4, 0.4),
    10: ('File:Oasis of the Seas.jpg', 0.4, 0.45),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video39", "title": "Why Don't Cruise Ships Tip Over?",
           "length_scale": 1.6, "scenes": S}, open("videos/video39/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
