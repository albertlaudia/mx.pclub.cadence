# User Workflow — Ultra-Detailed

> *The complete user journey, from first install to multi-year practice.*

This is the **deep companion** to `docs/PRD.md`. The PRD is the *what* — the elevator, the screens, the success metrics. This document is the *how* — every state, every transition, every edge case, every failure mode. The level of detail here is what a designer and engineer need to ship the product without guessing.

If `PHILOSOPHY.md` is the why and `PRD.md` is the what, this file is the **every micro-moment that compounds into a practice.**

---

## Table of Contents

1. User personas
2. The first 24 hours
3. The daily use loop
4. The weekly cycle
5. The monthly cycle
6. The yearly cycle
7. Section workflows (full lifecycle)
8. Settings workflows
9. Multi-device workflows
10. Re-engagement workflows
11. Edge cases and failure modes
12. Notification workflows
13. Search and discovery
14. The reflection workflow
15. Empty states
16. Error states
17. Locale and timezone workflows
18. Privacy and data workflows
19. Account lifecycle (creation → deletion)
20. The death of a user

---

## 1. User personas

Cadence is designed for **three primary personas**. Each has a different journey through the product. The features serve all three, but the default UX leans toward Persona A (the steady practitioner) because that's the largest segment by lifetime value.

### Persona A — "The Steady Practitioner"

- **Demographics:** 28–55, Christian (Catholic or Protestant, occasionally Orthodox), middle-class, smartphone-native
- **Why they're here:** They tried YouVersion / Hallow / Pray As You Go / a quiet app. They want a daily practice but the streak mechanics and the social pressure broke them. They came back to a paper journal twice. They want an app that *feels* like a journal.
- **Their cadence:** Morning or evening, every day, sometimes twice
- **Their Section behavior:** In a Section with 2-4 family members or a small prayer group. Quiet check-ins. No commentary.
- **What they need from Cadence:** A daily movement that doesn't feel like a checkbox. A chapter mark that lands. The sense that someone is also practicing.
- **What breaks them:** A streak counter. A "you missed 3 days!" notification. A "share to unlock" paywall. A 9-tier pricing ladder.

### Persona B — "The Returning Seeker"

- **Demographics:** 22–40, Christian or Christian-curious, post-a-season-of-distance
- **Why they're here:** They had a faith practice as a kid or in college. They drifted. They want back in but the apps feel like too much. They want something that doesn't make them feel guilty for the gap.
- **Their cadence:** Inconsistent. They want it to be daily but the practice has been quarterly.
- **Their Section behavior:** Mostly solo. Maybe a partner. The Section feature is nice-to-have, not core.
- **What they need from Cadence:** No shame. A "welcome back" that doesn't reference the gap. A short, low-stakes daily practice. Localized content.
- **What breaks them:** A day counter. A red badge. A "you're behind your Section" copy.

### Persona C — "The Discipled Group Member"

- **Demographics:** 18–35, often in a small group, accountability-driven
- **Why they're here:** Their small group leader (or pastor, or friend) said "let's all use this." They want the group to see them practice.
- **Their cadence:** Daily, often at a specific time set by the group
- **Their Section behavior:** In a Section of 5-7 friends from the group. Quiet check-ins, but the social layer is the point.
- **What they need from Cadence:** The Section. Easy invite. Quick "I prayed today" without writing. The composition mark at the end of the year.
- **What breaks them:** A leaderboard within the Section. A public profile. A "your Section is at 4/7 this week" copy.

### Secondary personas (not the focus of v1, but designed-for)

- **Persona D — "The Interfaith Explorer":** uses Cadence with a custom cadence that's not Christian. Needs the prompt pool to be denomination-agnostic enough to serve them.
- **Persona E — "The Solo Practitioner":** never joins a Section, never shares, never invites. Uses the product for years alone. Needs the solo path to be as good as the social path.

---

## 2. The first 24 hours

### T+0: Cold install

The user discovers Cadence through one of:
- App Store search (e.g., "prayer app", "daily devotional", "morning quiet")
- A friend sharing a Section invite link (deep link: `cadence://join?section=<token>#key=<key>`)
- Marketing (web, social, search ad)
- A referral from another pclub app (e.g., PULSE → "you might like Cadence")

#### Cold install → first launch

The app starts. **No splash screen with a logo. No onboarding that starts with a survey.** A single quiet screen:

```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│                                         │
│              cadence.                   │
│                                         │
│       A daily practice that keeps.      │
│                                         │
│                                         │
│            [ Begin ]                    │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

The "Begin" button is the only CTA. No "Sign up", no "Sign in", no "Continue with Google" yet. The user clicks Begin and *then* we ask for an account.

**Design rationale:** the first screen is not a wall. It is an invitation. The user should feel like they are entering a quiet space, not a checkout flow.

#### Locale detection

Behind the scenes, on first launch:
1. Detect device locale (e.g., `en-US`, `es-MX`, `pt-BR`)
2. Detect device timezone (e.g., `America/Los_Angeles`)
3. Set the user's locale and timezone as preferences
4. **Do not show a locale picker unless the device locale is unsupported or ambiguous** (e.g., `zh` could be Hans or Hant)

If ambiguous, a single-screen picker appears:

```
┌─────────────────────────────────────────┐
│                                         │
│      We noticed your device is set      │
│      to Chinese. Which variant?         │
│                                         │
│      [ 简体中文 ]                        │
│      [ 繁體中文 ]                        │
│                                         │
└─────────────────────────────────────────┘
```

If the locale is in our day-90 list (EN, ES, PT-BR, FR, zh-Hans, zh-Hant, JA, KO, TL), proceed. If it's not supported yet, the picker says:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your locale isn't supported yet.   │
│      For now, you can use Cadence in:   │
│                                         │
│      [ English ]                        │
│      [ Español ]                        │
│      [ ... ]                            │
│                                         │
│      We'll email you when [your locale] │
│      is ready.                          │
│                                         │
└─────────────────────────────────────────┘
```

And we collect the email (if the user wants notification). Otherwise the user can proceed in English/Spanish and we lose the locale signal — that's OK, we'll re-prompt when their locale is supported.

### T+30s: Account creation

After "Begin", the user gets to account creation. **No email-and-password form. The default is sign-in-with-Apple on iOS, sign-in-with-Google on Android.** Email is the fallback for users who refuse both.

```
┌─────────────────────────────────────────┐
│                                         │
│      To save your practice,             │
│      sign in with:                      │
│                                         │
│      [   Continue with Apple   ]         │
│      [   Continue with Google  ]         │
│      [   Use email            ]         │
│                                         │
│      Your practice is private.          │
│      We never sell your data.           │
│      See [privacy]                      │
│                                         │
└─────────────────────────────────────────┘
```

After sign-in, the user is in. No "verify your email" gate — the email is verified by the IdP.

**If the user got here via a Section invite link**, the deep link is processed after sign-in. The user is dropped into the Section join flow (see §7).

**If the user got here via a different pclub app referral**, the sign-in is shared (if the user is already signed into the other app) and the user is dropped directly into the cadence picker.

### T+45s: Cadence picker (Onboarding step 1)

```
┌─────────────────────────────────────────┐
│                                         │
│      What rhythm do you want to keep?   │
│                                         │
│   ┌───────────────────────────────┐     │
│   │  Morning Psalms               │     │
│   │  A 90-second quiet to start   │     │
│   │  the day.                     │     │
│   └───────────────────────────────┘     │
│                                         │
│   ┌───────────────────────────────┐     │
│   │  Daily Quiet                  │     │
│   │  A 60-second check-in, no     │     │
│   │  scripture.                   │     │
│   └───────────────────────────────┐     │
│                                         │
│   ┌───────────────────────────────┐     │
│   │  The Lent Arc                 │     │
│   │  40 days of reflection.       │     │
│   └───────────────────────────────┘     │
│                                         │
│   ┌───────────────────────────────┐     │
│   │  Evening Examen               │     │
│   │  A 90-second review of        │     │
│   │  the day.                     │     │
│   └───────────────────────────────┘     │
│                                         │
│   ┌───────────────────────────────┐     │
│   │  Gratitude Practice           │     │
│   │  A 60-second thanks.          │     │
│   └───────────────────────────────┘     │
│                                         │
│   [ + Custom cadence ] (paid)           │
│                                         │
└─────────────────────────────────────────┘
```

