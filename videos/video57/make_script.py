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
sc("""Near the top of Taipei one oh one, one of the tallest buildings in the world, hangs a golden steel ball weighing about six hundred and sixty tonnes. It is not decoration. It swings. When a typhoon hits Taiwan, the ball moves against the building's sway and calms it down. Today, eleven parts of a skyscraper, and why each one exists, starting with that giant ball.""",
   "Taipei 101 tuned mass damper", "A GIANT BALL INSIDE", cuts=8, chapter="Intro")
sc("""Skyscrapers look rigid, but they are not. They bend in the wind, they shake in earthquakes, and their tops move back and forth every day by centimeters, sometimes by much more. The real enemy of a tall building is usually not its own weight. It is the wind.""",
   "Taipei 101", "THE ENEMY IS THE WIND")
sc("""As always, every fact comes from a named source, building owners, engineering firms, and official reports, all listed in the description. Let's start with the ball.""",
   "tuned mass damper", "WHY DOES THIS EXIST?")

# ---------- 1. TUNED MASS DAMPER ----------
part(1, "The giant steel ball", "WHY IS THERE A GIANT BALL IN THIS BUILDING?", "Why Do Skyscrapers Hide a Giant Ball Inside?",
     """Why does Taipei one oh one have a six hundred and sixty tonne steel ball hanging inside it? Because it fights the sway. The ball hangs from cables, between the eighty seventh and ninety second floors, like a giant pendulum. It is tuned so that when the wind pushes the building one way, the ball's inertia makes it lag behind and pull the other way, taking energy out of the motion.""",
     "Taipei 101 tuned mass damper")
sc("""Hydraulic dampers under the ball absorb that energy and turn it into heat. Engineers say the ball can reduce the building's sway by up to about forty percent. In two thousand fifteen, during Typhoon Soudelor, it swung about a meter, the biggest movement ever recorded for it.""",
   "Taipei 101 tuned mass damper", "IT SWUNG ONE METER")
sc("""Most buildings hide their dampers. Taipei one oh one turned its damper into a tourist attraction, painted gold, with its own cartoon mascots. Visitors can walk around it and watch the counterweight that keeps the tower calm.""",
   "Taipei 101", "A TOURIST ATTRACTION")

# ---------- 2. SWAY ----------
part(2, "The top that moves", "WHY DOES THIS BUILDING SWAY?", "Why Are Skyscrapers Designed to Sway?",
     """Why are skyscrapers allowed to sway at all? Because a building that cannot bend would break. Steel and concrete flex a little under the wind, and that flexibility lets the building absorb gusts safely. The top of a very tall tower can move by tens of centimeters in a storm, and the structure is designed for it.""",
     "skyscraper sway")
sc("""The real limit is not strength, it is comfort. People feel motion long before the building is in any danger. Water in toilets sloshes, lamps swing, and some people feel seasick. So engineers set limits on how much the top floors may accelerate, especially in apartments where people sleep.""",
   "skyscraper", "THE LIMIT IS COMFORT")
sc("""Tall buildings are tested as models in wind tunnels before they are built, often in a model of the whole city around them, because neighboring towers change how the wind hits. The design is then adjusted until the motion at the top feels calm.""",
   "skyscraper wind tunnel", "TESTED IN A WIND TUNNEL")

# ---------- 3. CONFUSE THE WIND ----------
part(3, "The steps that confuse the wind", "WHY DOES THIS TOWER GET THINNER IN STEPS?", "Why Does the Burj Khalifa Get Thinner in Steps?",
     """Why does the Burj Khalifa get narrower in steps as it rises, like a spiral staircase? Because it confuses the wind. When wind flows around a tall building, it sheds swirls of air on alternate sides, called vortices. If those swirls form in a steady rhythm, they push the tower side to side, and the building can start to rock.""",
     "Burj Khalifa")
sc("""The Burj Khalifa's shape changes every few floors. Its Y shaped plan steps back in a spiral, so the width of the building is different at each height. The swirls cannot organize into one strong rhythm. Engineers called it confusing the wind, and they tested many versions in wind tunnels.""",
   "Burj Khalifa", "CONFUSING THE WIND")
sc("""The building was also turned on its site to face the strongest winds in the best direction. At eight hundred and twenty eight meters, the tallest building on Earth is shaped less by architecture than by air.""",
   "Burj Khalifa", "SHAPED BY AIR")

