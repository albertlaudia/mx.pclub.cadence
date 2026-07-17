# Commercial Analysis

> *The honest business case for Cadence, with numbers.*

This document is the **commercial and financial analysis** of Cadence. It is not promotional. It is not a pitch deck. It is the analysis a sophisticated investor or partner would do, and the answer a thoughtful founder needs to see before committing the next 3 years.

If `PHILOSOPHY.md` is the why and `PRD.md` is the what, this is the **how it makes money — and what happens if it doesn't.**

---

## TL;DR

Cadence's realistic commercial ceiling is **$300K–$2M ARR within 3 years** as a profitable lifestyle business, with a 10–15% chance of breaking out to the **$5–10M ARR tier** (Hallow challenger). The single sharpest insight: **the Section is the only feature that can compound virally without paid acquisition.** If Section adoption crosses 40% of MAU, the viral coefficient crosses 1.0 and the growth math changes. If Section adoption stays under 20%, Cadence is a paid-acquisition business competing against Hallow's $100M war chest — and the math is much harder.

---

## Market sizing (TAM / SAM / SOM)

| Layer | Size (annual) | Source / reasoning |
|---|---|---|
| **TAM** — global faith + meditation app market | ~$5B | Hallow ($50M+ ARR est.), Headspace/Calm ($150-200M each), Insight Timer, plus secular adjacent |
| **SAM** — Christian daily devotional + prayer app segment | ~$200M | Hallow's leadership, plus Abide, YouVersion, Prayer Lock, Lectio 365, Pray.com, etc. |
| **SOM (achievable for Cadence)** | $1–5M ARR | Top 5 in the niche, sustainable, not dominant. Probably top 3 by year 5 in a good scenario. |

The niche is dominated by **Hallow** (Catholic, $50M+ ARR est., 10M+ downloads, $9.99/mo or $99.99/yr, 100+ employees, $100M+ raised). Hallow has brand, network, and capital. Cadence cannot beat Hallow on feature parity or marketing budget. Cadence can win on:

- **The no-PBL positioning** — a daily practice without the gamification baggage
- **E2E Section privacy** — intimate social without the surveillance
- **Multi-denominational day one** — Catholic + Protestant + Orthodox served without picking a side
- **Cheaper price point** — $4.99/mo vs Hallow's $9.99
- **The manifesto** — the philosophy is the brand, the brand is the moat

---

## Comparable benchmarks (real numbers, not vibes)

| Product | ARR (est.) | Price | Subscribers (est.) | CAC (est.) | LTV (est.) | LTV/CAC |
|---|---|---|---|---|---|---|
| **Hallow** | $50M+ | $9.99/mo, $99.99/yr | 500K+ paying | $40-80 | $200+ | 3-5x |
| **Headspace** | $150M+ | $12.99/mo, $69.99/yr | 1M+ paying | $30-60 | $150+ | 3-5x |
| **Calm** | $200M+ | $14.99/mo, $69.99/yr | 1.5M+ paying | $40-80 | $180+ | 3-4x |
| **Prayer Lock** (Covenant Studios) | $300K (founder public claim) | $9.99–$99.99 ladder | ~5K paying | unknown | unknown | founder-claimed healthy ("50% margin") |
| **Abide** | $5-10M | $9.99/yr | 50K+ paying | $20-40 | $30-50 | 1-2x (tight) |
| **YouVersion (Bible App)** | n/a (free + ads + donations) | free | 100M+ MAU | $0 (organic) | n/a | n/a |

**The key reads:**

1. **Hallow/Headspace/Calm run on 3-5x LTV/CAC** with $40-80 CAC. This is the SaaS benchmark for healthy growth.
2. **Faith-app comps run tighter** (1-2x) because the audience is narrower and harder to acquire at scale.
3. **Prayer Lock** is the most directly comparable competitor. Their founder publicly claims $300K ARR at 50% margin. That's the benchmark for a focused Christian daily-practice app with paid acquisition.
4. **YouVersion** is the elephant in the room — 100M+ MAU, free, donation-supported. They are not a subscription competitor but they set the floor for what users expect to pay for faith content (i.e., often nothing).

---

## Unit economics for Cadence

**Pricing assumption:** $4.99/mo or $39.99/yr. Free tier is fully functional (1 cadence, 1 Section up to 7, 4 chapters of history).

