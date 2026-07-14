# Privacy

> What Cadence collects, what it doesn't, and the structural reasons why.

This document is the **privacy architecture** for Cadence. It's structured around one rule: **the only way to protect user privacy is to make the product not need the data in the first place.** Policy is a promise; structure is a guarantee.

---

## The rule

Cadence is built around **data minimization as architecture**, not just as policy. We do not collect data we do not need, and we have structured the product so that the data we don't collect *cannot leak* because it was never created.

The four categories:

1. **What we collect** — and why we need it
2. **What we don't collect** — and why we don't need it
3. **What's structurally private** — the user controls it, not us
4. **What we never will collect** — even if it would help retention

---

## 1. What we collect

| Data | Why | Storage | Retention |
|---|---|---|---|
| Email | Account recovery, sign-in | Firebase Auth | Until account deletion + 30 days |
| Display name | Personalization of the movement ("Good morning, Sarah.") | Firestore | Until account deletion |
| Locale + timezone | Localizing the movement, knowing when "your day" ends | Firestore | Until account deletion |
| Cadence choice | Generating the right kind of movement | Firestore | Until account deletion |
| Mood signal (1-tap) | Shaping today's movement | Firestore, end-to-end encrypted at rest | Until account deletion |
| Practice completion (boolean) | The chapter mark, the Section signal | Firestore, end-to-end encrypted at rest | Until account deletion |
| Reflection notes (free-text, optional) | The user's own journal of the practice | Client-side encrypted, key derived from user's password | Until user deletes |
| App version + device type | Crash diagnostics, OS-aware bug fixes | Firebase Crashlytics (no PII) | 90 days |
| Anonymized aggregates | "73% of users complete their movement on day 7" | BigQuery | 24 months |

**That's it.** The list is short on purpose.

---

## 2. What we don't collect

| Data | Why we don't |
|---|---|
| **The names of other apps on the device** | We don't need them. The Cadence practice is internal — what you do *outside* Cadence is not our business. (This is why we don't use Android's AccessibilityService — see §4.) |
| **The content of notifications** | Same reason. Notifications are the user's, not ours. |
| **Screen time data** | We don't need to know how much time you spent elsewhere. |
| **Location** | We use your timezone (which you set), not GPS. The difference matters: timezone is a preference, location is surveillance. |
| **Contact list** | We never read your contacts. The Section is invite-by-link, not contact-scraping. |
| **Microphone audio** | We don't record. Voice playback of the movement is a TTS feature, not a microphone feature. |
| **Camera** | We don't use it. No QR scanning, no profile photo upload. |
| **Biometric data** | No Face ID, no Touch ID, no fingerprint — only as an OS-level lock for the app, not as data we collect. |
| **Cross-app tracking** | No IDFA, no GAID, no SKAdNetwork, no Adjust, no AppsFlyer. None. |
| **Third-party SDKs** | No Mixpanel, no Amplitude, no Segment, no Heap. Firebase is the only third-party in the app. |

---

## 3. What's structurally private

The Section is the highest-stakes data Cadence handles. It's *intimate social data*, and the standard pattern (server can see it) is dangerous. Cadence uses **client-side encryption with a key derived from the Section's invite token** so that Cadence's servers never see who's in a Section or who practiced when.

**How it works:**
1. User creates a Section. The client generates a Section key.
2. The Section key is embedded in the invite link as a URL fragment (`#key=...`). The fragment is never sent to the server.
3. Section members install the key when they accept the invite. Their client decrypts Section messages locally.
4. The server only sees: "Section X has 4 members, they all practice the same cadence, here are some encrypted blobs." The server cannot read the practice signals.

**What this means:**
- Cadence cannot sell Section data — we can't read it.
- Cadence cannot be compelled to disclose Section membership — we don't have it.
- A Section data breach reveals nothing useful — the data is encrypted with a key only the members hold.

This is the same pattern used by Apple for iCloud Advanced Data Protection, by Signal for group messages, and by WhatsApp for backups. It's well-trodden. We are not inventing crypto; we are applying it.

**Cost:** ~$0.0001 / Section member / day in compute. Negligible.

**Trade-off:** if a Section member loses their key (reinstalls the app, switches devices without backup), they have to be re-invited. The Section doesn't break — they just get a fresh invite.

---

## 4. What we never will collect

These are the **architectural decisions** that are hard to reverse. Once we ship them, they shape the product forever. We make them in writing, here, so future contributors know the line.

### No AccessibilityService

Android's `AccessibilityService` API lets an app see *everything* on the screen — the names of other apps, the content of other apps, the text the user types. It's also the **only reliable way** to do cross-app blocking (which Prayer Lock uses).

