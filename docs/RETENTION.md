# Retention — The Three Mechanisms, Applied

> *"Addictive" app retention comes from architecture, not decorations.* — The Weird Science of Apps You Can't Stop Using

This document maps the three psychological mechanisms that drive long-term retention to **specific features** in Cadence, and pairs each with the **guardrail** that keeps the feature honest.

The TL;DR rule: **every feature in Cadence maps to one (and only one) of the three mechanisms, and ships with a guardrail that protects the user.**

---

## 1. The Craving Machine — variable ratio reinforcement

### The mechanism

The brain chases the *possibility* of reward, not the reward itself. B.F. Skinner's variable ratio reinforcement: behaviors rewarded on unpredictable schedules are the most resistant to extinction. Slot machines work this way. So does Instagram. So does a really good book — you don't know what the next page holds, so you keep reading.

### How it works in Cadence

**Feature: "Today's Movement"**

Every day, Cadence generates a 60-90 second movement for the user:
- A short prompt (a question, a sentence to complete, a quiet observation)
- An optional Bible verse / quote / passage contextual to the prompt
- A 30-second reflection slot
- A 1-tap "done" that records the practice and shows the next chapter mark

The *shape* is predictable. The *content* is novel. The user opens Cadence knowing they'll get something short and useful, but not knowing what *today's* thing will be. That's the variable.

**Why it's ethical here:** The variable is in the *content*, not in the *outcome*. There's no prize. There's no surprise reward. The reward is the practice itself — the reflection, the verse, the quiet. The user is not chasing a slot machine; they're chasing a moment of attention. The mechanism is the same, but the *thing being chased* is something the user actually values.

### Specific tactics

| Tactic | What it looks like in Cadence | Guardrail |
|---|---|---|
| Time-of-day shaping | Morning cadence gets psalms / gratitude / quiet; evening cadence gets examen / confession / peace | User can override. No "you should be doing this at this time" copy. |
| Weekly arc | Day 1–7: opening. Day 8–14: depth. Day 15–21: push. Day 22–28: integration. | The arc is invisible to the user unless they look. It never says "Day 14 of 28" — just the chapter mark. |
| Mood signal | A pre-movement 1-tap mood check (3 options: low / steady / bright) | Optional, never required. Skipping it still gives a full movement. |
| Surprise bonus | ~10% of days include a "Bonus Movement" — a longer, richer practice (e.g., a guided 5-min examen) | Bonuses are not rewards for streaks. They appear unpredictably *to everyone*, not as a carrot. |
| Preview tomorrow | User can tap "preview tomorrow's movement" if they want | Always available, never paywalled. Transparency beats withholding. |

### What Cadence does NOT do

- No loot boxes. No random "you won a 7-day streak free!" pop-ups.
- No A/B test that withholds a prayer to see if the user comes back faster.
- No dark-pattern scarcity ("Only 3 bonus movements left this month!").

---

## 2. The Infinite Game — loss aversion, no terminal state

### The mechanism

Losses hurt ~2x as much as equivalent gains feel good (Kahneman & Tversky, Prospect Theory). A streak is powerful because *losing* it is painful — even when the streak was artificial. The second mechanism: avoid ever reaching a "done" state. The user should never feel they "finished" the product. The best apps make stopping feel like leaving a conversation in the middle, not closing a checklist.

### How it works in Cadence

**Feature: "The Long Arc"**

