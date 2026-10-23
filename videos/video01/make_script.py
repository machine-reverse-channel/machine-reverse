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
sc("""There is a hole in your airplane window. There are tiny fins on the wing, little sticks on the tail, and a spiral painted on the engine. There is an ashtray in a bathroom where smoking has been banned for decades. You have seen all of them. Almost nobody can explain them. Today we are going to explain twelve of them, and one of these parts was the reason a whole generation of jets fell out of the sky.""",
   "airliner wing engine window view", "12 PARTS. 12 REASONS.", cuts=8, chapter="Intro")
sc("""Every part on an airliner has to earn its place. It adds weight, it adds cost, and it has to be inspected. So when something looks strange, pointless, or even silly, there is almost always a story behind it. Sometimes it is physics. Sometimes it is money. And sometimes it is a lesson that was written in blood, and turned into a rule that every airplane in the world now has to follow.""",
   "Boeing 737 airliner close up", "NOTHING ON A JET IS RANDOM", cuts=4)
sc("""Here is how this works. For every part, we start with a picture and one question. Why does this exist? Then we give you the real answer, with the source, and the story behind it. Every number in this video comes from a named source, like NASA, the Federal Aviation Administration, or an official accident investigation, and every source is listed in the description. Let's start with the one you can touch.""",
   "airplane cabin window seat view wing", "WHY DOES THIS EXIST?", cuts=4)

# ---------- 1. WINDOW HOLE ----------
part(1, "The hole in your window", "WHY IS THERE A HOLE HERE?", "Why Is There a Hole in Airplane Windows?",
     """Why is there a tiny hole in your airplane window? It looks like a mistake, but it is keeping the window working. An airplane window is not one pane. It is three. The inner one is just a scratch guard. The middle and outer panes are the real window. The tiny hole, called a breather hole or bleed hole, is in the middle pane. It lets the air pressure between the panes match the cabin, so during the flight, the cabin pressure pushes only on the outer pane. The middle pane carries almost nothing. It is a spare, waiting in case the outer one ever fails.""",
     "airplane cabin window breather hole", local="assets/window-panes.jpg", arrow={"x": 0.5, "y": 0.654})
sc("""Think about what that means. At cruise, the air outside is thin and cold, and the cabin is pressurized so that you can breathe normally. That difference in pressure pushes outward on every window, every flight, thousands of times over the life of the airplane. By loading only one pane and keeping a second one in reserve, the designers built a backup that is always there and never tired. If the outer pane cracks, the middle pane takes over.""",
   "aircraft cabin window", "THE OUTER PANE DOES THE WORK")
sc("""And the hole has a second job. Air between two panes of glass can hold moisture, and when the outside temperature drops far below freezing, that moisture would fog or frost the window. The breather hole lets that moist air move and dry out, so the window stays clear. One tiny hole, two jobs. A spare pane that is never stressed, and a clear view of the sky.""",
   "airplane window view clouds wing", "JOB TWO: NO FOG")

# ---------- 2. ROUND WINDOWS ----------
part(2, "The round windows", "WHY ARE THESE ROUND?", "Why Are Airplane Windows Never Square?",
     """Why are airplane windows always rounded, and never square? The answer starts with the first jet airliner in history, the de Havilland Comet. It entered passenger service on the second of May, nineteen fifty-two. Less than two years later, on the tenth of January, nineteen fifty-four, a Comet broke apart in the air near the island of Elba, and all thirty-five people on board died. Three months later, another Comet broke up near Naples, killing all twenty-one people on board. The cause was metal fatigue, and it started at a sharp corner.""",
     "de Havilland Comet airliner", file="File:DeHavilland Comet 4C (6661432457) (4).jpg", arrow={"x": 0.25, "y": 0.5})
sc("""Engineers put a Comet fuselage in a giant water tank and pressurized it again and again, simulating flight after flight. After three thousand and fifty-seven cycles, the fuselage burst open. On the crashed airplane, investigators traced the crack to a tiny rivet hole at the corner of a square cutout in the roof, a window for a navigation antenna. Every flight, the pressure flexed that corner a little. Eventually, the metal simply gave up.""",
   "de Havilland Comet 1", "3,057 CYCLES. THEN IT BURST.", file="File:Result of metal fatigue on a de Havilland Comet (50813201846).jpg")
