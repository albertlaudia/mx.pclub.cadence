# apps/mobile

Flutter app for iOS + Android.

## Brand

All icons and brand assets live in [`media/`](../media/). The app icon is the three-dots mark in midnight navy and amber.

- iOS: `apps/mobile/ios/Runner/Assets.xcassets/AppIcon.appiconset/`
- Android: `apps/mobile/android/app/src/main/res/mipmap-*/`

## Stack

When this is built, it will follow the pattern from `mx.pclub.caloriecounter` and `mx.pclub.pulse`:
- Single Flutter codebase
- iOS + Android from the same `lib/`
- Firebase Auth + Firestore
- Riverpod for state
- go_router for navigation
- E2E encrypted Section coordination
- Shared design system from `packages/ui`

See `docs/ARCHITECTURE.md` for the system that this app delivers.
