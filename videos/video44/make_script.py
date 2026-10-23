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
sc("""A train has no steering wheel. Its wheels are fixed to a solid steel axle, so both wheels always turn at exactly the same speed. And yet a train can go around a curve at three hundred kilometers an hour without grinding itself apart. The secret is a shape most people never notice. Train wheels are not flat cylinders. They are cones. Today, ten parts of a railway, and why each one exists.""",
   "railway wheelset", "NO STEERING WHEEL", cuts=8, chapter="Intro")
sc("""Railways are almost two hundred years old, and most of their important parts were invented in the eighteen hundreds, often after an accident. The wheels, the rails, the couplers and the brakes all look simple, even boring. But each one hides a clever solution to a problem that once killed people or destroyed trains.""",
   "steam locomotive wheels", "SIMPLE, NOT BORING")
sc("""As always, every fact comes from a named source, railway engineering references, accident investigations, and railway history, all listed in the description. Let's start with the shape of the wheel.""",
   "train wheel profile", "WHY DOES THIS EXIST?")

# ---------- 1. CONE ----------
part(1, "The cone-shaped wheel", "WHY ARE TRAIN WHEELS SHAPED LIKE CONES?", "Why Are Train Wheels Shaped Like Cones?",
     """Why are train wheels shaped like cones? Look closely at the surface that touches the rail. It is not flat. It is slightly tapered, wider near the inside of the wheel and narrower toward the outside. When a train enters a curve, the wheelset shifts a little toward the outside of the curve. Now the outer wheel rides on its wider part, and the inner wheel rides on its narrower part.""",
     "railway wheel conical tread")
sc("""A wider circle covers more distance in one turn. So the outer wheel travels farther than the inner wheel, even though both turn at the same speed. That is exactly what you need in a curve, where the outer rail is longer. The wheelset steers itself. The physicist Richard Feynman loved this example, because it is pure geometry doing the work of a steering system.""",
   "railway curve train", "GEOMETRY STEERS")
sc("""On a straight track, the cone also keeps the wheelset centered. If it drifts to one side, that wheel gets bigger, and it rolls back toward the middle. You can test this at home with two paper cups taped together at their wide ends. Roll them on two parallel rulers, and they stay on. Tape them at the narrow ends, and they fall off immediately.""",
   "two paper cups", "TRY IT WITH 2 CUPS")

# ---------- 2. FLANGE ----------
part(2, "The flange", "WHY ISN'T THIS LIP WHAT KEEPS TRAINS ON?", "Why Isn't the Flange What Keeps a Train on the Rails?",
     """Why does every train wheel have a lip on the inside? It is called the flange, and most people think it is what keeps the train on the rails. Actually, in normal running, the flange is a backup. The cone shape does most of the steering, and on a good straight track, the flange rarely touches the rail. It is there for sharp curves, switches, and the moments when the cone is not enough.""",
     "train wheel flange")
sc("""When the flange does rub the rail, on very tight curves, you hear it. That high pitched screech of a subway train in a curve is often the flange grinding against the rail, or the wheels slipping because the solid axle cannot adjust enough. Some railways put grease on the rails in tight curves, using machines called flange lubricators, to reduce wear and noise.""",
   "wheel flange lubricator", "THE SCREECH")
sc("""The flange is always on the inside of the rails, never the outside. That way, the two flanges trap the rails between them, and a switch can guide the train by pushing on one flange. If you ever see a toy train with flanges on the outside, it was designed by someone who never looked under a real one.""",
   "railway switch points frog", "ALWAYS ON THE INSIDE")

# ---------- 3. SOLID AXLE ----------
part(3, "The solid axle", "WHY CAN'T THESE WHEELS TURN SEPARATELY?", "Why Do Train Wheels Turn Together on One Axle?",
     """Why are both wheels of a train fixed to one solid axle? A car has a differential, a set of gears that lets the outer wheel spin faster in a curve. Trains do not need one, because the cone shape already solves the problem. A solid axle is simple, very strong, and it keeps the two wheels perfectly aligned. On a machine that carries thousands of tons, simple and strong wins.""",
     "railway wheelset")
sc("""But the cone has a side effect. At high speed, the self-centering motion can overshoot. The wheelset swings to one side, gets pushed back, overshoots to the other side, and starts swaying left and right in a wave. This is called hunting oscillation, and it was described in the eighteen eighties. At high speed, it can become violent and even damage the track.""",
   "high speed train bogie", "HUNTING")
sc("""Engineers fight hunting with careful wheel shapes, stiff connections between the wheelsets and the bogie, and special shock absorbers called yaw dampers. High speed trains are designed and tested to stay stable well above their top speed. The same cone that steers the train can shake it apart, so the engineering is all about keeping the cone calm.""",
   "yaw damper train bogie", "KEEP THE CONE CALM")

