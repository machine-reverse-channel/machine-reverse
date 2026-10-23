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
sc("""Almost everything you own crossed an ocean in a steel box, and every one of those boxes was lifted by a crane like this. A big ship-to-shore crane can weigh around two thousand tons, stand taller than a thirty-story building with its arm raised, and lift a box every couple of minutes, all day and all night. Today, ten parts of a port and its giant cranes, and why each one exists.""",
   "ship to shore container crane", "10 PARTS OF A GIANT", cuts=8, chapter="Intro")
sc("""Before the container, loading a ship was slow and brutal work. Dock workers carried sacks, barrels and crates one by one, and a ship could spend a week in port. Then, in nineteen fifty-six, an American trucking businessman named Malcom McLean sent fifty-eight metal boxes from New Jersey to Houston on an old tanker called the Ideal X. The world of shipping was never the same.""",
   "container ship port", "THE BOX THAT CHANGED THE WORLD")
sc("""As always, every fact comes from a named source, port authorities, standards organizations, and maritime histories, all listed in the description. Let's start with the strangest thing a port crane does. It lifts its own arm into the sky.""",
   "container terminal cranes", "WHY DOES THIS EXIST?")

# ---------- 1. BOOM ----------
part(1, "The arm that folds up", "WHY DOES THIS ARM FOLD UP?", "Why Do Port Cranes Raise Their Arms?",
     """Why do port cranes lift their long arms straight up into the sky? Because when a ship arrives or leaves, the arm, called the boom, would be right in the way. The boom sticks out far over the water to reach across the ship. A ship's bridge, its masts and antennas can stand dozens of meters tall. So the boom is hinged near the crane, and big cables pull it up until it points at the sky, leaving the berth free for the ship to slide in.""",
     "container crane boom raised")
sc("""Once the ship is tied up, the boom comes back down and becomes a bridge over the deck. A small cart called the trolley runs along it, carrying the container from the ship to the shore. On the biggest cranes, the boom reaches about seventy meters out over the water, more than two hundred feet. That is the length needed to grab the farthest box on the farthest side of the widest ships.""",
   "container crane trolley", "70 METERS OF REACH")
sc("""When several cranes stand at a quiet berth with their arms raised, they look like a row of giant animals. In fact, the legend says that the walkers of Star Wars were inspired by port cranes in Oakland, California. Whether that story is true or not, the shape has a simple reason. A crane with its arm up is a crane that is out of the way.""",
   "Port of Oakland cranes", "OUT OF THE WAY")

# ---------- 2. HEIGHT ----------
part(2, "The height", "WHY IS THIS CRANE SO TALL?", "Why Are Container Cranes So Tall?",
     """Why are container cranes so tall? Because the ships keep growing. The biggest container ships today are about four hundred meters long and more than sixty meters wide. They carry boxes stacked up to around ten high below deck and about ten high above deck, and twenty-four rows across. To lift the top box over the top of the stack, the crane needs a lifting height of around fifty meters above the rails, as tall as a fifteen-story building.""",
     "Panamax container crane")
sc("""In the nineteen eighties, many cranes were built for Panamax ships, the biggest that could fit through the old locks of the Panama Canal, about thirteen containers across. Then came post-Panamax ships, and then super post-Panamax. Many ports had to buy new cranes, or literally raise their old cranes, cutting the legs and inserting new steel sections to make them taller.""",
   "post panamax container crane", "CUT THE LEGS, ADD STEEL")
sc("""The reason ships grow is simple economics. One huge ship with one crew and one engine moves boxes more cheaply than two smaller ones. So shipping lines order bigger ships, and every port that wants to receive them needs bigger cranes, deeper water, and stronger docks. The crane is tall because the ship is big, and the ship is big because the cheapest box wins.""",
   "largest container ship", "THE CHEAPEST BOX WINS")

# ---------- 3. SPREADER ----------
part(3, "The spreader", "WHY DOES THIS FRAME HAVE 4 PINS?", "How a Port Crane Grabs a Container in Seconds",
     """Why does the crane hold a container with a flat steel frame instead of a hook? That frame is called a spreader. At each corner it has a pin called a twistlock. The spreader lands on top of the box, the four pins drop into four holes, and then each pin rotates ninety degrees. Its head is now crossways inside the hole, and it cannot come out. The box is locked. No ropes, no hooks, no workers on top. It takes seconds.""",
     "container crane spreader")
sc("""The spreader is also telescopic. In a few seconds, it can stretch from the size of a twenty-foot container to a forty-foot or forty-five-foot one. Many can even lift two twenty-foot boxes at once, and some cranes carry two forty-foot boxes side by side. Sensors tell the operator when all four twistlocks are seated, and a lift is blocked until they are.""",
   "spreader twistlock", "LOCKED IN SECONDS")
