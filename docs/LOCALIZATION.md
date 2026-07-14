# Localization

> Cadence is a product, not a translation. Every locale is a first-class citizen, not an afterthought.

This document is the **localization plan** for Cadence. The lesson from Prayer Lock was brutal: **translating the store listing without translating the product is worse than not translating at all.** It generates FR/PT/ZH reviews that complain "the prayers are in Spanish and there's no way to change it." Cadence is built to never have that failure mode.

---

## The rule

Every locale ships with three layers of localization, in this order:

1. **Listing localization** — store metadata, screenshots, app name, subtitle, keywords
2. **UI localization** — every button, every label, every error message, every onboarding screen
3. **Content localization** — every verse, every prompt, every chapter summary, every reflection

A locale does not ship until **all three layers** are complete. We do not ship "EN + ES at launch, FR later with a half-translated content layer." That is the Prayer Lock failure mode. We do not do that.

---

## Day-one locales (launch)

| Locale | Why | Status |
|---|---|---|
| **English (en)** | Default | ✓ in design |
| **Spanish (es)** | Largest faith app market globally. Prayer Lock taught us this is non-negotiable. | ✓ in design |

## Day-30 locales (within first month post-launch)

| Locale | Why | Status |
|---|---|---|
| **Portuguese (pt-BR)** | Brazil is the largest Catholic population in the world. | Planned |
| **French (fr)** | France + Francophone Africa + Quebec. | Planned |
| **Chinese Simplified (zh-Hans)** | The largest single-language market by population. | Planned |

## Day-90 locales (within first quarter)

| Locale | Why | Status |
|---|---|---|
| **Chinese Traditional (zh-Hant)** | Taiwan, Hong Kong, diaspora. | Planned |
| **Japanese (ja)** | High willingness-to-pay for premium apps. | Planned |
| **Korean (ko)** | High digital engagement. | Planned |
| **Tagalog (tl)** | Philippines is a meaningful faith market. | Planned |

## Day-180 locales (if user demand signals it)

- **Arabic (ar)** — RTL design system is ready; content is the gate
- **Hebrew (he)** — same
- **Hindi (hi)** — large population, growing smartphone market
- **Vietnamese (vi)**
- **Indonesian (id)**
- **German (de)**
- **Italian (it)**

---

## The three layers, in detail

### Layer 1: Listing localization

