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
sc("""In less time than it takes you to read this sentence, a Formula One team can lift a car, change all four tyres and send it back into the race. The record is one point eight seconds. That is not luck. Every tool in the pit box was designed for that number, from a gun that spins a nut in a blink to the lights that tell the driver to go. Today, ten parts of the F1 pit stop, and why each one exists.""",
   "Formula One pit stop", "1.8 SECONDS", cuts=8, chapter="Intro")
sc("""A pit stop is the only moment in a race when the car stands still, and every tenth of a second lost there is lost on the track. Gain one second in the pits, and you might jump a rival without overtaking him. So teams treat the stop like a sport inside the sport, with athletes, training and equipment that exists nowhere else.""",
   "Formula One pit crew", "A SPORT INSIDE THE SPORT")
sc("""As always, every fact here comes from a named source, the FIA, Formula One, Pirelli and motorsport references, all listed in the description. Let's start with the loudest tool in the pit lane.""",
   "Formula One pit lane", "WHY DOES THIS EXIST?")

# ---------- 1. WHEEL GUN ----------
part(1, "The wheel gun", "WHY IS THIS GUN SO FAST?", "Why Can an F1 Pit Stop Take Only 2 Seconds?",
     """Why can an F1 pit stop take only two seconds? Start with the wheel gun. It is a powerful air tool driven by high pressure gas, spinning at thousands of revolutions per minute. It removes the wheel nut in a fraction of a second, and tightens the new one just as fast. The gunner presses the trigger, and a switch on the gun tells the system when the nut is tight.""",
     "Formula One wheel gun")
sc("""Each gun is a precision tool, built specially for the teams, and every corner of the car has its gunner. They hold the gun against the nut before the car has even fully stopped. The gun switches direction automatically between loosening and tightening, so the gunner never has to look for a button. The whole job of the gunner is about two tenths of a second, repeated perfectly.""",
   "Formula One pit stop rear wheel", "TWO TENTHS OF A SECOND")
sc("""When something goes wrong, it is usually here. A nut that does not engage, a cross threaded thread, a gun that fails. Then the stop goes from two seconds to ten, and the race can be lost. That is why every crew has a spare gun ready at each corner, and why the gunners practise hundreds of stops every season.""",
   "Formula One pit stop crew practice", "TWO SECONDS OR TEN")

# ---------- 2. WHEEL NUT ----------
part(2, "The single wheel nut", "WHY IS THERE ONLY ONE NUT?", "Why Do F1 Wheels Have Only One Nut?",
     """Why does an F1 wheel have only one nut, when your car has four or five? Because removing five nuts would take five times longer. Racing cars use a centre lock wheel, one large nut in the middle holding the whole wheel onto a hub with pins that carry the torque. One nut means one movement of the gun, on and off.""",
     "Formula One wheel nut")
sc("""The nut stays inside the wheel. It is a captive nut, so it does not fall onto the floor when the wheel comes off, and the new wheel arrives with its own nut already in place. There is also a safety latch that holds the nut if it is not fully tight. A lost wheel at three hundred kilometres per hour is one of the most dangerous things in motorsport.""",
   "racing car centre lock wheel hub", "THE NUT NEVER FALLS")
sc("""That danger is also why the wheels are tied to the car with strong tethers, made of the same type of fibre used in bulletproof vests. If a crash breaks the suspension, the tethers keep the wheel from flying into the crowd or into another driver. The one nut is the speed. The tethers are the safety net behind it.""",
   "Formula One crash wheel", "THE SAFETY NET")

# ---------- 3. FRONT JACK ----------
part(3, "The front jack", "WHY DOES THIS JACK BEND?", "Why Does the F1 Front Jack Have a Hinge?",
     """Why does the front jack of an F1 pit crew look so strange? The car arrives at around eighty kilometres per hour in the pit lane and stops right in front of the jack man. He slides the jack under the nose, and pulls the long handle down to lift the front of the car in one move. Then the front of the jack swivels, so he can step to the side when the car leaves.""",
     "Formula One front jack")
sc("""The jack man is the bravest person in the pit crew. He stands directly in front of a car that is braking towards him, trusting the driver to stop on his marks. The jack is shaped to fit a specific point on the nose, so it cannot slip. At the back of the car, another jack man does the same with a rear jack, lifting the car from behind.""",
   "Formula One pit stop front jack man", "THE BRAVEST JOB")
sc("""Teams have also built quick release systems into the jacks, so that the car drops to the ground the instant the last wheel is on. Some even have a spare jack waiting at the side, in case the first one fails. Two seconds leaves no time to fix a broken tool. You simply grab the next one.""",
   "Formula One pit crew equipment", "ALWAYS A SPARE")

# ---------- 4. TYRE BLANKETS ----------
part(4, "The tyre blankets", "WHY ARE THESE TYRES WRAPPED IN BLANKETS?", "Why Are F1 Tyres Wrapped in Electric Blankets?",
     """Why are F1 tyres wrapped in blankets before they go on the car? Because cold racing tyres have almost no grip. These are electric heating blankets, and they warm the tyres for hours before they are fitted. A Formula One tyre only works in a narrow window of temperature. Cold, it slides like plastic. Warm, the rubber becomes sticky and grips the track.""",
     "Formula One tyre blankets")
