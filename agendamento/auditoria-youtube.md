# Formulário de auditoria da YouTube API: respostas prontas

Formulário: https://support.google.com/youtube/contact/yt_api_form
Escolha a opção **"I want to request an audit / quota extension"** (ou "Audit and quota extension").
Copie cada resposta em inglês no campo correspondente. Todos os campos estão preenchidos.

---

**Your name:** Vinicius Hoscher

**Email:** viniciusmcerqueira1@gmail.com

**Organization name:** Pickup Reality (individual YouTube creator)

**Organization website:** https://viniciushoscher-ctrl.github.io/american-trucks/

**Organization address / country:** New York, United States

**Google Cloud project number:** 72248929079

**Project ID:** pickup-reality

**API client name:** Pickup Reality Uploader

**Which YouTube API services do you use?** YouTube Data API v3

**API client link / URL:** https://viniciushoscher-ctrl.github.io/american-trucks/

**Privacy policy URL:** https://viniciushoscher-ctrl.github.io/american-trucks/privacy.html

**Terms of service URL:** https://viniciushoscher-ctrl.github.io/american-trucks/terms.html

**Who are the users of your API client?** Only me, the owner of the Pickup Reality channel. The tool is internal and is not offered to anyone else.

**Describe your API client and how it uses YouTube API Services:**

> Pickup Reality Uploader is a private, internal script that runs on GitHub Actions for a single YouTube channel I own (Pickup Reality, channel ID UCEz9APEqxg1No0-OyRpvgaQ). It uploads the channel's own documentary videos and Shorts with videos.insert, sets them as private with a publishAt date so they go public on a fixed schedule (one long video and two Shorts per day), and sets the custom thumbnail with thumbnails.set. It also calls channels.list (mine=true) to confirm which channel is authorized. It does not read, store, or display any data from other users or channels, and it does not access comments, analytics or subscribers. The only stored data is the OAuth refresh token (kept as an encrypted GitHub secret) and a log of uploaded video IDs and scheduled dates.

**Why do you need the audit / what is the issue?**

> My project is unverified, so every video uploaded through the API is locked as private, which makes scheduled publishing (publishAt) impossible. I am requesting the compliance audit so that videos uploaded by my own channel through this tool can be published on schedule.

**Quota requested:** 20,000 units per day

**Quota justification:**

> Daily use is 3 uploads (1 long video + 2 Shorts) × 1,600 units plus 3 thumbnails × 50 units, about 4,950 units per day. I request 20,000 units per day so that failed uploads can be retried and a backlog of already-produced videos (58 long videos and about 280 Shorts) can be scheduled ahead of time.

**Screenshots / demo:** a ferramenta não tem tela, ela roda em script. Se o formulário pedir um arquivo, envie um print da execução do workflow "youtube" no GitHub Actions (https://github.com/viniciushoscher-ctrl/american-trucks/actions/workflows/youtube.yml), que mostra a conexão com o canal Pickup Reality.