For each locale that ships, the store listing includes:
- App name (localized)
- Subtitle (localized)
- Description (localized, 4000 char max)
- What's New (localized)
- Screenshots with localized UI text (or screenshots that don't show UI text)
- Keywords (localized, in the locale's primary search terms)
- Promotional text (localized)
- Privacy policy URL (locale-specific or international English)

**Owner:** marketing, with a native-speaker review.

### Layer 2: UI localization

Every string in the app has a key. Every key has a translation in every shipped locale. The CI fails the build if a key is missing in any shipped locale.

This is *not* a translation memory. It's a build-time invariant. If a developer adds a new string to the EN locale, the build fails until the string is added to all shipped locales. (Unshipped locales can be missing keys, with a warning.)

**Tooling:** Flutter's `intl` + `flutter gen-l10n`. ARB files. The CI runs `flutter gen-l10n` and verifies completeness.

**Owner:** engineering, with native-speaker review.

### Layer 3: Content localization

This is the hard one. The content is the product.

#### Verses

Every verse in the library has translations in every shipped locale. The source is **public-domain translations** where available (e.g., Reina-Valera 1960 for Spanish, Louis Segond 1910 for French, Chinese Union Version for zh-Hans). For English, we use **multiple translations** (ESV, NIV, NLT) and let the user pick.

**Public-domain translation list (curated):**
- **EN:** KJV (public domain), WEB, YLT
- **ES:** Reina-Valera 1960
- **PT:** Almeida Revista e Atualizada
- **FR:** Louis Segond 1910
- **ZH-Hans:** Chinese Union Version (和合本)
- **ZH-Hant:** Chinese Union Version Traditional (和合本)
- **JA:** Colloquial Japanese Bible (口語訳)
- **KO:** Korean Revised Version (개역개정)
- **TL:** Filipino Bible (Magandang Balita)

For copyrighted translations (ESV, NIV, NLT), we either:
- License the translation from the rights holder
- Or show the public-domain version by default and let the user opt in to a licensed translation

**Verse library size:** 200 curated verses, 4+ translations each, at launch. 500+ by year one.

#### Prompts

Prompts are short, contextual questions. They are **not** scripture-quoted. They are written by a human for each locale, not translated from English.

Why? Because a good prompt in English ("What is one thing you are carrying that you could set down for an hour?") doesn't translate to French without losing the cadence. The French prompt needs to be written in French.

**Process:**
1. English copywriter writes the EN prompt
2. Locale-native copywriter writes the equivalent in their language
3. Locale-native theologian (or pastoral advisor) reviews for sensitivity
4. The prompt is added to the library with a `locale` field and an `englishOriginal` reference

**Prompt library size:** 200 prompts per locale, at launch. 500+ per locale by year one.

#### Chapter summaries

LLM-generated, in the user's locale. The LLM prompt is locale-aware and the LLM is instructed to write in the locale's natural register, not a translated register.

**Review process:** 1% of generated summaries are spot-checked by a native speaker weekly. The LLM prompt is tuned to match the failure modes.

#### Reflections

User-written, end-to-end encrypted. The app displays them in the user's own locale, but we don't translate them. The user's reflection is the user's reflection.

---

## The "no surprise language" guarantee

Prayer Lock's failure: the onboarding is in English, and then suddenly the user sees a prayer in Spanish with no language picker. The user can't fix it.

**Cadence's guarantee:** the user picks their locale in onboarding. From that moment, every string, every prompt, every chapter summary, every verse is in that locale. There is no silent fallback to EN or ES. If a verse or prompt doesn't have a translation in the user's locale, we **don't show it** — we show a fallback prompt that we *know* is in the user's locale, and we flag the missing translation to the content team.

The user never sees content in a language they didn't pick. Period.

---

## Locale picker

In onboarding, the user picks a locale. The picker is:
- Auto-detected from device locale on first launch
- Confirmed with a single tap: "We detected [locale]. Is that right?"
- The user can change it anytime in Settings

The locale picker is **not** a survey. It's a single question with a single tap.

---

## The "right-to-left" preparation

The design system is RTL-ready from day one. Even if Arabic and Hebrew don't ship on day one, the layout, the typography, and the icons are mirrored correctly. When we ship Arabic or Hebrew, the work is content + cultural, not technical.

**Tooling:** Flutter's `Directionality` + `TextDirection.rtl`. The design system has RTL variants of every component.

---

## Cultural sensitivity

Localization is not just translation. The *content* needs to be culturally appropriate for the locale.

- **Spanish (es)**: both Iberian and Latin American Spanish. The library uses a neutral register, with region-specific variations surfaced where it matters (e.g., "tú" vs "usted" — we default to "tú" for warmth).
- **Portuguese (pt-BR)**: Brazilian Portuguese, not European. Catholic and evangelical markets both.
- **French (fr)**: France, but also Francophone Africa. The library is written in a register that works for both.
- **Chinese (zh-Hans)**: Mainland China is a sensitive market. The product is **not** launched in mainland China (no ICP filing, no content review). The zh-Hans locale targets the diaspora (Singapore, Malaysia, US Chinese-speaking community).
- **Japanese (ja)**: high register, honorifics where appropriate.
- **Korean (ko)**: standard Seoul register.
- **Tagalog (tl)**: Filipino, with English code-switching where natural.

**Theology review:** every locale has a pastoral advisor who reviews the prompts and chapter summaries for denominational sensitivity. Catholic, Protestant, and Orthodox voices are all represented. The default cadence ("Daily Quiet") is denomination-neutral. Catholic and Protestant cadences are explicit and labeled.

---

## What we measure

- **Locale completion rate** at launch: 100% of the shipped locales have all three layers.
- **Locale drift:** every PR that adds a string or a content piece triggers a CI check on all shipped locales.
- **Locale-specific retention:** we measure day-30 retention *per locale*, not just in aggregate. A locale with low retention is a signal of a localization problem, not a market problem.
- **Reflection language:** we sample reflections (anonymized) to see what language the user is actually writing in. If 30% of French-locale users write reflections in English, the prompts might be off.

---

## Open questions

- **Theology review for chapter summaries:** is 1% spot-check enough? Or do we need 100% review for the first 3 months in each locale?
- **Verse licensing:** do we license NIV / ESV for the English market, or default to public-domain only?
- **Hindi / Arabic / Hebrew:** when do we commit to these locales? User signal or strategic call?
- **Dialect support:** do we ship pt-BR and pt-PT separately, or one Portuguese that works for both? Currently: one Portuguese, BR-leaning.
- **Indigenous languages:** Quechua, Nahuatl, Maori, etc. Out of scope for v1.0.

---

## References

- `docs/RETENTION.md` — the three mechanisms
- `docs/ARCHITECTURE.md` — the technical system
- `docs/PRIVACY.md` — the privacy boundaries
- `docs/PRD.md` — the product spec
- Prayer Lock platform review (2026-07): the localization failure that Cadence is designed to avoid
- pclub memory: "Engagement design: avoid PBL traps" — see AGENTS.md
