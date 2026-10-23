"""Append a video's Shorts to agendamento/calendar.json, two per day, on the first days without Shorts.
usage: queue_shorts.py NN (count is read from agendamento/meta/videoNN.json)"""
import datetime, json, sys

n = int(sys.argv[1])
cal = json.load(open("agendamento/calendar.json"))
count = len(json.load(open(f"agendamento/meta/video{n:02d}.json"))["shorts"])
queued = {tuple(s) for d in cal for s in d["shorts"]}
todo = [[n, k] for k in range(1, count + 1) if (n, k) not in queued]
days = {d["date"]: d for d in cal}
last = max(d["date"] for d in cal if d["shorts"])
day = datetime.date.fromisoformat(last)
while todo:
    day += datetime.timedelta(days=1)
    d = days.setdefault(day.isoformat(), {"date": day.isoformat(), "shorts": []})
    while len(d["shorts"]) < 2 and todo:
        d["shorts"].append(todo.pop(0))
cal = sorted(days.values(), key=lambda d: d["date"])
json.dump(cal, open("agendamento/calendar.json", "w"), indent=1)
print("shorts of video", n, "queued until", day)
