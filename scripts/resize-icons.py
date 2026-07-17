#!/usr/bin/env python3
"""
resize-icons.py — regenerate all icon sizes from the master.

The master is `media/icons/app-icon-1024.png` (1024x1024 master).
This script produces all iOS, Android, and favicon derivatives.
Run after updating the master.

Usage:
    python3 scripts/resize-icons.py

Requires:
    pip3 install pillow
"""

import os
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(REPO_ROOT, "media")
ICONS = os.path.join(MEDIA, "icons")
MASTER = os.path.join(ICONS, "app-icon-1024.png")


def main():
    if not os.path.exists(MASTER):
        print(f"ERROR: master not found at {MASTER}")
        return 1

    img = Image.open(MASTER).convert("RGBA")
    print(f"master: {MASTER} ({img.size})")

    # iOS asset catalog sizes
    ios_dir = os.path.join(ICONS, "ios")
    os.makedirs(ios_dir, exist_ok=True)
    ios_sizes = {
        "Icon-App-20x20@1x.png": 20,
        "Icon-App-20x20@2x.png": 40,
        "Icon-App-20x20@3x.png": 60,
        "Icon-App-29x29@1x.png": 29,
        "Icon-App-29x29@2x.png": 58,
        "Icon-App-29x29@3x.png": 87,
        "Icon-App-40x40@1x.png": 40,
        "Icon-App-40x40@2x.png": 80,
        "Icon-App-40x40@3x.png": 120,
        "Icon-App-60x60@2x.png": 120,
        "Icon-App-60x60@3x.png": 180,
        "Icon-App-76x76@1x.png": 76,
        "Icon-App-76x76@2x.png": 152,
        "Icon-App-83.5x83.5@2x.png": 167,
        "Icon-App-1024x1024@1x.png": 1024,
    }
    for name, size in ios_sizes.items():
        out = img.resize((size, size), Image.LANCZOS)
        out.save(os.path.join(ios_dir, name), "PNG", optimize=True)
        print(f"  ios/{name}: {size}x{size}")

    # Android mipmap sizes
    android_sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    for folder, size in android_sizes.items():
        out_dir = os.path.join(ICONS, "android", folder)
        os.makedirs(out_dir, exist_ok=True)
        out = img.resize((size, size), Image.LANCZOS)
        out.save(os.path.join(out_dir, "ic_launcher.png"), "PNG", optimize=True)
        out.save(os.path.join(out_dir, "ic_launcher_round.png"), "PNG", optimize=True)
        print(f"  android/{folder}/ic_launcher.png + ic_launcher_round.png: {size}x{size}")

    # Favicon sizes
    for size, name in [(16, "favicon-16.png"), (32, "favicon-32.png"), (48, "favicon-48.png"), (256, "favicon-256.png")]:
        out = img.resize((size, size), Image.LANCZOS)
        out.save(os.path.join(ICONS, name), "PNG", optimize=True)
        print(f"  {name}: {size}x{size}")

    # 512x512 for Play Store
    out = img.resize((512, 512), Image.LANCZOS)
    out.save(os.path.join(ICONS, "app-icon-512.png"), "PNG", optimize=True)
    print(f"  app-icon-512.png: 512x512")

    print("\nDone. Now copy the new icons into the app assets:")
    print("  cp media/icons/ios/*.png apps/mobile/ios/Runner/Assets.xcassets/AppIcon.appiconset/")
    print("  cp media/icons/android/mipmap-*/*.png apps/mobile/android/app/src/main/res/mipmap-*/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