# ---------- 4. RAIL CANT ----------
part(4, "The tilted rail", "WHY ARE THESE RAILS LEANING INWARD?", "Why Do Railway Rails Lean Inward?",
     """Why are railway rails tilted slightly inward? Look closely and you will see that the rails are not perfectly vertical. They lean toward each other at a small angle, often one in twenty or one in forty. The reason is the cone. A conical wheel touches the rail at an angle, so the rail is tilted to match it, and the contact point sits near the middle of the rail head.""",
     "rail cant tie plate")
sc("""That small tilt matters a lot. It keeps the wheel force pushing down through the center of the rail, instead of on its edge, which would bend and wear the rail faster. The tilt is usually created by the steel plates or the shape of the concrete sleeper under the rail. A tiny angle you can barely see, built into millions of sleepers.""",
   "concrete sleepers rail fastening", "A TINY ANGLE")
sc("""The contact between a wheel and a rail is incredibly small, about the size of a small coin. All the weight of that wheel, often more than ten tons, sits on that little patch of steel on steel. That is why trains roll so easily, with very low friction. And it is also why the shape of both surfaces must be perfect.""",
   "train wheel on rail close up", "THE SIZE OF A COIN")

# ---------- 5. BOGIE ----------
part(5, "The bogie", "WHY DOES A TRAIN CAR SIT ON THESE?", "Why Do Train Cars Sit on Swiveling Bogies?",
     """Why do train cars sit on separate wheel frames that swivel? They are called bogies, or trucks in America. Each car has two of them, and each bogie usually has two wheelsets. Long cars cannot have wheels fixed directly to the body, because in a curve, the wheels would be forced in the wrong direction. The bogie pivots under the car, so the wheels can follow the curve while the long body sweeps around above them.""",
     "railway bogie close up")
sc("""The bogie was a big step in railway history. In the eighteen thirties, the American engineer John B. Jervis used a swiveling front truck on a locomotive, so it could handle the sharp curves of early American railways. Today, the bogie also holds the springs, the dampers and the brakes. It is the part that decides how smooth your ride is.""",
   "locomotive bogie", "THE RIDE LIVES HERE")
sc("""Some trains share bogies between two cars, called Jacobs bogies, used on France's TGV. This keeps the cars connected more rigidly, and in some accidents it has helped the train stay upright and in line. One clever placement of wheels can change how a whole train behaves in a crash.""",
   "TGV Jacobs bogie", "SHARED WHEELS")

# ---------- 6. WELDED RAIL ----------
part(6, "The rail without gaps", "WHY DID THE CLICKETY-CLACK DISAPPEAR?", "Why Don't Modern Trains Go Clickety-Clack?",
     """Why don't modern trains make the classic clickety-clack sound? Because the gaps in the rails are gone. Old railways used short rails joined with gaps between them, so the steel could expand in summer heat. Every gap made a click under each wheel. Today, most main lines use continuous welded rail, with rails welded into long strings, often hundreds of meters or even kilometers long.""",
     "continuous welded rail")
sc("""But steel still expands in the heat. So how can a rail kilometers long have no gaps? The trick is to stop it from moving. The rail is clamped tightly to heavy sleepers buried in stones, and it is installed at a carefully chosen temperature. In the cold, it pulls in tension. In the heat, it pushes in compression. It wants to grow, but it is not allowed to.""",
   "rail clips concrete sleepers", "NOT ALLOWED TO GROW")
sc("""If the heat is too strong, or the track is weak, the rail can suddenly bend sideways. This is called a sun kink or buckle, and it can derail a train. That is why railways often slow trains down on very hot days, and why you sometimes see rails painted white, to reflect sunlight. A silent rail is a rail under enormous hidden stress.""",
   "rail buckle heat", "SUN KINK")

# ---------- 7. SANDER ----------
part(7, "The sandbox", "WHY DO TRAINS CARRY SAND?", "Why Do Trains Carry Sand?",
     """Why do locomotives carry sand? Because steel wheels on steel rails have low grip. That is great for rolling easily, but bad when starting a heavy train or stopping on a wet rail. So locomotives and many trains carry sand in boxes, with pipes that blow it right in front of the wheels. The sand increases grip between the wheel and the rail at exactly the moment it is needed.""",
     "railway sander locomotive")
sc("""In autumn, railways have an unexpected enemy. Leaves. When trains crush wet leaves on the rails, they form a slippery black layer that can be compared to ice. Trains slip when starting and slide when braking. In Britain, special trains spray the rails with high pressure water and apply a gel mixed with sand, to clean the rails during leaf season.""",
   "leaves on railway track", "LEAVES ON THE LINE")
sc("""Modern trains are also controlled by computers that detect wheelslip and wheel slide, a bit like the anti-lock brakes and traction control on a car. If a wheel starts spinning, the power is reduced. If it starts sliding, the brake is released for a moment. Sand plus software, the old and the new working together.""",
   "locomotive driver cab", "SAND PLUS SOFTWARE")

