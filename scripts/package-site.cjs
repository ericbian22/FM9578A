const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),out=path.join(root,'_site');
fs.mkdirSync(out,{recursive:true});
for(const name of ['index.html','formula-sheet.html','assets','downloads'])fs.cpSync(path.join(root,name),path.join(out,name),{recursive:true});
fs.writeFileSync(path.join(out,'.nojekyll'),'');
console.log('Packaged public website, local math assets and downloads only.');
