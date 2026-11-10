p='www/index.html';s=open(p,encoding='utf-8').read()
s=s.replace('<title>Talking Character Studio</title>','<title>TOONMAKER STUDIO</title>').replace('<h1>🗣️ Talking Character Studio</h1>','<h1>🎬 TOONMAKER STUDIO</h1>')
old="try{const d=window.claude?await claude.use('downloads'):null;"
assert old in s
native="""const CP=window.Capacitor;
 if(CP&&CP.isNativePlatform&&CP.isNativePlatform()){
  try{
   const b64=await new Promise((ok,no)=>{const r=new FileReader();r.onload=()=>ok(String(r.result).split(',')[1]);r.onerror=no;r.readAsDataURL(vBlob)});
   const FS=CP.Plugins.Filesystem;let where='Documents/ToonMaker/'+nm;
   try{await FS.writeFile({path:'ToonMaker/'+nm,data:b64,directory:'DOCUMENTS',recursive:true})}
   catch(e){const r=await FS.writeFile({path:nm,data:b64,directory:'CACHE'});where='your chosen location (via Share sheet)';await CP.Plugins.Share.share({title:nm,url:r.uri,dialogTitle:'Save video'})}
   status('✅ Video saved: '+where)
  }catch(e){status('Could not save the video: '+((e&&e.message)||e))}
  return}
 """
s=s.replace(old,native+old)
back="""/* ---------- Android back button ---------- */
(()=>{const CP=window.Capacitor,A=CP&&CP.Plugins&&CP.Plugins.App;if(!A)return;let last=0;
A.addListener('backButton',()=>{
 if($('vsPanel').classList.contains('open')){closeVS();return}
 const now=Date.now(),twice=now-last<2000;last=now;
 if(vr&&vr.state==='recording'&&!twice){status('Video is recording. Press Stop first, or press Back again to exit.');return}
 if(S.speaking||S.paused){stopSpeak();last=0;return}
 if(twice){A.exitApp();return}
 status('Press Back again to exit.')})})();
"""
s=s.replace('</script></body></html>',back+'</script></body></html>')
open(p,'w',encoding='utf-8').write(s)