Cadence does not need to block other apps. The practice is internal. So:

- **Cadence doesn't know which other apps you use.**
- **Cadence doesn't know how much time you spend on Instagram.**
- **Cadence doesn't know what notifications you receive.**

If the user wants to reduce screen time elsewhere, they use iOS Screen Time or Android Digital Wellbeing. We are not in the screen-time business. We are in the *practice* business.

This is a deliberate non-feature. It's the single biggest reason a user installs Prayer Lock ("block my apps until I pray") and the single biggest reason Prayer Lock loses the trust of that user (AccessibilityService is a Google-flagged high-risk permission, and the disclosure is alarming).

**Cadence's wedge is different:** the user doesn't install Cadence to *block* distraction. They install it to *have* a daily practice. The product doesn't need to see the rest of the phone. The user gets a more honest, less scary app. We get a smaller TAM but a more loyal user.

### No social graph integration

We never read contacts, never integrate with Facebook, never suggest "people you may know". The Section is invite-by-link. The user controls who they're in a Section with. This is a deliberate non-feature.

### No "share to unlock" mechanics

No Section feature requires posting publicly. No chapter summary requires sharing. No paid feature requires a screenshot. **Solo practice is full-featured and the default.** The Section is an additive.

### No global leaderboard

We will never ship a "compare yourself to other Cadence users" feature. No "Top Sections this month". No "Cadence Champions". The retention mechanism is *intimate*, not *performative*.

### No streak counter

We will never display "Day 47!" as a primary metric. The chapter mark is the primary metric. The number is internal. This is non-negotiable.

### No "streak repair" paywall

We will never sell "restore your 47-day streak" as a feature. The closest we will ship: a quiet "Welcome back" message that doesn't reference the gap. That's it.

### No A/B test that withholds a movement

We will never run an A/B test where the variant is "no movement, see if the user comes back faster". The A/B tests we run are content-quality variants (which movement landed better) and feature-onboarding variants (does the user complete the cadence-name step?), never engagement-extraction variants.

### No ad SDKs

Cadence is not an ad product. We will never integrate ad networks, no matter how lucrative. The product is funded by users (free + paid) and not by advertisers. This is structural — it means the only metric that matters is whether the practice met the user.

### No third-party analytics beyond Firebase

Firebase is the only third-party in the app. No Mixpanel, no Amplitude, no Segment, no Heap, no Hotjar, no FullStory. The data we collect is the data we listed in §1. We do not enrich it with third-party data. We do not sell it to data brokers. We do not share it with affiliates.

---

## 5. How we handle requests

- **Data export:** the user can export all their data (movements, reflections, chapter summaries) at any time, in JSON or PDF. One tap in Settings → Account → Export.
- **Data deletion:** the user can delete their account and all associated data at any time. Deletion is permanent and happens within 7 days. There's no "soft delete" with a 30-day recovery window. The user is in control.
- **Family / legal requests:** if a family member or legal authority requests data on a deceased user, we require a court order in the user's jurisdiction. We do not voluntarily disclose.
- **Government requests:** we publish a transparency report every 6 months with the number of government requests received, complied with, and rejected.
- **Bug bounty:** we run a public bug bounty with a focus on privacy bugs. The minimum payout is $500.

---

## 6. How we talk about privacy

Privacy is a feature, not a footnote. Cadence's marketing copy is explicit about what we don't collect. The store listing includes a "Privacy" section that lists the data categories in §1 and points to this document.

We do not use privacy as a marketing gimmick. We use it as a *design constraint*. The product is the privacy story. The privacy story is the product.

---

## 7. Open questions

- **Crash diagnostics:** Firebase Crashlytics collects some device data. We should evaluate switching to a self-hosted Sentry to remove the third-party entirely.
- **Reflection notes:** end-to-end encryption means we can't recover the user's notes if they lose their key. Is that OK? (Yes — but we should be explicit about it in onboarding.)
- **Aggregated metrics:** BigQuery aggregates are anonymized, but the small-section risk is real. A 2-person Section can be de-anonymized trivially. We should add differential privacy noise to all small-n aggregates.

---

## References

- `docs/RETENTION.md` — the three mechanisms, and why we don't need most of the data Prayer Lock collects
- `docs/ARCHITECTURE.md` — the technical system that delivers the privacy guarantees
- Apple iCloud Advanced Data Protection — the encryption pattern we follow for Section data
- Signal protocol — open-source reference for end-to-end encrypted groups
- EFF Surveillance Self-Defense — public reference for the privacy-by-design principles we follow