User picks one. The card highlights. They tap "Continue".

**For the Lent Arc**, an additional question appears:

```
┌─────────────────────────────────────────┐
│                                         │
│      When does Lent start for you?      │
│                                         │
│      [ Western (Feb/Mar) ]              │
│      [ Eastern (Mar/Apr) ]              │
│                                         │
└─────────────────────────────────────────┘
```

(The Eastern date is auto-detected by locale where possible.)

### T+60s: Section picker (Onboarding step 2)

```
┌─────────────────────────────────────────┐
│                                         │
│      Who's practicing with you?         │
│      Up to 7 people. Or skip and        │
│      go solo.                           │
│                                         │
│      [   Create a Section   ]           │
│      [   Join a Section     ]           │
│      [   Skip for now       ]           │
│                                         │
└─────────────────────────────────────────┘
```

**If "Create a Section"** → Section creation flow (see §7).
**If "Join a Section"** → paste invite link or scan QR code.
**If "Skip"** → proceed.

The "Skip" option is the **default highlighted** button. The product assumes solo first. The Section is an additive, not a requirement. This is part of the philosophy (§6 of PHILOSOPHY.md): "Solo is the default. The Section is the gift."

### T+75s: Practice window picker (Onboarding step 3)

```
┌─────────────────────────────────────────┐
│                                         │
│      When do you want to practice?       │
│                                         │
│      [   Morning (6–9am)   ]            │
│      [   Midday (11am–2pm) ]             │
│      [   Evening (8–10pm)  ]             │
│      [   Anytime           ]            │
│                                         │
│      Your timezone:                     │
│      [ America/Los_Angeles  ]            │
│                                         │
│      [ Continue ]                       │
│                                         │
└─────────────────────────────────────────┘
```

The timezone is auto-detected but editable. The window is what the system uses to time-shift the content (morning cadences lean psalms, evening cadences lean examen) and to schedule the optional daily notification.

### T+90s: First movement

The user is dropped into the home screen with **today's movement already generated.**

```
┌─────────────────────────────────────────┐
│                                         │
│            Good morning, Sarah.         │
│              Day 1 of your arc.         │
│                                         │
│      ┌─────────────────────────────┐    │
│      │                             │    │
│      │     Today's Movement        │    │
│      │                             │    │
│      │  "What is one thing you     │    │
│      │   are carrying that you     │    │
│      │   could set down for an     │    │
│      │   hour?"                    │    │
│      │                             │    │
│      │  Psalm 55:22                │    │
│      │  "Cast your burden on the   │    │
│      │   Lord, and he will         │    │
│      │   sustain you."             │    │
│      │                             │    │
│      │  [ Begin reflection ]       │    │
│      │                             │    │
│      └─────────────────────────────┘    │
│                                         │
│  ◯ ◯ ◯ ◯ ◯ ◯ ◯  Week 1                 │
│                                         │
└─────────────────────────────────────────┘
```

The user taps "Begin reflection" → the movement screen → taps "Mark complete" → sees the quiet "See you tomorrow" → closes the app.

**Total time to first practice: 90 seconds from cold install.**

### T+24h: First return

The next day, the user gets a notification (if opted in) or just opens the app. Today's movement is different from yesterday's. The chapter mark shows one filled dot, six empty. The user does the practice. The cycle is established.

---

## 3. The daily use loop

The 5-minute flow that happens 365 times a year. This is the heart of the product.

### 3.1 Cold open (notification opt-in)

**State: app is in the background. User taps the notification.**

The notification (if enabled) reads: **"Today's movement is ready."** No emoji. No urgency. No badge.

Tap → app foregrounds → home screen appears → movement card is the focus.

**State: app is in the background. User opens the app directly (no notification).**

Same flow. The home screen appears. The movement card is the focus.

**State: app is fresh-installed (within 24h of install).** First movement already done. Home screen shows the "see you tomorrow" or "rest well" state. Tapping does nothing — the user has to wait until tomorrow. A small text says: "Your next movement arrives in [X hours]."

### 3.2 Home screen states

The home screen has 5 distinct states:

**State A — Movement ready (default, ~95% of opens)**
The movement card is shown. The user can:
- Tap "Begin reflection" → movement screen
- Tap the chapter dots → chapter detail view (read-only, see §4)
- Open settings (gear icon top right)
- View Section (heart icon, see §3.5)

**State B — Movement completed (just-completed)**
After marking complete, the home screen shows a quiet acknowledgment:
```
┌─────────────────────────────────────────┐
│                                         │
│            See you tomorrow, Sarah.     │
│                                         │
│      ◉ ◯ ◯ ◯ ◯ ◯ ◯  Week 1              │
│                                         │
│      Today's movement:                  │
│      "What is one thing you are         │
│       carrying that you could set       │
│       down for an hour?"                │
│                                         │
│      Psalm 55:22                        │
│                                         │
└─────────────────────────────────────────┘
```
The "Today's movement" is tappable — the user can re-read it. The chapter dots show the completed day. No confetti. No animation. Just a quiet acknowledgment.

**State C — Chapter complete (end of week)**
The chapter mark appears. See §4.

**State D — Composition complete (end of year)**
The composition mark appears. See §6.

**State E — Welcome back (returning after ≥3 days absence)**
```
┌─────────────────────────────────────────┐
│                                         │
│            Welcome back, Sarah.         │
│                                         │
│      Here's where you were:             │
│      Last movement: "What is one        │
│      thing you are carrying..."         │
│      Psalm 55:22                        │
│      Tuesday, June 23                   │
│                                         │
│      [   Begin today's movement   ]     │
│                                         │
│      [   See the past week        ]     │
│                                         │
└─────────────────────────────────────────┘
```

No "you missed 3 days!" copy. No red dot. No "miss streak" indicator. Just a quiet re-entry.

### 3.3 Movement screen

