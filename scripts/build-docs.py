from exercises import *
import re,html
groups=[
[(1,2,'Title and overview'),(3,10,'Derivatives, contracts, participants'),(11,17,'Exercise rights and payoffs'),(18,24,'Contract details and quotes')],
[(1,12,'L1 review'),(13,13,'Mark to market/model'),(14,15,'Margin'),(16,16,'Missing referenced spreadsheet')],
[(1,2,'Overview'),(3,10,'Notation, effects, assumptions'),(11,16,'Bounds'),(17,17,'Parity')],
[(1,2,'Overview'),(3,5,'Synthetic positions and arbitrage'),(6,9,'Early exercise'),(10,11,'American bounds'),(12,14,'Dividends')],
[(1,11,'Overview and workflow; repeated builds'),(12,16,'Protection and covered positions'),(17,23,'Spreads'),(24,27,'Box and butterfly'),(28,29,'Calendar and diagonal'),(30,38,'Combinations'),(39,42,'Butterfly example and payoff/profit')],
[(1,2,'Overview'),(3,10,'One step and risk-neutral valuation'),(11,14,'Two-step call'),(15,16,'Two-step put'),(17,18,'Exercise and summary')],
[(1,2,'Overview'),(3,7,'American exercise'),(8,13,'Dynamic delta and root correction'),(14,25,'CRR, measure change, algorithms'),(26,32,'Yield and cash dividends'),(33,37,'Index and FX'),(38,41,'Forward/futures'),(42,47,'Exercises 1–6; 4 repeats 1')],
[(1,7,'Overview and Markov'),(8,18,'Wiener properties'),(19,27,'Scaling and paths'),(28,34,'Generalized Wiener')],
[(1,24,'L8 review; covariance p6'),(25,28,'Itô processes'),(29,32,'GBM'),(33,36,'Euler'),(37,39,'Correlation')]
]
names=['Lecture 1 FM9578.pdf','Lecture 2 FM9578.pdf','Lecture 3.pdf','Lecture 4.pdf','Lecture 5 FM9578A.pdf','Lecture 6 FM9578A.pdf','Lecture 7 FM9578A.pdf','Lecture 8 FM9578A.pdf','Lecture 9 FM9578A.pdf']
coverage=[]
for l,g,name in zip(lectures,groups,names):
    assert [p for a,b,_ in g for p in range(a,b+1)]==list(range(1,l['pages']+1))
    coverage.append(dict(file=name,pages=l['pages'],destination='index.html#'+l['id'],groups=[dict(first=a,last=b,topic=t) for a,b,t in g]))
coverage.extend([dict(file='Independence and Dependence Brownian Motions.pdf',pages=3,destination='index.html#dependence',examples=list('abcdefghi')),dict(file='FM9578A_Suggested_Exercises1.pdf',pages=7,destination='index.html#practice',questions=[dict(number=e['number'],parts=[a['part'] for a in e['answers']]) for e in exercises])])
assert sum(x['pages'] for x in coverage)==261
(ROOT/'downloads/source-coverage.json').write_text(json.dumps(coverage,indent=2),encoding='utf8')
def clean(s):
    s=re.sub(r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$',lambda m:m.group(0).replace('<','&lt;').replace('>','&gt;'),s)
    fence=chr(96)*3
    s=s.replace('<pre>','\n'+fence+'\n').replace('</pre>','\n'+fence+'\n').replace('<b>','**').replace('</b>','**').replace('<br>','\n')
    return html.unescape(re.sub('<[^>]+>','',s))
md=['# FM9578A — Mathematics of Financial Options','Course-specific notes based on supplied Lectures 1–9. Solutions are independently worked, not official. N(m,v) uses variance. Local approximations are marked. Physical PDF page references.']
for l in lectures:
    md+=['\n## Lecture '+str(l['number'])+' · '+l['title'],l['subtitle']]
    for s in l['sections']:md+=['\n### '+s['title'],clean(s['body'])]
md+=['\n## Notation','| Symbol | Meaning |','|---|---|']
md+=['| $'+s+'$ | '+m+' |' for s,m in notation]
md+=['\n## Suggested exercises — all 20 / 97 subparts']
for e in exercises:
    md+=['\n### Q'+str(e['number'])+' · '+e['title'],e['question']]
    md+=['\n('+a['part']+') '+clean(a['body']) for a in e['answers']]
md+=['\n## Brownian dependence supplement']
md+=['\n### ('+i+') $'+m+'$\n'+result+'. '+why for i,m,result,why in dependence]
md+=['\n## Lecture 7 exercise answers']
for e in extra:
    md+=['\n### Exercise '+e['label'],str(e['params']),'Value '+fmt(e['result']['price'])+'; next-node value slope '+fmt(e['delta'])+'; u '+fmt(e['result']['u'])+'; d '+fmt(e['result']['d'])+'; p '+fmt(e['result']['p'])]
    if e['label']=='1 / 4':md+=['To hedge 1000 short option units, buy '+fmt(1000*e['delta'])+' shares initially; multiply again if contracts have a multiplier.']
    for level in e['result']['levels']:
        md+=['Step '+str(level['i'])+': stock '+str(level['stocks'])+'; option '+str(level['values'])]
        if 'continuation' in level:md+=['Continuation '+str(level['continuation'])+'; immediate exercise '+str(level['exercise'])]
md+=['\nExercise 5: dt=1/12, r=.05, rf=.08, sigma=.12. u=exp(.12/sqrt(12)), d=1/u, a=exp(-.03/12), p=(a-d)/(u-d). Values: u=1.035248, d=0.965952, a=0.997503, p=0.455308.',
'\n## Limitations and corrections','L2 margin spreadsheet not supplied. L7 p13 root .9334 is inconsistent: parameters give .9497. CRR variance matching is local/asymptotic. Original source PDFs are not republished.']
(ROOT/'downloads/FM9578A-notes.md').write_text('\n\n'.join(md),encoding='utf8')
print('Coverage: 11 documents, 261 pages, 20 questions, 97 subparts; Markdown exported.')
