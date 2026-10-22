# How Pickup Reality videos are made, and how to replicate the channel in another niche

This guide explains the whole Pickup Reality machine: every piece, why it exists, the video spec, how to rebuild it for a new niche, the mistakes we already paid for, and the secrets checklist. It is written so that another project (or another Claude) can read it once and rebuild the setup without asking.

Status when written (2026-10-22): 58 long videos rendered (01-38 and 41-60; 39 and 40 were never finished), each with 5 Shorts, a Canva thumbnail and a GitHub Release. Longs are being uploaded and scheduled through the YouTube API; Shorts are scheduled by hand from a spreadsheet.

No secret values appear anywhere in this file, and none should ever be pasted into a chat.

---

## 1. The idea in one paragraph

A faceless ("dark") English channel about one niche, modeled on a channel that already works (@BritishVehicles: list titles with a number, a conflict and a year; red/yellow/black thumbnails; 20+ minute videos with chapters; an own e-book promoted in the description and pinned comment). Revenue comes from AdSense plus our own product (the "2027 Truck Buyer's Guide" e-book). Everything is produced from text: Claude writes a fact-checked script as JSON, GitHub Actions downloads real photos, narrates with a free TTS voice, edits the video with FFmpeg, burns the captions last, cuts the Shorts, packages everything as a GitHub Release, and a daily job uploads and schedules it on YouTube.

## 2. Architecture

```
 Claude (in the project)                      GitHub repo (public, free Actions minutes)
 ───────────────────────                      ─────────────────────────────────────────
 research + script      ──commit──▶  videos/videoNN/script.json (+ make_script.py, sources)
                                             │
                                             ▼  workflow render.yml (one run per video, ~55 min)
                                     fetch_media.py  → real photos from Wikimedia Commons + credits.json
                                     build.py        → Piper narration → photo scenes (Ken Burns) →
                                                       concat → captions burned LAST → final mp4,
                                                       srt, chapters, preview, frames
                                     shorts.py       → 5 vertical Shorts (9:16, < 60 s)
                                             │
                                             ▼  pushes to branch deliveries-videoNN
                                     (mp4 split in 90 MB parts + srt + chapters + shorts + media)
                                             │
 meta/videoNN.json (title, description,      ▼  workflow pacotes.yml (one Release per video)
 tags, Shorts texts)  ─────────────▶  Release "videoNN": videoNN.mp4, short1-5.mp4,
 thumbs/videoNN.jpg (Canva export)           captions.srt, textos.txt, thumbnail.jpg
                                             │
 calendar.json  ───────────────────▶         ▼  workflow youtube.yml (daily cron 09:15 UTC)
                                     yt_upload.py → upload private + publishAt, set thumbnail,
                                                    record ids in youtube-state.json
                                             │
                                             ▼
                                         YouTube (scheduled, goes public by itself)
```

Why GitHub does the heavy work: the Claude sandbox can only reach `api.github.com`. It cannot download from Wikimedia, Pexels, Pixabay, Archive.org, Canva exports or YouTube. GitHub Actions runners have open internet, free minutes on public repos, FFmpeg, and enough CPU to render a 20-minute video. So Claude writes files and triggers workflows; the runners do every download, render and upload.

## 3. Every piece and why it exists

### 3.1 Repository layout

