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
# ---------- HOOK ----------
sc("""Watch almost any big rocket lift off, and sheets of white ice come tumbling down its sides. It looks like the rocket is shaking off a coat of snow, on a hot summer morning in Florida. It is not snow. It is ice that formed on the outside of the rocket in the hours before launch, and it is one of the strangest problems in spaceflight. Today, ten parts of a rocket launch, and why each one exists.""",
   "rocket launch ice falling", "WHY DOES ICE FALL OFF?", cuts=8, chapter="Intro")
sc("""A rocket is mostly a flying tank of super cold liquids. Those liquids are what burn, but they are also what freeze the air around the tank. Over the decades, engineers have invented foam, heaters, vents and a huge amount of water to deal with that, and some of those fixes were learned the hard way.""",
   "rocket on launch pad", "A FLYING TANK OF COLD")
sc("""As always, every fact here comes from a named source, NASA documents, accident reports and spaceflight references, all listed in the description. Let's start with the ice itself.""",
   "rocket launch pad", "WHY DOES THIS EXIST?")

# ---------- 1. ICE ----------
part(1, "The ice on the rocket", "WHY IS THIS ROCKET COVERED IN ICE?", "Why Does Ice Fall Off Rockets at Launch?",
     """Why does a rocket get covered in ice on a warm day? Because of what is inside. Liquid oxygen, the part of the fuel that lets it burn, has to be colder than minus one hundred eighty-three degrees Celsius to stay liquid. Liquid hydrogen is even colder, at about minus two hundred fifty-three. The metal skin of the tank gets just as cold, and water vapor in the air turns into solid ice the moment it touches it.""",
     "rocket frost ice launch")
sc("""This is the same thing that happens on a cold glass of water, only much more extreme. The air near Florida's coast is very humid, so there is a lot of water vapor to freeze. The ice grows thicker the longer the rocket sits on the pad full of propellant. When the engines light up, the vibration and the wind shake it loose, and it falls off in plates.""",
   "rocket vapor launch pad", "IT FREEZES THE AIR")
sc("""Rockets that use kerosene, like the Falcon nine, have the same problem on the part of the tank that holds the liquid oxygen. SpaceX even chills its kerosene, to about minus seven degrees Celsius, to make it denser. The ice that you see falling off is nearly always from the oxygen tank, the coldest part of the rocket.""",
   "Falcon 9 liftoff frost", "THE COLDEST PART")

# ---------- 2. SATURN V ----------
part(2, "The bare Saturn V tank", "WHY IS THIS TANK COVERED IN FROST?", "Why Did the Saturn V Drop Ice When It Launched?",
     """Why did the giant Saturn V rocket drop ice at liftoff? Because its liquid oxygen tanks were not insulated on the outside. The cold of the tank went straight through the metal wall and iced the surface, and chunks fell off as the rocket began to climb. Ice fragments falling away from the Saturn V at liftoff are one of the best known images of the Apollo program.""",
     "Saturn V launch")
sc("""The Saturn V stood about one hundred ten meters tall, with its first stage carrying enormous tanks of oxygen and kerosene. At the time, the falling ice was simply a known part of a Saturn V launch, because nothing fragile was riding on the side of the rocket.""",
   "Saturn V Apollo launch pad", "PART OF THE LAUNCH")
sc("""That changed when rockets and spacecraft started to carry delicate things on their sides. A piece of ice that hits a solid tank is only a nuisance. A piece of ice, or foam, that hits something fragile can be a disaster. And that is exactly what happened with the next American rocket system.""",
   "Apollo Saturn V ice", "A NUISANCE... UNTIL IT ISN'T")

# ---------- 3. SHUTTLE FOAM ----------
part(3, "The orange foam", "WHY IS THIS TANK COVERED IN ORANGE FOAM?", "Why Was the Space Shuttle Tank Covered in Orange Foam?",
     """Why was the big tank under the Space Shuttle covered in orange foam? To keep the cold in and the ice out. The external tank held liquid hydrogen and liquid oxygen, and the shuttle sat right beside it. Ice breaking off could hit the orbiter, so engineers sprayed the tank with polyurethane foam, at least about one inch thick, which stops the outside of the tank from getting cold enough to build thick ice.""",
     "Space Shuttle external tank foam")
sc("""The foam did its job, but not perfectly. Moisture could get into small cracks and punctures, and then freeze and make pieces of foam pop off. The foam was thicker around the parts that stuck out, and the places where it was applied by hand, like around the supports of the tank, were the ones that shed the most. The orange color is the natural color of the foam.""",
   "Space Shuttle launch pad", "THE FOAM WASN'T PERFECT")