### Per-paid-user economics (annual)

```
Revenue (annual):                     $39.99
– Apple cut (after year 1, 15%):      -$6.00
– LLM cost (Claude Sonnet):          -$0.36
   ($0.03/user/month for daily
   movements + chapter + composition)
– Infra (Firestore + Cloud Run):      -$6.00
– Support amortized:                  -$2.00
– Localization amortized:             -$0.50
Net per paid user (year 1):           ~$25.13
Net per paid user (year 2+):          ~$30.13 (lower Apple cut)
```

### Per-free-MAU economics (monthly)

```
LLM (1 movement/day for free):        $0.10/mo
Infra (Firestore reads + writes):     $0.05/mo
Support amortized:                    $0.02/mo
Net per free MAU:                     -$0.17/mo
```

The free tier is a real cost center. The paid tier subsidizes it. This is the standard freemium math.

### Conversion assumptions (faith-app benchmarks)

- **Day-30 free → paid:** 3-5%
- **Day-90 free → paid:** 4-6% (Hallow's published benchmarks land here)
- **Annual paid retention:** 70-80% (faith apps retain better than secular apps)
- **ARPU at scale:** ~$0.30-0.50/MAU/month (because 95% of users are free)

### Customer Acquisition Cost (CAC)

| Channel | Effective CAC per paid user |
|---|---|
| App Store organic search | $0 |
| Apple Search Ads | $40-150 |
| Section viral invites | $0 |
| Referral from other pclub apps | $0-5 |
| Influencer / TikTok | $125-750 |
| **Blended CAC at scale** | **$30-80** |

### LTV / CAC analysis

At 2-year paid retention:

```
LTV per paid user = $25.13 (year 1) + $30.13 (year 2) = $55.26
CAC per paid user = $30-80
LTV/CAC = 0.7-1.8x
```

**This is the uncomfortable number.** At conservative assumptions, Cadence is barely profitable on paid acquisition. The unit economics only work if a meaningful share of users come from $0 channels. **That is the entire strategic question of Cadence: how much of growth is organic, and how much is paid?**

---

## The Section is the only feature that can compound virally

This is the single most important business insight in the spec.

### The math

- If 30% of new users are invited by an existing user, viral coefficient k = 0.30. Slow grower, not viral.
- If 60% of new users are invited by an existing user, k = 0.60. Grower, but still needs paid acquisition to break out.
- If 100% of new users are invited by an existing user (every user invites at least 1 more before churning), k = 1.0. **Exponential growth with zero paid acquisition — the Hallow-class outcome.**

### Why faith apps have unusual viral structure

- **Family groups** (parent → child, grandparent → grandchild) are natural Section use cases. The grandparent sends the link to the grandchild; the grandchild invites their college roommate.
- **Small groups / accountability partners** are natural Section use cases. A small group of 5-7 friends all join the same Section.
- **Lent and Advent** are natural viral moments. Annual spikes in "I'm going to actually pray this time" intent. A Lent push could deliver 20-30% of annual installs in 6 weeks.
- **Pastor-led adoption** creates a Section with 7 members instantly. One pastor mentioning Cadence in a sermon = 50-500 new Sections.

### The metric to watch

**Section adoption at 30, 60, and 90 days of beta is the single most important number in the company.**

- If Section adoption crosses 40% of MAU at 90 days, the viral math works and Cadence can grow without paid acquisition.
- If Section adoption is 20-40%, Cadence is a hybrid (some viral, some paid) and the unit economics are tight but workable.
- If Section adoption stays under 20%, Cadence is a paid-acquisition business competing with Hallow's $100M. The math doesn't work without a much larger budget or a strategic exit.

---

## Revenue scenarios (3 tiers)

### Scenario A — Modest (solo, side project)

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| MAU | 1,000 | 5,000 | 8,000 |
| Paid conversion | 4% | 4% | 5% |
| Paid users | 40 | 200 | 400 |
| MRR | $200 | $1,000 | $2,000 |
| Annual run rate | $2,400 | $12,000 | $24,000 |
| Team cost | $0 (solo) | -$80,000 | -$80,000 |
| COGS + Apple | -$200 | -$2,000 | -$4,000 |
| Marketing | -$1,000 | -$5,000 | -$5,000 |
| **Net** | **+$1,200** | **-$75,000** | **-$65,000** |

**Verdict:** Side project. The founder takes a loss in opportunity cost but the product exists. **Probability: 70%.**

### Scenario B — Moderate (2 FTE, paid + organic)

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| MAU | 8,000 | 40,000 | 80,000 |
| Paid conversion | 4% | 5% | 5% |
| Paid users | 320 | 2,000 | 4,000 |
| MRR | $1,600 | $10,000 | $20,000 |
| Annual run rate | $19,200 | $120,000 | $240,000 |
| Team cost (2 FTE) | -$160,000 | -$200,000 | -$200,000 |
| COGS + Apple | -$3,000 | -$15,000 | -$30,000 |
| Marketing | -$30,000 | -$80,000 | -$100,000 |
| **Net** | **-$174,000** | **-$175,000** | **-$90,000** |

Year 4 reaches cash-flow positive at $20K MRR. Year 5 hits $100-200K net profit. **Probability: 25%.**

### Scenario C — Aggressive (5 FTE, viral hit, Hallow challenger)

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| MAU | 30,000 | 200,000 | 500,000 |
| Paid conversion | 5% | 5% | 5% |
| Paid users | 1,500 | 10,000 | 25,000 |
| MRR | $7,500 | $50,000 | $125,000 |
| Annual run rate | $90,000 | $600,000 | $1,500,000 |
| Team cost (5 FTE) | -$300,000 | -$500,000 | -$500,000 |
| COGS + Apple | -$15,000 | -$75,000 | -$200,000 |
| Marketing | -$100,000 | -$200,000 | -$300,000 |
| **Net** | **-$325,000** | **-$175,000** | **+$500,000** |

Year 4 reaches $3-5M ARR. Year 5 hits $5-10M ARR with $1-2M net profit. **Probability: 5%.**

### Year 3 realistic projection (across all scenarios)

**$200K-$500K ARR, 1-2 person team, $50-150K net profit.** Profitable lifestyle business.

### Year 5 upside scenario

**$3-5M ARR, 5-10 person team, $1-2M net profit.** Real SaaS. Possible acquisition target at 4-6x revenue ($15-30M valuation).

---

## Strategic value beyond direct revenue

Even if Cadence stays at $300K ARR, it has value beyond the top line:

### 1. Brand halo for the pclub family

A product with this philosophy makes HEAL, Wordie, etc. look more serious. Investors, press, and users take the family more seriously. The pclub name gets associated with "the thoughtful one" instead of "another wellness app."

### 2. Acquisition target

A profitable $1-3M ARR faith app with 50K+ users and a Section feature is a meaningful exit for Hallow, Salem Communications, Guideposts, Pray.com, or similar faith publishers. **Realistic acquisition multiple: 4-8x ARR = $4-24M.** The Section + E2E privacy + multi-denom positioning is the differentiator that makes Cadence an attractive bolt-on.

### 3. IP / platform potential

The Section E2E encryption + the multi-denominational content engine is reusable. Could be productized as "Cadence Engine" — a white-label daily-practice platform licensed to other publishers. Realistic licensing revenue: $200K-$1M/yr per major publisher deal.

### 4. Cross-app flywheel

Cadence users are warm prospects for HEAL, Wordie, and any future pclub app. A Section member is the most qualified lead in any portfolio — they trust the product, they trust the founder, and they've already converted once.

### 5. Impact narrative

The product is a real social good. Useful for press, partnerships, grants (some foundations fund faith-tech), and ESG positioning. The manifesto is a press story waiting to happen.

---

## Risks that kill the thesis (ranked by severity)

### 1. Section adoption stays under 20%

Without the viral coefficient, Cadence is a paid-acquisition business competing with Hallow's $100M. Unit economics fail. **Probability: 40%.**

### 2. LLM cost doesn't come down

If user base grows 10x and LLM costs stay at Sonnet pricing, the unit economics on the free tier become unsustainable. **Mitigation:** hybrid curated + LLM, model downgrades for non-bonus days, aggressive caching, switch to open-source models if necessary. **Probability: 20% (cost trajectory is downward).**

### 3. Hallow copies the Section

Hallow has the resources. If they ship a "Hallow Together" small-group feature, Cadence loses the differentiation. **Mitigation:** deeper E2E privacy (Hallow won't go that far because it limits their data collection), the manifesto narrative (Hallow can't credibly adopt it without contradicting their existing gamification), multi-denominational positioning (Hallow is Catholic-first). **Probability: 30% over 3 years.**

### 4. The "no streak" thesis is wrong

The product thesis assumes retention without PBL. If it turns out retention actually requires a streak counter, Cadence has to either ship one (violating the philosophy) or accept lower retention. **This is the single biggest empirical question to answer in the alpha.** **Probability: 30%.**

### 5. Theological review is the gating cost

Every verse, every chapter summary, every prompt needs pastoral review. This is the difference between $200K and $2M ARR. Multi-denominational work scales linearly with reviewer time. **Mitigation:** paid tier funds the reviewer, contributor model where pastors contribute as side gigs. **Probability: 60% (this is a known cost, not a fatal risk).**

### 6. Apple/Google cut changes

Unlikely but possible. **Mitigation:** web app, direct subscriptions, pivot to Android if iOS becomes hostile. **Probability: 5%.**

### 7. Content licensing

Public-domain translations limit the English market. If users want ESV/NIV, we have to license. Costs balloon. **Mitigation:** lead with public-domain (KJV is beloved), license ESV only if user demand is overwhelming. **Probability: 40% (will need to license eventually).**

### 8. Cultural sensitivity failures

Wrong theological landing in any locale (e.g., Protestant prompt shown to Catholic user) tanks that market. **Mitigation:** locale-specific prompt pools, denomination-tagged cadences, pastoral review per locale. **Probability: 50% (will fail in some locale at some point).**

### 9. Churn is high

Faith apps have 30-40% churn in the first 3 months. Without PBL, churn could be higher. **Mitigation:** the Section (a Section member churns slower than a solo user), the chapter mark (chapter-resolved users churn slower than chapter-unresolved users), the welcome-back state (graceful re-entry after absence). **Probability: 70% (high churn is the default; design it for, not against).**

### 10. Solo founder can't scale

The product needs 1 engineer + 1 designer + pastoral advisors. The founder's solo capacity caps Cadence at the Modest scenario. **Mitigation:** find a co-founder, or stay solo and accept the cap. **Probability: 50% (most solo founders don't scale).**

