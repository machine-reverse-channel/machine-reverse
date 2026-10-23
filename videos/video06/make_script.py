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
sc("""On many airlines, the captain and the first officer are not allowed to eat the same meal. Not because of taste, because of what happened on a flight in nineteen seventy-five, when a breakfast made more than one hundred forty people sick in the air. The cockpit is full of rules and objects like that. An axe. A rope above the window. Switches hidden under red covers. Today, ten cockpit details pilots know and passengers never notice, and why each one exists.""",
   "airliner cockpit pilots", "10 COCKPIT SECRETS", cuts=8, chapter="Intro")
sc("""The cockpit of an airliner is the most carefully designed office in the world. Every switch has a position, every item has a place, and many of the rules were written after an accident or a near miss. From the outside, the pilots seem to just sit and fly. Inside, almost everything they do and use has a reason that goes back to a real event.""",
   "Airbus A320 cockpit", "THE MOST DESIGNED OFFICE")
sc("""As always, every fact here comes from a named source, the Federal Aviation Administration rules, official reports, and aviation references, all listed in the description. Let's start with lunch.""",
   "airline crew meal tray", "WHY DOES THIS EXIST?")

# ---------- 1. MEALS ----------
part(1, "The different meals", "WHY CAN'T PILOTS EAT THE SAME MEAL?", "Why Do Pilots Never Eat the Same Meal?",
     """Why do pilots on many airlines eat different meals? Because if both pilots get food poisoning at the same time, there is nobody left to fly the airplane. On February third, nineteen seventy-five, a Japan Air Lines flight stopped in Anchorage on its way to Copenhagen. The breakfast was ham omelettes, contaminated by a cook with infected cuts on his fingers. About an hour later, one hundred forty-four people on board were sick.""",
     "Japan Air Lines Boeing 747 1970s")
sc("""The flight landed safely for one reason. By pure chance, the captain and first officer had eaten steak instead of the omelettes. The airline had no rule about crew meals. An investigator recommended that cockpit crews eat meals prepared by different cooks, and many airlines adopted the idea. Today, it is common for the captain and first officer to get different dishes, and some airlines ask them not to eat at the same time.""",
   "airline catering truck", "PURE CHANCE")
sc("""There is no Federal Aviation Administration rule that forces this. It is a company policy, and different airlines do it differently. But the logic is simple and very aviation. Never let one single problem knock out both pilots. You will see that idea again and again in this video, in places you would not expect.""",
   "two pilots cockpit", "NEVER BOTH AT ONCE")

# ---------- 2. LEFT SEAT ----------
part(2, "The captain's seat", "WHY DOES THE CAPTAIN SIT ON THE LEFT?", "Why Does the Captain Always Sit on the Left?",
     """Why does the captain of an airliner always sit in the left seat? There is no single law of physics behind it. One common explanation goes back to early aviation, when pilots usually turned left around airfields and in holding patterns, and sitting on the left gave them the best view in the turn. Over time, the left seat became the command seat, and airliners were designed around it, with the controls and displays arranged for a captain on the left.""",
     "airliner cockpit captain seat")
sc("""On many airliners, only the left seat has the tiller, a small wheel used to steer the nose wheel while taxiing. So on the ground, the captain often taxis the airplane. In the air, the two pilots take turns flying, one as pilot flying and the other as pilot monitoring. The four stripes on the captain's sleeve and the left seat both mean the same thing. The final decision is made there.""",
   "nose wheel steering tiller cockpit", "THE FINAL DECISION")
sc("""Helicopters are often the opposite. In many helicopters, the pilot in command sits on the right. The usual explanation is that the right hand stays on the cyclic, the most important control, while the left hand can briefly let go of the collective to reach the switches in the center. The seat is not about tradition alone. It is about where the hands need to be.""",
   "helicopter cockpit pilot", "IT'S ABOUT THE HANDS")

# ---------- 3. STERILE COCKPIT ----------
part(3, "The silence below ten thousand feet", "WHY DO PILOTS STOP TALKING HERE?", "Why Pilots Stop Talking Below 10,000 Feet",
     """Why do pilots stop chatting below ten thousand feet? Because of the sterile cockpit rule. During takeoff, landing, taxi and any flight below ten thousand feet except cruise, pilots are forbidden from non-essential activities. No casual conversation, no eating, no reading unrelated material, and no non-urgent calls from the cabin. The rule was introduced by the Federal Aviation Administration in nineteen eighty-one, after a series of accidents caused by distraction.""",
     "cockpit approach pilots")
