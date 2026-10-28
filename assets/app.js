const C=window.COURSE;
const el=id=>document.getElementById(id);
const num=x=>Number(x).toLocaleString('en-US',{maximumFractionDigits:6});
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
let reviewed=[];try{const saved=JSON.parse(localStorage.getItem('fm9578-reviewed')||'[]');if(Array.isArray(saved))reviewed=[...new Set(saved)].filter(id=>C.lectures.some(l=>l.id===id));}catch(e){}
el('lecture-list').innerHTML=C.lectures.map(l=>'<article id="'+l.id+'" class="lecture searchable"><header class="lecture-heading"><div><span class="lecture-number">LECTURE '+String(l.number).padStart(2,'0')+' / '+l.pages+' SOURCE PAGES</span><h3>'+l.title+'</h3><p>'+l.subtitle+'</p></div><label class="review-check"><input type="checkbox" data-review="'+l.id+'" '+(reviewed.includes(l.id)?'checked':'')+'> Reviewed</label></header><div class="lecture-body">'+l.sections.map(s=>'<section class="note-section"><h4>'+s.title+'</h4><div class="body">'+s.body+'</div></section>').join('')+'</div></article>').join('');
document.querySelector('nav a[href="#notation"] span').textContent=C.notation.length;
el('notation-body').innerHTML=C.notation.map(([s,m])=>'<tr class="searchable"><td>$'+s+'$</td><td>'+m+'</td></tr>').join('');
el('exercise-list').innerHTML=C.exercises.map(e=>'<details class="exercise searchable" id="q'+e.number+'"><summary><span class="qno">'+String(e.number).padStart(2,'0')+'</span>'+e.title+'</summary><div class="question">'+e.question+'</div><div class="answers">'+e.answers.map(a=>'<div class="answer"><b>('+a.part+')</b><div>'+a.body+'</div></div>').join('')+'<div class="solution-reasoning"><h4>Why these steps work</h4>'+e.reasoning+'</div></div></details>').join('');
el('dependence-list').innerHTML=C.dependence.map(([id,math,status,why])=>'<article class="dep-card searchable" id="dep-'+id+'"><h4>('+id+') $'+math+'$</h4><span class="badge '+status.toLowerCase()+'">'+status+'</span><p>'+why+'</p></article>').join('');
el('extra-list').innerHTML=C.extra.map(e=>{
 const r=e.result,p=e.params;
 const early=r.levels.flatMap(l=>l.continuation?l.stocks.map((s,j)=>p.american&&l.exercise[j]>l.continuation[j]+1e-10?'step '+l.i+', price '+num(s):null).filter(Boolean):[]);
 return '<details class="exercise searchable"><summary>L7 exercise '+e.label+'</summary><div class="answers"><p>Inputs: '+Object.entries(p).map(([k,v])=>escapeHtml(k)+' = '+escapeHtml(v)).join('; ')+'. '+(e.label.startsWith('6')?'Futures: a = 1 (q=r here is an equivalent growth setting).':'')+'</p><p>u = '+num(r.u)+'; d = '+num(r.d)+'; p = '+num(r.p)+'; value = <b>'+num(r.price)+'</b>; next-node value slope = '+num(e.delta)+'.</p>'+(e.label==='1 / 4'?'<p>Short 1,000 option units: buy '+num(1000*e.delta)+' shares initially. If “options” means contracts, multiply by the stated contract multiplier.</p>':'')+(p.american?'<p>Strict early-exercise nodes: '+(early.join('; ')||'none')+'.</p>':'')+'<div class="table-wrap">'+nodeTable(r)+'</div></div></details>';
}).join('')+'<details class="exercise searchable"><summary>L7 exercise 5 · FX factors</summary><div class="answers"><p>Δt = 1/12, r=.05, r_f=.08, σ=.12.</p><p>u = '+num(Math.exp(.12/Math.sqrt(12)))+', d = '+num(Math.exp(-.12/Math.sqrt(12)))+', a = '+num(Math.exp(-.03/12))+', p = '+num((Math.exp(-.03/12)-Math.exp(-.12/Math.sqrt(12)))/(Math.exp(.12/Math.sqrt(12))-Math.exp(-.12/Math.sqrt(12))))+'. Discount at domestic r.</p></div></details>';
function nodeTable(r){return '<table><thead><tr><th>Step</th><th>Underlying (low → high)</th><th>Option values</th></tr></thead><tbody>'+r.levels.map(l=>'<tr><td>'+l.i+'</td><td>'+l.stocks.map(num).join(' · ')+'</td><td>'+l.values.map(num).join(' · ')+'</td></tr>').join('')+'</tbody></table>';}
el('source-table').innerHTML='<div class="table-wrap"><table><thead><tr><th>Source</th><th>Coverage</th><th>Location</th></tr></thead><tbody>'+C.lectures.map(l=>'<tr><td>Lecture '+l.number+'</td><td>'+l.pages+' pages; repeated builds grouped</td><td><a href="#'+l.id+'">'+l.title+'</a></td></tr>').join('')+'<tr><td>Suggested Exercises 1</td><td>7 pages · Q1–20 · 97 subparts</td><td><a href="#practice">Worked exercises</a></td></tr><tr><td>Brownian dependence supplement</td><td>3 pages · examples (a)–(i)</td><td><a href="#dependence">Dependence reference</a></td></tr></tbody></table></div>';
renderMath();
function progress(){el('progress-label').textContent=reviewed.length+' / 9 lectures reviewed';el('progress-bar').style.width=reviewed.length/9*100+'%';}
progress();document.querySelectorAll('[data-review]').forEach(box=>box.addEventListener('change',()=>{reviewed=Array.from(document.querySelectorAll('[data-review]:checked'),b=>b.dataset.review);try{localStorage.setItem('fm9578-reviewed',JSON.stringify(reviewed))}catch(e){}progress();}));
el('toggle-solutions').addEventListener('click',()=>{const open=el('toggle-solutions').textContent.startsWith('Show');document.querySelectorAll('#exercise-list details').forEach(d=>d.open=open);el('toggle-solutions').textContent=open?'Hide all solutions':'Show all solutions';});
const searchable=Array.from(document.querySelectorAll('.searchable')).map(n=>({n,text:n.textContent.toLowerCase(),wasOpen:n.open}));
let searchActive=false;
el('search').addEventListener('input',()=>{
 const q=el('search').value.trim().toLowerCase();let count=0;
 if(q&&!searchActive)searchable.forEach(entry=>entry.wasOpen=entry.n.open);
 searchable.forEach(({n,text,wasOpen})=>{const hit=!q||text.includes(q);n.hidden=!hit;if(n.tagName==='DETAILS')n.open=q?hit:wasOpen;if(hit)count++;});
 searchActive=!!q;el('search-status').textContent=q?count+' matching entries. Clear search to show all.':'';
});
function values(form){return Object.fromEntries(Array.from(new FormData(form),([k,v])=>[k,['strategy','underlying','kind','style'].includes(k)?v:Number(v)]));}
function chart(id,rows,xlabel){
 const svg=el(id),W=760,H=300,L=60,R=25,B=45,U=20;let xmin=rows[0][0],xmax=rows.at(-1)[0],ys=rows.flatMap(r=>r.slice(1));let ymin=Math.min(0,...ys),ymax=Math.max(0,...ys);if(ymax===ymin)ymax=ymin+1;const pad=(ymax-ymin)*.12;ymin-=pad;ymax+=pad;
 const x=v=>L+(v-xmin)/(xmax-xmin)*(W-L-R),y=v=>H-B-(v-ymin)/(ymax-ymin)*(H-B-U);let html='';
 for(let i=0;i<=4;i++){const v=ymin+(ymax-ymin)*i/4,yy=y(v);html+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+yy+'" y2="'+yy+'" stroke="#e4e9df"/><text x="'+(L-10)+'" y="'+(yy+4)+'" text-anchor="end" fill="#64766e" font-size="11">'+v.toFixed(2)+'</text>';const vx=xmin+(xmax-xmin)*i/4;html+='<text x="'+x(vx)+'" y="'+(H-24)+'" text-anchor="middle" fill="#64766e" font-size="11">'+vx.toFixed(2)+'</text>';}
 html+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+y(0)+'" y2="'+y(0)+'" stroke="#9cae9e"/>';
 [1,2].forEach((col,j)=>{html+='<path d="'+rows.map((r,i)=>(i?'L':'M')+x(r[0]).toFixed(2)+' '+y(r[col]).toFixed(2)).join(' ')+'" fill="none" stroke="'+['#276a57','#c58a34'][j]+'" stroke-width="2.5"/>';});
 html+='<text x="'+(W/2)+'" y="'+(H-3)+'" text-anchor="middle" fill="#64766e" font-size="11">'+xlabel+'</text>';svg.innerHTML=html;
}
function handle(form,result,fn){const run=e=>{if(e)e.preventDefault();try{fn(values(form));}catch(e){el(result).innerHTML='<p class="error">'+escapeHtml(e.message)+'</p>';}};form.addEventListener('submit',run);run();}
handle(el('payoff-form'),'payoff-result',o=>{
 if(![o.K,o.width,o.debit].every(Number.isFinite)||o.K<=0||o.width<=0)throw Error('Use a positive strike and strike width, and a finite net debit.');
 const xmax=Math.max(o.K*1.8,o.K+3*o.width),rows=Array.from({length:181},(_,i)=>{const s=xmax*i/180,v=Models.payoff(s,o.K,o.width,o.strategy);return[s,v,v-o.debit]});
 chart('payoff-chart',rows,'Terminal underlying price S_T');
 el('payoff-result').textContent='At S_T = K: payoff '+num(Models.payoff(o.K,o.K,o.width,o.strategy))+', profit '+num(Models.payoff(o.K,o.K,o.width,o.strategy)-o.debit)+'. For stock-containing strategies, net debit must include the stock purchase.';
});
handle(el('tree-form'),'tree-result',o=>{
 el('tree-nodes').innerHTML='';const r=Models.binomial(o);el('tree-result').innerHTML='<div class="result"><div>Option value<strong>'+num(r.price)+'</strong></div><div>Continuation hedge (units)<strong>'+(r.exerciseNow?'Exercise now':num(r.delta))+'</strong></div><div>Up probability p<strong>'+num(r.p)+'</strong></div></div><p>Δt = '+num(r.dt)+' · u = '+num(r.u)+' · d = '+num(r.d)+' · growth a = '+num(r.a)+'</p><p>'+ (r.exerciseNow?'Immediate exercise is optimal at the root; a continuation hedge is not recommended.':o.underlying==='future'?'Hedge is futures units per option unit, using next-node payoff differences and settlement at the next tree date; it is not the discounted price sensitivity.':'Hedge is initial underlying units per option unit. With yield/foreign interest reinvested, it equals exp(−q Δt) times the next-node value slope; for FX use q = r_f.')+'</p>';
 el('tree-nodes').innerHTML=o.N<=8?nodeTable(r):'<p>Full node table shown for N ≤ 8. Price above uses all '+o.N+' steps.</p>';
});
handle(el('brownian-form'),'brownian-result',o=>{
 const rows=Models.brownian(o.T,o.rho,o.seed);chart('brownian-chart',rows,'Time (years)');el('brownian-result').innerHTML='<div class="result"><div>Mean at T<strong>0</strong></div><div>Variance at T<strong>'+num(o.T)+'</strong></div><div>SD at T<strong>'+num(Math.sqrt(o.T))+'</strong></div><div>Covariance at T<strong>'+num(o.rho*o.T)+'</strong></div></div>';
});
if(location.hash){const target=document.getElementById(location.hash.slice(1));if(target){if(target.tagName==='DETAILS')target.open=true;requestAnimationFrame(()=>target.scrollIntoView());}}
