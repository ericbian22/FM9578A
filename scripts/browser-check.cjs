const fs=require('node:fs'),path=require('node:path'),os=require('node:os'),http=require('node:http'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),deps=path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules');
const {chromium}=require(path.join(deps,'playwright'));
const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.woff2':'font/woff2','.woff':'font/woff','.ttf':'font/ttf','.svg':'image/svg+xml','.pdf':'application/pdf'};
(async()=>{
 fs.mkdirSync(path.join(root,'test-results'),{recursive:true});
 const server=http.createServer((req,res)=>{let p=path.join(root,decodeURIComponent(req.url.split('?')[0]));if(req.url.split('?')[0].endsWith('/'))p=path.join(p,'index.html');if(!p.startsWith(root)||!fs.existsSync(p)){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',types[path.extname(p)]||'application/octet-stream');res.end(fs.readFileSync(p));});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const base='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(base);await page.evaluate(()=>document.fonts.ready);
 assert.equal(await page.locator('.lecture').count(),9);assert.equal(await page.locator('#exercise-list details').count(),20);assert.equal(await page.locator('#exercise-list .answer').count(),97);assert.equal(await page.locator('.dep-card').count(),9);assert.equal(await page.locator('.math-error').count(),0);
 const mathAudit=await page.evaluate(()=>COURSE.lectures.map(l=>({id:l.id,expected:l.sections.reduce((n,s)=>n+(s.body.match(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g)||[]).length,0),actual:document.querySelectorAll('#'+l.id+' .math-inline,#'+l.id+' .math-display').length})));
 for(const m of mathAudit)assert.equal(m.actual,m.expected,'Missing math in '+m.id);
 assert.equal(await page.locator('.study-figure img').count(),8);
 assert.equal(await page.locator('.solution-reasoning').count(),20);
 for(const graph of await page.locator('.study-figure img').all()){
  await graph.scrollIntoViewIfNeeded();await graph.evaluate(img=>img.decode());assert.ok(await graph.evaluate(img=>img.naturalWidth>0));
 }
 await page.locator('#l6 .study-figure').screenshot({path:path.join(root,'test-results/tree-study-graph.png')});
 await page.locator('#l8 .study-figure').last().screenshot({path:path.join(root,'test-results/overlap-study-graph.png')});
 await page.locator('#l1 .note-section').filter({has:page.locator('h4',{hasText:'Reading a position from start to finish'})}).screenshot({path:path.join(root,'test-results/detailed-bullets.png')});
 await page.goto(base);await page.evaluate(()=>document.fonts.ready);
 await page.screenshot({path:path.join(root,'test-results/home-desktop.png')});
 await page.locator('[data-review="l1"]').check();await page.reload();assert.ok(await page.locator('[data-review="l1"]').isChecked());
 await page.locator('#search').fill('parity');assert.ok(await page.locator('.lecture[hidden]').count()>0);await page.locator('#search').fill('');
 await page.locator('#search').fill('215/11');assert.ok(await page.locator('#q5').evaluate(e=>e.open),'Search must reveal matching solution');await page.locator('#search').fill('');
 await page.locator('#toggle-solutions').click();assert.equal(await page.locator('#exercise-list details[open]').count(),20);
 await page.locator('#search').fill('parity');await page.locator('#search').fill('');assert.equal(await page.locator('#exercise-list details[open]').count(),20);
 await page.locator('#tree-form [name=kind]').selectOption('put');await page.locator('#tree-form [name=style]').selectOption('american');await page.locator('#tree-form button').click();assert.ok((await page.locator('#tree-result').innerText()).includes('6.'));
 await page.locator('#tree-form [name=S]').fill('1');await page.locator('#tree-form button').click();assert.ok((await page.locator('#tree-result').innerText()).includes('Exercise now'));
 await page.locator('#tree-form [name=r]').fill('10');await page.locator('#tree-form button').click();assert.equal(await page.locator('#tree-nodes table').count(),0);assert.equal(await page.locator('#tree-result .error').count(),1);
 await page.locator('#payoff-form [name=strategy]').selectOption('straddle');await page.locator('#payoff-form button').click();assert.equal(await page.locator('#payoff-chart path').count(),2);
 await page.locator('#brownian-form [name=rho]').fill('-1');await page.locator('#brownian-form button').click();assert.equal(await page.locator('#brownian-chart path').count(),2);
 for(const width of [390,320]){await page.setViewportSize({width,height:844});await page.goto(base);await page.evaluate(()=>document.fonts.ready);assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'mobile overflow at '+width);if(width===390)await page.screenshot({path:path.join(root,'test-results/home-mobile.png')});}
 await page.setViewportSize({width:1100,height:1200});await page.goto(base+'/formula-sheet.html');await page.evaluate(()=>document.fonts.ready);assert.equal(await page.locator('.math-error').count(),0);
 const layout=await page.evaluate(()=>Array.from(document.querySelectorAll('.sheet')).map(s=>({id:s.id,height:s.getBoundingClientRect().height,columns:Array.from(s.querySelectorAll('.column')).map(c=>({bottom:c.getBoundingClientRect().bottom-s.getBoundingClientRect().top,contentBottom:c.lastElementChild.getBoundingClientRect().bottom-s.getBoundingClientRect().top,scroll:c.scrollWidth,width:c.clientWidth}))})));
 fs.writeFileSync(path.join(root,'test-results/sheet-layout.json'),JSON.stringify(layout,null,2));console.log(JSON.stringify(layout));
 for(const s of layout)for(const c of s.columns){assert.ok(c.bottom<s.height-8,'Page overflow '+s.id);assert.ok(c.scroll<=c.width+1,'Column overflow '+s.id);}
 const sourceMath=(fs.readFileSync(path.join(root,'formula-sheet.html'),'utf8').match(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g)||[]).length;
 assert.equal(await page.locator('.math-inline,.math-display').count(),sourceMath,'Missing sheet formulas');
 if(!process.argv.includes('--no-pdf'))await page.pdf({path:path.join(root,'downloads/FM9578A-formula-sheet.pdf'),preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});
 await page.screenshot({path:path.join(root,'test-results/sheet-screen.png'),fullPage:true});
 assert.deepEqual(errors,[]);console.log('PASS browser: content counts, math, graphs, progress, search, tools, responsive and sheet bounds.');
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);process.exit(1)});