sc("""One of those accidents was Eastern Air Lines Flight two twelve in nineteen seventy-four. It crashed short of the runway at Charlotte in dense fog. Investigators found that the crew had been talking about unrelated topics during the approach, and lost track of their altitude. The idea of the rule is that the most dangerous minutes of a flight deserve one hundred percent of the pilots' attention.""",
   "airliner approach fog runway", "FULL ATTENTION")
sc("""That is also why flight attendants are careful about when they call the cockpit, and why you may hear a chime pattern instead of a normal call during takeoff and landing. The cabin and the cockpit have a shared code for what is important enough to interrupt the pilots. In the critical minutes, only safety gets through.""",
   "flight attendant interphone", "ONLY SAFETY GETS THROUGH")

# ---------- 4. OXYGEN MASK ----------
part(4, "The five second mask", "WHY MUST THIS MASK GO ON IN 5 SECONDS?", "Why Pilots Must Put On Their Mask in 5 Seconds",
     """Why do pilots have special oxygen masks next to their seats? Because if the cabin loses pressure at high altitude, a person can lose useful consciousness in seconds. So the rules say the pilots' mask must be placed on the face from its ready position, sealed and supplying oxygen, with one hand, within five seconds. It is a quick donning mask. You squeeze the harness, it inflates, you pull it over your head, and it tightens on its own.""",
     "pilot quick donning oxygen mask")
sc("""The masks are tested before flight, and pilots practice putting them on in the simulator. Many also include smoke goggles, because the same mask protects against smoke in the cockpit. And at very high altitude, the rules are even stricter. Under US rules, above forty-one thousand feet, one pilot at the controls must wear and use the oxygen mask at all times. Two pilots, two masks, and one always ready.""",
   "pilot oxygen mask smoke goggles", "ONE ALWAYS READY")

sc("""Passengers have their own masks, but they work differently. The yellow masks in the cabin are fed by chemical oxygen generators that last only a few minutes, enough for the pilots to descend to an altitude where people can breathe normally. The pilots' masks are connected to oxygen bottles and can last much longer, because the pilots must stay sharp for the whole emergency descent and landing.""",
   "airliner oxygen masks deployed cabin", "MINUTES VS. THE WHOLE FLIGHT")

# ---------- 5. ESCAPE ROPE ----------
part(5, "The rope above the window", "WHY IS THERE A ROPE ABOVE THE WINDOW?", "Why Is There a Rope in the Airplane Cockpit?",
     """Why is there a rope stored above the cockpit side windows on many airliners? Because those side windows can open. On jets like the Airbus A three twenty and many Boeing models, the side windows slide back. If the cockpit door is blocked after an accident, the pilots can open the window, drop the rope outside, and climb down to the ground. It is the pilots' own emergency exit.""",
     "airliner cockpit sliding window")
sc("""The windows are also useful in normal life. Pilots can open them on the ground to talk to ground crew, to clear smoke, or simply to see better. In some cases, pilots have even flown with the window open at low speed to see the runway after a windshield was damaged. A window that opens on an airplane flying at forty thousand feet sounds dangerous. On the ground, it can save your life.""",
   "pilot window open ground crew", "AN EXIT FOR TWO")

sc("""The rope is not the only backup exit idea. On some larger airplanes, such as certain Boeing seven forty-seven versions, the flight deck has an escape hatch in the ceiling with descent devices, because the cockpit sits high above the ground. Whatever the design, the principle is the same. The pilots must always have a way out that does not depend on the cabin.""",
   "Boeing 747 cockpit upper deck", "ALWAYS A WAY OUT")

# ---------- 6. CRASH AXE ----------
part(6, "The axe in the cockpit", "WHY IS THERE AN AXE IN THE COCKPIT?", "Why Is There an Axe in Every Airplane Cockpit?",
     """Why is there an axe in the cockpit of an airliner? Under US rules, airplanes with more than nineteen passenger seats must carry a crash axe. It is not a weapon. It is a tool for fire. A fire can start behind a wall panel, in wiring you cannot reach. The axe lets the crew cut through the panel to find the fire and attack it with an extinguisher. It can also be used to remove barriers or cabin parts after an accident.""",
     "aircraft crash axe")