sc("""So the shuttle program lived with a strange compromise. Without foam, the tank would drop big sheets of ice onto the orbiter. With foam, the tank could drop foam instead. Both fall during the first minute of flight, and for years, engineers watched every launch video, looking for the pieces.""",
   "Space Shuttle external tank", "ICE OR FOAM")

# ---------- 4. COLUMBIA ----------
part(4, "The piece of foam", "WHY DID A PIECE OF FOAM DOWN A SPACE SHUTTLE?", "Why Did a Piece of Foam Destroy the Space Shuttle Columbia?",
     """Why did a piece of foam destroy a space shuttle? On the first of February, two thousand three, Columbia broke apart while returning from orbit, killing all seven astronauts. The investigation traced the damage to a piece of foam that fell off the tank during launch and hit the wing. Later tests fired a piece of foam weighing about one and two thirds pounds at five hundred thirty miles an hour into a wing panel, and it blew a hole sixteen inches wide.""",
     "Space Shuttle Columbia")
sc("""A hole in the wing's heat shield let the hot gases of reentry in. A lot of foam had come off earlier shuttle launches without causing a disaster, which made people think it was safe. The investigation called that a cultural problem. A danger that does not cause a crash the first few times starts to feel normal.""",
   "Space Shuttle launch foam", "IT FELT NORMAL")
sc("""After the accident, NASA spent about one and a half billion dollars on fixes to the tank and on safety upgrades. A foam ramp, thirty-seven feet long, was removed from the tank after it was blamed for a piece that nearly hit Discovery's wing in July two thousand five. Foam and ice stopped being small details, and became a safety issue for every launch.""",
   "Space Shuttle Discovery launch", "$1.5 BILLION OF FIXES")

# ---------- 5. HEATERS ----------
part(5, "The heater strips", "WHY IS THERE A HEATER ON A TANK OF ICE?", "Why Do Rockets Have Heaters on Their Frozen Tanks?",
     """Why would a rocket full of super cold liquid have heaters on its outside? To stop ice from forming in the worst places. On the shuttle's external tank, the long feedline that carried liquid oxygen, about seventy feet long and seventeen inches wide, had flexible joints with strip heaters of about half an inch wide around them. The heat kept ice from building up where it could break off and hit the orbiter.""",
     "external tank feedline heater")
sc("""After Columbia, NASA also added heaters at key points of the tank, to keep ice from forming under the foam. It is an odd sight, a machine carrying hundreds of tons of liquid hydrogen at minus two hundred fifty degrees, with small electric heaters stuck onto it. But where ice is dangerous, a little heat is cheaper than a big risk.""",
   "Space Shuttle fuel tank", "HEAT WHERE ICE IS DANGEROUS")
sc("""The vent system of the shuttle used the same idea. Warm, dry nitrogen gas was pumped into the vent hood, so the escaping oxygen did not freeze water vapor into ice. No water, no ice.""",
   "rocket valves umbilical", "NO WATER, NO ICE")

# ---------- 6. BEANIE CAP ----------
part(6, "The beanie cap", "WHY IS THERE A CAP ON TOP OF THIS TANK?", "Why Did the Space Shuttle Tank Wear a Cap Before Launch?",
     """Why did the shuttle tank wear a big cap on top before launch? It was called the beanie cap, a vent hood thirteen feet wide, on an arm of the launch tower. Liquid oxygen in the tank is always boiling off into gas, and the hood collected the gas and carried it away from the shuttle. It was warmed with nitrogen gas so the vented oxygen did not freeze water vapor into ice near the top of the tank.""",
     "Space Shuttle beanie cap vent hood")
sc("""The cap lifted off the tank about two and a half minutes before launch, in a process that took twenty-five seconds. The arm then swung back to the tower about one minute forty-five seconds before liftoff. And it was not latched during the countdown, so if there was a hold, the hood could come back down again.""",
   "Space Shuttle countdown tower", "T MINUS 2:30")
sc("""It is a small detail, but it shows how the countdown is a choreography. Every arm and every hose has its exact time to leave. If the launch team sees a problem before the cap lifts, the whole thing can stop and come back. On a rocket, a few seconds can matter enormously.""",
   "launch tower arms retract", "A CHOREOGRAPHY")

# ---------- 7. WHITE CLOUDS ----------
part(7, "The white clouds", "WHY DOES THE ROCKET SMOKE ON THE PAD?", "Why Do Rockets Release White Clouds Before Launch?",
     """Why do rockets hiss out big white clouds before liftoff? It is boil-off. The liquid oxygen in the tank warms up a little all the time, and some of it turns to gas. If the gas stayed inside, the pressure would build up, so valves vent it out. The vapor is so cold that it freezes the water in the air into a white cloud, just like your breath on a cold winter morning.""",
     "rocket venting vapor pad")