User taps "Begin reflection" on the home screen.

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      "What is one thing you are         │
│       carrying that you could set       │
│       down for an hour?"                │
│                                         │
│      ┌─────────────────────────────┐    │
│      │  Cast your burden on the    │    │
│      │  Lord, and he will          │    │
│      │  sustain you.               │    │
│      │                             │    │
│      │  Psalm 55:22                │    │
│      └─────────────────────────────┘    │
│                                         │
│      [ Copy verse ]                     │
│      [ Read context ]  ← optional,     │
│                            reveals 2-3  │
│                            sentences    │
│                            about the    │
│                            verse        │
│                                         │
│      ┌─────────────────────────────┐    │
│      │  (optional) write a         │    │
│      │  reflection...              │    │
│      │                             │    │
│      │                             │    │
│      └─────────────────────────────┘    │
│                                         │
│            [ Mark complete ]            │
│                                         │
│      [ Skip today ]  ← subtle,         │
│                         below the fold, │
│                         non-judgmental  │
│                                         │
└─────────────────────────────────────────┘
```

**Interaction details:**

- **The reflection is optional.** Tapping "Mark complete" without writing anything is fully supported. The user is not penalized for not writing.
- **The reflection is encrypted client-side.** The key is derived from the user's account password (or a system key on iOS, see §14). Cadence cannot read the reflection. The user can opt to make the reflection *searchable* (we send the encrypted index to the server) or not (the search is client-side only).
- **"Skip today"** is a non-judgmental option. Tapping it does not break anything. The user can skip a day and the practice resumes tomorrow. No "are you sure?" confirmation. No "you'll lose your streak!" copy. (There is no streak. The product simply doesn't have one.)
- **Verse actions:**
  - Copy: copies the verse to the system clipboard. The clipboard is treated as untrusted by the system; we don't read from it.
  - Read context: reveals 2-3 sentences about the verse (book, chapter, surrounding verses). This is content, not a chapter-of-the-Bible.
  - Share (subtle, behind a long-press on the verse): opens the system share sheet with the verse text. The user can paste it in any app. This is the **only** share path in the product. There is no "share to unlock" feature.
- **Audio playback (paid tier):** if the user has voice playback enabled, the verse is read aloud via TTS. The reflection is not read aloud — that would be a privacy violation (the reflection is encrypted). Only the public verse is.

### 3.4 Completion state

User taps "Mark complete".

The card animates a quiet heart in the top-right corner. The chapter dot fills. A small text appears: **"See you tomorrow"** (or **"Rest well"** in the evening window). The user is back on the home screen in state B (just-completed).

There is no "next" button. There is no upsell. There is no "share your practice" prompt. The user can close the app, and the cycle is complete.

If the user keeps the app open, after ~10 seconds the home screen auto-collapses to a minimal view:

```
┌─────────────────────────────────────────┐
│                                         │
│            See you tomorrow.            │
│                                         │
│      ◉ ◯ ◯ ◯ ◯ ◯ ◯  Week 1              │
│                                         │
└─────────────────────────────────────────┘
```

The reflection (if written) is saved encrypted. The verse is saved to history. The Section is notified (if any).

### 3.5 Section visibility on home screen

**If the user is in a Section:**

A small heart icon appears at the bottom of the home screen. Tapping it opens the Section view (see §7).

The home screen shows a **single line** above the heart:
```
Your Section — 3 of 4 practiced today.
```

Or, on a day the user hasn't practiced yet but a Section member has:
```
Your Section — 1 of 4 has practiced.
```

The names of who has or hasn't practiced are **not** shown on the home screen. The user has to open the Section view to see names.

**If the user is solo (no Section):**

The heart icon and the line are not shown. The home screen is cleaner.

### 3.6 The "off-day" state

**Days when the user doesn't open the app:**
- No notification is sent after the first one (we send one at the practice window, then nothing else). See §12.
- The home screen still shows today's movement when the user opens the app, until midnight in the user's timezone. After midnight, the movement rolls to "yesterday's movement" and the new one is generated.
- After 3 missed days, the home screen enters "Welcome back" state (State E above).
- After 7 missed days, the home screen still shows the movement, but the chapter mark starts to look sparser. No "you missed!" copy. The dots just don't fill.

### 3.7 Daily interaction summary

| User action | State change |
|---|---|
| Open app | Home screen, movement card |
| Tap "Begin reflection" | Movement screen |
| Write reflection (optional) | Reflection saved (encrypted) |
| Tap "Mark complete" | Home screen, just-completed state |
| Tap verse | Verse context expands |
| Long-press verse | System share sheet |
| Tap heart icon (Section) | Section view |
| Tap chapter dots | Chapter detail view |
| Tap gear icon | Settings |
| Tap "Skip today" | Movement marked skipped, no shame copy |
| Close app | State saved, next day's movement pre-generated |

---

## 4. The weekly cycle

The chapter is the week's unit. It resolves every 7 days.

### 4.1 Chapter timing

A chapter is **7 consecutive days** starting from the day the user installed the app. The first chapter starts on Day 1 (install day). The second chapter starts on Day 8. The third on Day 15. Etc.

The user can also choose a custom chapter start day (e.g., Sunday for Western, Monday for a work-aligned rhythm). The setting is in Settings → Cadence → Chapter starts on.

**Timezone handling:** the chapter day boundary is midnight in the user's *home* timezone, not the device's current timezone. This matters when the user travels — the chapter doesn't break just because the device clock shifted.

### 4.2 Chapter mark — end-of-week view

At midnight on the day the chapter ends (e.g., Day 7 → Day 8), the user sees the chapter mark when they open the app:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your week.                         │
│      Chapter 1, complete.               │
│                                         │
│  ◉ ◉ ◉ ◉ ◉ ◉ ◉                          │
│                                         │
│  This week your practice leaned into    │
│  patience. The verses that surfaced     │
│  most:                                  │
│                                         │
│    • Psalm 27:14                        │
│    • Psalm 46:10                        │
│    • Lamentations 3:22-23               │
│                                         │
│  [ Read the chapter ]                   │
│                                         │
│  Next week: a new movement shape.       │
│                                         │
└─────────────────────────────────────────┘
```

The chapter mark is:
- **Visible immediately** on next open (no notification)
- **Quiet** — no animation, no confetti
- **Stays for 24 hours** then transitions to the regular home screen with the new movement
- **Archived** in the chapter history (readable any time from the chapter detail view)

### 4.3 Chapter detail view (read-only)

User taps a chapter dot or "Read the chapter" on the chapter mark.

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      Chapter 1.                         │
│      Days 1-7.                          │
│      Jun 14 — Jun 20                    │
│                                         │
│   ┌─────────────────────────────────┐   │
│   │ Mon, Jun 14                      │   │
│   │ "What is one thing..."           │   │
│   │ Psalm 55:22                      │   │
│   │ ✓ practiced                      │   │
│   │ Reflection: "The kids..."        │   │
│   └─────────────────────────────────┘   │
│                                         │
│   ┌─────────────────────────────────┐   │
│   │ Tue, Jun 15                      │   │
│   │ "What does your soul..."         │   │
│   │ Psalm 42:5                       │   │
│   │ ✓ practiced                      │   │
│   │ Reflection: [empty]              │   │
│   └─────────────────────────────────┘   │
│                                         │
│   ... 5 more days ...                   │
│                                         │
│   This week your practice leaned into   │
│   patience. The verses that surfaced    │
│   most: Psalm 27:14, Psalm 46:10,       │
│   Lamentations 3:22-23.                 │
│                                         │
│   [ Export this chapter ]               │
│                                         │
└─────────────────────────────────────────┘
```

**Notes:**
- Reflections are shown if the user wrote them. The user can tap a reflection to read or edit it.
- The chapter summary paragraph is the LLM-generated arc note (see §4.4).
- "Export this chapter" generates a PDF or JSON with the chapter's movements, verses, and (if the user opts in) reflections. The export happens client-side. The file is offered through the system share sheet.

### 4.4 Chapter summary generation

The chapter summary is **LLM-generated** from the week's data:
- The 7 movements' prompts and verses
- The mood signals (if any)
- The 7 reflections (if any) — sent encrypted, decrypted server-side with the user's key (only the user's key, never stored server-side)

**Privacy boundary:** the LLM call happens server-side, but the reflections are decrypted in-memory only. The plaintext is not stored, not logged, not used for any other purpose. The prompt to the LLM is structured: "Here are 7 prompts, 7 verses, and (optionally) 7 reflection snippets. Generate a 1-paragraph summary in [user's locale]." The output is the summary paragraph.

**Cost:** ~$0.02 / user / week. Negligible.

**Review:** 1% of generated summaries are spot-checked by a native speaker weekly. The LLM prompt is tuned to match failure modes (overly evangelical, too Catholic, too preachy, etc.).

**Fallback:** if the LLM is down, the chapter still resolves — it just doesn't have a summary paragraph. The user sees the 7 days and a generic "A week of practice." text.

### 4.5 Chapter history

The user can browse past chapters. Free tier: last 4 chapters. Paid tier: full history (52+ weeks).

Chapter history is accessed from:
- Home screen → chapter dots → "See full history" (paid only, on free tier the last 4 are visible inline)
- Settings → Cadence → History

### 4.6 Skipped days in the chapter

A skipped day (user tapped "Skip today") shows in the chapter detail as:
```
┌─────────────────────────────────┐
│ Thu, Jun 17                      │
│ — skipped —                      │
│ [ Mark this day ]  ← optional    │
│                    rewind, the   │
│                    user can      │
│                    do the        │
│                    movement      │
│                    late          │
└─────────────────────────────────┘
```

A missed day (user didn't open the app) shows as:
```
┌─────────────────────────────────┐
│ Thu, Jun 17                      │
│ — —                              │
└─────────────────────────────────┘
```

Both are visually distinct from a "✓ practiced" day. Neither is shamed.

---

## 5. The monthly cycle

There is no explicit "monthly" feature in the product. The weekly cycle is the primary rhythm. The monthly cycle is implicit — every 4-5 chapters, the user has a "month" of practice.

The home screen never shows a month marker. The chapter is the unit. If the user wants to see a month, they can scroll the chapter history.

**One implicit monthly feature:** the LLM-generated chapter summary includes a one-line temporal note every 4th chapter:
"This is the close of your first month. The verses that found you most were..."

This is the only place "month" appears. It's not a milestone the user has to track. The product handles it.

---

## 6. The yearly cycle

The composition is the year's unit. It resolves every 365 days.

### 6.1 Composition timing

A composition is **365 consecutive days** starting from the user's install date. The first composition is "Your 2026 Composition" (or whatever year the user installed in). The second is "Your 2027 Composition."

**Cross-year installs:** if the user installs on December 15, the first composition is Dec 15 → Dec 14 next year. This is intentional — we don't want to break the arc just because the user installed near a calendar boundary. The composition is anchored to the user's start date, not the calendar year.

### 6.2 Composition mark — end-of-year view

At midnight on the day the composition ends, the user sees the composition mark when they open the app:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your 2026 composition.             │
│      365 movements. 52 chapters.        │
│                                         │
│      ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◯ ...        │
│      (52 chapter dots, some filled)     │
│                                         │
│   You practiced 287 days.               │
│   Your busiest chapter was week 14.     │
│   Your quietest was week 47.            │
│   The verse that found you most:        │
│   Psalm 46:10 — "Be still, and know     │
│   that I am God."                       │
│                                         │
│   [ Read the composition ]              │
│   [ Start 2027 ]                        │
│                                         │
└─────────────────────────────────────────┘
```

