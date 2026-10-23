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
sc("""The Titanic was the largest moving object ever built by humans. It had sixteen watertight compartments, electric doors that closed with one switch on the bridge, and a reputation for being practically unsinkable. It hit an iceberg at eleven forty at night, and two hours and forty minutes later, it was gone. The hole was not even big. Today, ten parts of the Titanic, and how each one helped a giant ship sink so fast.""",
   "RMS Titanic", "10 PARTS. 160 MINUTES.", cuts=8, chapter="Intro")
sc("""The Titanic left Southampton on April tenth, nineteen twelve, on its first voyage to New York. It was two hundred sixty-nine meters long, about eight hundred eighty-two feet, and it carried more than two thousand two hundred people. Its builders, Harland and Wolff in Belfast, were among the best shipbuilders in the world. And that is what makes the story so strange. Almost every part we will look at today was well made. The problem was how the parts worked together on one cold night.""",
   "Titanic leaving Southampton", "BUILT BY THE BEST")
sc("""As always, every fact comes from a named source, the official British and American inquiries, metallurgy studies of steel recovered from the wreck, and maritime historians, all listed in the description. Let's start with the walls that were supposed to save it.""",
   "Titanic Harland and Wolff", "WHY DOES THIS EXIST?")

# ---------- 1. BULKHEADS ----------
part(1, "The walls that stopped too low", "WHY DIDN'T THESE WALLS SAVE TITANIC?", "Why Didn't the Titanic's Watertight Walls Save It?",
     """Why didn't the Titanic's watertight walls save it? The hull was divided by fifteen steel walls called bulkheads, creating sixteen compartments. The ship could stay afloat with any two compartments flooded, and even with the first four flooded. But the iceberg opened the first five, and maybe a sixth. And here is the fatal detail. The bulkheads did not go all the way up. Most of them stopped at E deck, only a few decks above the waterline.""",
     "Titanic watertight bulkheads diagram")
sc("""So the compartments were not sealed boxes. They were more like an ice cube tray. As the bow filled with water and sank lower, the water reached the top of a bulkhead and simply spilled over into the next compartment. Then the next. Then the next. The ship designer, Thomas Andrews, walked through the damage and told the captain the Titanic would sink. He gave it about an hour or an hour and a half.""",
   "ice cube tray", "AN ICE CUBE TRAY")
sc("""Why build the walls so low? Higher bulkheads would have cut through the first class spaces, the long corridors and the grand public rooms that sold tickets. And the rules of the time did not require more. After the disaster, Titanic's sister ship Olympic was sent back to the shipyard, and several of its bulkheads were raised higher. The fix was easy. It just came too late.""",
   "RMS Olympic", "THE FIX CAME LATER")

# ---------- 2. DOUBLE BOTTOM ----------
part(2, "The double bottom", "WHY DID TITANIC HAVE TWO BOTTOMS?", "Why Did the Titanic Have a Double Bottom But Not Double Sides?",
     """Why did the Titanic have a double bottom? Because the most common danger for a big ship was running aground, tearing the bottom open on rocks. So the Titanic had a second steel skin inside the bottom of the hull, with a gap of about one and a half meters, a little over five feet, between the two. If the outer bottom was ripped open, the inner one would keep the sea out. Against rocks, it was excellent protection.""",
     "Titanic double bottom construction")
sc("""But the iceberg did not hit the bottom. It scraped along the side of the bow, below the waterline. And the sides of the Titanic were a single skin of steel, about two and a half centimeters thick, around one inch. Interestingly, the idea of a double skin on the sides was not new. The giant steamship Great Eastern had a double hull back in eighteen fifty-eight. It was expensive, it was heavy, and most liners did not use it.""",
   "SS Great Eastern", "ONE INCH OF STEEL")
sc("""After the Titanic, that changed. Olympic was refitted with an inner skin along the sides of its boiler and engine rooms. Today, oil tankers must have double hulls by law, after other disasters like the Exxon Valdez spill. The lesson took decades to spread, but it was simple. Protect the ship from the side it actually gets hit on.""",
   "double hull tanker construction", "PROTECT THE SIDE")

