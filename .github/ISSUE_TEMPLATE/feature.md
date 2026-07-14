---
name: Feature Request
about: Suggest a new feature for Cadence
title: "[Feature] "
labels: enhancement
assignees: ""
---

## What you want

A clear, concise description of the feature.

## Why it matters

What user need does this address? Which of the three retention mechanisms does it serve?

- [ ] Craving Machine (variable content, novel within familiar shape)
- [ ] Infinite Game (loss aversion, no terminal state, real arc)
- [ ] Invisible Scoreboard (intimate social, not public)
- [ ] None of the above (operational, e.g., bug fix, perf, a11y)

## Anti-PBL check

Before submitting, run the feature through `docs/RETENTION.md` §"Anti-PBL design checklist":

- [ ] Does this feature map to one (and only one) of the three mechanisms?
- [ ] Is the variable in *content*, not *outcome*?
- [ ] Is the loss in *practice*, not *number*?
- [ ] Is the visibility *intimate*, not *public*?
- [ ] Is the solo path as good as the social path?
- [ ] Can the user opt out without losing any of the core experience?
- [ ] Is the copy honest about what the feature is doing?

If any answer is "no", please revise the proposal or discuss in `#design` first.

## Privacy check

- [ ] This feature does NOT require AccessibilityService access
- [ ] This feature does NOT require contact list access
- [ ] This feature does NOT require cross-app tracking
- [ ] This feature does NOT require a public profile
- [ ] This feature does NOT require a global leaderboard
- [ ] Solo users are fully supported

If any of these is "yes", please discuss in `#design` first.

## Localization

- [ ] This feature is locale-ready (no hardcoded strings, no EN-only content)
- [ ] This feature works in RTL (if applicable)
- [ ] The relevant pastoral advisors have been consulted (if content-bearing)

## Tier

- [ ] Free tier
- [ ] Paid tier
- [ ] Both

## Open questions

What do you need to know before this can be built? Who needs to weigh in?
