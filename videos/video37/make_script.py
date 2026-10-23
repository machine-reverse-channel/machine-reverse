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
sc("""Take an empty plastic bottle down to the bottom of a deep swimming pool, and it gets squeezed. Now imagine going three hundred metres under the sea. The water pushes on every square metre of a submarine with the weight of hundreds of tonnes. And yet, inside, the crew walks around in normal air, at normal pressure. Today, ten parts of a submarine, and why each one exists.""",
   "submarine underwater", "WHY NOT CRUSHED?", cuts=8, chapter="Intro")
sc("""Every ten metres of sea water adds about one more atmosphere of pressure. At three hundred metres, the water pushes about thirty times harder than the air at the surface. A submarine is a machine built to resist that push, while staying quiet, hidden and able to come back up.""",
   "submarine diving", "ONE ATMOSPHERE EVERY 10 METRES")
sc("""As always, every fact here comes from a named source, navies and naval references, all listed in the description. Some details, like exact diving depths, are secret, so we will stay with what is publicly known. Let's start with the hull.""",
   "submarine surfacing", "WHY DOES THIS EXIST?")

# ---------- 1. PRESSURE HULL ----------
part(1, "The pressure hull", "WHY IS THIS SUBMARINE A TUBE?", "Why Don't Submarines Get Crushed?",
     """Why is a submarine shaped like a long tube? Because a cylinder is one of the best shapes to resist pressure from all sides. Inside the outer skin, there is a thick steel tube called the pressure hull, where the crew lives. The water presses evenly all around the circle, and the steel works in compression, the way an arch holds up a bridge.""",
     "submarine pressure hull")
sc("""The steel is a special high strength alloy, and the tube is reinforced from the inside with rings called frames, spaced along its length. A flat surface would bend under the pressure. A curved one spreads the force around the ring. Even the ends of the pressure hull are domed, never flat.""",
   "submarine hull frames", "RINGS INSIDE THE TUBE")
sc("""Even so, the hull is squeezed a little as the submarine dives. Sailors have told stories of a string stretched across a compartment going slack at depth, as the hull gets slightly smaller. The steel bends, but it does not break, as long as the submarine stays above its limit.""",
   "submarine interior", "IT SHRINKS A LITTLE")

# ---------- 2. DEPTH LIMIT ----------
part(2, "The depth limit", "WHY DOES THIS SUBMARINE HAVE A DEPTH LIMIT?", "Why Do Submarines Have a Depth Limit?",
     """Why does every submarine have a strict depth limit? Because there is a depth where the hull would fail. Navies define a test depth, the deepest the submarine is designed to go in normal operations, and a much deeper crush depth, where the hull is expected to collapse. The gap between them is the safety margin.""",
     "submarine depth gauge")
sc("""The exact numbers are secret for most military submarines, but modern attack submarines are generally believed to operate at several hundred metres. Going deeper means a thicker, heavier hull, or stronger materials. Every metre of depth is a trade with weight, speed and cost.""",
   "attack submarine", "A SECRET NUMBER")
sc("""The Soviet Union built some submarines with titanium hulls, which are strong and light. One of them, the Komsomolets, reached a depth of about one thousand metres in nineteen eighty-four, a record for a military submarine. Titanium was extremely expensive and hard to weld, so very few were built.""",
   "Soviet submarine titanium", "TITANIUM")

# ---------- 3. BALLAST TANKS ----------
part(3, "The ballast tanks", "WHY DOES THIS SUBMARINE BLOW OUT WATER?", "Why Do Submarines Blow Out Water to Surface?",
     """Why does a submarine blast out sprays of water when it surfaces? Because of its ballast tanks. A submarine dives by letting sea water into large tanks, which makes it heavier. To come back up, it uses compressed air to push the water out, making the submarine lighter, so it floats up.""",
     "submarine emergency surfacing")
sc("""The main ballast tanks sit outside the pressure hull, between it and the outer skin. They do not need to resist the full pressure, because they are open to the sea at the bottom. Air pushed in at the top simply forces the water out of the openings below.""",
   "submarine ballast tank", "OPEN AT THE BOTTOM")
sc("""In an emergency, the crew can blow all the tanks at once with high pressure air. The submarine rises fast and can burst out of the water at a steep angle, throwing up a huge spray. It is the most dramatic moment in a submarine's life, and the last line of defence if something goes wrong.""",
   "submarine breaching", "EMERGENCY BLOW")

