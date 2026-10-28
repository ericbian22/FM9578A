function updateFormulaOverflow(el){
 const wide=el.scrollWidth>el.clientWidth+1;
 el.classList.toggle('formula-scrollable',wide);
 if(wide){el.tabIndex=0;el.setAttribute('role','region');el.setAttribute('aria-label','Mathematical formula; scroll horizontally to see all symbols');}
 else{el.removeAttribute('tabindex');el.removeAttribute('role');el.removeAttribute('aria-label');}
}
const formulaResize=typeof ResizeObserver==='undefined'?null:new ResizeObserver(entries=>entries.forEach(entry=>updateFormulaOverflow(entry.target)));
window.renderMath=function(root=document.body){
 const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>/^(SCRIPT|STYLE|TEXTAREA|PRE|CODE)$/.test(n.parentElement.tagName)||n.parentElement.closest('.katex')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT});
 const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
 for(const node of nodes){if(!node.nodeValue.includes('$'))continue;
 const re=/\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g;let match,last=0,found=false;const frag=document.createDocumentFragment();
 while((match=re.exec(node.nodeValue))){found=true;frag.append(document.createTextNode(node.nodeValue.slice(last,match.index)));const el=document.createElement(match[1]?'div':'span');el.className=match[1]?'math-display':'math-inline';
 try{ReviewKatex.render(match[1]||match[2],el,{displayMode:!!match[1],throwOnError:true,strict:'ignore',trust:false});}catch(e){el.classList.add('math-error');el.textContent=match[0];console.error(e.message);}
 frag.append(el);last=re.lastIndex;}if(found){frag.append(document.createTextNode(node.nodeValue.slice(last)));node.replaceWith(frag);}
 }
 const displays=[...root.querySelectorAll('.math-display')].filter(el=>!el.closest('.sheet'));
 displays.forEach(el=>{updateFormulaOverflow(el);formulaResize?.observe(el);});
 document.fonts?.ready.then(()=>displays.forEach(updateFormulaOverflow));
 };