sc("""The crash axe is kept where the crew can reach it, but passengers cannot during normal flight, usually in the cockpit. Its handle is typically insulated, because the panels it cuts through are full of electrical wires. A hidden fire is one of the most dangerous things on an airplane, because by the time you see smoke, it may have been growing for a while. The axe exists to buy time.""",
   "aircraft fire extinguisher cockpit", "TO BUY TIME")

sc("""The cockpit has other tools for fire. There is a halon fire extinguisher, protective breathing equipment that covers the head and supplies oxygen, and heat resistant gloves on many airplanes. The crew trains to fight fires in the cabin and in the cockpit. On an airplane, you cannot pull over and wait for the fire department. The crew is the fire department.""",
   "aircraft halon extinguisher", "THE CREW IS THE FIRE DEPARTMENT")

# ---------- 7. WINDSHIELD ----------
part(7, "The heated windshield", "WHY IS THIS WINDSHIELD HEATED?", "Why Are Airplane Windshields Heated?",
     """Why is the windshield of an airliner heated, even on a warm day? Two reasons. First, to stop ice and fog from blocking the view. Second, and less obvious, heat makes the layers of the windshield tougher. An airliner windshield is a sandwich of glass and plastic layers, and warm plastic absorbs impacts better than cold, brittle plastic. And it needs to. The rules say a windshield must survive hitting a four pound bird at the airplane's design cruising speed at sea level.""",
     "airliner cockpit windshield")
sc("""The tail is held to an even higher standard. It must survive an eight pound bird, because a damaged tail could make the airplane uncontrollable. Birds are not a theory. Most bird strikes happen near the ground, during takeoff and landing, which is exactly when a pilot most needs to see out. A windshield that cracks but holds is a successful windshield.""",
   "bird strike windshield damage", "4 POUNDS AT CRUISE SPEED")
sc("""You may also notice that cockpit windshields have wipers, which surprises people. At high speed, the airflow often clears the rain on its own. But at slow speed, during taxi, takeoff and landing, rain can sit on the glass. So the wipers are used exactly in the moments when the view matters most. Some airliners also use special coatings that make water bead and run away.""",
   "cockpit windshield wipers rain", "WIPERS FOR THE SLOW PART")

# ---------- 8. GUARDED SWITCHES ----------
part(8, "The covered switches", "WHY ARE THESE SWITCHES COVERED?", "Why Are Some Cockpit Switches Under Covers?",
     """Why are some cockpit switches hidden under small covers, often red or striped? Because some switches must never be moved by accident. Things like engine fuel cutoff, emergency power, or a system that cannot easily be turned back on. The cover forces the pilot to do two separate actions, lift the guard, then move the switch. That extra step turns an accidental bump into something that almost cannot happen.""",
     "cockpit guarded switch")
sc("""Cockpit designers use many tricks like this. Some switches must be pulled out before they can move. Some levers have different shapes so they can be identified by touch, even in smoke or darkness. The landing gear lever on many airplanes ends in a small wheel shape, and the flap lever in a wing shape. A pilot's hand can tell them apart without looking.""",
   "airliner landing gear lever wheel shape", "SHAPED TO BE FELT")

sc("""Color is part of the language too. In modern cockpits, red usually means a warning that needs immediate action, amber or yellow means a caution, and green or white means normal. Many airliners are designed with a dark cockpit philosophy, where lights are off when everything is normal. If a light comes on, something deserves attention. Silence and darkness mean all is well.""",
   "airliner overhead panel lights", "DARK MEANS NORMAL")

# ---------- 9. FIRE HANDLES ----------
part(9, "The fire handles", "WHY DO THESE HANDLES LIGHT UP RED?", "What Happens When a Pilot Pulls the Fire Handle?",
     """Why are there big handles in the middle of the cockpit that can light up red? They are the engine fire handles. If an engine catches fire, its handle lights up and an alarm sounds. On many airliners, pulling the handle shuts off fuel, hydraulic fluid and bleed air to that engine and arms the fire extinguishers. Turning it then fires an extinguisher bottle into the engine. If the fire is still burning, the pilots can fire a second bottle.""",
     "engine fire handle cockpit")
