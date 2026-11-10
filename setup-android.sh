#!/usr/bin/env bash
# Prepares the Android project (run once, and again after changing www/).
set -e
npm install
[ -d android ] || npx cap add android
python3 tools/patch_manifest.py
npx capacitor-assets generate --android
npx cap sync android
echo "Android project ready. Build with: cd android && ./gradlew assembleDebug"
