p='android/app/src/main/AndroidManifest.xml';s=open(p,encoding='utf-8').read()
add='''    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="28" />
    <uses-feature android:name="android.hardware.microphone" android:required="false" />
    <queries>
        <intent><action android:name="android.intent.action.TTS_SERVICE" /></intent>
    </queries>
'''
if 'RECORD_AUDIO' not in s:
    s=s.replace('</manifest>',add+'</manifest>');open(p,'w',encoding='utf-8').write(s);print('Manifest patched')
else: print('Manifest already patched')