sc("""That speed is the whole point. A good crane team can move around thirty boxes an hour with each crane. With several cranes working one ship, thousands of boxes can be moved in a day or two. A ship that once stayed a week in port can now arrive, unload, reload and leave in a short stay, because of four pins that turn ninety degrees.""",
   "container terminal night", "FOUR PINS, NINETY DEGREES")

# ---------- 4. CORNER CASTING ----------
part(4, "The corner holes", "WHY DOES EVERY CONTAINER HAVE THESE HOLES?", "Why Does Every Shipping Container Have Holes in the Corners?",
     """Why does every shipping container in the world have the same holes at its corners? They are called corner castings, solid steel blocks with oval openings. They are where the twistlocks grab the box, where boxes lock to each other in a stack, and where they lock onto trucks and trains. And their size and position are set by international standards, so a box from China fits a crane in Germany and a truck in Brazil.""",
     "container corner casting")
sc("""This standard is the real invention. Malcom McLean's containers worked because they were all the same, and in the nineteen sixties the industry agreed on standard sizes, now set by the International Organization for Standardization. The most common box is twenty or forty feet long and eight feet wide. That is why port capacity is measured in TEU, twenty-foot equivalent units.""",
   "shipping containers stacked", "ONE SIZE FOR THE WORLD")
sc("""Those little corners carry enormous loads. A loaded container can be stacked under eight or nine other loaded boxes on a ship, and all that weight goes down through the corner posts, not the walls. The walls are thin corrugated steel. The corners are the skeleton. An empty container weighs only a few tons, but its four corners can hold a tower.""",
   "container stack ship", "THE CORNERS ARE THE SKELETON")

# ---------- 5. CABIN ----------
part(5, "The cabin with a glass floor", "WHY DOES THIS CABIN HAVE A GLASS FLOOR?", "Why Do Crane Operators Sit Over a Glass Floor?",
     """Why does the crane operator sit in a cabin with a glass floor? Because the operator's job is to look straight down. The cabin hangs under the trolley and travels with it, high above the ship. The operator sits leaning forward, watching the spreader drop into a narrow slot dozens of meters below, with only a few centimeters to spare. Doing that for hours, in wind and at night, takes enormous skill and concentration.""",
     "container crane operator cabin")
sc("""The spreader swings like a pendulum when the trolley stops. Modern cranes have anti-sway systems that move the trolley in a smart way to cancel the swing, the same idea as moving your hand under a hanging object to keep it still. Still, wind, rain and a moving ship make every lift a little different. Crane operators are among the best paid workers in many ports.""",
   "container crane lifting container", "CANCEL THE SWING")
sc("""More and more, that cabin is empty. In automated terminals, such as those in Rotterdam and several Asian ports, the operator works from an office on land, watching cameras and helping the machine only for the hardest parts of the lift. The view changed from a glass floor to a screen. The precision did not.""",
   "Port of Rotterdam Maasvlakte cranes", "FROM GLASS TO SCREEN")

# ---------- 6. RAILS ----------
part(6, "The wheels and rails", "WHY DOES THIS CRANE NEED SO MANY WHEELS?", "Why Do Port Cranes Need So Many Wheels?",
     """Why does a port crane stand on so many wheels? Because it weighs as much as a small ship, and it has to move. The crane rolls along two rails that run the length of the dock, so it can line up with any row of boxes on the ship. Its weight, plus the load and the force of the wind, is spread over many small wheels grouped at each leg, because a few large wheels would crush the dock.""",
     "container crane rail wheels")
sc("""The legs are far apart, often around thirty meters, so trucks and vehicles can drive between them and park right under the crane. The dock itself is a serious piece of engineering, often built on deep piles, because it must carry these moving giants plus stacks of loaded containers right at the edge of deep water.""",
   "container crane legs trucks", "TRUCKS DRIVE BETWEEN THE LEGS")
sc("""Power usually comes through a thick cable that unrolls from a giant reel as the crane moves along the dock. Many cranes even recover energy. When a container is lowered, the motors work as generators, the same trick as an electric car braking. A crane lowering thousands of boxes a day can feed power back into the system.""",
   "container crane cable reel", "POWER FROM LOWERING")

# ---------- 7. SHIPPED ASSEMBLED ----------
part(7, "Cranes that cross the ocean", "WHY IS THIS SHIP CARRYING CRANES?", "Why Are Port Cranes Shipped Fully Assembled?",
     """Why do new port cranes often cross the ocean already standing up? Because building them in one factory and shipping them complete is faster and cheaper than assembling them piece by piece at the port. Special heavy-lift ships carry two, three or more giant cranes standing on deck, fully assembled. Most of the world's large ship-to-shore cranes come from one Chinese company, ZPMC.""",
     "ZPMC crane ship delivery")
sc("""The trip can be tricky. Cranes arriving in San Francisco Bay have had to wait for the right tide and conditions to pass under the Golden Gate Bridge with very little clearance. At the destination, the cranes are rolled off the ship onto the dock's rails. A port can go from an empty berth to working cranes in a matter of weeks.""",
   "crane ship transport cranes", "UNDER THE GOLDEN GATE")