sc("""Now here is the twist. Most people say the square passenger windows brought the Comet down. That is not quite true. According to the investigation, the crack began at that roof cutout, not at a passenger window. But the lesson was the same for every opening. A sharp corner concentrates stress in one point, and a rounded shape spreads it out. That is why, on every pressurized jet today, every window and every door has rounded corners.""",
   "airliner fuselage windows row", "THE REAL CULPRIT: A CORNER")

# ---------- 3. VORTEX GENERATORS ----------
part(3, "The tiny fins on the wing", "WHY ARE THESE FINS HERE?", "Why Do Airplane Wings Have Tiny Fins?",
     """Why are there tiny fins sticking out of this wing? They look like a factory forgot to sand them off. They are called vortex generators, and each one is a miniature wing. As the air passes, each fin spins off a small swirl of air. That swirl grabs fast moving air from above and mixes it into the slow, tired layer of air right against the wing's skin. That energized layer stays attached to the wing for longer, so the wing keeps making lift at angles where it would otherwise stall. A row of fins the size of your thumb, buying safety at low speed.""",
     "vortex generators wing Boeing 737", file="File:Airforce Museum Berlin-Gatow 514.JPG", arrow={"x": 0.4, "y": 0.2})
sc("""The thin layer of air touching the wing is called the boundary layer. It is slowed down by friction with the skin, and when the wing tilts up, it struggles against rising pressure toward the back of the wing. If it slows too much, it separates, and the smooth flow breaks down. That is a stall. Vortex generators fight that separation by constantly feeding energy into the boundary layer.""",
   "aircraft wing airflow", "THE ENEMY: FLOW SEPARATION")
sc("""On airliners, you often find them right in front of the flaps, or near the engines, because those are the places where the airflow has the hardest job. On high speed jets, they also help keep control surfaces working behind shock waves. Small airplanes use them too. Kits with dozens of tiny fins are sold to let bush planes fly slower and land shorter. It is one of the cheapest upgrades in aviation.""",
   "vortex generators aircraft", "CHEAP. SMALL. CRUCIAL.")

# ---------- 4. STATIC WICKS ----------
part(4, "The sticks on the wingtips", "WHY ARE THESE STICKS HERE?", "What Are These Sticks on Airplane Wings?",
     """Why are there little sticks hanging off the back of every airliner's wings and tail? They are not antennas, and they are not decoration. They are static wicks, also called static dischargers. When a jet flies through rain, snow, ice crystals or dust, friction charges the whole airplane with static electricity. More than five hundred thousand volts have been measured on small airplanes in flight. If that charge leaks off in uncontrolled sparks, it creates a roar of radio noise. The wicks bleed it off quietly, through sharp points, so the pilots can still hear the radio.""",
     "static discharger aircraft wing", file="File:Easyjet a319-100 g-ezbv winglet arp.jpg", arrow={"x": 0.355, "y": 0.49})
sc("""Pilots call this problem precipitation static. Without dischargers, the charge escapes from the wing tips and tail edges in a crackling corona discharge. In the headset, it sounds like a loud hiss. It can drown out voice radio, confuse navigation receivers, and even make some instruments behave erratically. In the middle of a storm, that is exactly when you need the radio most.""",
   "aircraft tail static wicks", "THE PROBLEM: RADIO NOISE")
sc("""Static wicks have a long history. An early patent for a static discharger was filed in nineteen twenty. Modern carbon wicks were patented in the early nineteen fifties by a team of engineers that included Mary Sullivan. Today, they are simple, light, and cheap, and they are on almost every airliner you will ever board. Next time you look out at the wing, count them.""",
   "airliner wing trailing edge", "INVENTED IN THE 1950S")

# ---------- 5. WINGLETS ----------
part(5, "The bent wingtips", "WHY DOES THE WING BEND UP?", "Why Do Airplane Wings Bend Up at the Tip?",
     """Why does the tip of this wing bend straight up? It is called a winglet, and it exists to save fuel. A wing works because the pressure under it is higher than the pressure on top. But at the tip, that high pressure air tries to escape around the edge, and it rolls up into a spinning tornado of air called a wingtip vortex. That vortex costs energy, a penalty called induced drag. A winglet weakens that vortex. According to NASA, winglet technology generally saves four to six percent of fuel. On a big airline, that is millions of dollars.""",
     "blended winglet Boeing 737", file="File:Slats and winglet, Épiais-lès-Louvres (SIAE2200) (cropped).jpg", arrow={"x": 0.55, "y": 0.47})
