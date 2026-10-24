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
sc("""Look at any modern Formula One car and you will see a curved bar rising over the driver's head. When it first appeared, in twenty eighteen, many fans hated it. They called it ugly, and said it ruined the look of the cars. Then it started saving lives, and the criticism mostly stopped. It is called the halo, and it is one of the most important safety parts ever added to a racing car. Today, ten parts of the halo story, and why each one exists.""",
   "Formula One halo cockpit", "WHY IS THERE A BAR OVER THE HEAD?", cuts=8, chapter="Intro")
sc("""The halo weighs about seven kilograms and must stand up to loads equal to a bus sitting on top of it. And it was not made to stop crashes, but to stop one particular thing, a flying object hitting the driver's head. Let's see how it works.""",
   "Formula One halo driver", "BUILT FOR ONE THING")
sc("""As always, every fact here comes from a named source, motorsport reports and reference works, all listed in the description. Let's start with the bar itself.""",
   "Formula One halo close up", "WHY DOES THIS EXIST?")

# ---------- 1. THE HALO ----------
part(1, "The bar over the head", "WHY IS THERE A BAR OVER THE DRIVER'S HEAD?", "Why Is There a Bar Over Every F1 Driver's Head?",
     """Why is there a bar over every Formula One driver's head? It is the halo, a curved bar of titanium that protects the driver's head in a crash. It was introduced in twenty eighteen. Formula One cars have open cockpits, with the driver's head sitting out in the air, and for decades, nothing protected it from flying wheels or other loose parts.""",
     "Formula One halo")
sc("""The halo does not close the cockpit. The driver can still get out quickly, and can still see. It is a bar in front and two arms that go back on the sides, as a frame around the head. The idea was to add the protection of a roof, without the risk of a closed car.""",
   "Formula One halo frame", "A FRAME, NOT A ROOF")
sc("""So when you see the halo, you are looking at a very simple idea. A strong bar, in the place where something would hit the driver, in the shape that stops it, without blocking the view too much.""",
   "Formula One cockpit halo view", "A SIMPLE IDEA")

# ---------- 2. TITANIUM ----------
part(2, "The titanium tube", "WHY IS THE HALO MADE OF TITANIUM?", "Why Is the F1 Halo Made of Titanium?",
     """Why is the halo made of titanium? Because titanium is strong and light. The halo is made from a single piece of titanium tubing, in a grade called Ti-6Al-4V, and weighs about seven kilograms. A steel bar strong enough would be much heavier, and every kilogram on a racing car changes the way it handles.""",
     "Formula One halo titanium")
sc("""The halo sits high on the car, at the very top, so its weight matters even more. A heavy part high up would raise the center of gravity of the car, and make it harder to handle in corners. Titanium gives the strength with a lot less weight.""",
   "Formula One halo weight", "STRONG AND LIGHT")
sc("""And because it is one piece of tube, there are no weak welds in the main body of the bar. The material, the shape and the weight were all chosen together. The bar that you see is the result of many tests.""",
   "titanium tube halo manufacturing", "ONE PIECE OF TUBE")

# ---------- 3. THE 125 KN TEST ----------
part(3, "The load test", "WHY DOES THE HALO NEED TO HOLD A BUS?", "How Strong Is the F1 Halo?",
     """How strong is the halo? In the official test, it has to withstand a force of one hundred twenty-five kilonewtons from above, for five seconds. That is roughly the weight of twelve tonnes, about the weight of a London bus. And it must do this without breaking, or letting the bar touch the driver's head.""",
     "Formula One halo load test")
sc("""The test loads are higher than those of the main roll bar, so the halo acts as a second, forward roll structure. In a rollover, the halo is stronger than the roll hoop behind the driver. That was a surprise to many people, who thought it was only a shield.""",
   "Formula One halo roll structure", "STRONGER THAN THE ROLL HOOP")
sc("""It is hard to picture twelve tonnes sitting on a bar of tubing you could hold with two hands. But that is the design, and each halo is built to pass the same test. If it fails, the car does not race.""",
   "Formula One halo crash test", "A BUS ON A BAR")