# ---------- 4. TRIM TANKS ----------
part(4, "The trim tanks", "WHY DOES THIS SUBMARINE MOVE WATER INSIDE?", "Why Do Submarines Pump Water Inside Themselves?",
     """Why does a submarine pump water around inside itself? To stay perfectly balanced. Underwater, a submarine should be neither heavier nor lighter than the water around it, so it hovers without sinking or rising. That is called neutral buoyancy. Small tanks called trim tanks fine tune the weight.""",
     "submarine control room")
sc("""The weight of a submarine keeps changing. Food is eaten, fuel is used, torpedoes are fired, and water density changes with temperature and salt. Even the crew walking from one end to the other can tip the boat. The trim tanks move water forward or backward, and take water in or pump it out, to keep the balance.""",
   "submarine crew", "THE WEIGHT KEEPS CHANGING")
sc("""A well trimmed submarine can hover silently, with almost no use of its engine. That is a huge advantage, because a moving propeller makes noise. Balancing a ship of thousands of tonnes to within a few hundred kilograms is one of the quiet skills of a submarine crew.""",
   "submarine underwater hovering", "HOVERING IN SILENCE")

# ---------- 5. ANECHOIC TILES ----------
part(5, "The rubber tiles", "WHY IS THIS SUBMARINE COVERED IN TILES?", "Why Are Submarines Covered in Rubber Tiles?",
     """Why are many submarines covered in black rubber tiles? They are anechoic tiles, which means without echo. An enemy can find a submarine by sending a sound pulse through the water and listening for the echo, which is called active sonar. The tiles absorb part of that sound, so the echo is weaker.""",
     "submarine anechoic tiles")
sc("""The tiles also work from the inside. Machines on the submarine, like pumps and generators, make vibrations that travel through the hull and into the water. The rubber layer dampens those sounds before they escape, making the submarine harder to hear. The Soviet Union was one of the first to use them widely.""",
   "submarine hull rubber", "DAMPENING THE NOISE")
sc("""Look closely at photos of submarines in port, and you will sometimes see missing tiles, like gaps in a mouth. Keeping the tiles glued on is a constant maintenance job. For a submarine, being heard is the biggest danger of all, more than the pressure itself.""",
   "submarine in port", "BEING HEARD IS THE DANGER")

# ---------- 6. DIVING PLANES ----------
part(6, "The diving planes", "WHY DOES THIS SUBMARINE HAVE SMALL WINGS?", "Why Do Submarines Have Small Wings?",
     """Why do submarines have small wings on the tower or the bow? They are diving planes, and they work like the elevators on the tail of a plane. When the submarine is moving, tilting the planes pushes the bow up or down, so the boat can change depth smoothly without changing its ballast.""",
     "submarine diving planes")
sc("""On many American submarines, the planes were placed on the tower, called the sail. That keeps them away from the noisy bow sonar. But planes on the sail must turn vertical to break through ice when the submarine surfaces in the Arctic. Newer designs often move them to the bow, where they can fold away.""",
   "submarine sail", "BREAKING THROUGH ICE")
sc("""At the stern, a set of control surfaces in a cross or X shape steers the submarine left, right, up and down. An X shape gives each surface a part of every move, and more control if one is damaged. Underwater flight is still flight, just in a much thicker fluid.""",
   "submarine stern planes", "UNDERWATER FLIGHT")

# ---------- 7. PROPULSOR ----------
part(7, "The hidden propeller", "WHY IS THIS PROPELLER HIDDEN?", "Why Do Submarines Hide Their Propellers?",
     """Why are the propellers of modern submarines so secret, often covered when the boat is in dry dock? Because the shape of a propeller decides how much noise it makes. An enemy listening with sensitive microphones can identify a submarine by the sound of its propeller.""",
     "submarine propeller covered")
sc("""Older submarines used a propeller with many curved blades, shaped to avoid cavitation, the bubbles that form and collapse when a propeller spins too fast. Those bubbles are loud underwater. Many modern submarines use a pump jet instead, a rotor spinning inside a duct, which is quieter at high speed.""",
   "pump-jet submarine", "A PUMP JET")