# ---------- 4. TWIST ----------
part(4, "The twisting tower", "WHY IS THIS SKYSCRAPER TWISTED?", "Why Is the Shanghai Tower Twisted?",
     """Why does the Shanghai Tower twist as it rises? Because the twist cuts the wind load. The tower rotates by about a hundred and twenty degrees from bottom to top, with a rounded triangle shape. Wind tunnel tests showed that this twist reduces the wind loads on the building by about a quarter compared to a plain rectangular tower.""",
     "Shanghai Tower")
sc("""Less wind load means less steel and concrete. The designers said it saved tens of millions of dollars in structure. At six hundred and thirty two meters, it is the tallest building in China, and the twist also gives it a glass skin with spaces between the inner and outer walls, used as sky gardens.""",
   "Shanghai Tower", "LESS STEEL")
sc("""Twisting, tapering, and cutting holes through the top are now common tricks in supertall design. They all do the same thing. They stop the wind from finding a steady rhythm to push against.""",
   "skyscraper", "NO STEADY RHYTHM")

# ---------- 5. CITICORP ----------
part(5, "The building fixed in secret", "WHY WAS THIS TOWER FIXED IN SECRET?", "Why Was This Skyscraper Secretly Repaired at Night?",
     """Why was a New York skyscraper secretly repaired at night in nineteen seventy eight? The building was the Citicorp Center, famous for standing on four tall columns at the middle of each side, not at the corners. After it opened, a question from a student led the structural engineer, William LeMessurier, to recheck his design for winds hitting the building diagonally, at its corners.""",
     "Citicorp Center")
sc("""He found a serious problem. The diagonal braces had been joined with bolts instead of welds, and under certain winds those joints were too weak. His calculations suggested that a strong storm could bring the building down. Hurricane season was coming. So, at night, welders covered the joints with thick steel plates while offices worked normally during the day.""",
   "Citicorp Center", "WELDING AT NIGHT")
sc("""Emergency plans were made to evacuate the neighborhood if a hurricane approached. The repairs were finished before any storm tested them, and the public did not learn the full story until nineteen ninety five. The building also has a tuned mass damper on top, a block of concrete of about four hundred tonnes, sliding on oil.""",
   "Citicorp Center", "SECRET FOR 17 YEARS")

# ---------- 6. CORE ----------
part(6, "The concrete core", "WHY DOES EVERY TOWER HAVE A CONCRETE SPINE?", "Why Do Skyscrapers Have a Concrete Spine?",
     """Why do most skyscrapers have a massive concrete tube running up their middle? It is the core, the building's spine. It holds the elevators, stairs, pipes and cables, and it is the main structure that stops the tower from bending in the wind. Thick concrete walls on all sides of the core make it very stiff.""",
     "skyscraper core")
sc("""On a construction site, the core usually rises first, several floors ahead of everything else. Special climbing forms are pushed up a few meters at a time, and concrete is poured around steel bars. The floors and outer columns follow behind.""",
   "skyscraper", "THE CORE RISES FIRST")
sc("""The core is also the safe zone. Stairs inside it are protected by fire resistant walls and pressurized with fresh air to keep smoke out. Some towers in Asia also have refuge floors every so many levels, open floors where people can wait safely during a fire.""",
   "skyscraper", "THE SAFE ZONE")

# ---------- 7. OUTRIGGERS ----------
part(7, "The giant arms at the top", "WHY ARE THERE GIANT TRUSSES UP HERE?", "Why Do Skyscrapers Have Giant Steel Arms Inside?",
     """Why do some skyscrapers have entire floors filled with giant steel trusses? They are outriggers. A core alone would bend like a fishing rod in the wind. Outriggers are huge braces that connect the core to the columns on the outside of the building, so the whole width of the tower works together.""",
     "skyscraper outrigger")
sc("""When the wind pushes the tower, the core tries to bend. The outriggers turn that bending into pushing and pulling on the outer columns, which are far apart and very effective at resisting it. It is like a person spreading their arms to keep their balance.""",
   "skyscraper", "SPREADING ITS ARMS")
sc("""Outrigger floors are usually used for machinery, because the trusses get in the way of offices. If you see a tower with dark bands every few dozen floors, those bands often hide outriggers and mechanical rooms.""",
   "skyscraper", "THE DARK BANDS")

# ---------- 8. ELEVATORS ----------
part(8, "The sky lobby", "WHY DO YOU CHANGE ELEVATORS HALFWAY UP?", "Why Do You Change Elevators in Tall Buildings?",
     """Why do you have to change elevators halfway up a very tall building? Because elevators take up space, and space is money. If every elevator went from the ground to every floor, the bottom of the building would be almost all elevator shafts. So supertall towers use express elevators to sky lobbies, where you change to local elevators that serve only a group of floors.""",
     "skyscraper elevator")