sc("""For years, teams heated tyres to around one hundred degrees. Pirelli and the FIA have been reducing that limit, to around seventy degrees, to save energy and push tyre design forward. The blankets come off seconds before the car arrives, so the heat stays in the rubber. The driver leaves the pits with tyres that are ready to grip in the first corner.""",
   "Formula One tyres garage", "A NARROW WINDOW")
sc("""Without blankets, the first lap after a stop would be slow and dangerous, especially on a cold day. In other series that ban blankets, drivers often slide off the track on their out lap. That is why you see drivers weaving left and right behind the safety car. They are trying to put heat into the tyres when there is no blanket to do it.""",
   "Formula One safety car", "WHY DRIVERS WEAVE")

# ---------- 5. TYRE COLOURS ----------
part(5, "The coloured stripes", "WHY DO THESE TYRES HAVE COLOURS?", "Why Do F1 Tyres Have Coloured Stripes?",
     """Why do F1 tyres have red, yellow or white markings on the side? They tell everyone which rubber the car is using. Pirelli brings three dry compounds to every race. Red is the soft, the fastest but the quickest to wear out. Yellow is the medium. White is the hard, slower but longest lasting. For rain there are two more, green for intermediates and blue for full wets.""",
     "Pirelli Formula One tyres")
sc("""The colours are there for the fans and for the rivals. Under the rules, each car must use at least two different dry compounds in a dry race. So every team watches the colours on its rivals' cars and guesses their strategy. A car on red tyres will stop earlier. A car on white will go longer and attack at the end.""",
   "Formula One tyre compounds", "A STRATEGY YOU CAN SEE")
sc("""That rule is the hidden reason pit stops exist at all in modern Formula One, now that refuelling is banned. The car could perhaps finish on one set of hard tyres, but the rules make it stop at least once in a dry race. So the stop is not only about tyres. It is a chess move, and the colours are the pieces on the board.""",
   "Formula One pit stop tyres", "A CHESS MOVE")

# ---------- 6. SPEED LIMITER ----------
part(6, "The pit lane speed limiter", "WHY DO F1 CARS SLOW DOWN HERE?", "Why Do F1 Cars Crawl Through the Pit Lane?",
     """Why do F1 cars drive so slowly in the pit lane? There is a speed limit, usually eighty kilometres per hour, and lower on some tight tracks. Mechanics are standing in the lane, with no barrier between them and the cars. At the white line at the entrance, the driver presses a button on the steering wheel, and a limiter holds the car exactly at the speed limit.""",
     "Formula One pit lane entry")
sc("""The limit is checked electronically, and going even one kilometre per hour too fast earns a penalty. That is why drivers brake very late before the line and accelerate the instant they cross the exit line. Every metre of the pit lane is timed. Some tracks have long pit lanes, and a stop there costs twenty five seconds or more in total, even if the tyres change in two.""",
   "Formula One pit exit", "EVERY METRE IS TIMED")
sc("""Speed limits in the pit lane exist because of real accidents. In the past, cars entered at full speed and crew members were hurt. Today the pit lane is one of the safest places on the circuit, and the limiter is the reason. A machine built for three hundred kilometres per hour, crawling past people at a fixed speed, by rule.""",
   "Formula One pit lane mechanics", "SAFETY BY RULE")

# ---------- 7. RELEASE LIGHTS ----------
part(7, "The release lights", "WHY IS THERE A TRAFFIC LIGHT IN THE PIT BOX?", "Why Do F1 Teams Use a Traffic Light in the Pits?",
     """Why is there a traffic light hanging over the pit box? It tells the driver when to go. Each wheel crew presses a button when its wheel is done. When all four signals are in and the lane is clear, the light turns green. Before these systems, a man held a sign on a stick in front of the driver, called the lollipop, and lifted it when the stop was finished.""",
     "Formula One pit stop lights")
sc("""Lights are faster than any human reaction, and every hundredth of a second counts. But they made a famous mistake. At the Singapore Grand Prix of two thousand eight, Felipe Massa's Ferrari got the signal to go while the fuel hose was still attached. He drove off dragging the hose down the pit lane, and his race was ruined.""",
   "Felipe Massa Ferrari 2008", "THE HOSE STAYED ON")
sc("""Releasing a car into the path of another one is called an unsafe release, and it brings a penalty. Some teams have a person who watches the lane and can stop the release. The traffic light is fast, but the final decision often still depends on one person looking at the pit lane, ready to keep the driver waiting.""",
   "Formula One pit lane cars", "FAST, BUT WATCHED")