| Path | What it is | Why |
|---|---|---|
| `videos/videoNN/script.json` | The video as data: title, `length_scale`, and a list of scenes | The single source of truth for one video. Rendering is deterministic from it, so a fix means editing JSON and re-running. |
| `videos/videoNN/make_script.py` | Python that builds `script.json` from readable blocks (hook, cold open, list items, verdict) | Long scripts are easier to write and review as prose blocks than as raw JSON. |
| `pipeline/fetch_media.py` | Downloads real photos per scene and records license and author | Real vehicles, no AI images, and an audit trail for attribution. |
| `pipeline/build.py` | Narration, scene rendering, captions, final encode, preview, frames, chapters | The editor. |
| `pipeline/shorts.py` | Cuts 5 Shorts from the caption-free master | Shorts feed the long videos at zero extra script work. |
| `pipeline/shorts_from_final.py` | Cuts Shorts from an already finished mp4 (blurred background layout) | Fallback for videos rendered before `shorts.py` existed (01, 02). |
| `pipeline/make_desc.py` | Builds the description (intro, e-book line, chapters, sources, photo credits) | Consistent descriptions and license compliance. |
| `pipeline/yt_upload.py` | YouTube Data API uploader (`check`, `status`, `upload`, `lote`) | Hands-off scheduling. |
| `agendamento/meta/videoNN.json` | Final title, description (max ~4,900 chars), tags, Shorts titles and descriptions | What gets published. The e-book link is the placeholder `[LINK HERE]`, replaced at upload time from the repo variable `EBOOK_URL`, so changing the link never means editing 58 files. |
| `agendamento/creditos/videoNN.md` | Full photo credit list | YouTube descriptions are capped at 5,000 characters; long credit lists live here and the description links to them. |
| `agendamento/thumbs/videoNN.jpg` | 1280x720 thumbnail | Attached to the Release and set through the API. |
| `agendamento/calendar.json` + `calendario.md` | Day-by-day posting plan (machine + human versions) | The uploader follows the JSON; Vinicius reads the Markdown. |
| `agendamento/shorts-schedule.csv` | Every Short with publish time and direct download URL | Manual (or browser-agent) scheduling of Shorts. |
| `agendamento/youtube-state.json` | Which items were uploaded, video id, publishAt | Makes the daily job idempotent: it never uploads twice. |
| `agendamento/pacotes.txt` | Space-separated list of video numbers to package | Pushing this file triggers `pacotes.yml`. |
| `agendamento/branding/` | Banner, profile picture, their credits | Channel art from real CC photos. |
| `docs/` (index, privacy, terms) | The app's public website on GitHub Pages | Google requires a homepage and privacy policy on a domain you control for the OAuth app and the API audit. |

### 3.2 The script format (`script.json`)

```json
{
  "id": "video05",
  "title": "What Tariffs Really Did to Truck Prices (Model by Model)",
  "length_scale": 1.55,
  "scenes": [
    {
      "text": "Narration for this scene, 3-6 sentences, numbers written out as words.",
      "query": "Chevrolet Silverado 1500 pickup",
      "caption": "TARIFFS VS TRUCK PRICES",
      "cuts": 8,
      "chapter": "Intro"
    }
  ]
}
```

- `text`: what the narrator says. Numbers are spelled out ("twelve point six percent") because Piper reads digits badly.
- `query`: Wikimedia Commons search for this scene's photos. Be specific (make + model + body); add exclusions when results go wrong.
- `caption`: the red tag shown top-left during the scene (the "what am I looking at" anchor). Short, uppercase.
- `cuts`: how many different photos the scene cuts between (default 2; the hook uses 8 for a fast start).
- `chapter`: optional; becomes a YouTube chapter and a Shorts anchor.
- A typical 20-22 min video is about 40 scenes and ~3,000-3,100 words.

### 3.3 Real photos: `fetch_media.py` (Wikimedia Commons)

- Searches Commons, keeps only JPEGs at least 2,000 px wide, landscape (width > 1.3 x height), license starting with CC / Public domain / PD, never the same file twice in one video.
- If a query finds nothing it drops the last word and retries; if still nothing, it reuses the previous photo instead of failing a 55-minute run.
- Writes `credits.json` (file title, page, author, license, scene) for every photo. This is what makes CC BY / CC BY-SA use legal: attribution goes into the description or the credits page.
- Retries with backoff and caches searches because Commons rate-limits bursts.
- **Why Commons:** free, no API key, huge archive of real vehicles, clear licenses. For another niche, check Commons coverage first (see section 5).

### 3.4 Narration: Piper TTS

- Voice `en_US-ryan-high` (downloaded from Hugging Face `rhasspy/piper-voices` in the workflow). Free, offline, runs on the runner, no account. ElevenLabs was explicitly ruled out.
- `length_scale` slows the voice. Measured rate: **words per minute ≈ 219 / length_scale**. At 1.55 that is ~141 wpm, so ~3,000 words ≈ 21 minutes. At the default 1.0 the same script is only ~14 minutes.
- Don't go much past ~1.6: a very slow voice (scale ~2) sounded dragged and hurts retention. Add words instead.
- One Piper call per sentence, with fixed gaps (0.18 s between sentences, 0.35 s at scene end). **Why:** we then know the exact start and end of every sentence, which is what keeps captions perfectly in sync.

### 3.5 Editing: `build.py` (FFmpeg)

