# packages/auth

Shared Firebase Auth wrapper. **Phase 1 — not yet scaffolded.**

When this is built, it will be:
- A shared TypeScript package consumed by `apps/mobile` and `apps/web`
- Wraps Firebase Auth with Apple, Google, and email sign-in
- Handles session persistence, token refresh, sign-out
- Locale-aware (sign-in flow is localized)

Pattern from `mx.pclub.caloriecounter`.
