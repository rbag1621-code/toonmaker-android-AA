# TOONMAKER STUDIO – Android project (Capacitor)

App name: TOONMAKER STUDIO · Package ID: com.toonmakerstudio.app
The app is your existing website (`www/index.html`) in a native Android shell.
No ads, no payments, no premium features are included (nothing to configure).

## Easiest way: build online (no PC software)
1. Create a free account on github.com → New repository → upload ALL files of this folder
   (including the hidden `.github` folder).
2. Open the repo → **Actions** tab → **Build Android APK and AAB** → **Run workflow**.
3. When it turns green, open the run → **Artifacts** → download `TOONMAKER-STUDIO-debug-apk`
   (zip containing `app-debug.apk`).

## Install the APK on your phone
1. Unzip, copy `app-debug.apk` to your phone (or download it on the phone).
2. Tap it. If asked, allow "Install unknown apps" for your browser/Files app.
3. Open TOONMAKER STUDIO. Allow the microphone when asked (needed for voice recording).

## Build on your own PC instead
Needs Node 20+, JDK 21, Android Studio (SDK installed).
    bash setup-android.sh
    cd android && ./gradlew assembleDebug
APK: android/app/build/outputs/apk/debug/app-debug.apk

## Google Play (AAB)
`./gradlew bundleRelease` makes `app-release.aab`, but it is UNSIGNED. Before uploading:
1. `keytool -genkey -v -keystore toonmaker.jks -alias toonmaker -keyalg RSA -keysize 2048 -validity 10000`
2. Add that keystore as a signing config in android/app/build.gradle (or enrol in Play App Signing
   and sign the upload with this key). KEEP the .jks file and passwords safe; never upload them publicly.

## Android behaviour
- Videos save to Documents/ToonMaker; if the phone blocks that, the Share sheet opens so you can save the file.
- Back button: closes Voice Settings → stops speech → asks to press Back twice to exit (also protects a running recording).
- Bengali/English speech uses the phone’s text-to-speech voices. Install the Bengali voice in
  Settings → System → Languages → Text-to-speech (Google), or use Record/Upload.
- Video is saved as MP4 if the phone’s WebView supports it, otherwise WebM.