# ---------- 3. RIVETS ----------
part(3, "The rivets", "WHY DID THESE RIVETS POP?", "Why Did the Titanic's Rivets Fail?",
     """Why do some researchers blame tiny rivets for the Titanic's fate? The hull plates were held together by about three million rivets. In the middle of the ship, they were steel, driven by big hydraulic machines. But at the bow and the stern, where the hull curves and the machines could not fit, workers hammered them in by hand, and many of those were wrought iron. And the bow is exactly where the iceberg hit.""",
     "Titanic hull plates rivets")
sc("""In two thousand eight, metallurgists Jennifer Hooper McCarty and Tim Foecke studied rivets recovered from the wreck. Some had high amounts of slag, glassy impurities that make wrought iron weaker. Their theory is that the iceberg pushed against the plates, the rivet heads snapped off, and the seams between plates opened like zippers. That would explain why the damage was a series of thin openings instead of one big gash.""",
   "wrought iron rivets", "SEAMS LIKE ZIPPERS")
sc("""Not every expert agrees, and the rivets were not unusual for their time. But the wreck supports one part of the idea. When the bow was surveyed with sonar in the nineteen nineties, investigators found the damage was mostly narrow slits along the seams. At the British inquiry, the shipbuilder's naval architect estimated the total opening at only around twelve square feet, about one square meter. A ship of forty-six thousand tons, sunk through a hole the size of a door.""",
   "Titanic wreck bow", "A HOLE THE SIZE OF A DOOR")

# ---------- 4. STEEL ----------
part(4, "The cold steel", "WHY DID THIS STEEL CRACK LIKE GLASS?", "Why Did the Titanic's Steel Act Like Glass?",
     """Why might the Titanic's steel have cracked so easily? Because steel changes its personality with temperature. Warm steel bends before it breaks. Cold steel can shatter. The sea that night was about minus two degrees Celsius, twenty-eight degrees Fahrenheit, colder than freezing because it was salt water. In the nineteen nineties, scientists tested steel recovered from the wreck, and at that temperature it was brittle compared with modern ship steel.""",
     "Titanic hull plates")
sc("""The reason was the chemistry. The steel had a lot of sulfur and relatively little manganese, and it was made in a way that left it more brittle in the cold. That was normal for nineteen twelve. Nobody understood brittle fracture well until the Second World War, when some Liberty ships cracked in half in cold water, a few of them while sitting in port.""",
   "Liberty ship broken", "THE LIBERTY SHIP LESSON")
sc("""Today, ship steel is tested for exactly this. Engineers hit a small notched sample with a heavy pendulum at low temperature, called a Charpy test, to prove it will bend instead of shatter. Ships built for icy waters must pass at colder temperatures. The Titanic was built with the best steel of its time. It was just tested by the coldest water of its life.""",
   "Charpy impact test machine", "BEND, DON'T SHATTER")

# ---------- 5. RUDDER ----------
part(5, "The rudder", "WHY COULDN'T THIS RUDDER TURN IN TIME?", "Why Couldn't the Titanic Turn in Time?",
     """Why couldn't the Titanic turn away from the iceberg? Look at the rudder. It was about seventy-eight feet tall, twenty-four meters, and weighed more than one hundred tons. That sounds huge, but compared with the size of the ship, it was narrow. It met the rules of the time, and it was designed for a ship that would cross the ocean in straight lines, not dodge obstacles. A big liner was built to be stable, not agile.""",
     "Titanic rudder")
sc("""The lookouts saw the iceberg only about thirty-seven seconds before the impact. First Officer William Murdoch ordered the helm hard over, and the bow began to swing. In that time, the Titanic, traveling at about twenty-two knots, covered more than four hundred meters, about a quarter of a mile. The ship had started to turn, and that is exactly why it did not hit head-on. It scraped along the side.""",
   "Titanic bridge wheel", "37 SECONDS")
