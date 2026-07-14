## What this PR does

A clear, concise description of the change.

## Why

Link to the issue or design discussion.

## Mechanism check

This PR touches:

- [ ] Craving Machine (variable content) — see `docs/RETENTION.md` §1
- [ ] Infinite Game (loss aversion, no terminal state) — see `docs/RETENTION.md` §2
- [ ] Invisible Scoreboard (intimate social) — see `docs/RETENTION.md` §3
- [ ] None of the above (operational, e.g., bug fix, perf, a11y)

If a mechanism is checked, this PR is changing how that mechanism works in the product. Please explain the change and the guardrail in the PR description.

## Anti-PBL check

- [ ] The variable is in *content*, not *outcome*
- [ ] The loss is in *practice*, not *number*
- [ ] The visibility is *intimate*, not *public*
- [ ] Solo practice is unaffected (or improved)
- [ ] The user can opt out without losing the core experience
- [ ] The copy is honest about what the feature is doing

## Privacy check

- [ ] No new data collection
- [ ] No AccessibilityService usage
- [ ] No contact list / social graph access
- [ ] No cross-app tracking
- [ ] No public profile changes
- [ ] No global leaderboard
- [ ] Section data is end-to-end encrypted

If any of these is "no", this PR needs a design discussion first.

## Localization

- [ ] All new strings have translations in all shipped locales
- [ ] All new content (prompts, verses) has translations in all shipped locales
- [ ] The CI locale check passes (`flutter gen-l10n` + verification)

## Testing

- [ ] Unit tests pass
- [ ] Widget tests pass
- [ ] Integration tests pass (if applicable)
- [ ] Manual testing on iOS
- [ ] Manual testing on Android
- [ ] Manual testing on web (if applicable)
- [ ] Manual testing in a non-EN locale (if applicable)

## Screenshots / recordings

If applicable, add screenshots or screen recordings.

## Migration / rollout

If this is a breaking change or a feature flag, describe the rollout plan.

## Open questions

What do you need a reviewer to weigh in on?
