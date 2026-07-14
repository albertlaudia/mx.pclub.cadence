# Cadence

> A rhythmic, daily, faith-led habit platform — built on the three mechanisms that make apps feel inevitable, applied with the guardrails that keep them honest.

**Tagline:** *One movement a day. A rhythm you can keep.*

**Repo:** `albertlaudia/mx.pclub.cadence` (architecture, manifesto, and product spec)
**Org prefix:** `mx.pclub.*` (pclub product family)
**Sibling apps:** `mx.pclub.caloriecounter`, `mx.pclub.pulse`, `mx.pclub.web`

---

## What Cadence is

A daily practice platform that helps a person build a long, compounding, deeply personal rhythm — whether that's prayer, scripture, gratitude, exercise, learning, or whatever the user names as their movement.

The user picks **one cadence** (a rhythm with a name and a shape: e.g., *Morning Psalms*, *Daily Quiet*, *The Lent Arc*). The platform plays back a **movement** every day — a short, contextual practice shaped by the user's week, time of day, mood signal, and prior movements. The movement is *novel within a familiar shape*. The user never knows exactly what today's movement will be, but they know it will be short, useful, and made for them.

Cadence is **not** a streak counter, a points system, or a leaderboard. The retention comes from the *quality of the practice*, not the *quantity of the score*. This is a deliberate, non-PBL (no points / badges / leaderboards) design — and it's also the most direct application of the three psychological mechanisms that make apps feel inevitable.

---

## The three mechanisms

Every "can't-stop" app is built on three things. Cadence uses all three — but **transparently, and with the user's dignity intact**.

### 1. The Craving Machine — variable ratio reinforcement

The brain chases the *possibility* of reward, not the reward itself. Variable rewards (Skinner) build the strongest habits. Cadence applies this to *content*, not *prizes*: every day's movement is generated from the user's state, the calendar, and the prior week's arc, so it never feels rote. The user opens the app not knowing what they'll get — but they know it will be useful, short, and made for them.

**Guardrail:** The unpredictability is in the *content*, not the *outcome*. No loot boxes. No random "bonus rewards". The user can always preview tomorrow's movement if they want.

### 2. The Infinite Game — no terminal state, real loss aversion

A cadence is a lifelong rhythm. The user never "finishes" Cadence — but they're never on a treadmill either. Each week is a **movement**, each month is a **chapter**, each year is a **composition**. The arc is real, multi-year, and always shows the next beat. Stopping is painful not because of a streak counter, but because the *practice* — the actual quiet, the actual prayer, the actual conversation with God — is hard to give up once it becomes part of a day.

**Guardrail:** Quitting is allowed and non-shaming. The user can pause, archive, return. The loss aversion is in the *practice*, not the *number*. There is no fake "you're 80% to level 10".

### 3. The Invisible Scoreboard — intimate visibility, not public

Humans don't stick to things because of leaderboards. They stick because *someone they chose to play with* will notice if they stop. Cadence ships a primitive called **The Section** — a small, named, chosen circle of 2–7 people. They can see each other's *practice days* (a quiet heart, a chapter mark, never a number). No public profile, no social graph, no "share to unlock" mechanics. The visibility is *intimate*, not performative.

**Guardrail:** Solo practice is fully supported and never penalized. The Section is opt-in, configurable, and never required. No third-party social graph integration. No public profile pages.

---

## Why this matters

Most consumer apps use these three mechanisms, but with PBL mechanics bolted on top: points, badges, leaderboards. Those create a 30-day spike and then a retention crater. The mechanisms work; the PBL is the part that fails. Cadence uses the mechanisms directly, without the PBL.

This is the *smarter and sharper* version: same retention force, no exploitative wrapper.

---

## What's in this repo

This repo is the **architecture, manifesto, and product spec** for Cadence. The actual app code lives in the monorepo, which will be initialized once the spec is locked. Files here:

- `PHILOSOPHY.md` — **the deepest layer.** The why underneath the why. Read this first.
- `README.md` — this file. What Cadence is, why it exists, the three mechanisms.
- `docs/ARCHITECTURE.md` — technical architecture: client, backend, data, sync, costs.
- `docs/RETENTION.md` — the three mechanisms, mapped to specific features and guardrails.
- `docs/PRIVACY.md` — what data Cadence collects, what it doesn't, and why there's no AccessibilityService.
- `docs/PRD.md` — product requirements: the "today" experience, the "week" experience, the "year" experience.
- `docs/LOCALIZATION.md` — the FR/PT/ZH/ES/EN/TL/JA/KO localization plan, with content parity as a first-class goal.
- `LICENSE` — MIT for the documentation. The product code is closed-source (see `LICENSE`).
- `.github/ISSUE_TEMPLATE/` — bug report, feature request, design discussion.

---

## How to read this repo

1. Read `PHILOSOPHY.md` — the why.
2. Read `README.md` (you're here) — the what.
3. Read `docs/RETENTION.md` to see the three mechanisms translated into features.
4. Read `docs/ARCHITECTURE.md` to see the system that delivers them.
5. Read `docs/PRIVACY.md` to see the boundaries.

If you're a contributor, start with `docs/RETENTION.md` — every feature in this product maps to one of the three mechanisms, and the guardrail tells you how to ship it without crossing the line.

---

## Status

**v0.1 — manifesto + architecture**
- [x] Three mechanisms translated into product features
- [x] Architecture spec drafted
- [x] Privacy boundaries defined
- [x] Localization plan sketched
- [ ] Monorepo scaffolded (`apps/mobile`, `apps/api`, `packages/content`)
- [ ] First vertical slice: "one movement a day" end-to-end
- [ ] Internal alpha (5 users, 14 days)
- [ ] External beta (50 users, 60 days)

---

## Lineage

This is the *smarter, sharper* version of the lessons learned from:

- **Prayer Lock** — showed the *app-blocker-as-prayer* wedge works, but mandatory subscription + AccessibilityService scare the audience. Cadence has neither.
- **PULSE** — showed the *lonely-companion* wedge is real. Cadence adds the Section, so the practice is not lonely by default.
- **HEAL** — showed *audio + cadence* compounds. Cadence leans on this hard.
- **Connect** — showed *intake-driven onboarding* converts. Cadence uses a 3-step intake (name the cadence, name the section, name the practice window) instead of a survey.
- **Wordie / 1perc** — showed *content generation + curation* can scale without an editor in the loop. Cadence's movement generator follows the same pattern.

---

## License

Documentation: MIT. See `LICENSE`.

Product code: closed-source, all rights reserved. (When the monorepo is initialized.)