The repo is OpenMontage-*inspired*, not a copy of it. OpenMontage (`calesthio/OpenMontage`, AGPL-3.0) is the open-source tool the reference channel's creator sells access to; it uses the same free stack (Piper, FFmpeg, Wikimedia/Pexels/Pixabay/Archive.org). It is built around an interactive assistant with approval steps, so we kept its ideas and wrote a small headless pipeline that runs unattended in Actions. If you want to use OpenMontage itself, it's AGPL: fine for making videos, but don't resell it closed-source.

What `build.py` does, in order:
1. TTS for all scenes (4 in parallel).
2. Each scene: its photos split the scene duration evenly; each photo gets a slow zoom (`zoompan`), alternating zoom-in / zoom-out so consecutive cuts never look the same; in the first 4 scenes every cut gets a white flash (energy for the hook); the red caption tag is drawn on top. 1920x1080, 30 fps.
3. Concatenate scenes into `nocaps.mp4` (a caption-free master, kept on purpose for the Shorts).
4. Build `captions.srt` from the **measured** audio: scene start = sum of real scene durations, sentence times = real TTS durations, split into chunks of max ~7 words ending at punctuation.
5. Burn the captions (white bold DejaVu Sans, black outline, bottom center) into the final mp4. CRF 26, maxrate 2.5 Mbit/s, AAC 96k, which keeps a 21-min video around 170-250 MB.
6. Also writes `chapters.txt`, `timeline.json`, a 640x360 `preview.mp4`, and 7 sample frames for quick review.

**Why captions are burned LAST:** if captions are burned per scene or before the final concat, any change in scene length shifts every later subtitle. Burning once, from timings measured on the finished audio, is the only way they never drift. This was a hard rule from day one.

### 3.6 Shorts

- `shorts.py` (runs inside `render.yml`): picks 5 windows of consecutive scenes, each under 58 s: the hook, plus the start of 4 evenly spaced chapters (skipping the closing chapter). It crops the **caption-free** master to 9:16, re-times the subtitles to the clip and burns them last (yellow, larger), and adds a "PICKUP REALITY" banner at the top. Writes `shorts.md` with a title and description per Short.
- `shorts_from_final.py`: for videos already rendered with captions burned in, it puts the 16:9 video in the middle of a blurred 9:16 copy of itself, so the burned captions stay readable. Starts and ends exactly on caption boundaries.
- **Why 5 Shorts per long:** the plan is 2 Shorts a day and a long every other day, so 4 Shorts per long are needed; the 5th is a spare.
- Gotcha: `shorts.yml` (Shorts from an existing delivery) only lives on branch `add-shorts-workflow`. `workflow_dispatch` only works for workflows that exist on the **default branch**, so it returns 404 until merged.

### 3.7 Delivery: `deliveries-videoNN` branches

- After rendering, `render.yml` force-pushes an orphan branch `deliveries-videoNN` with: the final mp4 split into 90 MB parts (`split -b 90M`), preview, srt, chapters, frames, credits, the photos used, and the Shorts.
- **Why branches and 90 MB parts:** GitHub rejects files over 100 MB in git, and the sandbox cannot download Actions artifacts. A branch is readable through `api.github.com`, which is the only host the sandbox reaches. Join with `cat videoNN.mp4.part* > videoNN.mp4`.
- One branch per video (not one shared `deliveries` branch) so parallel renders don't overwrite each other.
- The full mp4 is also uploaded as an Actions artifact for direct download from the run page.

### 3.8 Packages: GitHub Releases (`pacotes.yml`)

- One Release per video, tag `videoNN`, containing `videoNN.mp4` (joined), `short1-5.mp4`, `captions.srt`, `textos.txt` (title, description with the real e-book link, tags, Shorts texts) and `thumbnail.jpg`.
- Triggered by pushing `agendamento/pacotes.txt`. Skips videos that already have a Release (only refreshes `textos.txt`). Max 6 in parallel.
- **Why Releases:** release assets can be up to 2 GB, have permanent direct download URLs, don't count against the project folder, and are what the uploader downloads from. They are the real "source of truth" for finished videos.
- `lote.yml` builds one zip per video for a batch (01-10) plus a schedule spreadsheet, for manual scheduling.

### 3.9 Thumbnails (Canva)

