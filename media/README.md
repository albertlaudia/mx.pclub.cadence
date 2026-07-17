# Media — Brand assets for Cadence

This folder holds all the brand and platform images for Cadence. The `/media` directory is the single source of truth for visual assets. Every platform (iOS, Android, web, marketing) draws from here.

## Files

### Brand mark
- `icons/app-icon-1024.png` — **iOS App Store master icon** (1024×1024, PNG)
- `icons/app-icon-512.png` — **Android Play Store icon** (512×512, PNG)
- `icons/favicon-256.png`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png` — web favicons

### iOS app icon set
- `icons/ios/Icon-App-*.png` — every required size for the iOS asset catalog
  - 20×20 @1x/@2x/@3x (Notification)
  - 29×29 @1x/@2x/@3x (Settings)
  - 40×40 @1x/@2x/@3x (Spotlight)
  - 60×60 @2x/@3x (Home screen)
  - 76×76 @1x/@2x (iPad)
  - 83.5×83.5 @2x (iPad Pro)
  - 1024×1024 @1x (App Store marketing)

### Android mipmap set
- `icons/android/mipmap-{mdpi,hdpi,xhdpi,xxhdpi,xxxhdpi}/ic_launcher.png` — all 5 density buckets
- `icons/android/mipmap-{mdpi,hdpi,xhdpi,xxhdpi,xxxhdpi}/ic_launcher_round.png` — round variants for Android 7.1+

### Marketing
- `social-preview-1280x640.png` — **GitHub social preview** (the banner that shows when the repo is shared)
- `hero-1920x1080.png` — **README hero / marketing banner**

### Reserved folders
- `screenshots/` — reserved for App Store + Play Store screenshots (not yet captured)

## The mark

**Three amber dots in a gentle arc on a deep midnight navy background.**

Why this mark:
- **Three dots** = the three mechanisms (Craving, Infinite Game, Scoreboard)
- **Three dots** = the three time scales (today, week, year)
- **Three dots** = the rhythm of a daily practice (movement → chapter → composition)
- **The arc** = a phrase rising, a breath in, a musical cadence
- **The colors** = midnight navy (#0F1A2E) is contemplative, reverent, not aggressive. Warm amber (#C8A45C) is the practice — warm but not loud.
- **No text in the mark** = the name is the wordmark, the mark is the symbol. They live together but separately.

## Color palette

| Token | Hex | Use |
|---|---|---|
| Midnight | `#0F1A2E` | Primary background, deep |
| Amber | `#C8A45C` | Mark, accent, the practice |
| Cream | `#F5EFE0` | Primary text on dark, light backgrounds |
| Charcoal | `#2A2D3A` | Secondary background |
| Mute | `#8A8B95` | Secondary text |

## Typography (in-app)

- **Headings:** a warm serif (e.g., Lora, Spectral, or Source Serif Pro)
- **Body:** a clean sans (e.g., Inter, Source Sans Pro)
- **Numerals:** tabular figures for the chapter dots
- **Verses:** a serif (matches the contemplative register of scripture)

## How to use these files

- **App Store / Play Store submission:** use `icons/app-icon-1024.png` (iOS) and `icons/app-icon-512.png` (Android) as the marketing icon
- **GitHub social preview:** upload `social-preview-1280x640.png` via the repo Settings → Social preview
- **README hero:** reference `hero-1920x1080.png` from the README
- **Web favicon:** use `icons/favicon-32.png` and `icons/favicon-16.png`

## When updating the mark

If the mark ever changes:
1. Update the source `app-icon-1024.png` (1024×1024 master)
2. Re-run the resize script in `scripts/resize-icons.py` to regenerate all derivatives
3. Re-copy the derivatives into `apps/mobile/ios/Runner/Assets.xcassets/AppIcon.appiconset/` and `apps/mobile/android/app/src/main/res/mipmap-*/`
4. Commit and push

The icons are generated from the master. The master is the source of truth.