# ---------- 4. SIDE AND ROLLOVER ----------
part(4, "The side and rollover tests", "WHY IS THE HALO TESTED FROM SEVERAL ANGLES?", "Why Is the F1 Halo Tested From Several Directions?",
     """Why is the halo tested from several directions? Because crashes come from different angles. The front load is one hundred twenty-five kilonewtons. A side load of ninety-three kilonewtons is applied from the side to simulate a wheel impact, and a rollover load of one hundred sixteen kilonewtons is applied to the top. The halo has to survive all three.""",
     "Formula One halo tests")
sc("""A car can flip, slide or be hit from the side by another car, and each of those loads goes through the halo in a different way. By testing them separately, the FIA makes sure it works in a real accident, and not only in one situation.""",
   "Formula One crash test halo angles", "THREE KINDS OF CRASH")
sc("""These numbers are what the engineers must prove before a halo can be used. Safety in racing is built from numbers like these, written in rules, after real accidents.""",
   "FIA crash test Formula One", "NUMBERS FROM REAL ACCIDENTS")

# ---------- 5. THE WHEEL ----------
part(5, "The flying wheel", "WHY IS THE HALO BUILT TO STOP A WHEEL?", "What Is the F1 Halo Built to Stop?",
     """What is the halo built to stop? The biggest danger is a loose wheel. The halo is designed to stop a twenty kilogram Formula One wheel, traveling at about one hundred forty miles an hour, from hitting the driver. In an open cockpit, a wheel that comes off another car in a crash can fly through the air and hit a head.""",
     "Formula One wheel flying crash")
sc("""Wheels are tied to the car by cables, but they can still come loose in a big crash. And a wheel is heavy and fast. A twenty kilogram wheel at that speed carries enough energy to cause fatal injuries, which is why the test uses it.""",
   "Formula One wheel tether crash", "A 20 KG WHEEL AT 140 MPH")
sc("""So the shape of the halo was designed around this one danger. It is not a rain guard or a roll bar. It is a barrier, in the exact place a wheel would come from.""",
   "Formula One wheel halo barrier", "A BARRIER FOR A WHEEL")

# ---------- 6. MOUNTING ----------
part(6, "The mounting points", "WHY IS THE HALO BOLTED TO THE CORE OF THE CAR?", "How Is the F1 Halo Attached to the Car?",
     """How is the halo attached to the car? It is bolted straight to the survival cell, the strong carbon fiber shell around the driver, with reinforced mounting points. A bar that strong is only useful if it is held by something just as strong. So the force from a hit goes through the halo, and into the structure that protects the driver.""",
     "Formula One halo mounting survival cell")
sc("""If the halo were attached only to the bodywork, it would tear off in an impact. The survival cell is the part of the car designed to stay in one piece, so the halo and the cell work together as one protective frame.""",
   "Formula One survival cell halo attachment", "ONE FRAME")
sc("""The mounting points are reinforced, to carry the load of the tests. It is the least visible part of the halo, and it is one of the most important. A strong bar on weak bolts would be useless.""",
   "Formula One halo bolts", "A STRONG BAR NEEDS STRONG BOLTS")

# ---------- 7. WHY IT WAS NEEDED ----------
part(7, "The accidents that led to it", "WHY DID F1 NEED A BAR AFTER ALL THESE YEARS?", "Why Did Formula One Add the Halo?",
     """Why did Formula One add the halo? Because of accidents. In two thousand nine, Henry Surtees was killed in a Formula Two race after he was hit by a wheel. In the same year, Felipe Massa was seriously injured when a suspension spring hit his helmet. Both accidents showed the same weak point, the driver's head in an open cockpit.""",
     "Formula One accident open cockpit")
sc("""For years, the sport debated what to do. Different ideas were tried, including shields, and some were rejected because of how they affected the view or how a driver could escape. The halo was chosen because it gave strong protection with a clear view.""",
   "Formula One cockpit protection tests", "YEARS OF DEBATE")
