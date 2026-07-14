# Architecture

> The system that delivers a daily movement, an intimate Section, and a multi-year composition — without a PBL trap in sight.

This document is the **technical architecture** for Cadence. It maps directly to `docs/RETENTION.md`: each mechanism has a feature, each feature has a system, each system has a guardrail.

---

## System overview

```
┌─────────────────────────────────────────────────────────────┐
│                        Cadence                             │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   Mobile     │    │   Web App    │    │   Wearable   │  │
│  │   (Flutter)  │    │   (Next.js)  │    │  (WatchOS)   │  │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
│         │                   │                   │          │
│         └─────────┬─────────┴─────────┬─────────┘          │
│                   │                   │                    │
│              ┌────▼────┐         ┌────▼────┐                │
│              │  Auth   │         │  Sync   │                │
│              │Firebase │         │ Realtime│                │
│              └────┬────┘         └────┬────┘                │
│                   │                   │                    │
│         ┌─────────▼───────────────────▼─────────┐          │
│         │            Edge (Cloud Run)           │          │
│         │     - movement generator              │          │
│         │     - Section coordination            │          │
│         │     - composition archiver            │          │
│         └─────────┬───────────────────┬─────────┘          │
│                   │                   │                    │
│         ┌─────────▼────┐     ┌─────────▼────┐               │
│         │  Firestore   │     │  Cloud SQL   │               │
│         │  (user state)│     │  (compos.)   │               │
│         └─────────┬────┘     └─────────┬────┘               │
│                   │                   │                    │
│         ┌─────────▼───────────────────▼─────────┐          │
│         │     Content + Models Layer            │          │
│         │  - curated verse library               │          │
│         │  - LLM movement generator (variable)   │          │
│         │  - chapter composer (weekly)           │          │
│         └───────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

---

## Why this stack

The pclub family uses a consistent pattern: **Flutter mobile + Next.js web + Firebase + GCP**. Cadence follows the pattern. Reuse over reinvention.

| Choice | Why |
|---|---|
| **Flutter** (iOS + Android) | Single codebase, fast iteration, pattern from `mx.pclub.caloriecounter`, `mx.pclub.pulse` |
| **Next.js** (web) | SEO for the marketing site, plus a web app for users on a laptop. Pattern from `mx.pclub.web` |
| **Firebase Auth** | Frictionless sign-in, Apple/Google/email, the same auth as the rest of the pclub apps |
| **Firestore** (user state) | Real-time, scales, works well with the Section's "did your friend practice today?" query |
| **Cloud SQL** (Postgres) | The composition archive, the chapter summaries, the verse library — relational, queryable |
| **Cloud Run** (edge) | The movement generator and Section coordination. Stateless. Scales to zero. |
| **GCP-native** | We're already on GCP. No new vendor. |
| **No accessibility services** | See `docs/PRIVACY.md` for the full argument. |
| **No ad SDKs** | Cadence is not an ad product. Never will be. |

---

## The three mechanisms → three systems

### 1. Movement generator (Craving Machine)

The variable in the variable ratio.

**Inputs:**
- User's current cadence (the rhythm they picked: e.g., "Morning Psalms")
- Time of day (morning / midday / evening)
- Day of the week (the weekly arc: opening / depth / push / integration)
- Day in the composition (so the content can climb across a year)
- Mood signal (optional, from the user)
- Last 7 days of practice (to avoid repetition)
- Section activity (subtly — if a Section member just practiced, the generator leans into the same vein)

**Pipeline:**
1. Pull a candidate pool: 3–5 verses, 3–5 prompts, 1 chapter context note
2. LLM (Anthropic Claude, small model) generates the 60-90s movement: prompt + verse + reflection
3. Tone-moderator: checks for denominational sensitivity (no Christological bias unless the user's cadence specifies it)
4. Cache the result in Firestore under `users/{uid}/movements/{date}`
5. If the date is a "bonus movement" day (~10%), generate a longer 3-5 min movement

**Cost:**
- ~150 tokens in, ~600 tokens out per movement
- With caching (each user gets 1 movement/day), a 1K-user day = 1.5M tokens
- At Claude Sonnet pricing, that's roughly $9/day for 1K daily active users
- For 10K DAU: ~$90/day
- For 100K DAU: ~$900/day
- We can switch to a smaller model (Haiku) for non-bonus days and cut this by ~5x

**Guardrail:**
- The LLM never sees the user's content from other apps. Period. The prompt is scoped to the cadence inputs only.
- The LLM prompt includes a "no manipulative copy" instruction. Reviewers spot-check 1% of generated movements.
- If the LLM is down, we fall back to the curated pool. The user always gets a movement.

### 2. Composition archiver (Infinite Game)

The thing that makes stopping painful in the *practice*, not the *number*.

**Inputs:**
- The 7 movements from the past week
- The mood signals from the past week
- The Section activity for the week (without revealing specifics)

**Pipeline:**
1. End of chapter (every 7 days): generate a chapter summary
   - The 3 verses that surfaced most often in the user's movements
   - The 2 prompts that landed best (which the user kept open longest)
   - A short, beautiful 1-paragraph arc note ("This week your practice was mostly about patience. The verses leaned into waiting.")
2. Archive the chapter in Cloud SQL under `compositions/{uid}/{year}/{chapter}`
3. Update the user's "current chapter" pointer in Firestore
4. The user sees: a quiet chapter mark, a 1-paragraph note, the verses

**Cost:**
- One LLM call per chapter, per user = ~$0.02 / user / week
- Negligible

**Guardrail:**
- The chapter summary is *true to the data*. No "growth" or "transformation" copy unless the data supports it.
- The user can opt out of LLM-generated summaries and just see a list of the 7 movements.

### 3. Section coordination (Invisible Scoreboard)

The thing that makes stopping identity-relevant, in a small intimate circle.

**Inputs:**
- Section membership (2–7 users, all in the same cadence)
- Today's practice signal (boolean: did you complete today's movement?)

**Pipeline:**
1. End of each user's "day" (their local time, not server time): they post a single `practiced=true` flag to their Section
2. The flag is propagated to Section members via Firestore listeners
3. Each Section member sees: the quiet heart on the day, the chapter mark, never a number
4. No "you broke your streak" copy. No "your Section is at 5/7" copy. Just: the heart, the mark.

**Privacy:**
- Section data is end-to-end encrypted. Cadence cannot see who is in a Section.
- The Section invite is a one-time token, expires in 24h.
- A Section can be dissolved by any member, immediately, no questions.
- Solo practice has zero social layer. The Section is opt-in only.

**Cost:**
- One Firestore write per Section member per day = 7 writes for a 7-person Section
- At 100K DAU, 50% in Sections = 50K Section-active users, average Section size 4 = ~200K writes/day
- Negligible (well under Firestore free tier)

**Guardrail:**
- No "compare your Section to other Sections" feature. Ever.
- No "Section leaderboard within your Section". Ever.
- No "Section streak counter". Ever.
- The Section sees *practice days*, not *streak length*.

---

## Data model (high-level)

```
users/{uid}
  - email
  - displayName
  - currentCadence: "morning-psalms" | "daily-quiet" | ...
  - currentComposition: "2026-psalms"
  - currentChapter: 14  (1-52)
  - sectionId: <ref>     (optional)
  - locale: "en"
  - timezone: "America/Los_Angeles"
  - freeUntil: <ts>      (paid tier expires)
  - createdAt: <ts>