sc("""That concentration has also become a political issue. In two thousand twenty-four, the United States announced plans to support crane manufacturing at home, partly because of concerns about relying on foreign-made cranes with connected software. A piece of steel that looks simple is also a computer on legs.""",
   "container terminal cranes", "A COMPUTER ON LEGS")

# ---------- 8. STORM ANCHORS ----------
part(8, "The storm anchors", "WHY IS THIS CRANE CHAINED DOWN?", "Why Are Port Cranes Chained to the Ground?",
     """Why are port cranes chained to the ground before a storm? Because a crane on rails is a giant sail on wheels. A strong wind can push it along its rails, or even tip it over. So every crane has storm anchors. Heavy pins drop into holes in the dock, and tie-downs connect the legs to anchors in the concrete. An anemometer at the top measures the wind, and above a certain speed, work must stop.""",
     "container crane storm tie down")
sc("""This is not theory. In two thousand three, Typhoon Maemi hit the port of Busan in South Korea, and the wind knocked over several giant container cranes. Some fell onto each other. Cranes have also collapsed in other storms and in accidents when a ship hit a crane while berthing. When a crane falls, it can take a berth out of service for months.""",
   "container crane collapse", "A SAIL ON WHEELS")
sc("""That is why the boom position matters in a storm too. A raised boom catches the wind differently than a lowered one, and port rules say how each crane must be parked. Before a hurricane, crews park the cranes, lock them down, and leave. The safest crane in a storm is one that cannot move at all.""",
   "port cranes hurricane", "PARK IT, LOCK IT")

# ---------- 9. CELL GUIDES ----------
part(9, "The rails inside the ship", "WHY ARE THERE RAILS INSIDE THIS SHIP?", "Why Do Container Ships Have Rails Inside?",
     """Why are there vertical steel rails inside a container ship? They are called cell guides. Below deck, the hold is divided into slots, and each slot has guides at its four corners, like a giant elevator shaft. The crane simply lowers the box into the slot, and the guides lead it down into place. No lashing is needed below deck, because the guides hold the stack in place even when the ship rolls.""",
     "container ship cell guides")
sc("""On deck, there are no guides. Boxes are locked to each other with twistlocks and tied down with long steel rods called lashing bars, put in by hand by workers called lashers. In very bad weather, these stacks can still fail. In twenty twenty, the ship ONE Apus lost more than eighteen hundred containers overboard in a storm in the Pacific.""",
   "container lashing rods", "1,800 BOXES OVERBOARD")
sc("""That is why ships plan every box. A computer decides where each container goes, heavy ones low, light ones high, dangerous cargo apart, and boxes for the next port on top. The crane is not just lifting boxes. It is solving a giant puzzle, in the right order, so the ship stays stable and the next port can unload fast.""",
   "container ship stacking", "A GIANT PUZZLE")

# ---------- 10. STRADDLE CARRIER ----------
part(10, "The machine on stilts", "WHY DOES THIS MACHINE WALK OVER BOXES?", "Why Do Ports Use Machines on Stilts?",
     """Why do ports use strange machines that look like boxes on stilts? They are straddle carriers. They drive over a container, lift it up between their tall legs, and carry it away. Because they straddle the box, they can stack containers in rows, drive over a row, and pick up the one they need. They connect the crane at the ship to the stacks in the yard, nonstop.""",
     "straddle carrier")
sc("""Other ports use a different system. Driverless vehicles carry boxes from the ship cranes to automated stacking cranes in the yard. The first terminal with automated guided vehicles opened in Rotterdam in nineteen ninety-three. Today, many of the busiest terminals run day and night with very few people in the yard.""",
   "automated stacking crane container terminal", "DRIVERLESS SINCE 1993")
sc("""Every system has the same goal. Keep the giant crane at the ship busy every second, because the ship is the most expensive thing in the port. A ship waiting in port costs a fortune every day. So everything in the terminal, from straddle carriers to computers, exists to feed the crane.""",
   "container terminal aerial", "FEED THE CRANE")

# ---------- VERDICT ----------
sc("""So here are the ten. An arm that folds up out of the way. A height set by the biggest ships. A spreader with four turning pins, and corner holes that fit every crane in the world. A cabin with a glass floor, wheels that spread the weight, cranes that cross the ocean standing up, anchors against the storm, rails inside the ship, and machines on stilts to feed it all.""",
   "ship to shore container crane", "10 PARTS. 1 BOX.", chapter="The verdict", cuts=6)
sc("""The next time you open a package, remember it probably rode in a steel box, under a crane like this. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "container ship sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video42", "title": "Why Are Port Cranes So Gigantic?",
           "length_scale": 1.6, "scenes": S}, open("videos/video42/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
