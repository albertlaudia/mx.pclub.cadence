# packages/section

End-to-end encrypted Section coordination. **Phase 1 — not yet scaffolded.**

When this is built, it will be:
- A shared TypeScript package consumed by `apps/mobile` and `apps/web`
- Generates Section keys from invite tokens (URL fragment, never sent to server)
- Encrypts Section messages client-side
- The server only sees encrypted blobs; it cannot read Section membership or practice signals

See `docs/PRIVACY.md` §3 for the encryption pattern. The reference is Apple iCloud Advanced Data Protection and the Signal protocol.