users/{uid}/movements/{date}
  - prompt: string
  - verse: { ref, text, translation }
  - reflection: string
  - completed: bool
  - completedAt: <ts>
  - durationSeconds: int

sections/{sectionId}
  - name: "the morning crew"
  - members: [uid1, uid2, ...]  (2-7)
  - cadence: "morning-psalms"
  - createdAt: <ts>
  - createdBy: uid

compositions/{uid}/{year}/{chapter}
  - week: 14
  - versesSurfaced: [...]
  - promptSummary: "..."
  - arcNote: "..."

contentLibrary/verses
  - { ref, text, translations: { esv, niv, nlt, ... } }

contentLibrary/prompts
  - { id, text, tags, denominations: ["catholic", "protestant", ...] }
```

---

## The "free vs paid" line

Cadence is **not** a mandatory-subscription product. The free tier is real, complete, and doesn't gate the core experience.

| Feature | Free | Paid |
|---|---|---|
| One daily movement | ✓ | ✓ |
| One Section (up to 7) | ✓ | ✓ |
| Current chapter summary | ✓ | ✓ |
| Localized content (EN, ES, FR, PT, ZH, JA, KO, TL) | ✓ | ✓ |
| 7-day preview of tomorrow's movement | ✓ | ✓ |
| Last 4 chapters archived | ✓ | ✓ |
| **Full composition history (52+ weeks)** | ✗ | ✓ |
| **Unlimited Sections** | ✗ (1 max) | ✓ |
| **Voice playback of the movement** | ✗ | ✓ |
| **Custom cadence (user-named rhythm)** | ✗ | ✓ |
| **Apple Watch / Wear OS app** | ✗ | ✓ |

Paid is a true upgrade, not a paywall. Solo practice is fully free.

---

## Localization

Localization is the product, not an afterthought.

- **Day-one locales:** EN, ES (Prayer Lock taught us this is non-negotiable)
- **Day-30 locales:** PT (BR), FR, ZH (Hans + Hant)
- **Day-90 locales:** JA, KO, TL (Tagalog — Philippines is a meaningful faith market)
- **All verse translations** in the library are pre-translated. The LLM-generated *prompts* and *arc notes* are translated at generation time, not at runtime (so we can review before they ship).
- **Right-to-left** (Arabic, Hebrew) is in the design system from day one, even if we don't ship it on day one.

See `docs/LOCALIZATION.md` for the full plan.

---

## What Cadence does NOT do

- **No AccessibilityService.** Never. (See `docs/PRIVACY.md`.)
- **No ad SDKs.** Never.
- **No third-party analytics beyond Firebase.** No Mixpanel, no Amplitude, no Segment.
- **No social graph integration.** No Facebook friend finder, no contact list scraping.
- **No public profile pages.** No "share my practice" social posts.
- **No global leaderboard.** No "compare to other users" anything.
- **No "streak repair" paywall.** No "you broke your streak, pay to restore" nonsense.
- **No A/B test that withholds a movement to see if the user comes back faster.**

---

## Build phases

**Phase 0 — Manifesto (this repo, current state)**
- [x] Three mechanisms translated
- [x] Architecture spec
- [x] Privacy boundaries
- [x] Localization plan
- Status: ✅ done

**Phase 1 — Monorepo scaffold (next 1-2 weeks)**
- [ ] `apps/mobile` (Flutter, iOS + Android)
- [ ] `apps/web` (Next.js, marketing + web app)
- [ ] `apps/api` (Cloud Run, movement generator + Section coord)
- [ ] `packages/content` (verse library, prompt pool)
- [ ] `packages/auth` (shared Firebase wrapper)
- [ ] `packages/ui` (shared design system)
- [ ] CI: GitHub Actions → TestFlight + Play Internal
- [ ] Auth: Firebase Auth with Apple/Google/email

**Phase 2 — First vertical slice (week 3-4)**
- [ ] "One movement a day" end-to-end on iOS
- [ ] Curated verse pool (200 verses, 4 translations)
- [ ] Curated prompt pool (100 prompts)
- [ ] LLM-generated movement (Claude Sonnet) with tone moderation
- [ ] Onboarding: name the cadence, name the Section (or skip)
- [ ] Movement screen: prompt + verse + reflection
- [ ] "Mark complete" + next chapter mark
- [ ] Localized in EN + ES

**Phase 3 — Internal alpha (week 5-6)**
- [ ] 5 internal users, 14 days
- [ ] Daily: do they complete the movement? do they come back tomorrow?
- [ ] Weekly: chapter summary lands well?
- [ ] Measure: NPS, qualitative interviews, "what's missing?"

**Phase 4 — Section + Android (week 7-8)**
- [ ] Section creation + invite flow
- [ ] Section privacy: E2E encryption
- [ ] Android app: parity with iOS
- [ ] Wearable: Apple Watch (movement on the wrist)
- [ ] Localized in EN, ES, PT, FR, ZH

**Phase 5 — External beta (week 9-12)**
- [ ] 50 external users across 4 locales
- [ ] Paid tier: composition history + voice playback
- [ ] App Store + Play Store listings
- [ ] Marketing site: cadence.app

**Phase 6 — Public launch (week 13+)**
- [ ] Public release on iOS + Android
- [ ] All 8 locales live
- [ ] Custom cadence feature
- [ ] Wear OS parity

---

## Open questions

- **What's the right LLM?** Claude Sonnet is the front-runner. Need to evaluate GPT-4o-mini and Gemini Flash for cost.
- **Section E2E encryption:** the simplest path is client-side encryption with a shared key derived from the Section's invite token. Need a security review before shipping.
- **Apple Watch app:** how much of the movement lives on the wrist? Probably just the prompt + verse + 1-tap "done". The reflection happens on the phone.
- **Custom cadence feature:** user-named rhythms. Are these free? Paid? The free tier should probably allow 1 custom cadence.

---

## References

- `docs/RETENTION.md` — the three mechanisms
- `docs/PRIVACY.md` — privacy boundaries
- `docs/PRD.md` — product requirements
- `docs/LOCALIZATION.md` — localization plan
- `mx.pclub.caloriecounter` — sibling app, Flutter + Firebase pattern
- `mx.pclub.pulse` — sibling app, async-companion UX
- `mx.pclub.web` — sibling app, Next.js + Firebase pattern
