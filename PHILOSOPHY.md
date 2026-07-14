# Philosophy

> *The why underneath the why.*

This is the deepest layer. Below the mechanisms, below the architecture, below the features. The worldview that makes Cadence what it is — and the line that, once crossed, would make it something else.

If you only read one file in this repo, read this one. If you read three, read this one, `README.md`, and `docs/RETENTION.md`.

---

## 1. The user is a whole person, not an engagement metric.

Most consumer apps treat the user as a stream of behavioral signals to be optimized against. Open rate, time on app, tap-through, return frequency, conversion probability. Every product decision is justified by moving one of these numbers.

Cadence refuses this frame.

The user is a person. The person has a life. The life has noise — sick kids, a hard week at work, a season of grief, a travel month, a stretch where prayer feels empty. The product has to hold the person through the noise, not punish them for it.

If we ever find ourselves saying "this feature will lift our 30-day retention by 4% but it shames users who missed a day," we don't ship it. The metric moves; the person doesn't.

This is a hard rule to hold. Engagement metrics are how consumer companies are valued. But the goal of Cadence is not to be valued by consumers-of-attention. The goal is to be *useful* to a person who is trying to keep a rhythm in a noisy life. Different goal. Different rules.

---

## 2. The mechanisms work. PBL is the part that fails.

The video that inspired Cadence describes three psychological mechanisms — Craving Machine, Infinite Game, Invisible Scoreboard — and notes that they are "morally complicated." It is right. They are.

But it would be a mistake to conclude that the mechanisms are wrong and the PBL is right, or that the mechanisms are right and the PBL is wrong. The truth is more precise: **the mechanisms are load-bearing, and the PBL is the part that snaps.**

- The Craving Machine is the variable reward. It works because humans are wired to chase possibility, not certainty. Used honestly, this is the difference between a dull checklist and a meaningful practice.
- The Infinite Game is the loss aversion. It works because loss hurts more than gain satisfies. Used honestly, this is the difference between a habit that lasts three weeks and a practice that lasts a lifetime.
- The Invisible Scoreboard is the social visibility. It works because humans hold themselves accountable to other humans. Used honestly, this is the difference between practicing alone and practicing with a chosen circle.

PBL — points, badges, leaderboards — is the cheap version of these mechanisms. It substitutes an external score for an internal practice. It optimizes for the *appearance* of progress, not the *substance* of practice. It is what happens when a product team understands the mechanisms but does not respect the user.

Cadence uses the mechanisms. Cadence refuses the PBL.

This is the line.

---

## 3. Transparency is the antidote to manipulation.

The video is correct that the mechanisms are morally complicated. The complication is not the mechanism itself — it is the *opacity* of the mechanism. A user who doesn't know they are being nudged cannot consent to the nudge. A user who doesn't know they are being ranked cannot refuse the rank. A user who doesn't know their behavior is being shaped cannot choose otherwise.

Cadence ships the mechanisms *with the wiring diagram attached.* This is the doctrine of transparent architecture.

- The Craving Machine is visible in the "weekly arc" and the "preview tomorrow" feature. The user sees the rhythm. The user can preview what is coming. There is no surprise loot box, no hidden algorithm, no unpredictable penalty.
- The Infinite Game is visible in the chapter mark and the composition summary. The user sees the arc. The user sees the next chapter. There is no "day 23 of 365" countdown pressuring them; there is a quiet chapter mark saying "you're here."
- The Invisible Scoreboard is visible in the Section. The user sees who is in the Section, what they see, what they don't see. There is no "your friend Sarah has a 47-day streak" notification, no comparison meter, no "you fell behind your Section this week" copy.

A mechanism the user can see is a mechanism the user can consent to. A mechanism the user can consent to is a mechanism that builds trust instead of breaking it.

This is the only honest way to ship retention architecture.

---

## 4. The product shape determines the ethics.

Privacy is not a setting. It is a consequence of the product.

Prayer Lock needed cross-app blocking, so it needed AccessibilityService. AccessibilityService is a high-risk permission. The permission is a Google-flagged red flag. Users panic when they see it. Some leave bad reviews calling the app "fake" or "data-stealing" — not because the app is, but because the permission is alarming.

Cadence's product shape is *internal practice.* The user opens the app, has a moment, closes the app. Nothing about the practice requires reading the rest of the phone. So Cadence does not need AccessibilityService. The privacy boundary is a consequence of the right product shape, not a separate policy.

This is the deeper principle: **the most reliable privacy guarantee is a product that doesn't need the data.** The second most reliable is end-to-end encryption. The third is policy. The fourth is "trust us." Most apps live in the fourth tier. Cadence lives in the first.

This applies beyond privacy. The most reliable way to avoid streak-counter shame is a product without a streak counter. The most reliable way to avoid "share to unlock" is a product where nothing is gated behind sharing. The most reliable way to avoid social-graph creep is a product that does not have a social graph.

The product shape is the ethics. Choose the shape carefully.

---

## 5. The music, not the metrics.

Cadence is named after a musical term for a reason.