Cadence is structured as a **composition**:
- **Movement** = one day (a beat in the larger piece)
- **Chapter** = one week (a phrase)
- **Composition** = one year (the whole work)
- **The Long Arc** = multiple years (the user's lifetime practice)

The user can see the *current chapter* and the *next* one. They cannot see a "completion" state — there isn't one. The arc is genuinely lifelong, not artificially extended.

**Why it's ethical here:** The loss aversion is in the *practice*, not the *number*. If the user stops opening the app, they don't lose a streak counter — they lose the actual quiet, the actual prayer, the actual daily check-in with God. The mechanism is the same, but the *thing being lost* is something the user values. The user can pause, archive, and return without penalty.

### Specific tactics

| Tactic | What it looks like in Cadence | Guardrail |
|---|---|---|
| Multi-year structure | A composition spans a year. The next composition starts automatically. | User can switch compositions anytime. "Daily Quiet" is a valid composition; "Lent" is a valid composition. |
| Chapter mark | End of each chapter: a 1-page summary of the arc, the verses that surfaced, the mood pattern. | Free tier sees last 4 chapters. Paid tier sees the full history. |
| Pause + return | User can pause for a week / month / season. Cadence greets them on return with "Welcome back. Here's where you were." | No "you lost 23 days!" shame copy. No "missed you!" dark-pattern push. |
| Composition archive | Past compositions are kept forever, accessible from a single tap. | Never paywalled to "unlock" the user's own history. |
| Open-ended verse pool | The verse / quote / passage library is curated and growing — never exhausted. | No "you've seen every verse" completion state. The pool is open. |

### What Cadence does NOT do

- No "Day 30 of 365" countdown. The number is internal; the user sees chapters, not days.
- No fake "you're 80% to level 10". Levels mean something (e.g., 100 chapters completed) — not a manufactured progress bar.
- No "streak repair" paywall ("Pay $4.99 to restore your 23-day streak"). That's the worst of PBL.

---

## 3. The Invisible Scoreboard — intimate visibility, not public

### The mechanism

Public visibility of progression makes quitting *identity-relevant*. Stopping becomes "I admitted to others I stopped" — not just "I privately decided to quit." This is the third mechanism, and the one that makes the first two irreversible.

### How it works in Cadence

**Feature: "The Section"**

A Section is a small, named, chosen circle of **2–7 people** who play the same cadence. The user can create one or join one. They see each other's *practice days* (a quiet heart, a chapter mark) — never a number, never a score, never a rank. The Section is opt-in and never required to use the product.

**Why it's ethical here:** The visibility is *intimate*, not performative. There's no public profile, no global leaderboard, no "share to unlock" mechanism. The Section is to a habit what a small ensemble is to a piece of music — you practice with people you chose, and they notice if you stop showing up. That's the mechanism. There's nothing to game, nothing to post, nothing to perform.

### Specific tactics

| Tactic | What it looks like in Cadence | Guardrail |
|---|---|---|
| Section size cap | 2–7 people, hard cap | Solo practice is the default. The Section is an additive, not a requirement. |
| What others see | A quiet heart on the day you practiced. A chapter mark. Never a number. | The user controls what they share. Default is "just the heart". |
| Section invite | User generates a link, sends to up to 7 people. | No contact scraping. No "find your friends" via social graph. |
| Section privacy | All Section data is end-to-end encrypted. Cadence cannot see who is in your Section. | Privacy is structural, not policy. We can't leak what we can't read. |
| Section language | "Your Section" / "Your ensemble" / "Your circle" — never "Your leaderboard" or "Your team". | Copy is curated. The frame is musical, not competitive. |
| Section lifecycle | A Section can be dissolved by any member. No "you left your Section" guilt copy. | Dissolving is one tap. The remaining members get a quiet notice. |

### What Cadence does NOT do

- No global leaderboard. Ever.
- No public profile pages. Ever.
- No "share to unlock" mechanics. Section features don't require posting publicly.
- No social graph integration (no Facebook friend finder, no contact list scraping).
- No "Your Section vs Other Sections" competitive framing.

---

## How the three mechanisms stack

The video's core insight: **the mechanisms stack.**

- **Craving alone** = the user keeps coming back, but can walk away.
- **Craving + Infinite Game** = the user is engaged and the cost of leaving grows.
- **Craving + Infinite Game + Invisible Scoreboard** = the user is engaged, leaving is costly, and leaving is *socially visible*. The retention is now architectural, not motivational.

Cadence ships all three — but the **Invisible Scoreboard is the smallest** by design. The Section is opt-in, capped at 7, and structurally private. The user has to *want* the social layer to get it.

The majority of users will use Cadence solo. The platform is designed to be excellent for them. The Section is the additive for users who want the social layer — and for those users, it's the difference between a habit and a practice.

---

## Anti-PBL design checklist

Before shipping any feature, run it through this list:

- [ ] Does this feature map to one (and only one) of the three mechanisms?
- [ ] Is the variable in *content*, not *outcome*?
- [ ] Is the loss in *practice*, not *number*?
- [ ] Is the visibility *intimate*, not *public*?
- [ ] Is the solo path as good as the social path?
- [ ] Can the user opt out without losing any of the core experience?
- [ ] Is the copy honest about what the feature is doing?

If any answer is "no", the feature goes back to design.

---

## What we measure

Cadence measures *practice quality*, not practice quantity:

- **Primary:** Did the user complete today's movement? (binary, per day)
- **Secondary:** Did the user come back tomorrow? (binary, per day)
- **Tertiary:** Did the user finish a chapter? (binary, per week)
- **Survey:** Weekly 1-question: "Did this practice meet you where you were?" (5-point scale)

What we **do not** measure:
- Number of app opens
- Time spent in the app
- Taps, scrolls, or any micro-engagement signal
- Whether the user opened the app but didn't complete the movement

We don't measure these because optimizing for them is exactly the PBL trap. The only thing worth optimizing is: *did the practice meet the user?*

---

## References

- The Weird Science of Apps You Can't Stop Using (YouTube, 2026) — the source of the three-mechanism framework
- B.F. Skinner, *The Behavior of Organisms* (1938) — variable ratio reinforcement
- Daniel Kahneman & Amos Tversky, *Prospect Theory* (1979) — loss aversion
- Leon Festinger, *A Theory of Social Comparison Processes* (1954) — social comparison
- Internal lesson (pclub memory, 2026-07): "Engagement design: avoid PBL traps" — see AGENTS.md
