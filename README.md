# Weekly Planner & Wellness Tracker

A weekly planner, mood & focus tracker, medication tracker, and personal journal — installable on your phone as an app (PWA).

## 📲 Install on your phone

1. Open this site's GitHub Pages URL in your phone's browser (Safari on iPhone, Chrome on Android).
2. **iPhone (Safari):** tap the Share icon → **Add to Home Screen**.
3. **Android (Chrome):** tap the **⋮** menu → **Install app** (or use the "⬇️ Install App" button that appears in the header).
4. Open it from your home screen — it runs full-screen like a native app, and works offline once loaded.

## ✨ Features

- 📅 **Weekly Planner** — top 3 priorities, hourly schedule, notes. Navigate any week (past or future — 2026 through 2035+) using the arrows or the date-jump picker in the header.
- 😊 **Mood & Focus** — daily mood, focus stars, energy level, and reflection prompts.
- 💊 **Medication Tracker** — add medications, check off daily doses, track side-effect notes, and see adherence stats.
- 📓 **Personal Journal** — free-form journal entries, separate from daily reflections, with search.
- 📊 **Weekly Summary** — mood/focus charts, medication adherence ring, streaks, and weekly reflection.
- 💾 **Backup & Restore** — export all your data as a JSON file and restore it later (menu: ⚙️ icon in the header).
- 📆 **Calendar Export** — export the current week's schedule and priorities as an `.ics` file you can import into your phone's Calendar app.

## 🗄️ Data & privacy

All data is stored **locally on your device** (`localStorage`) — nothing is sent to a server. Use the **Backup** button regularly if you want a safety copy, especially before clearing browser data or switching phones.

## 🛠️ Local development

This is a static site — no build step required.

```sh
python -m http.server 8080
```

Then open `http://localhost:8080`.