- Style: one beautiful vehicle vs an old/worse one (before/after, old vs new), big outlined text, red/yellow/black, like the reference channel.
- Made with the Canva connector. When Canva AI generation fails or credits run out (they did), copy the channel's old-vs-new template design and edit its two photos, two headlines and tag. Keep each headline word to about 8 characters and the tag to about 5, or the text wraps.
- Canva cannot import Wikimedia URLs. Feed it `raw.githubusercontent.com` URLs of photos already on a `deliveries-videoNN` branch.
- The sandbox cannot download Canva exports (proxy 403), and committing the signed export URLs to git was blocked. So `thumbs.yml` takes `NN@url|NN@url` as a workflow input, downloads on the runner, fits to 1280x720, commits `agendamento/thumbs/videoNN.jpg` and attaches it to the Release.

### 3.10 Upload and scheduling: `youtube.yml` + `yt_upload.py`

- Auth: OAuth 2 refresh token (scope `https://www.googleapis.com/auth/youtube.force-ssl`) for the channel owner's Google account, stored as GitHub secrets. No service accounts (YouTube doesn't support them for uploads).
- Uploads as `private` with `publishAt`, so YouTube publishes it by itself at the right time. Category 2 (Autos & Vehicles), language en, not made for kids. Sets the custom thumbnail right after upload.
- Reads the calendar, skips anything already in `youtube-state.json` or whose slot is less than 2 h away, stops when the daily quota budget is spent, commits the state back to the repo.
- Runs daily at 09:15 UTC (after the quota resets at midnight Pacific). Modes: `check` (tests credentials, prints channel), `status` (privacy status of uploaded ids), `upload` (calendar), `lote` (longs 01-10 on fixed dates).
- Shorts are skipped unless `YT_SHORTS=1`, because quota is spent on the longs (see 3.11). Shorts are scheduled by hand from `shorts-schedule.csv` (Vinicius used a Chrome browser agent for it).

### 3.11 Quota, verification and the Google audit

- Default YouTube Data API quota: 10,000 units/day. One upload costs 1,600, a thumbnail 50, so **about 6 uploads per day**. That's why the uploader prioritises longs.
- A new, unaudited API project is officially limited (videos uploaded by unverified projects can be locked private). In practice our first scheduled long (video 01) did go public on time through the API on 2026-10-22, but don't count on that holding; file the audit anyway.
- The audit ("YouTube API Services - Audit and Quota Extension" form) needs a homepage and privacy policy on a domain you control. We used GitHub Pages of the repo (`docs/index.html`, `privacy.html`, `terms.html`). Prepared answers are in `agendamento/auditoria-youtube.md`; ask for ~50,000 units/day.
- The OAuth consent screen must be set to **In production**; in "Testing" the refresh token expires every 7 days and uploads silently stop.
- Channel requirements: phone verification (needed for videos > 15 min and custom thumbnails), and for higher daily upload limits in YouTube Studio, the account verification in Studio > Settings > Channel > Feature eligibility (short face video or ID). Studio's own daily upload limit blocked manual Shorts scheduling until that was done.

### 3.12 Calendar

- Longs every other day at 16:00 UTC (12:00 US Eastern, 13:00 Brasília); first days were consecutive for launch momentum. 2 Shorts per day at 20:00 and 00:00 UTC (17:00 and 21:00 Brasília), cut from the longs already published, so each Short points to an existing video.
- Times are aimed at the US audience; communicate them to Vinicius in Brasília time.
- Leftover Shorts continue at 2 per day after the last long.

## 4. Long video spec

- **Length:** final video over 20 minutes (watch hours for monetization). Write ~3,000-3,500 words with `length_scale` ~1.5. A few came out at ~16 min (14-16) because the script was short: count words before rendering.
- **Hook in the first minute:** open with the most surprising concrete numbers, then promise the payoff ("the last twist changes how you should shop"). Fast cuts and flashes in the first 4 scenes.
- **Twist every ~2 minutes:** each list item is built as fact, then expectation, then a reversal backed by data ("the price rose 3 times more than the tariff explains"). No predictable structure.
- **Strictly factual:** every number comes from a named source (manufacturer, Cox Automotive, NHTSA, KBB, iSeeCars, TFL, etc.), cited in the narration ("according to...") and listed in the description. If a number can't be sourced it's left out; never invented. Keep a sources file per video.
- **Current news:** tie each topic to 2026 to 2027 news to stay timely.
- **Structure used:** hook, cold open, "how we got the data", big picture, numbered items (each with its own chapter), verdict, "what to check before you buy", call to the e-book.
- **Title formula:** number + object + conflict + year/urgency, e.g. "7 Pickups Americans Are Walking Away From Before 2027 (The Real Reasons)". The title is the main lever.
- **Visuals:** real photos only (no AI images), 2-8 cuts per scene with slow zooms, red caption tag per scene, captions burned last.
- **Every delivery:** title, thumbnail, full video, .srt, description with chapters, sources, credits and e-book link, 5 Shorts with texts.