The composition mark is:
- **Visible immediately** on next open
- **Stays for 7 days** then transitions to the regular home screen with the new composition
- **Archived permanently** (paid tier) or for 4 weeks (free tier, then archived to "the past")

### 6.3 Composition detail view

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      Your 2026 composition.             │
│      Jun 14, 2025 — Jun 13, 2026.       │
│                                         │
│      ┌──────────────────────────┐       │
│      │                          │       │
│      │   The 5 verses that      │       │
│      │   found you most:        │       │
│      │                          │       │
│      │   1. Psalm 46:10         │       │
│      │      "Be still..."       │       │
│      │                          │       │
│      │   2. Psalm 23:4          │       │
│      │      "Even though I..."  │       │
│      │                          │       │
│      │   3. Isaiah 41:10        │       │
│      │      "Do not fear..."    │       │
│      │                          │       │
│      │   4. Matthew 11:28       │       │
│      │      "Come to me..."     │       │
│      │                          │       │
│      │   5. Philippians 4:6     │       │
│      │      "Do not be          │       │
│      │       anxious..."        │       │
│      │                          │       │
│      └──────────────────────────┘       │
│                                         │
│      The arc of your year:              │
│      Your practice started in summer    │
│      and deepened through fall. You     │
│      wrote reflections in the weeks     │
│      your kids were sick. The           │
│      "Even though I walk" verse found   │
│      you in October and stayed through  │
│      winter. Lent pulled you into       │
│      Lamentations. Easter brought       │
│      joy.                               │
│                                         │
│      [ Export the composition ]         │
│      [ Share the composition ]          │
│                                         │
└─────────────────────────────────────────┘
```

The composition detail view is read-only. The user can export it (PDF, JSON) or share a single line ("The verse that found me most this year was Psalm 46:10") to the system share sheet.

### 6.4 The arc note

The composition summary paragraph is the **arc note** — a 1-paragraph narrative of the user's year of practice. It is LLM-generated, locale-aware, and tone-moderated.

**Privacy boundary:** the LLM call uses the same encryption-decryption pattern as the chapter summary. Reflections are decrypted in-memory only. The plaintext is not stored, not logged, not used for any other purpose.

**Cost:** ~$0.05 / user / year. Negligible.

**Tone moderation:** the arc note is reviewed for:
- Not preachy
- Not denominationally biased (unless the user's cadence specifies it)
- Not making claims about the user's life ("You grew closer to God this year") that aren't supported by the data
- Not making theological claims

The arc note is descriptive, not prescriptive. It says what happened, not what it meant.

### 6.5 Starting the next composition

User taps "Start 2027" on the composition mark. The next composition is automatically created. The current one is archived.

The user can also start a new composition manually at any time (Settings → Cadence → Start a new composition). The current one is archived. The new one begins.

The "year" framing is just a default. Some users will have 6-month compositions. Some will have 2-year compositions. The framework supports any duration.

---

## 7. Section workflows (full lifecycle)

The Section is the most complex feature in the product. It has 4 distinct user-facing flows: **create, join, manage, dissolve.**

### 7.1 Creating a Section

User taps "Create a Section" in onboarding (or Settings → Section → Create a Section).

**Step 1: Name the Section.**

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      Name your Section.                 │
│                                         │
│      [ The morning crew         ]       │
│                                         │
│      (2-30 characters. Visible to       │
│      your Section members.)             │
│                                         │
│      [ Continue ]                       │
│                                         │
└─────────────────────────────────────────┘
```

**Step 2: Pick the cadence.**

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      What will you practice together?   │
│                                         │
│      ◉ Morning Psalms                   │
│      ○ Daily Quiet                      │
│      ○ Evening Examen                   │
│      ○ Custom (paid)                    │
│                                         │
│      Everyone in the Section            │
│      practices the same cadence.        │
│                                         │
│      [ Continue ]                       │
│                                         │
└─────────────────────────────────────────┘
```

A Section is anchored to one cadence. The cadence choice is a Section-level setting. If a member wants to practice a different cadence, they leave and join a different Section (or create one).

**Step 3: Generate the invite.**

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      Your Section is ready.             │
│                                         │
│      "The morning crew"                 │
│      1 of 7 members.                    │
│                                         │
│      Invite up to 6 more people.        │
│                                         │
│      [ Copy invite link ]               │
│      [ Share via... ]                   │
│      [ Show QR code ]                   │
│                                         │
│      Section links expire in 24 hours.   │
│      Generate a new link anytime.       │
│                                         │
│      [ Done ]                           │
│                                         │
└─────────────────────────────────────────┘
```

**Behind the scenes:**
1. The client generates a Section key (a 256-bit symmetric key).
2. The key is embedded in the invite link as a URL fragment: `cadence://join?section=<id>#key=<key>`.
3. The URL fragment is never sent to the server. The server only sees the Section ID and the unencrypted metadata (name, cadence).
4. The Section ID, name, cadence, and creator are stored in Firestore.
5. The Section key is stored in the creator's local keychain (iOS Keychain, Android Keystore).

**Re-invite:** if the link expires or a member loses the key, the creator generates a new link. Existing members are unaffected.

### 7.2 Joining a Section

User receives an invite link. Taps it. The app deep-links to:

```
cadence://join?section=<id>#key=<key>
```

If the user doesn't have Cadence installed, the link opens the App Store / Play Store. After install, the user is dropped into the join flow.

If the user has Cadence installed:

**Step 1: Confirm the Section.**

```
┌─────────────────────────────────────────┐
│                                         │
│      "Sarah Chen" invited you to        │
│      join "The morning crew".           │
│                                         │
│      You'll practice Morning Psalms     │
│      with up to 7 people.               │
│                                         │
│      Cadence can't see who's in this    │
│      Section or when you practice.      │
│      Your practice is end-to-end        │
│      encrypted.                         │
│                                         │
│      [   Join the Section   ]            │
│      [   Not now            ]            │
│                                         │
└─────────────────────────────────────────┘
```