sc("""The modern winglet came from NASA. In nineteen seventy-six, after the oil crisis, NASA engineer Richard Whitcomb published research predicting that winglets could cut induced drag by about twenty percent. NASA, the US Air Force and Boeing then flight tested them on a KC one thirty-five tanker in nineteen seventy-nine and nineteen eighty. The results matched the prediction.""",
   "Richard Whitcomb NASA winglet KC-135", "NASA, 1976")
sc("""Then the numbers became enormous. According to NASA, a typical Southwest Airlines Boeing seven thirty-seven seven hundred with blended winglets saves about one hundred thousand gallons of fuel per year. And by twenty ten, blended winglets had saved roughly two billion gallons of jet fuel worldwide, worth about four billion dollars. A bent piece of wing, paying for itself every single day.""",
   "Southwest Airlines Boeing 737 winglets", "2 BILLION GALLONS SAVED")

# ---------- 6. FLAP TRACK FAIRINGS ----------
part(6, "The canoes under the wing", "WHY ARE THESE CANOES HERE?", "What Are the Canoes Under Airplane Wings?",
     """Why are there long pods, shaped like canoes, hanging under the wing? They are called flap track fairings, and they have two jobs. The first is obvious once you know it. Inside each canoe is the heavy mechanism that slides the flaps backward and down for takeoff and landing. The second job is hidden. Their long shape sticks out past the back of the wing on purpose, and it actually reduces drag at cruise speed. They are not just covers. They are shaped to make the whole airplane slip through the air more easily.""",
     "flap track fairing Airbus A320 wing", file="File:Antishock body on B787 wing (2).jpg", arrow={"x": 0.46, "y": 0.63})
sc("""That shape comes from a famous rule in aerodynamics, the area rule, developed by NASA's Richard Whitcomb in the nineteen fifties. Near the speed of sound, drag rises sharply. But if the cross section of the airplane changes smoothly from nose to tail, without sudden jumps, that drag is reduced. Airliners cruise at around eighty to eighty-five percent of the speed of sound, which is right in the zone where this matters.""",
   "airliner wing underside flaps", "THE AREA RULE")
sc("""Whitcomb even proposed pods on the back of the wing for this purpose, and in Britain, the aerodynamicist Dietrich Küchemann reached a similar idea. His pods became known as Küchemann carrots. So when you look at those canoes under the wing, you are looking at two things at once. A cover for heavy machinery, and a carefully shaped trick to beat the drag of near sonic flight.""",
   "Handley Page Victor bomber", "THE KÜCHEMANN CARROTS")

# ---------- 7. CHEVRONS ----------
part(7, "The teeth on the engine", "WHY DOES THIS ENGINE HAVE TEETH?", "Why Does This Jet Engine Have Teeth?",
     """Why does the back of this jet engine have teeth? These sawtooth edges are called chevrons, and they exist for one reason. Noise. The hot, fast exhaust of a jet engine slams into the slower air around it, and that violent mixing creates the roar you hear on the ground. The chevrons make the two streams blend more gently, so the roar is smaller. According to NASA, on the Boeing seven eighty-seven, its industry partner Boeing reported a sixty-nine percent smaller noise footprint. That is why the Dreamliner sounds so different.""",
     "Boeing 787 engine chevrons", file="File:General Electric GEnx-1B (14233497776) (cropped).jpg", arrow={"x": 0.46, "y": 0.32})
sc("""NASA spent the nineteen nineties and early two thousands refining chevron shapes with computer simulations, then ground tests and flight tests. Those tests showed lower noise both on the ground and inside the passenger cabin. For people living near airports, a smaller noise footprint means fewer homes inside the loudest zone around the runway.""",
   "Boeing 787 Dreamliner takeoff", "LESS NOISE FOR THE CITY")
sc("""The Boeing seven forty-seven eight also uses chevrons, and Boeing reported a twenty-nine percent smaller noise footprint for it. But chevrons are not free. Sticking teeth into the exhaust stream costs a little efficiency, and some newer engine designs reduce noise in other ways instead. So engineers keep weighing the same trade-off. A quieter neighborhood, against a little more fuel.""",
   "Boeing 747-8 engine", "THE TRADE-OFF: FUEL")