sc("""Racing has a long history of safety changes coming after tragedies. The halo was one of the few that tried to come before the next one.""",
   "Formula One safety history", "BEFORE THE NEXT ONE")

# ---------- 8. ALONSO TEST ----------
part(8, "The roll that tested it", "WHY DID A CRASH IN AUSTRALIA MATTER FOR THE HALO?", "How Did Engineers Test the Halo Against Real Crashes?",
     """How did engineers test the halo against real crashes? They recreated accidents on a computer. One of them was Fernando Alonso's roll at the two thousand sixteen Australian Grand Prix, which was used in testing. The recreations found no case where the halo made things significantly less safe, which was a worry people had before it was introduced.""",
     "Formula One Alonso crash Australia 2016")
sc("""The worries were fair. A bar in front of the driver could block the view, make it harder to leave the car, or even get in the way of rescuers. So the testing was not only about the bar being strong, but also about it not creating new problems.""",
   "Formula One halo escape test", "WOULD IT CREATE NEW PROBLEMS?")
sc("""The drivers were tested too. They had to prove that they could get out of the car in a few seconds with the halo in place. A safety part is only useful if it does not trap the person it protects.""",
   "Formula One driver exit cockpit", "CAN THE DRIVER STILL ESCAPE?")

# ---------- 9. GROSJEAN ----------
part(9, "The Bahrain crash", "WHY DID THIS CAR SPLIT IN TWO?", "How Did the Halo Help in the Grosjean Crash?",
     """How did the halo help in Romain Grosjean's crash? At the two thousand twenty Bahrain Grand Prix, his Haas car went through the safety barrier and split in two. He got out of the burning car and was taken by helicopter to the hospital. His injuries were second-degree burns to his hands, and nothing worse. Simulations by the FIA reportedly showed the crash would have been fatal without the halo.""",
     "Romain Grosjean crash Bahrain 2020 halo")
sc("""The car hit the barrier at high speed, and the halo took part of the impact on the top of the driver's head. Mixed with the strong survival cell, the fire-resistant suit and the quick work of the rescue team, he walked away. It was the moment that changed the mind of many critics.""",
   "Formula One Bahrain 2020 rescue", "THE MOMENT THAT CHANGED MINDS")
sc("""Nobody can say for sure what would have happened without it. But for many people in the sport, this was the clearest proof that the halo was worth its looks.""",
   "Formula One halo Grosjean", "WORTH ITS LOOKS")

# ---------- 10. LOOKS ----------
part(10, "The ugly bar", "WHY DID EVERYONE HATE THE HALO AT FIRST?", "Why Did Fans Hate the F1 Halo at First?",
     """Why did fans hate the halo at first? Because of the way it looked. It broke the clean lines of open-cockpit cars, which many people thought were the heart of Formula One. And it appeared in twenty eighteen on every car, with no choice. For a sport that is built around image, it was a big change.""",
     "Formula One halo 2018 introduction")
sc("""But a few seasons later, most people had stopped noticing it. Drivers said they hardly saw it while driving, and fans got used to the look. Safety, in the end, mattered more than the shape.""",
   "Formula One car with halo", "WE STOPPED NOTICING")
sc("""And that is the story of the halo. A part that nobody wanted to look at, and many drivers are glad is there. A bar over the head that says, in plain titanium, that the sport values the people inside the cars.""",
   "Formula One halo driver safety", "A BAR THAT SAYS: WE CARE")

# ---------- VERDICT ----------
sc("""So here are the ten. A bar over the head, made of titanium tube, built to hold twelve tonnes. Tests from the front, the side and above, a wheel it must stop, bolts that tie it to the core of the car, and the accidents that made it necessary. And a crash in Bahrain that ended the arguments.""",
   "Formula One halo sunset", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""Next time you see the halo on a Formula One car, you will know what it is made of, and what it is there to stop. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Formula One halo race", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video20", "title": "Why Is There a Bar Over Every F1 Driver's Head?",
           "length_scale": 1.6, "scenes": S}, open("videos/video20/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