# ---------- 8. FUEL HOSE ----------
part(8, "The missing fuel hose", "WHY DON'T F1 CARS REFUEL ANYMORE?", "Why Did F1 Ban Refuelling?",
     """Why don't F1 cars refuel during the race anymore? Refuelling was banned from twenty ten. Before that, from nineteen ninety-four to two thousand nine, pit stops included a giant fuel hose, pushing around twelve litres per second into the car. A stop took seven or eight seconds, and the fuel decided the strategy.""",
     "Formula One refuelling 2000s")
sc("""It was dangerous. In nineteen ninety-four, at Hockenheim, fuel sprayed over Jos Verstappen's Benetton during a stop and caught fire. The car and crew were engulfed in flames for several seconds. The crew survived, with minor burns. There were other fires over the years, and hoses that stayed connected, like Massa's in Singapore.""",
   "Benetton 1994", "A FIREBALL IN THE PITS")
sc("""The ban was also about cost and racing. Carrying heavy equipment around the world was expensive, and many overtakes happened in the pits instead of on track. Today, F1 cars start the race with all the fuel they need for the whole distance. That is why tyre changes became so fast. There is nothing else left to wait for.""",
   "Formula One race start", "NOTHING LEFT TO WAIT FOR")

# ---------- 9. THE CREW ----------
part(9, "The pit crew", "WHY DOES ONE CAR NEED 20 PEOPLE?", "Why Does an F1 Pit Stop Need 20 People?",
     """Why does one F1 pit stop need about twenty people? Because each person does only one tiny job. At each wheel there are three, a gunner, one to pull the old wheel off and one to put the new wheel on. Then two jack men, people holding the car steady, someone for the front wing, and the person watching the release. Nobody does two things.""",
     "Formula One pit crew stop")
sc("""Most of them are not full time pit crew. They are mechanics who build and fix the car all weekend, and switch to their pit stop roles during the race. They train like athletes, with fitness programs and hundreds of practice stops at the factory, measured with sensors and video. A tenth of a second is found in the position of a foot.""",
   "Formula One mechanics garage", "MECHANICS, THEN ATHLETES")
sc("""The fastest stop ever recorded in Formula One was one point eight seconds, by McLaren for Lando Norris at the Qatar Grand Prix of twenty twenty-three. Before that, Red Bull held the record with one point eight two seconds. These are not lucky stops. They are the result of twenty people moving as one machine.""",
   "McLaren Formula One pit stop", "20 PEOPLE, ONE MACHINE")

# ---------- 10. PIT BOARD ----------
part(10, "The pit board", "WHY DO TEAMS STILL USE THIS BOARD?", "Why Do F1 Teams Still Hold Up a Pit Board?",
     """Why do F1 teams still hold out a sign board on the pit wall, when drivers have a radio? Because radios fail. The pit board shows the driver his position, the gap to the cars around him and the laps remaining. It is the oldest communication tool in racing, and it works when everything else does not.""",
     "Formula One pit board")
sc("""Radio problems are common in Formula One. Interference, broken connectors, or simply a driver who cannot hear over the engine. When that happens, the pit board is the only way to tell him to come in for tyres.""",
   "Formula One pit wall", "WHEN THE RADIO FAILS")
sc("""Think about it the next time you see a stop. A board from the nineteen fifties, a gun spinning at thousands of revolutions, electric blankets, traffic lights and twenty people moving as one. A two second pit stop is the most practised two seconds in all of sport.""",
   "Formula One pit stop night", "THE MOST PRACTISED 2 SECONDS")

# ---------- VERDICT ----------
sc("""So here are the ten. A wheel gun that works in a blink. One nut instead of five. A jack that swivels away. Blankets that heat the tyres, colours that show the strategy, a speed limiter that protects the crew, lights that release the car, a fuel hose that was banned, twenty people with one job each, and a board that works when the radio does not.""",
   "Formula One pit stop", "10 PARTS. 10 REASONS.", chapter="The verdict", cuts=6)
sc("""A pit stop looks like chaos, but it is one of the most designed moments in sport. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "Formula One car pit lane", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
    1: ("File:Formula One Wheel Gun.jpg", 0.5, 0.45),
    2: ("File:Williams FW35 front wheel 2013 Malaysia.jpg", 0.48, 0.5),
    3: ("File:Alonso Renault Pitstop Chinese GP 2008.jpg", 0.86, 0.55),
    4: ("File:Tyre warmer 2005 United States GP (19890682).jpg", 0.45, 0.6),
    5: ("File:Pirelli P Zero Formula 1 Medium Slick Tyre 2026.jpg", 0.85, 0.5),
    6: ("File:Toyota steering wheel 1.jpg", 0.29, 0.33),
    7: ("File:Kimi Raikkonen 2017 United States GP (37946719176).jpg", 0.66, 0.35),
    8: ("File:Fale F1 Monza 2004 77.jpg", 0.37, 0.65),
    9: ("File:Massa Ferrari Pitstop Chinese GP 2008.jpg", 0.5, 0.45),
    10: ("File:Istanbul park kubica pit wall.JPG", 0.52, 0.5),
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video23", "title": "Why Can an F1 Pit Stop Take Only 2 Seconds?",
           "length_scale": 1.6, "scenes": S}, open("videos/video23/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