sc("""A Falcon nine does the same, venting liquid oxygen on the pad as the propellant warms. The white cloud is a sign that the rocket is fueled and cold, and that its tanks are doing what they should.""",
   "Falcon 9 vapor countdown", "A SIGN IT IS FUELED")
sc("""There is another white cloud at liftoff, and it has a completely different cause. When the engines fire, huge amounts of water on the pad turn to steam. That is the next part on our list, and it might surprise you how much water is involved.""",
   "launch pad steam", "A DIFFERENT CLOUD")

# ---------- 8. WATER ----------
part(8, "The water tower", "WHY DO ROCKETS SPRAY WATER AT LAUNCH?", "Why Do Launch Pads Spray Water at Rockets?",
     """Why does a launch pad flood with water as the rocket lifts off? The noise. A rocket engine's exhaust can reach around two hundred decibels near liftoff, so loud that the sound waves bounce off the pad and can damage the rocket itself. Water poured into the exhaust absorbs a lot of that acoustic energy. At the Space Shuttle pad, it brought the sound down to about one hundred forty-two decibels.""",
     "launch pad water sound suppression")
sc("""The shuttle pad's water tower held about three hundred thousand gallons. The water started flowing about six and a half seconds before the main engines lit, and drained in about forty-one seconds. For the huge SLS rocket, the system was upgraded to four hundred thousand gallons, at a peak flow of one point one million gallons a minute. Much of that water boils into the white clouds you see at launch.""",
   "launch pad water deluge", "300,000 GALLONS IN 41 SECONDS")
sc("""So water protects the rocket from its own sound. Without it, the sound reflecting off the pad could damage the rocket and what it carries. A rocket does not just fight gravity. It fights its own noise.""",
   "rocket launch sound waves", "IT FIGHTS ITS OWN NOISE")

# ---------- 9. FLAME TRENCH ----------
part(9, "The flame trench", "WHY IS THERE A HOLE UNDER THE ROCKET?", "Why Do Rockets Launch Over a Giant Trench?",
     """Why is there a giant trench under a launch pad? Because the exhaust of a rocket has nowhere good to go. If it hit flat ground, it would bounce straight back up into the rocket. The trench and the flame deflector guide the exhaust away from the pad. They also redirect the sound energy, which makes the water system's job easier.""",
     "launch pad flame trench")
sc("""The deflector is a huge curved or wedge-shaped surface, built to take the full blast of the engines. The concrete and steel around it are covered in special heat-resistant layers. Even so, a pad can need repairs after a launch, because the exhaust is one of the harshest things a structure can face.""",
   "flame deflector rocket", "BUILT FOR THE BLAST")
sc("""Not every launch site looks the same, but all of them solve the same problem. Whatever comes out of the engines needs a safe and quick way out, or the rocket will have to survive its own exhaust.""",
   "rocket launch exhaust", "A WAY OUT FOR THE FLAME")

# ---------- 10. UMBILICAL ----------
part(10, "The arms that let go", "WHY DOES THIS ARM FALL AWAY?", "Why Do Launch Towers Drop Their Arms Seconds Before Liftoff?",
     """Why do the arms on a launch tower pull away just before liftoff? They carry the propellant, power and data lines to the rocket, called umbilicals, like the cord of a newborn baby. Until the last moments, the rocket is fed from the ground. Then each line has to disconnect, in the right order, and the arm has to swing out of the way of the rocket.""",
     "launch tower umbilical arm")
sc("""On the Space Shuttle, the oxygen vent arm with the beanie cap retracted about one minute forty-five seconds before liftoff. But it stayed unlatched until the very end, so it could return if the countdown stopped. That way, a delay meant going back one step, not starting from zero. On a rocket, every system has a plan for when things do not go to plan.""",
   "Space Shuttle fixed service structure", "A PLAN FOR EVERY DELAY")
sc("""And when it all works, the last thing you see is the ice. Once the arms have retreated and the engines have lit, the rocket shrugs off the white plates of frost, and climbs. What fell off was the cold, the part the rocket no longer needs.""",
   "rocket liftoff ice", "THE COLD FALLS AWAY")

# ---------- VERDICT ----------
sc("""So here are the ten. Ice from the cold tanks, and a Saturn V that let it fall. Orange foam that stopped the ice and became a danger of its own, a piece of foam that destroyed Columbia, heaters on the frozen feedlines, and a cap that vented oxygen. White clouds of boil-off, a water tower that fights the noise, a trench for the flame, and arms that let go at the last moment.""",
   "rocket launch sunrise", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see ice falling off a rocket, you will know what it is. A rocket at the pad is a cold machine in a warm world, and everything around it is there to manage that. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "rocket launch night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video11", "title": "Why Does Ice Fall Off Rockets at Launch?",
           "length_scale": 1.6, "scenes": S}, open("videos/video11/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