# ---------- 8. WHEEL TAP ----------
part(8, "The hammer test", "WHY DID WORKERS HIT TRAIN WHEELS WITH HAMMERS?", "Why Did Railway Workers Hit Wheels With Hammers?",
     """Why did railway workers walk along trains hitting the wheels with hammers? They were called wheel tappers, and they were listening. A healthy steel wheel rings like a bell. A cracked wheel makes a dull sound. It was a simple test, but it could find hidden cracks before they turned into a disaster. Today, railways use ultrasonic testing and sensors along the track to do the same job.""",
     "wheel tapping hammer")
sc("""The reason is fatigue. A wheel takes millions of loads, and a tiny crack can grow a little with each turn. On June third, nineteen ninety-eight, a German high speed ICE train near the village of Eschede had a wheel with a steel tire, a ring around the wheel center, that had a fatigue crack. The tire broke at about two hundred kilometers an hour. The train derailed and hit a bridge, and one hundred one people died.""",
   "ICE 1 train", "ESCHEDE, 1998")
sc("""After Eschede, those wheels were replaced with solid one-piece wheels, and inspection rules became much stricter. It remains the deadliest high speed rail accident in Germany. And it shows why the old hammer test existed in the first place. On a train, the most dangerous crack is the one you cannot see.""",
   "railway wheel ultrasonic inspection", "THE CRACK YOU CAN'T SEE")

# ---------- 9. COUPLER ----------
part(9, "The knuckle coupler", "WHY IS THIS COUPLER SHAPED LIKE A HAND?", "Why Are Train Couplers Shaped Like Hands?",
     """Why are many train couplers shaped like a curled hand? It is a knuckle coupler, and it was invented to save lives. Before it, many railways used link and pin couplers. A worker had to stand between two moving cars, hold a metal link, and drop a pin in at the right moment. Thousands of workers lost fingers, hands, or their lives doing it.""",
     "knuckle coupler")
sc("""In eighteen seventy-three, Eli Janney patented the knuckle coupler. When two cars are pushed together, the knuckles close and lock automatically, like two hands gripping each other. To separate them, a worker pulls a lever from the side of the car, without stepping between them. In eighteen ninety-three, the United States passed the Safety Appliance Act, which required automatic couplers and air brakes on trains.""",
   "Janney coupler", "LIKE TWO HANDS")
sc("""Variations of Janney's design are still used across North America and on many railways around the world, and its basic shape has barely changed in one hundred fifty years. A coupler today can hold together a freight train weighing thousands of tons. It is one of the most successful safety inventions in history, and almost nobody knows its name.""",
   "freight train couplers", "150 YEARS, SAME SHAPE")

# ---------- 10. AIR BRAKE ----------
part(10, "The air brake hose", "WHY DO THESE HOSES STOP A TRAIN?", "Why Do Train Brakes Work When the Air Is Lost?",
     """Why do the hoses between train cars matter so much? They carry compressed air for the brakes. In the eighteen sixties and seventies, George Westinghouse developed the railway air brake. And his key idea was brilliant. In the automatic air brake, air pressure in the pipe keeps the brakes released. To brake, the driver lowers the pressure. So if the pipe breaks, or the train splits in two, the pressure drops and every car brakes on its own.""",
     "air brake hose train")
sc("""This is called fail-safe design. The system is built so that its most likely failure leads to the safe outcome, a stopped train. Before air brakes, workers called brakemen had to climb on top of moving cars and turn hand wheels to brake each car, often in rain and snow. Many fell to their deaths. The air brake made trains longer, faster, and much safer.""",
   "railway brake shoe", "FAIL-SAFE")
sc("""The same idea is everywhere in railways. A driver must keep pressing a pedal or button, called a dead man's switch, or the train stops. Signals turn red when they lose power. On a railway, if something fails, it should fail toward stopping. A train that stops by mistake is an annoyance. A train that cannot stop is a catastrophe.""",
   "railway signal red", "FAIL TOWARD STOP")

# ---------- VERDICT ----------
sc("""So here are the ten. A cone that steers without a steering wheel, and a flange that is only a backup. A solid axle that needs no differential, and rails that lean in to meet it. A swiveling bogie, rails without gaps, sand for grip, a hammer that listened for cracks, a coupler shaped like a hand, and brakes that work when the air is lost.""",
   "train curve", "10 PARTS. NO STEERING WHEEL.", chapter="The verdict", cuts=6)
sc("""The next time you ride a train, remember that it is steering itself with a cone. If you want more machines explained part by part, subscribe to Machine Reverse. And tell us in the comments which machine you want us to take apart next.""",
   "train sunset", "SUBSCRIBE: MACHINE REVERSE", cuts=4)

# Exact photo of each part and where the arrow points (fractions of the 16:9 frame).
PICKS = {
}
for s in S:
    n = int(s["chapter"].split(".")[0]) if s.get("short") else None
    if n in PICKS:
        s["file"], s["arrow"] = PICKS[n][0], {"x": PICKS[n][1], "y": PICKS[n][2]}

json.dump({"id": "video44", "title": "Why Are Train Wheels Shaped Like Cones?",
           "length_scale": 1.6, "scenes": S}, open("videos/video44/script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes,", words, "words, about", round(words / (219 / 1.6)), "min")