sc("""There is another limit. Steel elevator ropes get heavier the longer they are, and at some point they mostly carry their own weight. That limited a single elevator rise to around five hundred meters. Newer carbon fiber ropes are much lighter, and could allow elevators to rise twice as far.""",
   "skyscraper elevator", "ROPES THAT CARRY THEMSELVES")
sc("""Some buildings use double deck elevators, two cabins stacked on top of each other, serving two floors at once. Fast elevators also control air pressure in the cabin, so passengers' ears do not hurt as they climb hundreds of meters in under a minute.""",
   "skyscraper elevator", "DOUBLE DECK")

# ---------- 9. WARNING LIGHTS ----------
part(9, "The red lights on top", "WHY DO SKYSCRAPERS HAVE RED LIGHTS?", "Why Do Skyscrapers Have Blinking Red Lights?",
     """Why do skyscrapers have red or white lights blinking on their tops? They are aircraft warning lights. Any structure tall enough to be a hazard for planes and helicopters must be marked, so pilots can see it at night and in bad weather. Aviation authorities set the rules for color, brightness and flash rate.""",
     "aircraft warning light skyscraper")
sc("""Very tall structures often use bright white flashing lights during the day and red lights at night. The lights are placed at the top and at levels along the height, so the whole outline of the structure can be seen, not just one point.""",
   "skyscraper", "WHITE BY DAY, RED BY NIGHT")
sc("""Changing a bulb at the top of a skyscraper can be a climbing job of its own, which is why modern lights use long life LEDs. And in some cities, people use the blinking red lights to tell the time of night, the weather, or simply as a sign of home.""",
   "skyscraper", "A SIGN OF HOME")

# ---------- 10. GONDOLA ----------
part(10, "The machine that cleans the windows", "WHY IS THERE A CRANE ON THE ROOF?", "Why Is There a Crane on Top of Skyscrapers?",
     """Why is there a small crane on the roof of many skyscrapers? It is a building maintenance unit. It moves around the roof on rails and lowers a platform, called a gondola, down the face of the building. Workers ride it to clean windows, replace broken glass and inspect the outer skin.""",
     "skyscraper window cleaning gondola")
sc("""On a supertall tower, cleaning all the windows once can take months. The Burj Khalifa has several of these machines, some hidden inside the building and rolled out when needed. Window cleaners there work hundreds of meters above the ground, often in strong wind and heat.""",
   "Burj Khalifa", "MONTHS PER CLEANING")
sc("""The roof machine is part of the design from the start, because every shape on the facade must be reachable. Fancy curves and sloping glass may look great, but somebody has to clean them, and the gondola must be able to follow.""",
   "skyscraper", "DESIGNED TO BE CLEANED")

# ---------- 11. FOUNDATION ----------
part(11, "The piles under the tower", "WHY DOES THIS TOWER NEED DEEP PILES?", "Why Do Skyscrapers Need Foundations Deep Underground?",
     """What holds up a building weighing hundreds of thousands of tonnes? Foundations that reach deep underground. The Burj Khalifa stands on a thick concrete raft supported by about two hundred concrete piles, each about one and a half meters wide and more than forty meters long. The ground under Dubai is not hard rock, so the piles hold the building mostly by friction along their length.""",
     "skyscraper foundation piles")
sc("""The groundwater in Dubai is also salty and aggressive to concrete and steel. So the foundation used special dense concrete and a system that protects the steel inside from corrosion, the same way ships protect their hulls.""",
   "Burj Khalifa", "SALTY GROUNDWATER")
sc("""Foundations are the least glamorous part of a skyscraper. Nobody visits them, and nobody photographs them once they are buried. But every meter of height above ground depends on what was done below it, before the tower even began to rise.""",
   "skyscraper", "WHAT IS BELOW")

# ---------- VERDICT ----------
sc("""So here are the eleven. A giant ball that fights the sway, and a top that is allowed to move. Steps that confuse the wind, a twist that cuts the load, and a tower fixed in secret. A concrete spine, steel arms reaching out to the edges, elevators you change halfway up, red lights for pilots, a crane that cleans the windows, and piles deep in the ground.""",
   "skyscraper", "11 PARTS. 1 GIANT BALL.", chapter="The verdict", cuts=6)
sc("""Next time you stand at the top of a tall building, remember that it is moving with you, exactly as planned. If you want more machines and structures explained part by part, subscribe to Machine Reverse. And tell us in the comments what you want us to take apart next.""",
   "skyscraper", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video57", "title": "Why Do Skyscrapers Hide a Giant Ball Inside?",
           "length_scale": 1.6, "scenes": S}, open("videos/video57/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