**Step 2: Accept the cadence (if different from current).**

If the Section's cadence is different from the user's current cadence:
```
┌─────────────────────────────────────────┐
│                                         │
│      The Section practices              │
│      Morning Psalms.                    │
│                                         │
│      You're currently practicing        │
│      Daily Quiet.                       │
│                                         │
│      Joining this Section will change   │
│      your cadence.                      │
│                                         │
│      [ Switch to Morning Psalms ]       │
│      [ Keep my current cadence ]        │
│      [ Cancel ]                         │
│                                         │
└─────────────────────────────────────────┘
```

The user is warned that joining the Section changes their cadence. This is intentional — the Section is anchored to one cadence.

**Step 3: Section joined.**

The Section key is installed in the user's local keychain. The Section is now visible on the home screen.

**Behind the scenes:**
1. The client extracts the key from the URL fragment.
2. The key is used to decrypt the Section's metadata (members list, practice signals) that the server sends.
3. The user is added to the Section's encrypted member list.
4. The server never sees the key. The server only sees encrypted blobs.

### 7.3 Section view (in-product)

User taps the heart icon on the home screen. The Section view opens:

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      The morning crew                   │
│      4 of 7 members.                    │
│                                         │
│      Today                              │
│                                         │
│      ◉ Sarah Chen          practiced    │
│      ◉ James Park          practiced    │
│      ◯ Anna Rodriguez                   │
│      ◉ David Kim           practiced    │
│                                         │
│      This week                          │
│                                         │
│      ◉ ◉ ◉ ◯ ◉ ◉ ◉  Sarah               │
│      ◉ ◯ ◉ ◉ ◯ ◉ ◯  James               │
│      ◉ ◉ ◉ ◉ ◯ ◯ ◯  Anna                │
│      ◉ ◉ ◉ ◉ ◉ ◯ ◯  David               │
│                                         │
│      [ Invite a new member ]            │
│      [ Section settings ]               │
│                                         │
└─────────────────────────────────────────┘
```

**Privacy details:**
- The user sees only Section members who are *also visible to them.* If a member has set "hidden from view" (a Section setting), they don't appear. (Most users don't enable this.)
- The "practiced" indicator is a quiet heart. No "streak" line. No "best in Section" ranking. No "you've outlasted Anna!" copy.
- The week dots show which days each member practiced. No numbers (like "5/7"). Just the dots.
- The user can tap a member's name to see their chapter marks — but only if the member has set "chapter marks visible to Section." Default: yes.

### 7.4 Section settings

User taps "Section settings" in the Section view.

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      The morning crew                   │
│                                         │
│      Section name                       │
│      [ The morning crew         ]       │
│                                         │
│      Cadence                            │
│      [ Morning Psalms           ]       │
│      (change requires a new Section)    │
│                                         │
│      Privacy                            │
│      [ ●  My chapter marks visible ]    │
│      [ ●  I'm visible to members  ]     │
│      [ ●  Practice day visible    ]     │
│                                         │
│      Members                            │
│      Sarah Chen (creator)               │
│      James Park                         │
│      Anna Rodriguez                      │
│      David Kim                          │
│      [ + Invite a new member ]          │
│                                         │
│      [ Dissolve the Section ]           │
│      (visible to all members)           │
│                                         │
└─────────────────────────────────────────┘
```

**Dissolve the Section:**
- Visible to any member. Any member can dissolve.
- A confirmation dialog: "Dissolve the Section? This cannot be undone. All members will be notified."
- On confirm: Section is marked dissolved. All members see a quiet notice: "Sarah has dissolved The morning crew." Members are unlinked.
- The Section key is destroyed on all members' devices.

**Leave the Section (without dissolving):**
- A different action. "Leave the Section" is in the user's own Section settings, not in the Section's settings.
- The user leaves. The remaining members see: "Sarah has left the Section." The user is unlinked but the Section continues.
- The user can re-join only via a new invite link (the creator must generate a new one).

### 7.5 Section failure modes

**Member loses their key (reinstalls the app, switches devices without backup):**
- The user is still a member, but cannot decrypt Section data.
- The Section view shows: "Your Section key is missing. Ask [creator name] to send you a new invite."
- The creator generates a new invite link. The user accepts it. The new key overwrites the missing one.

