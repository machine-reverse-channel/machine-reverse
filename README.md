# Machine Reverse

Faceless English YouTube channel: "Why does this exist?" — the engineering behind strange parts of planes, rockets, race cars, ships, trains and giant machines.

Built on the Pickup Reality pipeline (see `agendamento/GUIA-REPLICAR-CANAL.md`): script as JSON → GitHub Actions (Wikimedia Commons photos, Piper voice, FFmpeg) → Release → scheduled YouTube upload.

## What is different from Pickup Reality
- A scene with `"arrow": {"x": 0.55, "y": 0.4}` (fractions of the 16:9 frame, or `true` for the center) shows a bouncing red arrow on that point, a slow zoom into it and the scene `caption` as a big yellow question ("WHY DOES THIS HOLE EXIST?").
- `"file": "File:Exact name.jpg"` forces the first photo of a scene to a specific Commons file, so the arrow position is known.
- `"short": "Title"` names the Short cut from that part. `shorts.py` cuts one Short per arrow scene, with the full 16:9 frame over a blurred background so the arrow is never cropped.
- YouTube category 28 (Science & Technology). No e-book for now.
