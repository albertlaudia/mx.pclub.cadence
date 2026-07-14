# PRD — Product Requirements

> The "today", "week", and "year" experience of Cadence, in concrete terms.

This document is the **product spec** for Cadence. It's deliberately concrete: every screen, every tap, every day. If `docs/ARCHITECTURE.md` is *how we build it* and `docs/RETENTION.md` is *why it retains*, this is *what the user actually sees.*

---

## The one-paragraph elevator

Cadence is a daily practice app. The user picks a *cadence* (the rhythm they want to keep), names a *Section* (the small circle of 2-7 people who'll practice with them — or skips this and goes solo), and then every day they get a *movement* — a 60-90 second practice shaped to their day, their week, their year. They do the movement, tap "done", and the day is marked. Every week, the movements resolve into a chapter. Every year, the chapters resolve into a composition. The user is on a multi-year arc that's longer than their current view. The Section sees their quiet heart on the day they practiced. That's it. The product is the practice.

---

## Onboarding (first session, ~90 seconds)

The user opens Cadence for the first time. Three steps, no signup wall, no survey.

### Step 1: Name the cadence

> "What rhythm do you want to keep?"

A grid of pre-built cadences, each with a 1-sentence description:
- **Morning Psalms** — A 90-second quiet to start the day.
- **Daily Quiet** — A 60-second check-in, no scripture.
- **The Lent Arc** — 40 days of reflection.
- **Evening Examen** — A 90-second review of the day.
- **Gratitude Practice** — A 60-second thanks.
- **Custom cadence** — Name your own.

User picks one. (Free tier: 1 cadence. Paid: unlimited.)

### Step 2: Name the Section (or skip)

> "Who's practicing with you? Up to 7 people. Or skip and go solo."

Three options:
- **Create a Section** — Name it, generate an invite link, share it.
- **Join a Section** — Paste an invite link.
- **Skip for now** — Solo practice. Add a Section later.

The user can be in exactly one Section on the free tier, unlimited on paid.

### Step 3: Pick a practice window

> "When do you want to practice?"

A simple time-of-day selector: morning (6-9am), midday (11am-2pm), evening (8-10pm), or anytime. The user's timezone is set automatically from device locale.

The movement generator uses this window to time-shift the content (morning gets psalms, evening gets examen).

### That's it.

The user is in. No "tell us about yourself" survey. No "enable notifications" prompt. (Notifications are off by default. The user opts in from settings.)

---

## The "today" experience

### Home screen (the only screen most users see most days)

```
┌─────────────────────────────────────────┐
│                                         │
│            Good morning, Sarah.         │
│              Day 14 of your arc.        │
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
│  ◉ ◉ ◉ ◉ ◉ ◉ ◯ ◯ ◯ ◯ ◯ ◯ ◯  Week 2    │
│                                         │
│  § Your Section — 3 of 4 practiced      │
│    today.                               │
│                                         │
└─────────────────────────────────────────┘
```

The "week dots" are the chapter mark — a quiet visualization of the current week, not a streak counter. The user can see they're on day 6 of 7 this week. There's no "you missed day 3!" copy. Just dots.

The Section line is small, quiet, and below the fold. If the user has no Section, the line doesn't appear. If the user is in a Section, the line shows the practice count for today (a quiet "3 of 4"), never the names of who hasn't practiced.

### Movement screen

User taps "Begin reflection". The screen expands to show:

```
┌─────────────────────────────────────────┐
│                                         │
│      "What is one thing you are         │
│       carrying that you could set       │
│       down for an hour?"                │
│                                         │
│      ┌─────────────────────────────┐    │
│      │                             │    │
│      │  Cast your burden on the    │    │
│      │  Lord, and he will          │    │
│      │  sustain you.               │    │
│      │                             │    │
│      │  Psalm 55:22                │    │
│      │                             │    │
│      └─────────────────────────────┘    │
│                                         │
│      ┌─────────────────────────────┐    │
│      │  (optional) write a         │    │
│      │  reflection...              │    │
│      │                             │    │
│      └─────────────────────────────┘    │
│                                         │
│            [ Mark complete ]            │
│                                         │
└─────────────────────────────────────────┘
```

The reflection is **optional**. The user can mark complete without writing anything. The reflection is encrypted client-side; Cadence can't read it.

### Completion

When the user taps "Mark complete":
- The day gets a quiet heart on the home screen.
- The Section (if any) sees a quiet heart.
- A small "See you tomorrow" or "Rest well" message appears.
- The user closes the app.

No confetti. No "🔥 14-day streak!" No "share to Twitter!" No upsell to paid. Just a quiet acknowledgment.

---

## The "week" experience

End of the week (Sunday evening, or whenever the user's chapter ends):

The home screen shows a chapter mark, replacing the daily dots:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your week.                         │
│      Chapter 2, complete.               │
│                                         │
│  This week your practice leaned into    │
│  patience. The verses that surfaced     │
│  most: Psalm 27, Psalm 46,              │
│  Lamentations 3:22-23.                  │
│                                         │
│      [ Read the chapter ]               │
│                                         │
│  Next week: a new movement shape.       │
│                                         │
└─────────────────────────────────────────┘
```

The chapter summary is one paragraph, LLM-generated from the week's data. It's honest, beautiful, and short. The user can read it or skip it. The next week's movements are already queued.

---

## The "year" experience

End of the year (or end of the user's chosen composition):

The home screen shows a composition mark:

```
┌─────────────────────────────────────────┐
│                                         │
│      Your 2026 composition.             │
│      365 movements. 52 chapters.        │
│                                         │
│  You practiced 287 days.                │
│  Your busiest chapter was week 14.      │
│  Your quietest was week 47.             │
│  The verse that found you most:         │
│  Psalm 46:10 — "Be still, and know      │
│  that I am God."                        │
│                                         │
│      [ Read the composition ]           │
│      [ Start 2027 ]                     │
│                                         │
└─────────────────────────────────────────┘
```

The composition summary is the multi-year arc the user has built. It's not a score. It's a story.

---

## Section lifecycle

A Section is created in onboarding, or later from Settings → Section. The flow:

1. User names the Section ("The morning crew")
2. Picks a cadence (everyone in the Section practices the same one)
3. Generates an invite link
4. Sends the link to up to 7 people
5. Section members accept the invite, install the Section key
6. The Section is live

What the Section members see:
- A quiet heart on the day they each practiced
- A chapter mark when the week closes
- **Nothing else.** No number. No "your friend Sarah has a 47-day streak". No "your Section is at 5/7 this week".

What the Section members don't see:
- The names of who hasn't practiced (everyone's day is binary: heart or no heart, on the user's own home screen)
- The number of consecutive days anyone has practiced
- Any metric that would create social pressure

What happens when someone leaves:
- A quiet "Anna has left the Section" notice, no other detail
- The remaining Section members see the heart pattern shift, but no explanation

What happens when someone doesn't practice for a while:
- Nothing. The user just doesn't see a heart on that day. The Section doesn't comment.

---

## Notifications (off by default, opt-in)

Cadence is a quiet app. It does not nag. Notifications are off by default, and the user opts in from Settings.

When opted in:
- One notification per day, at the user's practice window
- The notification copy is: "Today's movement is ready." (Never "You haven't opened the app today!")
- The user can disable anytime

When not opted in:
- The user can still see the movement when they open the app
- No badge counts, no red dots, no "5 unread movements"

---

## Free vs paid

| Feature | Free | Paid |
|---|---|---|
| Daily movement | ✓ | ✓ |
| One Section (up to 7) | ✓ | ✓ |
| Current chapter summary | ✓ | ✓ |
| Localized content (8 locales) | ✓ | ✓ |
| 7-day preview | ✓ | ✓ |
| Last 4 chapters archived | ✓ | ✓ |
| **Full composition history** | ✗ | ✓ |
| **Unlimited Sections** | ✗ | ✓ |
| **Voice playback** | ✗ | ✓ |
| **Custom cadence** | ✗ | ✓ |
| **Apple Watch / Wear OS app** | ✗ | ✓ |

**Free is the default.** The free tier is a complete daily-practice experience, with all 8 locales, all 4 pre-built cadences, one Section, and 4 weeks of chapter history. Paid is a true upgrade, not a paywall.

The paid pitch is honest: "For $4.99/month, you get the full archive, unlimited Sections, voice playback, custom cadences, and the wearable app." Not "Unlock your spiritual potential". Not "Become a Premium Cadence member". The feature list, plainly stated.

---

## What we explicitly do not build

- **No public profile.** No "share my Cadence journey" social posts.
- **No global leaderboard.** No "Top Sections this month". No "Cadence Champions".
- **No streak counter.** No "Day 47!". No "🔥 47 day streak!".
- **No streak repair paywall.** No "Restore your streak for $4.99".
- **No app blocking.** No AccessibilityService. No "block Instagram until you pray".
- **No social graph integration.** No Facebook friend finder. No contact scraping.
- **No ad SDKs.** No third-party ad networks. Ever.
- **No A/B test that withholds a movement** to see if the user comes back faster.
- **No "share to unlock" mechanics.** Section features don't require posting publicly.

---

## Success metrics

**Primary (the only ones we optimize for):**
- Daily completion rate: % of users who complete today's movement (target: 65% on day 30, 50% on day 90)
- Day-7 retention: % of users who complete a movement on day 7 (target: 55%)
- Day-30 retention: % of users who complete a movement on day 30 (target: 40%)
- Section retention: % of Section members who are still in the Section at day 90 (target: 70%)

**Secondary (we look at these, don't optimize for them):**
- Weekly chapter summary read rate
- Section invite acceptance rate
- Free-to-paid conversion (target: 4% at 90 days)
- 30-day paid retention (target: 85%)
- NPS (target: 60+)

**Anti-metrics (we measure these to make sure we are NOT optimizing for them):**
- App opens per day per user
- Time spent in the app
- Notification tap rate
- "Share" button tap rate

If any anti-metric starts climbing faster than the primary metrics, we have a problem. The product is becoming engagement-extraction, not practice-delivery.

---

## Open questions

- **Section discovery:** should there be a public way to *find* Sections? Or is it invite-only forever? (Currently: invite-only. Public Section discovery is a PBL risk.)
- **Custom cadences:** free or paid? (Currently: paid. But maybe 1 free custom cadence is the right call.)
- **Reflection notes:** searchable? exportable? (Currently: end-to-end encrypted, user can export, but no in-app search across reflections.)
- **Voice playback on free tier:** TTS is cheap. Maybe voice should be free, and the paid upgrade is just the archive + Sections + wearables.

---

## References

- `docs/RETENTION.md` — the three mechanisms
- `docs/ARCHITECTURE.md` — the technical system
- `docs/PRIVACY.md` — the privacy boundaries
- `docs/LOCALIZATION.md` — the localization plan