**Creator loses their key:**
- The Section is still alive, but the creator cannot decrypt Section data either.
- Any member can take ownership: Settings → Section → Take ownership. The new owner generates a new invite link for everyone. All members re-accept.
- (The old creator's key is destroyed on their device.)

**Section is dissolved while a member is offline:**
- The member sees the dissolve notice the next time they open the Section view.
- The member is unlinked automatically.

**Section is full (8th member tries to join):**
- The invite link is one-time and capped. The 8th person sees: "This Section is full. Ask the creator to start a new one."

**Section has only 1 member (everyone else left):**
- The remaining member sees a quiet notice: "You're the only one left in The morning crew. You can invite more people, or dissolve the Section."
- The Section is still functional — just solo. The member can practice with the Section, just no one else will see.

---

## 8. Settings workflows

Settings is the gear icon on the home screen. The settings screen is a single scrollable list:

```
┌─────────────────────────────────────────┐
│  [ ← back ]                             │
│                                         │
│      Settings                           │
│                                         │
│      Account                            │
│      Sarah Chen                         │
│      sarah@example.com                  │
│      [ Sign out ]                       │
│      [ Delete account ]                 │
│                                         │
│      Cadence                            │
│      Morning Psalms                     │
│      [ Change cadence ]                 │
│      [ Chapter starts on... Sunday ]    │
│      [ Practice window: Morning ]       │
│      [ Locale: English (US) ]           │
│      [ Timezone: America/Los_Angeles ]  │
│      [ Start a new composition ]        │
│                                         │
│      Section                            │
│      The morning crew (4 of 7)          │
│      [ Open Section ]                   │
│      [ Section settings ]               │
│      [ Leave Section ]                  │
│                                         │
│      Notifications                      │
│      [ ●  Daily reminder ]              │
│        [ 7:30am in your timezone ]      │
│      [ Bonus movement reminder ]        │
│      [ Weekly chapter mark ]            │
│      [ Monthly review ]                 │
│      [ Yearly composition mark ]        │
│                                         │
│      Voice                              │
│      [ ●  Voice playback (paid) ]       │
│      [ Voice: English (US), Female ]    │
│      [ Speed: 1.0x ]                    │
│                                         │
│      Privacy & data                     │
│      [ Export my data ]                 │
│      [ Reflections: encrypted, ]        │
│      [   searchable on this device ]    │
│      [ Delete my account ]              │
│      [ Privacy policy ]                 │
│      [ Terms of use ]                   │
│                                         │
│      Subscription                       │
│      Free tier                          │
│      [ Upgrade to Cadence+ ]            │
│      $4.99 / month or $39/year          │
│                                         │
│      About                              │
│      Version 0.1.0 (build 100)          │
│      [ What's new ]                     │
│      [ Help & support ]                 │
│      [ Send feedback ]                  │
│                                         │
└─────────────────────────────────────────┘
```

### 8.1 Change cadence

User taps "Change cadence". A confirmation dialog: "Changing your cadence will start a new composition. Your current composition will be archived. Continue?"

If yes, the user is dropped into the cadence picker (same as onboarding). The new cadence is set. The current composition is archived. The new one begins.

**Exception:** if the user is in a Section, the cadence is locked to the Section's cadence. The user must leave the Section first, or wait for the Section to dissolve.

### 8.2 Chapter start day

User picks Sunday, Monday, or Saturday. (Default: the user's locale's standard — Sunday for US, Monday for EU, etc.)

### 8.3 Practice window

User picks morning, midday, evening, or anytime. The setting affects:
- When the daily notification is sent (if enabled)
- When the movement content time-shifts (morning leans psalms, evening leans examen)

### 8.4 Locale and timezone

User can change the locale at any time. The change affects:
- All UI strings
- All verse translations shown by default
- All LLM-generated content
- The locale picker for ambiguous locales (e.g., `zh` → ask Hans vs Hant)

Timezone change is auto-detected from device. The user can override (e.g., a frequent traveler who wants their "home" timezone).

**Edge case:** if the user is in a Section, the locale is independent per-user. The Section is locale-agnostic; the prompt and verse shown to each member is in their own locale.

### 8.5 Notifications

All notifications are off by default. The user opts in from Settings → Notifications.

The user can enable:
- Daily reminder: one notification at the practice window
- Bonus movement reminder: a notification on bonus-movement days (~10% of days)
- Weekly chapter mark: a notification when the chapter resolves
- Monthly review: a notification at the end of each 4-chapter cycle
- Yearly composition mark: a notification at the end of the composition

**Notification copy:**
- Daily: "Today's movement is ready." (no emoji, no urgency)
- Bonus: "Today's movement is a longer one. Take 5 minutes if you can."
- Chapter mark: "Your week resolved. Here's what surfaced."
- Composition mark: "Your year resolved. Here's the verse that found you most."

The user can disable any of these. There is no "you haven't opened the app in 3 days!" notification. **Cadence does not send guilt notifications.** (See PHILOSOPHY.md §1 and §3.)

### 8.6 Voice playback (paid)

User enables voice. The verse (only) is read aloud via TTS. The voice is selected from the user's locale's available voices. Speed is adjustable.

The reflection is **never** read aloud. Even if the user has voice enabled, the reflection is silent.

### 8.7 Privacy & data

- **Export my data:** generates a JSON or PDF of all the user's data. The export happens client-side. The file is offered through the system share sheet. The export includes:
  - All movements and verses
  - All reflections (decrypted locally, included in the export)
  - All chapter marks
  - All composition marks
  - The user's account email and preferences
  - **Excludes:** Section data (it's encrypted, we can't read it)
- **Reflections: encrypted, searchable on this device:** the user picks whether the reflection index is uploaded to the server (for cross-device search) or kept local. Default: local. Paid users can opt in to server-side encrypted search.
- **Delete my account:** confirmation dialog. The user is signed out, all data is deleted from the server within 7 days. Local data is deleted immediately.
- **Privacy policy** and **Terms of use** open in the in-app browser.

### 8.8 Subscription

- **Free tier** is the default. Free users see the upgrade pitch in Settings → Subscription → "Upgrade to Cadence+". The pitch is honest: "$4.99/month. Full archive, unlimited Sections, voice playback, custom cadences, wearable app." No "Become a Premium Member!" copy.
- **Paid users** see "You're on Cadence+. Renews [date]. [Manage subscription]". Tapping "Manage" opens the App Store / Play Store subscription settings.
- **No upsell** on the home screen, in the movement screen, or in the chapter mark. The only place the upgrade pitch lives is in Settings.

---

## 9. Multi-device workflows

Cadence supports iPhone + iPad + Apple Watch (paid) and Android phone + Android tablet + Wear OS (paid). The user signs in with the same Apple/Google/email account on each device. Data syncs via Firestore.

### 9.1 Sync model

- **User state** (cadence, locale, settings) syncs in real-time via Firestore listeners.
- **Movements** (prompts, verses, completion) sync in real-time. The user can mark complete on one device and see the heart on another.
- **Reflections** sync encrypted. The reflection is encrypted client-side with the user's key, uploaded as a blob, and decrypted on each device.
- **Section data** is end-to-end encrypted. The Section key is per-device. When the user adds a new device, they need to be re-invited to the Section on the new device. (Or the creator generates a "multi-device" invite that includes the key for all their devices.)
- **Chapter and composition marks** sync in real-time once generated.

### 9.2 Conflict resolution

- **Last-write-wins** for all state. The user is not multi-device-collaborative — they're solo on each device. The last tap wins.
- **Reflection edits** are last-write-wins. If the user edits a reflection on iPhone at 7am and on iPad at 7:05am, the iPad version wins. The iPhone version is overwritten.
- **No merge UI.** The product is not a notes app. The reflection is a journal, not a doc.

### 9.3 Apple Watch / Wear OS

The wearable app is a minimal client:
- Shows today's movement (prompt + verse)
- "Mark complete" button
- Today's chapter dots
- **No reflections** on the wearable (too small, too private)
- **No Section view** on the wearable (too small)
- **No settings** on the wearable (use the phone)

The wearable is for the *in-the-moment practice* — the user raises their wrist, sees the movement, marks complete, lowers their wrist. The reflection happens on the phone, later.

### 9.4 Device migration

User gets a new phone. Signs in with the same account. All data is restored (via Firestore). The Section is the exception — the user has to be re-invited (or accept a multi-device invite) to get the Section key on the new device.

If the user is on the free tier, the Section cap is 1. If they were in a Section on the old device, they're not in one on the new device until they re-join. This is acceptable — re-joining is one tap.

---

## 10. Re-engagement workflows

### 10.1 Returning after 3-7 days

User opens the app. The home screen enters "Welcome back" state (State E in §3.2). The movement card shows today's movement, not the missed days. The chapter dots show the gap as empty.

The home screen does not say "you missed 4 days!" It says "Welcome back."

### 10.2 Returning after 7-30 days

Same as above, but the chapter mark at the end of the week is more sparse. The user has missed a significant chunk. The home screen still shows today's movement — the practice resumes, not restarts.

If a chapter ends during the absence, the chapter resolves with a quiet summary: "A chapter of scattered practice. Here's what surfaced anyway." The LLM handles this gracefully.

### 10.3 Returning after 30+ days

The home screen still shows today's movement. The chapter mark looks sparse. The product does not shame the user. The user is welcomed back.

If the user is on the paid tier and the subscription lapsed, the user is downgraded to free. The Section cap of 1 applies. The history cap of 4 weeks applies. The user is not penalized further.

If the user is on the free tier, nothing changes.

### 10.4 The "I'm done" state

The user can pause their practice. Settings → Cadence → Pause practice. The home screen shows:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your practice is paused.           │
│                                         │
│      When you're ready,                 │
│      [   Resume practice   ]            │
│                                         │
│      Your history is still here when     │
│      you come back.                     │
│                                         │
└─────────────────────────────────────────┘
```

Pause is non-judgmental. No "are you sure?" No "you'll lose your [streak]!" The product just stops asking. The user can resume at any time. The composition continues (the pause is just a longer skipped stretch).

Pause is not delete. The account and data are preserved. The user can also explicitly delete the account (Settings → Delete account).

---

## 11. Edge cases and failure modes

### 11.1 Network failure

- **Movement screen loads but verse fails to load:** a quiet fallback. The verse area shows "Tap to retry." If retry fails, the user can still tap "Mark complete" and the practice is logged without the verse. The verse is loaded later (the next time the user opens the chapter detail view).
- **Reflection save fails:** the reflection is queued locally. The user sees a small "Saved on this device" indicator. The next time the device is online, the reflection syncs.
- **Section data fails to load:** the heart icon on the home screen is dimmed. The user can still see today's movement. The Section view shows "Section data unavailable. Pull to refresh."

### 11.2 LLM failure

- **Movement generation fails:** the user gets a fallback movement from the curated pool (no LLM, just a pre-written prompt + verse). The fallback is still novel within the weekly arc. The user does not see "AI unavailable" copy.
- **Chapter summary fails:** the chapter resolves without a summary paragraph. The user sees: "A week of practice. [Read the 7 days]"
- **Composition arc note fails:** the composition resolves without the arc note. The user sees the verses and chapter marks, but no narrative paragraph.

### 11.3 Server outage

The app is designed to be **read-only functional** during a server outage:
- The user can read all of their locally-cached movements
- The user can write reflections (queued locally)
- The user can mark complete (queued locally)
- The user can browse the chapter history (locally cached)
- The user **cannot** join a Section, change settings that require server confirmation, or sync to a new device

When the server is back, all queued data syncs.

### 11.4 Time zone changes

- **User travels across time zones:** the device clock changes. The home screen updates to the new timezone immediately. The movement content is still in the user's home locale. The chapter day boundary is in the user's *home* timezone (per §4.1).
- **Daylight saving:** the device clock handles this. The user might see two movements on the "fall back" day (the same Sunday morning) — one at 1:30am, one at 2:30am. The system dedupes; the user sees one movement per calendar day in their home timezone.

### 11.5 Locale changes mid-use

- **User changes device locale:** the app picks up the new locale on next launch. The user is offered: "We noticed your device locale changed to [locale]. Switch Cadence to [locale]?" If yes, all strings, verses, and content switch. If no, Cadence stays in the previous locale.
- **User changes locale in Cadence settings:** instant switch. The user is warned: "Changing your locale will switch verse translations. Your reflections stay the same." (Reflections are in the user's own words, not translated.)

### 11.6 Subscription lapses

- **User's paid subscription expires:** the user is downgraded to free tier. The Section cap of 1 applies. The history cap of 4 chapters applies. The custom cadence (if any) is preserved as the new default but cannot be changed to another custom one. The user is not kicked out of Sections they were in (they can stay in up to 1).
- **User's payment fails:** Apple/Google sends a billing retry notification. The user is given a 7-day grace period on paid features. After 7 days, downgrade to free.

### 11.7 Account compromise

- **User suspects their account is compromised:** Settings → Sign out everywhere. All devices are signed out. The user signs back in on their trusted device.
- **User lost access to their email:** contact support. Identity verification is required.

### 11.8 Reflection content moderation

- **User writes a reflection with concerning content (self-harm, violence, etc.):** the reflection is end-to-end encrypted and not visible to Cadence. The product cannot intervene. The user is on their own.
- **This is a known limitation.** The trade-off is privacy for safety. We accept it because the alternative — server-side access to encrypted reflections — would violate the privacy promise.
- **The support page** has a "If you're in crisis" section linking to local crisis hotlines (per locale). The user is directed there from the welcome screen and from the settings → help page.

---

## 12. Notification workflows

### 12.1 Default state

All notifications are OFF. The user opts in.

### 12.2 Opt-in flow

User taps any notification setting toggle for the first time. The app shows:

```
┌─────────────────────────────────────────┐
│                                         │
│      Allow Cadence to send              │
│      notifications?                     │
│                                         │
│      We'll only send you:               │
│                                         │
│      • A daily reminder at your         │
│        practice window                  │
│      • A weekly chapter mark            │
│        (if you opt in)                  │
│      • A yearly composition mark        │
│        (if you opt in)                  │
│                                         │
│      We will never send you:            │
│                                         │
│      • "You missed a day!" reminders    │
│      • Streak-loss warnings             │
│      • Marketing or upsell              │
│      • Anything that adds guilt         │
│                                         │
│      [   Allow notifications   ]        │
│      [   Not now               ]        │
│                                         │
└─────────────────────────────────────────┘
```

If the user taps "Allow notifications", the system permission dialog appears. If the user grants, the settings page shows the toggles. If the user denies, the settings page shows: "Notifications are blocked in your device settings. Open Settings to enable."

### 12.3 The daily reminder

Sent at the user's practice window (in their home timezone). Copy: "Today's movement is ready."

Tap → app foregrounds → home screen.

**If the user already completed the movement today:** no notification is sent. The system checks before sending.

**If the user has notifications disabled:** nothing is sent.

**If the device is in Do Not Disturb:** the notification is suppressed by the OS. We do not bypass DND.

### 12.4 The chapter mark

Sent at the moment the chapter resolves (midnight in the user's home timezone on the chapter-end day). Copy: "Your week resolved. Here's what surfaced."

Tap → app foregrounds → chapter mark view.

**Opt-in only.** Off by default. The user has to explicitly enable this.

### 12.5 The composition mark

Sent at the moment the composition resolves. Copy: "Your year resolved. Here's the verse that found you most."

Tap → app foregrounds → composition mark view.

**Opt-in only.** Off by default.

### 12.6 Bonus movement notification

Sent on bonus-movement days (~10% of days) when the user has voice playback or longer movements enabled. Copy: "Today's movement is a longer one. Take 5 minutes if you can."

**Opt-in only.** Off by default.

### 12.7 What we never send

- "You missed a day!" (any variant)
- "Don't break your streak!" (we don't have a streak)
- "You're falling behind your Section" (we never compare)
- Marketing notifications
- Upsell notifications
- Re-engagement notifications ("We miss you!")
- "Special offer" notifications

These are the lines. The push notification system has a hard-coded blocklist of these patterns. New notification copy has to be reviewed against the blocklist.

---

## 13. Search and discovery

Cadence is not a search-first product. The user comes back for the daily movement, not to search. But some search is necessary.

### 13.1 Verse search

User can search for a verse by reference (e.g., "John 3:16") or by keyword (e.g., "peace", "fear not").

The search is **client-side** for free users (searches the user's own history). For paid users with reflections, the search can also be **client-side encrypted search** (the encrypted index is on the device).

The search never returns results from other users or from a public library. The product is not a Bible app — it's a personal practice app.

### 13.2 Past movement search

User can search past movements by date or by keyword in the prompt. The search is client-side.

### 13.3 Chapter search

User can browse chapters by date. The free tier sees the last 4 chapters. Paid tier sees the full history.

There is no "search across all chapters" UI. The user can scroll or filter by year.

### 13.4 Section search

Not applicable. The Section has at most 7 members. The user knows them by name.

---

## 14. The reflection workflow

The reflection is the most private data in the product. It is end-to-end encrypted. Cadence cannot read it.

### 14.1 Writing a reflection

User opens a movement → writes a reflection in the optional text field → taps "Mark complete".

The reflection is encrypted with a key derived from the user's account password (or, if the user uses sign-in-with-Apple/Google without a password, a device-stored key managed by the OS keychain).

The encryption happens **on the device** before any network call. The server only ever sees ciphertext.

### 14.2 Reading a reflection

User opens the chapter detail view → taps a day → the reflection is decrypted on the device and shown.

If the device is new and the key is missing (e.g., the user signed in on a new device with Apple ID but the key wasn't transferred), the reflection is unreadable. The user sees: "This reflection is encrypted with a key that's not on this device. [Restore from another device] or [Skip]."

### 14.3 Editing a reflection

User opens the chapter detail view → taps the reflection → edits → saves. The new reflection is encrypted and uploaded. The old reflection is deleted from the server (overwritten with the new ciphertext, then garbage-collected).

### 14.4 Searching reflections

User opens Settings → Privacy → Searchable reflections.

- **Off (default, free):** the reflection index is on the device only. Search happens locally.
- **On (paid):** the encrypted index is uploaded to the server. Search can be done across all devices. The server cannot read the index.

### 14.5 Exporting reflections

User opens Settings → Privacy → Export my data → Includes reflections. The export is generated client-side. The reflections are decrypted, included in the export, and the file is offered through the system share sheet.

### 14.6 Deleting a single reflection

User opens the chapter detail view → taps the reflection → Delete. The reflection is overwritten on the server (and the local copy). The user is warned: "This will permanently delete this reflection from Cadence. This cannot be undone."

### 14.7 Deleting all reflections

User opens Settings → Privacy → Delete all reflections. This is a power-user feature. The user is warned twice. On confirm, all reflections are deleted (overwritten) on the server. The local copies are deleted. The chapter and composition marks are preserved (they don't include reflection text).

### 14.8 Death of a user — see §20

If the user dies, the executor of the estate can request a data export. See §20 for the full workflow.

---

## 15. Empty states

The product has many empty states. Each is designed to be quiet, not shamed.

### 15.1 First install, no movements yet

The home screen shows the first movement immediately. There is no "empty home" state.

### 15.2 Solo user, no Section

The heart icon is hidden. The bottom of the home screen is clean.

### 15.3 No reflections yet

The reflection field shows the placeholder: "(optional) write a reflection..."

### 15.4 No chapter history (first week)

The chapter dots show: ◯ ◯ ◯ ◯ ◯ ◯ ◯. Tapping shows: "Your first chapter is in progress. Complete today to fill the first dot."

### 15.5 No composition history (first year)

The composition dots show: ◯ ◯ ◯ ... (52 dots, mostly empty). Tapping shows: "Your first composition is in progress. Complete chapters to fill the dots."

### 15.6 Section with only 1 member (everyone else left)

The Section view shows: "You're the only one left in The morning crew. You can invite more people, or dissolve the Section." The user can still practice with the Section — the practice is logged, just no one else to see it.

### 15.7 No notifications enabled

The settings → notifications page shows: "All quiet. You can enable notifications from this page or your device settings."

### 15.8 No paid features used

The settings → subscription page shows: "Free tier. You have access to [list of free features]." No upsell modal. No "Upgrade to unlock" buttons elsewhere in the app.

---

## 16. Error states

The product has very few error states, because the product is designed to be resilient (offline-first, fallback movements, etc.). But some are unavoidable.

### 16.1 Sign-in failure

User sees: "Sign-in failed. Check your connection and try again. [Retry] [Use a different account]"

### 16.2 Movement generation failure (LLM down)

The user sees the fallback movement from the curated pool. No error message. The user does not know the LLM was involved.

### 16.3 Reflection save failure (network)

The reflection is queued locally. The user sees: "Saved on this device. We'll sync when you're back online." A small cloud icon with a slash appears next to the reflection.

### 16.4 Section data unavailable

The heart icon is dimmed. The Section view shows: "Section data unavailable. Pull to refresh." Tapping the dimmed heart does nothing.

### 16.5 Account locked (after too many failed sign-in attempts)

The user sees: "Your account is temporarily locked for your security. Try again in [X minutes]." This is a system-level lockout, not a product decision.

### 16.6 Out of storage (device)

The product warns the user: "Your device is low on storage. Cadence needs [X] MB to function properly. Free up some space or contact support."

### 16.7 Out of date (app version)

The user sees a soft prompt: "A new version of Cadence is available. [Update] [Later]". The app still functions. The user can update at their convenience.

### 16.8 Reflection decryption failure (lost key)

The user sees: "This reflection is encrypted with a key that's not on this device. [Restore from another device] [Skip]". The reflection is unreadable but not deleted.

---

## 17. Locale and timezone workflows

### 17.1 Locale auto-detection

On first launch, the device locale is detected. If the locale is in our day-90 list, it is used. If the locale is in our day-180 list, the user is offered to use it (in beta) or to fall back to English/Spanish. If the locale is unsupported, the user is offered the closest supported locale.

### 17.2 Locale change in settings

User can change the locale at any time. The change is instant. The user is warned: "Changing your locale will switch verse translations. Your reflections stay in your own words."

### 17.3 Ambiguous locales

If the device locale is ambiguous (e.g., `zh`), the user is asked to pick: 简体中文 or 繁體中文.

### 17.4 Timezone auto-detection

On first launch, the device timezone is detected. The user can override in Settings.

### 17.5 Timezone change (travel)

The home screen updates to the new timezone immediately. The movement content is in the user's home locale. The chapter day boundary is in the user's *home* timezone (per §4.1).

### 17.6 Locale and Section

Each Section member uses their own locale. The Section is locale-agnostic. The prompt and verse shown to each member is in their own locale.

### 17.7 Locale and reflections

Reflections are in the user's own words, not translated. The user can write in any language regardless of the app locale.

### 17.8 RTL locales (Arabic, Hebrew)

The design system is RTL-ready. When these locales ship, the entire UI mirrors. The Section view mirrors. The chapter detail view mirrors.

The reflection field is LTR or RTL depending on the user's input. The app does not force a direction.

---

## 18. Privacy and data workflows

### 18.1 Export data

User opens Settings → Privacy → Export my data. The export is generated client-side. The file is offered through the system share sheet.

The export includes:
- All movements and verses (in the user's current locale)
- All reflections (decrypted, in the user's own words)
- All chapter marks
- All composition marks
- The user's account email and preferences
- Section metadata (name, cadence, member names) — but **not** Section practice signals (they're E2E encrypted and we can't read them)

The export format: JSON (machine-readable) or PDF (human-readable). The user picks.

### 18.2 Delete account

User opens Settings → Privacy → Delete account. The user is warned twice:

1. "This will permanently delete your account and all associated data from Cadence. Your history, reflections, and Section memberships will be gone. This cannot be undone."
2. "Are you absolutely sure? Type DELETE to confirm."

The user types DELETE. The account is marked for deletion. The user is signed out immediately. All server data is deleted within 7 days. Local data is deleted immediately on sign-out.

**Caveat:** the user cannot delete Section data. The Section key is held by all members. If the user wants the Section data gone, they have to ask the Section creator to dissolve the Section.

### 18.3 Privacy policy and ToS

In Settings → Privacy → Privacy policy / Terms of use. Opens in the in-app browser. Locale-aware (the user sees the policy in their locale).

### 18.4 Contact support

In Settings → Help & support. Opens the support email composer (mailto:hello@cadence.app). Or, in iOS, opens the in-app support form. The user can attach screenshots.

Support is staffed during business hours (9am-5pm PT). The user can expect a response within 24 hours.

---

## 19. Account lifecycle (creation → deletion)

### 19.1 Creation

User signs in with Apple, Google, or email. The account is created. The user is dropped into the cadence picker.

### 19.2 Active use

User uses the product. Daily movements, weekly chapters, yearly compositions.

### 19.3 Pause

User opens Settings → Pause practice. The home screen enters the paused state. The user can resume at any time.

The account remains active. The subscription (if any) continues to renew. The user can cancel the subscription at any time.

### 19.4 Subscription lapse

The user's paid subscription expires. The user is downgraded to free tier after a 7-day grace period. The account remains active.

### 19.5 Account deletion

User opens Settings → Delete account. The account is marked for deletion. The user is signed out. All data is deleted within 7 days.

### 19.6 Account recovery

User can sign back in within 7 days of deletion request. After 7 days, the account is permanently gone.

### 19.7 Account compromise

User opens Settings → Sign out everywhere. All devices are signed out. The user signs back in on their trusted device. If the user can't access their account, they contact support.

---

## 20. The death of a user

A user dies. Their family or executor wants their data. The product has a procedure.

### 20.1 The user's data

The user can pre-arrange this. Settings → Privacy → Legacy access. The user can designate an email address (e.g., a family member) that can request a data export in the event of the user's death.

The designated email is stored in the user's account. If the user does not designate one, the default is: no one. The data is deleted with the account.

### 20.2 The executor's request

The executor emails support@cadence.app with:
- The deceased user's email
- A death certificate (or other legal proof)
- The executor's identity (passport, driver's license)
- A statement of relationship

The support team verifies the request. If approved, the data export is generated. The export is sent to the executor via a one-time download link (valid for 7 days).

The export includes:
- All movements and verses
- All reflections (decrypted)
- All chapter and composition marks
- The account email and preferences

The export does **not** include Section data (it's E2E encrypted and we can't read it).

### 20.3 What Cadence does not do

- Cadence does not memorialize the account. There is no "in memoriam" state.
- Cadence does not allow the executor to "post" anything in the deceased's name.
- Cadence does not convert the account to a public profile.

The data is given to the executor, in private, and that's it. The product is not a social network. The user's data is theirs, and after death, it's their family's.

---

## Closing notes

This document is the operational spec. The PRD is the elevator. PHILOSOPHY.md is the why. This is the **every micro-moment that compounds into a practice.**

When in doubt, return to the three mechanisms and the philosophy. If a workflow can't be traced to one of the three mechanisms, with a guardrail that protects the user, it doesn't ship.

The product is the practice. The practice is the user. The user is a whole person.

— end —