## 5. Step by step: recreate it in a new niche

1. **Pick the niche and reference channel.** Analyse a channel that already works (titles, thumbnails, length, product). Check that the niche has **free, licensable real images**: search Wikimedia Commons for 10 typical topics. Cars are perfect on Commons; history, places, animals and products are fine; people/celebrities and recent private events are weak (consider Pexels/Pixabay APIs, which need API keys as secrets, or public-domain archives).
2. **Create a new public repo** on the same GitHub account (`viniciushoscher-ctrl/<channel>`), so Actions minutes are free. Claude can't create repos; you do it and connect it to the project.
3. **Copy what is reusable as is:** `pipeline/` (all scripts), `.github/workflows/` (render, shorts, pacotes, thumbs, youtube, lote), the `docs/` page structure, the `agendamento/` structure (meta, creditos, thumbs, calendar, state, CSV). Put `shorts.yml` and every workflow you want to dispatch on the **default branch** from the start.
4. **Change these niche/brand strings:**
   - Channel name in `shorts.py` and `shorts_from_final.py` (the `PICKUP REALITY` banner), the `User-Agent` in `fetch_media.py`, the e-book line and outlet list in `make_desc.py` and `shorts.py`.
   - Colors: caption tag `0xC8102E` (red) in `build.py`, `shorts.py`, `shorts_from_final.py`.
   - `categoryId` in `yt_upload.py` (2 = Autos & Vehicles; e.g. 27 Education, 28 Science & Technology, 22 People & Blogs), default tags in `meta/*.json`.
   - `SLOTS_UTC` and the cron in `youtube.yml` for the new audience's time zone.
   - Voice: another Piper voice if you want (any `rhasspy/piper-voices` model; set `PIPER_MODEL` and the download URL in `render.yml`), then re-measure words per minute.
   - `docs/` pages: new name, description, channel URL, contact.
5. **New Google Cloud project for the new channel** (each channel has its own OAuth project): enable YouTube Data API v3, consent screen External + In production, Web client with redirect `https://developers.google.com/oauthplayground`, get the refresh token in OAuth Playground while choosing the **new channel**. Step-by-step in `agendamento/guia-credenciais-youtube.md`.
6. **Set secrets and variables** (section 7), run `youtube.yml` with mode `check`, confirm the channel name it prints.
7. **Enable GitHub Pages** (Settings > Pages > branch main, folder `/docs`), then submit the audit form with the Pages URLs.
8. **Write a topic plan** (60 titles in themed blocks) and make **one 30-second test video** first, then one full long as the quality gate. Only then batch.
9. **Batch:** one `script.json` per video, dispatch `render.yml` per video (about 20 run in parallel; the rest queue), review previews/frames, make thumbnails, write `meta/videoNN.json`, push `pacotes.txt`, fill `calendar.json`, let the daily cron upload.
10. **Measure weekly:** CTR, retention, views; adjust titles, thumbnails and topics.

## 6. Lessons learned and pitfalls