sc("""And here is one of the cruelest ideas in the story. Many naval architects believe that a head-on collision would have crushed the bow and flooded maybe the first two or three compartments, which the ship could survive. By turning, the Titanic opened more compartments along its side. The turn was the correct reaction. It just happened to be the worst possible way to meet that iceberg.""",
   "iceberg North Atlantic", "THE TURN THAT HURT")

# ---------- 6. CENTER PROPELLER ----------
part(6, "The center propeller", "WHY COULDN'T THIS PROPELLER REVERSE?", "Why Couldn't the Titanic's Middle Propeller Reverse?",
     """Why couldn't the Titanic's middle propeller go in reverse? The ship had three propellers. The two outer ones were driven by giant steam engines, each as tall as a building. The center one was driven by a turbine that ran on leftover steam from those engines, a clever way to squeeze more power from the same coal. But that turbine could only turn one way. To stop or reverse, the center propeller simply had to stop.""",
     "Titanic propellers")
sc("""And the center propeller sat right in front of the rudder. Its water flow helps a rudder bite. According to testimony from the inquiries, the engines may have been ordered to stop or reverse as the ship turned. If that happened, the center propeller stopped pushing water over the rudder at the worst moment, and the turn became weaker. Historians still debate the exact orders, but the design made this possible.""",
   "Olympic propellers Harland Wolff", "IN FRONT OF THE RUDDER")
sc("""The mixed system was not a mistake. It was more efficient, and it was used on Olympic and Britannic too. Each design choice on a ship has a price, and this one was paid in maneuverability, something a liner almost never needed. Almost never. Engineers today still talk about this when they study how propulsion and steering work together.""",
   "ship propeller drydock", "A PRICE IN AGILITY")

# ---------- 7. CROW'S NEST ----------
part(7, "The crow's nest", "WHY HAD NO BINOCULARS UP HERE?", "Why Did the Titanic's Lookouts Have No Binoculars?",
     """Why did the Titanic's lookouts have no binoculars? The crow's nest, high up on the front mast, was where two men watched for danger. But the binoculars were locked in a box, and the key was with an officer, David Blair, who was removed from the crew at the last minute before the voyage and left with the key in his pocket. Lookout Frederick Fleet later testified that with binoculars, they could have seen the iceberg in time to get out of the way.""",
     "Titanic crow's nest")
sc("""That claim is still debated, because binoculars narrow your view and lookouts were trained to scan with their eyes. And the night itself was against them. There was no moon, and the sea was perfectly calm. Normally, small waves break at the base of an iceberg and create a white line you can spot. That night, there were no waves at all. The iceberg was a dark shape on a dark sea.""",
   "iceberg at night", "NO MOON. NO WAVES.")
sc("""In two thousand seven, the key to that binocular box was sold at auction for ninety thousand pounds. It is sometimes called the key that could have saved the Titanic. The real lesson is less dramatic. Modern ships use radar, which sees through darkness and fog, and no one relies only on human eyes and a small box with a lock.""",
   "ship radar antenna", "THE KEY")

# ---------- 8. WIRELESS ROOM ----------
part(8, "The wireless room", "WHY DID NOBODY ANSWER THIS RADIO?", "Why Didn't the Closest Ship Hear the Titanic?",
     """Why didn't the closest ship come to save the Titanic? The Titanic had one of the most powerful radios at sea, run by two Marconi operators, Jack Phillips and Harold Bride. But they worked for the Marconi company, and their main job was sending private messages for rich passengers. That day, the Titanic received several ice warnings from other ships. At least one never made it to the bridge.""",
     "Titanic Marconi wireless room")
sc("""The ship Californian was stopped in the ice, close enough to see the Titanic's lights, maybe ten to twenty miles away. Its radio operator tried to warn the Titanic about the ice, and Phillips, busy with passenger messages, cut him off with a message that basically said shut up, I am busy. A little later, the Californian's operator turned off his radio and went to bed. Minutes later, the Titanic hit the iceberg. Its distress calls went to a ship that was no longer listening.""",
   "SS Californian", "SHUT UP, I AM BUSY")