sc("""Before pulling a fire handle, pilots confirm which engine they are dealing with, often by both touching the handle and saying it out loud. Shutting down the wrong engine is one of the worst mistakes in aviation, and it has happened. So the procedure is slow on purpose, even in an emergency. Confirm, then act. In the cockpit, speed is less important than being right.""",
   "airliner engine fire training", "CONFIRM, THEN ACT")

sc("""Fire handles are also checked before every flight. Pilots press a test switch, and every fire warning light and bell must come on, to prove the detection system works. The test sounds alarming the first time you hear it from the cabin, but it is routine. A warning system that cannot be tested is a warning system you cannot trust.""",
   "cockpit fire test switch", "TEST BEFORE YOU TRUST")

# ---------- 10. CVR ----------
part(10, "The microphone above the pilots", "WHY DOES THIS BOX HEAR THE PILOTS?", "Why Is There a Microphone Above the Pilots?",
     """Why is there a small microphone in the cockpit ceiling, between the pilots? It feeds the cockpit voice recorder, one of the two black boxes. It records the pilots' voices, the radio, and the sounds of the cockpit, like alarms, switches, and even engine noise. After an accident, those sounds can tell investigators what the crew knew, what they did, and when. And despite the name, black boxes are painted bright orange so they can be found.""",
     "cockpit voice recorder")
sc("""For years, cockpit voice recorders in the United States kept only the last two hours, recording over older audio. That meant important sounds could be erased if an airplane kept running after an incident. In twenty twenty-six, the Federal Aviation Administration set a twenty-five hour standard for newly built airliners. More recording means more chances to understand what went wrong, and to write the next rule before it happens again.""",
   "flight data recorder orange", "FROM 2 HOURS TO 25")

sc("""The other black box is the flight data recorder. It stores thousands of measurements, like speed, altitude, control positions and engine settings, for many hours. Both boxes are built to survive extreme impact and fire, and they carry underwater locator beacons that ping for weeks if the airplane goes into the sea. Together, they turn a tragedy into lessons.""",
   "flight data recorder black box", "TRAGEDY INTO LESSONS")

# ---------- VERDICT ----------
sc("""So here are the ten. Different meals so both pilots never get sick together. A left seat for the final decision. Silence below ten thousand feet. A mask that goes on in five seconds. A rope for climbing out the window, and an axe for hidden fires. A heated windshield for birds, covers on dangerous switches, fire handles that are slow on purpose, and a microphone that listens for the next lesson.""",
   "airliner cockpit night", "10 SECRETS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""The cockpit is where aviation keeps its memory. Almost every rule in it was written by an accident that should never happen again. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "airliner takeoff sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Approaching ORY, in the cockpit.jpg", 0.5, 0.55),
    2: ("File:Boeing 737-300 Cockpit.jpg", 0.2, 0.6),
    3: ("File:B737-original crew in cockpit during final approach.jpg", 0.5, 0.5),
    4: ("File:U.S. Air Force Tech. Sgt. Vidal Hill, with the 18th Aeromedical Evacuation Squadron, wears a quick don oxygen mask while preparing for a mission aboard a C-130H Hercules aircraft during Air Mobility Rodeo 2011 110725-F-RM405-010.jpg", 0.6, 0.28),
    5: ("File:Boeing 737 S7 VQ-BKW cockpit May 2011.jpg", 0.12, 0.32),
    6: ("File:Airbus A320-211 Vueling EC-FNR cockpit (6503776229).jpg", 0.28, 0.62),
    7: ("File:Cockpit windows of a Boeing 787 (1).jpg", 0.35, 0.38),
    8: ("File:Overhead panel of an Airbus A320 during cruise.jpg", 0.19, 0.27),
    9: ("File:Boeing 737-300 Cockpit.jpg", 0.5, 0.7),
    10: ("File:Cockpit voice recorders.JPG", 0.5, 0.45),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video06", "title": "Why Do Pilots Never Eat the Same Meal?",
           "length_scale": 1.6, "scenes": S}, open("videos/video06/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