A musician's life is not a streak. A pianist does not say "I have a 4,732-day streak." A singer in a choir does not ask "what is my rank among tenors?" A composer does not check "what level am I?" These are the wrong frames.

A musician's life is a long arc of practice, in the company of a small ensemble, in pursuit of something they cannot fully articulate but can feel in the work. The practice is the point. The ensemble is the mirror. The arc is the meaning.

The chapter mark in Cadence is not a streak. It is a phrase in a longer piece. The Section is not a team. It is a small ensemble playing the same movement. The composition is not a year of points. It is one year of a life's work.

When the product team is unsure whether a feature is right, the question is: *does this fit the music?* A streak counter does not fit the music. A chapter mark does. A leaderboard does not fit the music. A Section does. A "level up!" notification does not fit the music. A quiet "see you tomorrow" does.

The frame matters. The frame is the philosophy in miniature.

---

## 6. Solo is the default. The Section is the gift.

Most social products are built backward: the social layer is the default, and the user has to opt *out* of it. This produces two failure modes — the user feels surveilled, or the user feels lonely. Both are wrong.

Cadence flips it. **Solo practice is the default. The Section is opt-in, capped at seven, end-to-end encrypted.** A user can use Cadence for a decade and never touch the Section. The product is excellent for them. They get the practice, the chapter marks, the composition summary, the quiet. They are not pestered to invite friends. They are not shown a "Section 0/7" empty state with a "find people" CTA.

The Section exists for users who want it, and it exists for a specific reason: the practice is private, but a chosen small circle can hold you to it in a way that a streak counter cannot. The Section is not a feature; it is a *gift* the user can give themselves.

This is the difference between a coach and a crowd. A coach knows you. A crowd watches you. Cadence is the coach.

---

## 7. The free tier is the product. The paid tier is a thank-you.

Prayer Lock's mandatory-subscription model is the worst of consumer faith apps. It charges the user before delivering the practice. It tells the user that the practice is a paid product, not a free act of attention. It makes the user a customer before they are a practitioner.

Cadence refuses this.

The free tier is a *complete* daily-practice experience. The user gets a daily movement. The user gets the chapter mark. The user gets the four-week history. The user gets EN, ES, PT, FR, ZH, JA, KO, TL. The user gets a Section of up to seven people. The user gets a real product.

The paid tier — when it ships — is a thank-you, not a toll. It is for the user who wants more: the full multi-year composition archive, unlimited Sections, voice playback, custom cadences, the wearable app. It is a true upgrade. It is not required to use the product well.

This is the difference between a company that needs your money to exist and a company that exists to serve you, and is grateful when you support it.

---

## 8. We do not optimize for engagement. We optimize for practice.

Engagement is a metric invented by the attention economy. It counts what the user does in the app. It says nothing about whether the user's life is better.

Practice is a metric invented by every serious discipline that has ever existed. It counts what the user *is*. It is the only thing worth optimizing for.

Cadence's primary metrics:
- Did the user complete today's movement? (binary, per day)
- Did the user come back tomorrow? (binary, per day)
- Did the user finish a chapter? (binary, per week)
- Did the practice meet the user? (weekly 5-point survey)

Cadence's anti-metrics — the ones we *measure to make sure we are not optimizing for*:
- App opens per day
- Time spent in the app
- Notification tap rate
- "Share" button tap rate

If the anti-metrics start climbing faster than the primary metrics, we have a problem. The product is becoming engagement-extraction, not practice-delivery. We fix the product, not the metrics.

This is the discipline. The discipline is the philosophy in action.

---

## 9. Ship the manifesto before the code.

This repo exists *before* the product code. That is intentional.

The reason: the philosophy has to be locked in writing *before* the product team starts shipping. Every PR, every feature, every line of code gets measured against the manifesto. If a feature cannot be traced to one of the three mechanisms, with a guardrail that protects the user, it does not ship.

If the manifesto came after the code, every conflict would be resolved in favor of the code. "We already built it" is the most powerful argument in any company. It is also the argument that ships the PBL trap, the streak shame, the social-graph creep, the AccessibilityService overreach. The code is a sunk cost. The philosophy is not.

By writing the philosophy first, we make the philosophy the sunk cost. Every future PR has to defend itself against this document. The document has to be defeated, not the product.

This is a small piece of institutional design. It matters.

---

## 10. The line, when it comes.

There will be a moment — probably in the second year, probably when growth slows — when someone on the team proposes a feature that crosses the line. A streak counter, but "with a friendly framing." A "share to unlock" custom cadence, but "just one tier." A leaderboard, but "for Sections only, and only opt-in." A "we noticed you missed three days" notification, but "with an opt-out."

Every one of these proposals will be reasonable in isolation. Every one will lift a metric. Every one will be defended by a smart person who has thought about it carefully.

The answer, every time, is no.

Not because the person proposing it is wrong. Because the line is the line. The line is the philosophy. The philosophy is the product. The product is Cadence.

When the line comes, and it will come, we reread this document. We reread `docs/RETENTION.md`. We reread the section in the PRD titled "What we explicitly do not build." And we hold the line.

This is the philosophy. This is Cadence.

---

*— end —*