---

## The realistic ceiling + the path to break it

### Without a strategic event

**$2-3M ARR, 3-5 person team, $1M+ profit, 8-12 years to peak.** Profitable lifestyle business. Acquisition target at $10-25M.

### Path to break the ceiling

One of the following has to happen:

1. **Viral coefficient crosses 1.0** (Section adoption > 40%, every user invites 1+ before churning). Then the growth math runs itself. Probability: 15-20%.

2. **Strategic partnership with a faith publisher** (Salem, Guideposts, Hallow, etc.) that distributes Cadence to their existing audience. Distribution deal worth $5-10M in exit value. Probability: 10-15%.

3. **Acquisition by Hallow or larger competitor** at 5-8x ARR = $10-40M exit. The Section + E2E privacy + multi-denom positioning is the differentiator. Probability: 10-20% by year 5.

4. **The "no-PBL" thesis is proven in market** (Cadence retention matches or beats Hallow without gamification). This becomes a category-defining story. Press, partnerships, talent acquisition all become easier. Probability: 15-25%.

### The single most important thing to test in alpha

**Section adoption at 30/60/90 days.** This number determines the entire business outcome. Ship the alpha. Get 5 internal users. Get 50 beta users. Measure. If 40%+, scale aggressively. If 20-40%, scale moderately. If < 20%, pause and rethink the social layer before spending on growth.

---

## The recommendation

Cadence is worth building because:

1. **The downside is bounded** — $0 sunk cost in code today, only the docs exist. The only real risk is the founder's time.
2. **The realistic outcome is positive** — $50-150K net profit by year 3, $1M+ by year 5.
3. **The upside is non-trivial** — acquisition at $10-40M is plausible if the Section goes viral or the no-PBL thesis is proven.
4. **The strategic value exceeds the direct revenue** — brand halo, cross-app flywheel, IP value, impact narrative.

**Build it. Measure the Section. Let the data decide.**

---

*Last updated: 2026-07-14 — by the founder, for the founder.*