# ---------- 8. SPINNER SPIRAL ----------
part(8, "The spiral on the engine", "WHY IS THIS SPIRAL HERE?", "Why Do Jet Engines Have a Spiral?",
     """Why is there a white spiral painted on the center of this engine? Many people think it scares birds away. Boeing engineers say it does not reduce bird strikes. Its real job is to protect people on the ground. A turning fan can look almost still, especially at night. The spiral turns into a flickering blur the moment the engine moves, so the ground crew can tell at a glance that it is running. And that matters, because the area in front of a running engine is one of the most dangerous places at an airport.""",
     "jet engine spinner spiral", file="File:Jet engine Spiral spinners.png", arrow={"x": 0.12, "y": 0.33})
sc("""How dangerous? For a Boeing seven thirty-seven, the hazard zone in front of and beside the engine extends about nine feet at idle, and fourteen feet or more above idle. Bigger jets, like the seven seventy-seven, have much bigger zones. A person who walks into that area can be pulled into the engine. The spiral is a simple, cheap warning sign painted where everyone is already looking.""",
   "airport ground crew engine", "DANGER ZONE: 9 FEET AT IDLE")
sc("""And the bird theory? It is not completely crazy. In nineteen eighty-six, the Japanese airline All Nippon Airways tested eye-like markings on its engines for a year and reported a small reduction in bird strikes. But other studies were inconclusive, and a Rolls-Royce representative noted that in flight, the engine spins far too fast for a bird to see any pattern at all. The spiral is for people.""",
   "All Nippon Airways engine", "THE BIRD MYTH")

# ---------- 9. PITOT TUBE ----------
part(9, "The little tube on the nose", "WHY IS THIS TUBE SO IMPORTANT?", "This Tiny Tube Can Bring Down a Plane",
     """Why is this small tube on the nose of an airliner so important? It is a pitot tube, and it measures how fast the airplane is moving through the air. Air rams into the opening, and the pressure tells the computers the airspeed. Without it, the pilots are flying blind on one of the most important numbers in aviation. That is why the tubes are heated, and why there are always several of them. On the ground, you will often see them covered with red tags that say remove before flight, because even an insect nest inside one can be deadly.""",
     "pitot tube airliner nose", file="File:ILA-Pitotrohr.jpg", arrow={"x": 0.42, "y": 0.77})
sc("""The most famous pitot tube story is Air France flight four forty-seven. On the first of June, two thousand nine, an Airbus A three thirty flying from Rio de Janeiro to Paris was cruising at about thirty-five thousand feet over the Atlantic. Ice crystals blocked the pitot tubes, and the airspeed readings became inconsistent. The autopilot disconnected, and the crew had to fly by hand.""",
   "Airbus A330 Air France", "AIR FRANCE 447, 2009")
sc("""The blockage was temporary. But according to the final report from the French investigation agency, the BEA, the crew lost control of the flight path, and the airplane entered a stall it never recovered from. It fell for about three and a half minutes before hitting the ocean. All two hundred twenty-eight people on board died. After the accident, European regulators ordered the older pitot probes replaced on Airbus jets, and pilot training for unreliable airspeed changed around the world.""",
   "Airbus A330 cockpit", "228 LIVES. NEW RULES.")

# ---------- 10. RAM AIR TURBINE ----------
part(10, "The hidden propeller", "WHY DOES A JET HAVE A PROPELLER?", "Why Does This Jet Have a Hidden Propeller?",
     """Why does a modern jet airliner carry a tiny propeller hidden in its belly? It is called a ram air turbine, or RAT, and it is the last line of defense. If an airliner loses all its engine power, the RAT drops out into the wind. The air spins it like a windmill, and it drives a hydraulic pump, a generator, or both. That powers the essentials, the flight controls and the core instruments, so the pilots can still fly. It works without electricity to deploy, because it is built for the moment when everything else has failed.""",
     "ram air turbine deployed", file="File:Ram Air Turbine on F-104S Starfighter (14199964717).jpg", arrow={"x": 0.46, "y": 0.52})
