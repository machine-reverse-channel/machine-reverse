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
sc("""In nineteen forty one, German soldiers met a Soviet tank their guns could barely hurt. Its armor was not especially thick. But it was tilted, slanted back at a steep angle, and shells that should have gone through bounced off. That tank was the T thirty four, and its sloped armor changed tank design for decades. Today, eleven parts of a tank, and why each one exists, starting with that angle.""",
   "T-34 tank", "WHY IS IT SLANTED?", cuts=8, chapter="Intro")
sc("""A tank is a balance of three things that fight each other. Protection, firepower and mobility. More armor means more weight, and more weight means slower speed, more fuel, and bridges that cannot carry it. So every part of a tank is a trick to get more protection without carrying more steel.""",
   "M1 Abrams", "THE IRON TRIANGLE")
sc("""As always, every fact comes from a named source, military history references, army publications, and museum archives, all listed in the description. Let's start with the slanted plate on the front.""",
   "tank glacis plate", "WHY DOES THIS EXIST?")

# ---------- 1. GLACIS ----------
part(1, "The slanted front plate", "WHY IS THIS ARMOR SLANTED?", "Why Is Tank Armor Slanted?",
     """Why is the front armor of a tank tilted back? Because a shell hitting a slanted plate has to travel through more steel. Imagine a plate tilted at sixty degrees. A shell flying straight at it crosses a path about twice as long as the plate is thick. So a plate forty five millimeters thick can act like one of about ninety, without weighing more.""",
     "T-34 tank")
sc("""There is a second effect. A shell that hits at a steep angle may not bite into the steel at all. It can skid along the surface and fly off, which tankers call a ricochet. The T thirty four's front plate was slanted at sixty degrees from vertical, and many early German shells simply bounced.""",
   "T-34 tank", "THE RICOCHET")
sc("""The Germans learned fast. Their Panther tank, built from nineteen forty three, copied the idea with a thick front plate sloped at fifty five degrees. After the war, almost every tank in the world had a slanted front. The angle was free protection, paid for only with a little interior space.""",
   "Panther tank glacis", "COPIED BY EVERYONE")

# ---------- 2. WEDGES ----------
part(2, "The wedge on the turret", "WHY DOES THIS TURRET HAVE A WEDGE?", "Why Do Modern Tank Turrets Have Wedges?",
     """Why do some modern tanks, like later versions of the Leopard two, have pointed wedges on the front of the turret? Because they are extra armor, mounted in front of the main armor with a gap behind them. A shell or missile hits the wedge first, at a steep angle, and part of its energy is spent or deflected before it reaches the real armor.""",
     "Leopard 2 tank")
sc("""Modern tank shells are long, thin darts of very dense metal, fired at more than a kilometer and a half per second. Against these, slope helps less than it did in the nineteen forties, because a dart tends to turn into the plate instead of bouncing off. So designers combine slope with spaced layers and special materials.""",
   "Leopard 2 tank", "DARTS AT 1.5 KM/S")
sc("""The wedge is also a modular part. When better armor is developed, the wedge can be removed and replaced without rebuilding the whole tank. Modern armor is designed to be upgraded, like software, one module at a time.""",
   "Leopard 2 tank", "ARMOR YOU CAN UPGRADE")

# ---------- 3. COMPOSITE ----------
part(3, "The secret layers inside", "WHY IS THIS ARMOR KEPT SECRET?", "Why Is Modern Tank Armor Kept Secret?",
     """Why can no one tell you exactly what is inside the armor of a modern tank? Because it is not just steel. In the nineteen sixties and seventies, British researchers developed a new kind of armor, later known as Chobham armor. It uses layers of different materials, such as ceramics and metals, packed together. Each layer breaks or slows the attacker in a different way.""",
     "M1 Abrams")
sc("""Ceramics are very hard. They shatter the tip of an incoming dart or disrupt the jet of a missile warhead. The metal layers behind catch the fragments. Together, they stop much more than the same weight of plain steel. The American M one Abrams and the British Challenger were built around this idea.""",
   "Chobham armour", "HARDER THAN STEEL")
sc("""The exact recipe is still classified. Later versions of the Abrams were reported to add depleted uranium, a very dense metal, inside the armor. The boxy, flat-sided look of modern tanks comes from this. Composite armor works best in thick flat packs, so the turret became a big box.""",
   "M1 Abrams", "STILL CLASSIFIED")

# ---------- 4. ERA ----------
part(4, "The bricks that explode", "WHY ARE THERE EXPLODING BRICKS ON THIS TANK?", "Why Do Tanks Wear Bricks That Explode?",
     """Why are some tanks covered in boxes full of explosive? Because these boxes destroy the weapon before it reaches the tank. They are called explosive reactive armor. Many anti tank missiles use a shaped charge, which turns a metal cone into a jet of metal moving at several kilometers per second, able to punch through thick steel.""",
     "explosive reactive armour")
