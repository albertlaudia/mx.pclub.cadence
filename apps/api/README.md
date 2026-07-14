# apps/api

Cloud Run API: movement generator + Section coordination + composition archiver. **Phase 1 — not yet scaffolded.**

When this is built, it will be:
- TypeScript + Hono (or Fastify)
- Deployed to GCP Cloud Run
- Stateless, scales to zero
- Calls Claude Sonnet for movement generation
- Coordinates Section data with end-to-end encryption

See `docs/ARCHITECTURE.md` for the system that this app delivers.