sc("""In two thousand one, Air Transat flight two thirty-six, an Airbus A three thirty with more than three hundred people on board, lost both engines over the Atlantic because of a fuel leak. The RAT deployed. Its pump kept the flight controls alive, and the airplane glided for more than fifteen minutes, covering roughly one hundred twenty kilometers, to a landing in the Azores. Everyone survived.""",
   "Air Transat Airbus A330", "AIR TRANSAT 236: A 120 KM GLIDE")
sc("""And in two thousand nine, when US Airways flight fifteen forty-nine lost both engines after hitting birds over New York, the RAT deployed on the Airbus A three twenty and helped power its fly by wire controls during the ditching in the Hudson River. All on board survived. Most passengers will never see a RAT. On most flights, it stays folded away, waiting for the worst day.""",
   "US Airways Flight 1549 Hudson", "THE HUDSON, 2009")

# ---------- 11. TRIANGLE STICKER ----------
part(11, "The triangle above your seat", "WHY THIS WINDOW?", "What Does the Triangle Above Your Seat Mean?",
     """Why is there a small triangle sticker above some airplane windows? It marks the window with the best view of the wing. If the crew needs to check the flaps, the slats, the engine, or ice on the wing, they know exactly which window to walk to, without searching row by row. There is usually at least one on each side of the cabin. You are not expected to do anything if you sit there. But if you want the best photo of the wing, or to watch the deicing, that is your seat.""",
     "aircraft cabin window wing view", file="File:EasyJet, Airbus A320neo, G-UZHP, Wing View.jpg", arrow={"x": 0.6, "y": 0.55})
sc("""A former airline pilot, Daniel Bubb, told Reader's Digest that the main purpose is to help the crew locate problems quickly in an emergency or a malfunction of the wing flaps, slats, engine and other parts. The triangles are more common on larger Airbus and Boeing jets, and some airlines skip them entirely. Fans have even nicknamed it the William Shatner seat, after a famous Twilight Zone episode with a monster on the wing.""",
   "airplane cabin interior windows", "THE CREW'S WINDOW")

# ---------- 12. ASHTRAY ----------
part(12, "The ashtray in the bathroom", "WHY IS THERE AN ASHTRAY HERE?", "Smoking Is Banned. So Why the Ashtray?",
     """Why is there an ashtray in an airplane bathroom, when smoking has been banned on flights for decades? Because the law requires it. US federal regulations say that lavatories must have self-contained, removable ashtrays, even though smoking is prohibited. The logic is simple. Some people break the rules. If someone lights a cigarette anyway, the worst thing they can do is throw it in the trash bin full of paper towels. The ashtray gives them a safe place to put it out. It is a part designed for people who are breaking the rules.""",
     "aircraft lavatory ashtray", file="File:Diehl Sylvia, PEW 2018, Hamburg (1X7A3759).jpg", arrow={"x": 0.21, "y": 0.2})
sc("""The rule is written in Title fourteen of the Code of Federal Regulations, part twenty-five, section eight fifty-three. Smoking was banned on all US domestic flights in February nineteen ninety, except a few flights over six hours, and since two thousand, it has been banned on all flights to and from the United States. Yet the ashtrays remain, and if more than half of an airplane's lavatory ashtrays are broken, they must be repaired within seventy-two hours.""",
   "airplane lavatory", "14 CFR 25.853")

# ---------- VERDICT ----------
sc("""So here are the twelve. A hole that keeps a spare window ready. Rounded corners born from a disaster. Fins that delay a stall, sticks that silence the radio, and wingtips that save billions of gallons of fuel. Canoes that beat drag, teeth that quiet a city, and a spiral that saves the ground crew. A tube that cost two hundred twenty-eight lives when it froze, a propeller for the worst day, a triangle for the crew, and an ashtray for rule breakers.""",
   "airliner takeoff sunset", "12 PARTS. 12 REASONS.", chapter="The verdict", cuts=6)
sc("""The pattern is always the same. Every strange part on an airplane is the answer to a question somebody had to ask, often the hard way. If you want more machines explained part by part, rockets, Formula One cars, ships and giant trains, subscribe to Machine Reverse. And tell us in the comments which part on an airplane you have always wondered about. We might explain it next.""",
   "airliner landing runway", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

json.dump({"id": "video01", "title": "12 Airplane Parts You've Seen But Can't Explain (Why They Exist)",
           "length_scale": 1.5, "scenes": S}, open("videos/video01/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.5)), "min")