sc("""When that jet hits a reactive armor brick, the explosive inside goes off and throws a steel plate outward, across the path of the jet. The moving plate keeps cutting into the jet and breaks it up, so much less of it reaches the main armor. Israel first used it in combat in Lebanon in nineteen eighty two, and the Soviet Union soon followed.""",
   "reactive armour", "BREAKING THE JET")
sc("""It comes with a cost. A brick that explodes is gone, leaving a gap, and the blast is dangerous to soldiers walking next to the tank. Newer types are also designed to work against the darts fired by enemy tanks, not only against missiles.""",
   "explosive reactive armour", "ONE USE ONLY")

# ---------- 5. SLAT ----------
part(5, "The cage around the tank", "WHY IS THIS TANK IN A CAGE?", "Why Do Some Tanks Wear Metal Cages?",
     """Why do some armored vehicles have a cage of metal bars around them? Because it is a cheap shield against rocket propelled grenades. The bars are spaced so that the warhead of an RPG gets caught between them. Its nose can be crushed or its fuze short circuited, so it fails to go off properly, or it explodes far enough away from the armor to do less damage.""",
     "slat armour")
sc("""Slat armor does not stop every hit. Studies and military reports suggest it defeats roughly half of the grenades that strike it. But it is light, cheap, and quick to bolt on, so armies used it widely in Iraq and Afghanistan, on trucks and armored vehicles that could not carry heavy armor.""",
   "slat armour", "ABOUT HALF")
sc("""In recent wars, soldiers have added cages on top of turrets too, against drones that drop explosives from above. People sometimes laugh at them. But the logic is the same as the slanted plate in nineteen forty one. Find a cheap trick that makes the attacker fail.""",
   "tank turret", "CAGES AGAINST DRONES")

# ---------- 6. BLOWOUT PANELS ----------
part(6, "The roof panels that blow off", "WHY DOES THIS ROOF BLOW OFF ON PURPOSE?", "Why Are Tank Roofs Designed to Blow Off?",
     """Why does the M one Abrams have panels on its turret roof designed to blow off? Because the most dangerous thing in a tank is its own ammunition. If a hit sets the shells on fire, they can explode inside. On the Abrams, the main ammunition sits in a compartment at the back of the turret, behind sliding armored doors, separated from the crew.""",
     "M1 Abrams")
sc("""If that ammunition explodes, the blast takes the easiest way out. The roof panels above it are made weaker on purpose, so they blow off and send the explosion and fire upward, away from the crew. The tank may be destroyed, but the people inside have a chance to get out alive.""",
   "M1 Abrams", "BLOW OUT, NOT IN")
sc("""Tanks that store ammunition around the crew, without this separation, have suffered badly. Photos from recent wars show turrets thrown meters into the air when the ammunition below them exploded. The blowout panel is a simple idea: if something must explode, choose where.""",
   "tank turret", "CHOOSE WHERE IT EXPLODES")

# ---------- 7. ENGINE IN FRONT ----------
part(7, "The engine in the front", "WHY IS THIS TANK'S ENGINE IN THE FRONT?", "Why Does the Merkava Tank Put Its Engine in Front?",
     """Why does Israel's Merkava tank have its engine in the front, when most tanks have it at the back? Because the engine is a big block of steel that can stop shells too. Israel designed the Merkava with one priority above all, survival of the crew. Putting the engine in front means anything that hits the front must go through the engine before it can reach the people.""",
     "Merkava tank")
sc("""It also frees the back of the tank. The Merkava has a door at the rear, so the crew can get in and out under cover, away from enemy fire. That space can even carry wounded soldiers or extra infantry in an emergency, something few other battle tanks can do.""",
   "Merkava tank", "A DOOR AT THE BACK")
sc("""The engine is not perfect armor, and a damaged engine leaves the tank stuck. But a tank can be repaired, and a trained crew is much harder to replace. In the Merkava, the whole layout of the machine says one thing. The people matter most.""",
   "Merkava tank", "THE PEOPLE MATTER MOST")

# ---------- 8. PERISCOPES ----------
part(8, "The periscopes", "WHY DOES THE CREW LOOK THROUGH THESE?", "Why Do Tank Crews See Through Periscopes?",
     """Why do tank crews look out through small periscopes instead of windows? Because a window is a hole in the armor. Periscopes bend the light with mirrors or prisms, so the glass that the enemy can hit is outside, and the crew's eyes stay below the armor. If the outer glass is shattered, the periscope can be swapped, and no bullet comes straight in.""",
     "tank periscope")
sc("""The weakness is that a tank crew sees very little. Old tanks had narrow vision slits, and commanders often stood up with their head out of the hatch to see better, which made them targets. Modern tanks use thermal cameras and sights that show the world on screens, even at night or through smoke.""",
   "tank turret", "HEAD OUT OF THE HATCH")
sc("""Some new designs even use cameras around the whole tank, letting the crew look through the armor in any direction on a headset. But even the most modern tanks still keep simple periscopes as backup. When the electronics fail, glass and mirrors still work.""",
   "tank periscope", "GLASS STILL WORKS")