sc("""That is why you may see tarps or panels hiding the back of a submarine in harbour photos. Its exact shape is one of the most guarded secrets in naval engineering. A submarine's whole value is in staying unheard, and the propeller is the part most likely to give it away.""",
   "submarine dry dock", "A GUARDED SECRET")

# ---------- 8. PHOTONICS MAST ----------
part(8, "The periscope", "WHY DOESN'T THIS SUBMARINE HAVE A PERISCOPE?", "Why Do Modern Submarines Not Have a Periscope?",
     """Why do some modern submarines have no traditional periscope? A classic periscope is a long tube with mirrors or prisms, passing right through the pressure hull into the control room. That tube needs a large hole in the hull, and it decides where the control room must be, directly under the sail.""",
     "submarine periscope")
sc("""The American Virginia class uses photonics masts instead. They carry cameras and sensors, and send images by cable to screens inside. Nothing has to pass through the hull except wires, so the control room can be placed lower and wherever designers want it, with more space.""",
   "Virginia class submarine", "CAMERAS INSTEAD OF MIRRORS")
sc("""The mast can also take a quick panoramic picture in a moment and then go down, so it spends less time above the water, where it could be spotted by radar. The crew can study the image later. The periscope, the most famous part of a submarine, is being replaced by a camera.""",
   "submarine mast", "A QUICK LOOK")

# ---------- 9. ESCAPE HATCH ----------
part(9, "The escape hatch", "HOW DO SAILORS ESCAPE A SUNKEN SUBMARINE?", "Why Do Submarines Have Escape Hatches?",
     """How can sailors escape from a sunken submarine? Through an escape trunk, a small chamber with a hatch, built into the pressure hull. A sailor enters, the inner hatch is closed, and the chamber is slowly flooded until the pressure inside matches the sea outside. Then the outer hatch can open.""",
     "submarine escape hatch")
sc("""The sailor rises to the surface wearing a special suit, which provides air and keeps them warm. The rise must be fast but controlled, because the air in the lungs expands as the pressure drops. Escape is only possible from limited depths. Deeper, rescue vehicles must come down and connect to the hatch.""",
   "submarine escape suit", "A FAST, CONTROLLED RISE")
sc("""Deep rescue submersibles can attach to the escape hatch like a docking spacecraft, and carry sailors up a few at a time in normal pressure. Navies around the world practise these rescues together, because when a submarine is in trouble, every hour counts.""",
   "submarine rescue vehicle", "EVERY HOUR COUNTS")

# ---------- 10. TRIESTE ----------
part(10, "The deep sphere", "WHY IS THIS CABIN A PERFECT SPHERE?", "Why Are the Deepest Submarines Shaped Like Spheres?",
     """Why are the cabins of the deepest diving vehicles perfect spheres? Because a sphere is the strongest shape against pressure from all sides. In nineteen sixty, the bathyscaphe Trieste carried two men to the bottom of the Challenger Deep, almost eleven kilometres down. They sat inside a steel sphere about two metres across.""",
     "bathyscaphe Trieste")
sc("""At that depth, the pressure is more than one thousand times that at the surface. The walls of the Trieste's sphere were about thirteen centimetres thick. A long tube like a military submarine could never survive there. Only a sphere spreads the force evenly in every direction.""",
   "Trieste sphere", "A THOUSAND ATMOSPHERES")
sc("""The rest of the Trieste was a huge float filled with petrol, which is lighter than water and hard to compress. That is the same lesson as every submarine. The deeper you go, the simpler and stronger the shape must be, and the more you depend on the laws of physics, not on luck.""",
   "Challenger Deep", "PHYSICS, NOT LUCK")

# ---------- VERDICT ----------
sc("""So here are the ten. A round pressure hull with steel rings. A depth limit with a margin. Ballast tanks that blow out water. Trim tanks that keep perfect balance. Rubber tiles that swallow sound. Diving planes for underwater flight. Hidden propellers that stay quiet. Cameras instead of periscopes. Escape hatches for the worst day. And a perfect sphere for the deepest place on Earth.""",
   "submarine", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A submarine is a machine that fights the whole ocean, quietly. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments, would you dare to live on a submarine for three months?""",
   "submarine night", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video37", "title": "Why Don't Submarines Get Crushed?",
           "length_scale": 1.6, "scenes": S}, open("videos/video37/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