- **Project storage is 10 GB and fills fast.** 20 finished mp4s (~11 GB) filled it, and later large files silently disappeared (a write over the limit looks saved but isn't). Production paused because of it. Never copy full videos into the project folder; keep them on `deliveries-videoNN` branches and Releases and send links.
- **Upload quota is ~6 uploads per day** at the default 10,000 units. Plan uploads days ahead, prioritise longs, request the quota extension early.
- **Verification takes time:** phone verification for > 15 min videos and thumbnails; Studio account verification for higher daily limits; the API audit can take days to weeks. Start all three on day one.
- **OAuth app left in "Testing" = token dies in 7 days.** Publish it to production. Strip whitespace from secrets (a pasted client secret had a leading space; the script now `.strip()`s them).
- **Licenses:** only CC BY, CC BY-SA, CC0 and public domain are accepted. CC BY-SA requires credit (author + license + link) and share-alike for the adapted image. Credits go in the description or in `agendamento/creditos/` linked from it; the channel banner/profile photos need a credit line in the channel description too.
- **Generic photo queries return wrong vehicles** (an older or different model shows up). Check `credits.json` / frames after each render and use exclusion terms (`-H2`).
- **Thumbnails that look AI-made** hurt trust (thumbs 01 and 21-24 were flagged). Use real photos in the template, not generated images; avoid over-smoothed or impossible-looking vehicles.
- **Canva:** AI credits run out; keep a manual template. Wikimedia URLs fail in Canva (use raw.githubusercontent.com). Exports must be downloaded by a workflow.
- **Sandbox limits:** only `api.github.com` is reachable; no artifact downloads, no Canva exports, no Wikimedia. Design everything so the runner does the internet work and writes results to a branch or Release.
- **Actions limits:** about 20 concurrent jobs per account; a 21-min render takes ~55 min; job logs can only be read after the job ends; `workflow_dispatch` needs the workflow on the default branch.
- **Claude can't merge PRs or create repos in this environment** without your review, so anything that must be on `main` needs your click.
- **Voice speed:** too slow sounds robotic and lowers retention; lengthen scripts instead of slowing the voice.
- **Hearth attachments:** a message takes at most 6 attachments and a thread at most 24; zip Shorts or link them.
- **YouTube policy:** fully automated, mass-produced content with synthetic voice is at risk of demonetization ("inauthentic content"). Keep human review of each video, real sources, original scripts, and a reasonable cadence.
- **Monetization deadline (as researched in Oct 2026):** YPP requirements were reported to rise on 2027-02-01; re-check the current rules before planning around them.
- **Revenue expectations:** AdSense can't pay before YPP approval; the e-book is the faster revenue lever, so get its sales page and real link (`EBOOK_URL`) live early.

## 7. Secrets and variables checklist (names only, never values)

GitHub repo > Settings > Secrets and variables > Actions.

| Name | Type | Used by | What it is |
|---|---|---|---|
| `YT_CLIENT_ID` | Secret | youtube.yml | OAuth client ID of the channel's Google Cloud project |
| `YT_CLIENT_SECRET` | Secret | youtube.yml | OAuth client secret |
| `YT_REFRESH_TOKEN` | Secret | youtube.yml | Refresh token for the channel's Google account (scope `youtube.force-ssl`) |
| `EBOOK_URL` | Variable | youtube.yml, pacotes.yml | Real e-book sales link; replaces `[LINK HERE]` |
| `YT_BUDGET` | Variable (optional) | youtube.yml | Quota units to spend per run (default 9,900) |
| `YT_SHORTS` | Env (optional) | yt_upload.py | `1` makes the API upload Shorts too |
| `PIPER_MODEL`, `PIPER_LENGTH_SCALE` | Env (optional) | build.py | Voice model and speed (the script's `length_scale` wins) |
| `GITHUB_TOKEN` | Automatic | all workflows | Provided by Actions; workflows need `permissions: contents: write` |
| `PEXELS_API_KEY` / `PIXABAY_API_KEY` | Secret (only if you add those sources) | fetch_media | Not used today; Commons needs no key |

Outside GitHub:
- Google Cloud project for the channel (YouTube Data API v3 enabled, consent screen in production).
- YouTube channel phone-verified and account-verified in Studio.
- GitHub Pages on, with homepage, privacy policy and terms.
- API audit / quota extension form submitted.
- Canva account with the thumbnail template.
- E-book platform and real sales link.

Never paste any secret value into a chat, an issue, a commit or a workflow file.

## 8. Daily operations cheat sheet

- New video: write `videos/videoNN/script.json` → Actions > render > Run workflow (`videoNN`) → check `deliveries-videoNN` (preview, frames, credits) → thumbnail in Canva → `thumbs.yml` → `agendamento/meta/videoNN.json` + `creditos/videoNN.md` → add NN to `pacotes.txt` and push → add the date to `calendar.json`.
- Test credentials: Actions > youtube > mode `check`.
- See what's scheduled: `agendamento/youtube-state.json`, or mode `status`.
- Manual scheduling: download from the Release (`releases/download/videoNN/...`) and use `textos.txt` for copy-paste; Shorts from `shorts-schedule.csv`.