# ---------- 9. SMOKE ----------
part(9, "The tubes on the turret", "WHY ARE THERE TUBES ON THIS TURRET?", "Why Do Tanks Have Tubes on the Turret?",
     """What are those small tubes on the sides of a tank's turret? They are smoke grenade launchers. When the crew sees a threat, like a missile being fired or a laser pointing at the tank, they can fire a wall of smoke in front of the tank in seconds. Then the tank can back away or move, hidden behind the cloud.""",
     "tank smoke grenade launcher")
sc("""Modern smoke does more than block normal sight. Some types also block infrared and thermal cameras, and the lasers that guide some missiles. Many tanks carry laser warning sensors that can fire the smoke automatically, faster than a human could react.""",
   "tank smoke grenade launcher", "AUTOMATIC SMOKE")
sc("""It is the oldest form of defense on the battlefield, if they cannot see you, they cannot hit you, done in a modern way. A few kilograms of smoke can protect a tank of sixty tonnes as well as a meter of steel, for a few precious seconds.""",
   "main battle tank", "IF THEY CANNOT SEE YOU")

# ---------- 10. TRACKS ----------
part(10, "The wide tracks", "WHY ARE THESE TRACKS SO WIDE?", "Why Do Tanks Use Tracks Instead of Wheels?",
     """Why do tanks run on wide tracks instead of wheels? Because a tank weighs as much as forty cars, and wheels would sink into mud, sand or snow. A track spreads that weight over a long, wide strip of ground. A modern main battle tank presses on the ground with about the same pressure as a person walking, despite weighing sixty tonnes.""",
     "tank track")
sc("""The T thirty four had unusually wide tracks for its time, and in the mud of the Russian autumn, that gave it a big advantage over tanks with narrow tracks. Tracks also let a tank turn on the spot, by moving one side forward and the other side backward.""",
   "T-34 tank", "BUILT FOR MUD")
sc("""The price is wear and maintenance. Tracks are heavy, they can break or be thrown off in tight turns, and crews spend hours fixing them. But no wheeled vehicle can carry that much armor across that much bad ground.""",
   "tank track", "HOURS OF REPAIRS")

# ---------- 11. ACTIVE PROTECTION ----------
part(11, "The radar that shoots back", "WHY DOES THIS TANK SHOOT DOWN MISSILES?", "Why Can Some Tanks Shoot Down Missiles?",
     """Why do some tanks carry small radar panels on their turret? Because they can shoot down incoming missiles. They are part of an active protection system. The radar detects a rocket or missile flying toward the tank, a computer calculates its path, and a launcher fires a burst that destroys or deflects it a few meters before it hits.""",
     "Merkava tank")
sc("""Israel's Trophy system, mounted on the Merkava, made the first combat interception in two thousand eleven, near Gaza, stopping an anti tank missile. Since then, it has been fitted to some American Abrams and German Leopard tanks too. The whole sequence takes a fraction of a second.""",
   "Merkava tank", "TROPHY, 2011")
sc("""It is a big change in thinking. For a century, tanks survived by being hard to break. Now they also survive by not being hit at all. Slope, layers, bricks, cages and radar, every generation added a new layer of defense, and each one exists because the weapons got better too.""",
   "main battle tank", "NOT BEING HIT AT ALL")

# ---------- VERDICT ----------
sc("""So here are the eleven. A slanted front plate, a wedge on the turret, and secret layers inside. Bricks that explode, a cage of bars, and roof panels that blow off on purpose. An engine in the front, periscopes instead of windows, tubes that fire smoke, wide tracks for the mud, and a radar that shoots back.""",
   "main battle tank", "11 PARTS. 60 TONNES.", chapter="The verdict", cuts=6)
sc("""A tank looks like a simple block of steel, but every angle on it is a calculation. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "main battle tank", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:T-34-85 Tank at the Imperial War Museum.jpg", 0.25, 0.58),
    2: ("File:Leopard 2 A7.JPG", 0.38, 0.5),
    3: ("File:M1 Abrams Turret Bustle Side Special Armor.png", 0.88, 0.6),
    4: ("File:IDET2007 reactive armor DYNA.jpg", 0.3, 0.4),
    5: ("File:Slat armour on the Stridsvagn 103C at the Swedish Army Museum September 2015.jpg", 0.5, 0.4),
    6: ("File:M1 Abrams noBG.jpg", 0.68, 0.3),
    7: ("File:Merkava-1-batey-haosef-1.jpg", 0.5, 0.7),
    8: ("File:JGSDF Type 61 Tank periscope at Camp Imazu November 9, 2014.jpg", 0.45, 0.5),
    9: ("File:Leopard 2A6 Kokonaisturvallisuus 2015 03 smoke grenade launchers.JPG", 0.62, 0.4),
    10: ("File:Kette T-34 85 IWM.jpg", 0.75, 0.45),
    11: ("File:NGP 6692.jpg", 0.47, 0.38),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video54", "title": "Why Is Tank Armor Slanted?",
           "length_scale": 1.6, "scenes": S}, open("videos/video54/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