sc("""The Carpathia, about fifty-eight miles away, heard the call and raced north through the ice. It arrived around four in the morning, more than an hour and a half after the Titanic was gone. After the disaster, new rules required ships to keep their radios staffed twenty-four hours a day. A radio is only a safety device if someone is listening.""",
   "RMS Carpathia", "SOMEONE MUST LISTEN")

# ---------- 9. LIFEBOATS ----------
part(9, "The lifeboats", "WHY WERE THERE SO FEW LIFEBOATS?", "Why Did the Titanic Have So Few Lifeboats?",
     """Why did the Titanic have so few lifeboats? It carried twenty boats, enough for about one thousand one hundred seventy-eight people, with more than two thousand two hundred on board. And it was perfectly legal. British rules from the eighteen nineties based the number of lifeboats on the ship's tonnage, and the scale stopped at ten thousand tons. The Titanic was more than four times bigger, and it actually carried more boats than the law required.""",
     "Titanic lifeboats davits")
sc("""The davits, the cranes that lowered the boats, were designed so each one could handle several boats. One designer had proposed far more lifeboats. But the deck space was kept open for passengers to walk on, and in those days, lifeboats were seen as ferries, used to move people to a rescue ship, not to hold everyone at once. On the night, some boats left half empty. The first boat lowered had room for sixty-five people, and it left with about twenty-eight.""",
   "Titanic lifeboat Carpathia", "65 SEATS, 28 PEOPLE")
sc("""About fifteen hundred people died. In nineteen fourteen, the first International Convention for the Safety of Life at Sea, called SOLAS, required lifeboat space for everyone on board, plus lifeboat drills and the ice patrol that still watches the North Atlantic. The Titanic did not just sink. It rewrote the rules of the sea.""",
   "lifeboat drill ship", "A SEAT FOR EVERYONE")

# ---------- 10. EXPANSION JOINT ----------
part(10, "The expansion joint", "WHY DID TITANIC BREAK IN TWO?", "Why Did the Titanic Break in Half?",
     """Why did the Titanic break in two? As the bow sank, the stern rose out of the water, until a huge part of the ship was hanging in the air, unsupported. The hull was never designed to carry that load. Near the end, the ship broke apart, roughly between the third and fourth funnels. The upper structure even had expansion joints, small built-in gaps that let it flex in waves. Some researchers think one of them was a weak point where the break began.""",
     "Titanic sinking illustration")
sc("""For seventy-three years, many people believed the Titanic sank in one piece, because the official inquiries did not conclude that it broke apart, even though some survivors said it did. Then, in nineteen eighty-five, Robert Ballard's expedition found the wreck at about three thousand eight hundred meters, more than twelve thousand feet deep. The bow and stern were lying about six hundred meters apart. The survivors had been right.""",
   "Titanic wreck", "THE SURVIVORS WERE RIGHT")
sc("""The bow sank at an angle and plowed into the mud almost intact. The stern spun as it fell and was torn apart. Once the ship broke, the end came fast. At two twenty in the morning, the Titanic disappeared. Two hours and forty minutes after a scrape, it was resting on the bottom of the Atlantic.""",
   "Titanic stern wreck", "2:20 AM")

# ---------- VERDICT ----------
sc("""So here are the ten. Walls that stopped too low. A double bottom, but single sides. Rivets that may have popped, and steel that turned brittle in freezing water. A narrow rudder and a propeller that could not reverse. Lookouts without binoculars, a radio nobody answered, lifeboats for only half, and a hull that broke in two. No single part sank the Titanic. They did it together.""",
   "RMS Titanic", "10 PARTS. ONE NIGHT.", chapter="The verdict", cuts=6)
sc("""Every ship you board today carries a piece of the Titanic in its rules, from lifeboats for everyone to radios that never sleep. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "cruise ship lifeboats", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video41", "title": "Why Did the Titanic Sink So Fast?",
           "length_scale": 1.6, "scenes": S}, open("videos/video41/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
