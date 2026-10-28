from content import *
def money(x):return '$'+fmt(x)+'$'
ex(1,'No-arbitrage bounds',r'$S_0=64,K=60,T=.75,r=.05$, no dividends. Find both bounds, test call $4.50$, construct arbitrage.',[
'Call lower '+money(64-60*math.exp(-.0375))+', upper $64$.',
'Put lower $0$, upper '+money(60*math.exp(-.0375))+'.',
'Call quote violates the lower bound.',
r'Buy call and bond paying $60$; short stock. Initial receipt $64-4.5-60e^{-.0375}=$ '+money(64-4.5-60*math.exp(-.0375))+r'. Terminal payoff $(S_T-60)^++60-S_T=(60-S_T)^+\ge0$. Invest the initial receipt.'])
ex(2,'Parity arbitrage',r'$S_0=82,K=85,T=.5,r=.04,c=5.20$; test market put $9$.',[
r'$c+Ke^{-rT}=p+S_0$.',
r'$p=5.2+85e^{-.02}-82=$ '+money(5.2+85*math.exp(-.02)-82)+'.',
'Market put is overpriced relative to its replication.',
r'Buy call and bond paying $85$; short put and stock. Initial receipt $9+82-5.2-85e^{-.02}=$ '+money(9+82-5.2-85*math.exp(-.02))+r'. Terminal $(S_T-85)^++85-(85-S_T)^+-S_T=0$. Invest the receipt.'])
ex(3,'Long straddle',r'Buy call $K=75$ for $6$ and put $K=75$ for $4$. Payoffs, profits at $60,75,95$, break-evens and sketch; ignore financing.',[
r'Call $(S_T-75)^+$; put $(75-S_T)^+$.',r'Combined payoff $|S_T-75|$.',
r'Profit $|S_T-75|-10$: $5,-10,10$ respectively.',r'Break-evens $65,85$.',
r'V-shaped profit: slope $-1$ below $75$, $+1$ above; vertex $(75,-10)$, zero at $65,85$. See payoff explorer.'])
ex(4,'American and European calls','Compare exercise rights, values and early exercise, with and without dividends.',[
'European: only at expiry. American: any allowed time through expiry.',
r'$C\ge c$: more rights cannot reduce value.',
r'No dividends and $r\ge0$: early exercise sacrifices optionality and pays the strike sooner; $C=c$.',
'Dividends may justify exercise immediately before ex-dividend; compare the benefit with lost time value and early strike payment.'])
t5=tree(48,49,.06,.25,1,u=54/48,d=43/48)
ex(5,'One-step replication',r'$S_0=48,S_u=54,S_d=43,K=49,T=.25,r=.06$. Payoffs, hedge, price and probability.',[
r'$f_u=5,f_d=0$.',r'$\Delta=5/11=.454545$.',
r'Long $5/11$ shares, short one call: both states pay $H=54(5/11)-5=43(5/11)=215/11$.',
r'$f_0=48(5/11)-(215/11)e^{-.015}=$ '+money(t5['price'])+'.',
r'$p=(48e^{.015}-43)/11=$ '+money(t5['p'])+r'; $e^{-.015}(5p)=$ '+money(t5['price'])+'.'])
p6=(math.exp(.0125)-.9)/.25
ex(6,'Pricing versus physical probability',r'$S_0=100,u=1.15,d=.9,r=.05,T=.25,\mu=.12$.',[
r'$p_Q=(e^{.0125}-.9)/.25=$ '+money(p6)+'.',
r'$p_Q115+(1-p_Q)90=100e^{.0125}=$ '+money(100*math.exp(.0125))+'.',
r'$p^*=(e^{.03}-.9)/.25=$ '+money((math.exp(.03)-.9)/.25)+'.',
r'Physical probability matches expected return $\mu$; pricing probability matches $r$. Replication prices the option without the investor’s return forecast.'])
t7=tree(60,62,.04,.5,2,u=1.12,d=.9)
ex(7,'Two-step European call',r'$S_0=60,u=1.12,d=.9,r=.04,\Delta t=.25,N=2,K=62$.',[
r'$60\to(67.2,54)\to(75.264,60.48,48.6)$ (high to low).',
r'$p=(e^{.01}-.9)/.22=$ '+money(t7['p'])+'.',r'Payoffs $13.264,0,0$.',
'Upper intermediate '+money(t7['levels'][1]['values'][1])+', lower $0$; root '+money(t7['price'])+'.',
r'$e^{-.02}[p^2(13.264)+2p(1-p)0+(1-p)^2 0]=$ '+money(t7['price'])+'.'])
t8=tree(75,78,.05,2,2,u=1.25,d=.8,put=True)
ex(8,'Two-step European put',r'$S_0=75,K=78,u=1.25,d=.8,r=.05,\Delta t=1,N=2$.',[
r'$75\to(93.75,60)\to(117.1875,75,48)$.',
r'$p=(e^{.05}-.8)/.45=$ '+money(t8['p'])+'.',r'Payoffs $0,3,30$.',
'Upper intermediate '+money(t8['levels'][1]['values'][1])+', lower '+money(t8['levels'][1]['values'][0])+', root '+money(t8['price'])+'.',
'Discount the risk-neutral expected payoff. This is valuation, not a real-world forecast.'])
t9=tree(45,48,.05,1,2,american=True,put=True)
ex(9,'American put: exercise decisions',r'$S_0=45,K=48,r=.05,\sigma=.3,T=1,N=2$; CRR.',[
r'$\Delta t=.5$.',
r'$u=e^{.3\sqrt{.5}}=$ '+money(t9['u'])+', $d=1/u=$ '+money(t9['d'])+'.',
r'$p=(e^{.025}-d)/(u-d)=$ '+money(t9['p'])+'.',
'Intermediate high-to-low: '+', '.join(map(money,reversed(t9['levels'][1]['stocks'])))+'. Terminal prices: '+', '.join(map(money,reversed(t9['levels'][2]['stocks'])))+'. Put payoffs: '+', '.join(map(money,reversed(t9['levels'][2]['values'])))+'.',
'Upper: continuation '+money(t9['levels'][1]['continuation'][1])+' exceeds exercise $0$. Lower: continuation '+money(t9['levels'][1]['continuation'][0])+' below exercise '+money(t9['levels'][1]['exercise'][0])+': exercise.',
'Root '+money(t9['price'])+' exceeds immediate exercise $3$: continue. Early exercise at the low intermediate node.'])
t10=tree(.72,.73,.05,.5,2,sigma=.15,q=.03)
ex(10,'FX call',r'$S_0=.72,K=.73,r=.05,r_f=.03,\sigma=.15,T=.5,N=2$. Domestic per foreign unit.',[
r'$u=e^{.15\sqrt{.25}}=$ '+money(t10['u'])+', $d=$ '+money(t10['d'])+'.',
r'$p=(e^{(.05-.03).25}-d)/(u-d)=$ '+money(t10['p'])+'.',
r'$S_{i,j}=.72u^jd^{i-j}$. Intermediate low-to-high: '+', '.join(map(money,t10['levels'][1]['stocks']))+'; terminal: '+', '.join(map(money,t10['levels'][2]['stocks']))+'.',
'Terminal payoffs low-to-high: '+', '.join(map(money,t10['levels'][2]['values']))+'.',
'Discount at domestic r: call '+money(t10['price'])+'.',
r'Foreign interest acts as yield, reducing growth to $r-r_f$, not replacing domestic discounting.'])
ex(11,'Wiener distributions and tails',r'Standard $W_0=0$: distributions at 2 and over [2,5], moments at 4, tail at 1.5, independence.',[
r'$W_2\sim N(0,2)$.',r'$W_5-W_2\sim N(0,3)$.',
r'$E[W_4]=0$, variance $4$, SD $2$.',r'$P(W_1>1.5)=1-\Phi(1.5)\approx.066807$.',
'Independent non-overlapping increments are a defining property. Levels are not generally independent.'])
ex(12,'Generalized Wiener process',r'$dX=8dt+12dW,X_0=30$ million; years.',[
r'Drift $8$, variance rate $144$; diffusion $12$.',r'$X_1\sim N(38,144)$.',
r'$E[X_{.5}]=34$ million.',r'SD at two years $12\sqrt2=16.9706$ million.',
r'$P(X_1<25)=\Phi(-13/12)\approx.1393$.'])
ex(13,'Mean reversion',r'$dX=.6(50-X)dt+8dW$; drift at $40,50,65$; local moments at $40,\Delta t=.1$.',[
r'$a=.6(50-X)$, $b=8$.',r'Drifts $6,0,-9$.',
r'Drift pulls toward $50$, proportional to distance; noise remains.',
r'$E_t[\Delta X]\approx.6$, variance $\approx6.4$. Local, not exact finite-time mean-reversion moments.'])
ex(14,'Local Itô moments',r'$dX=(4+.2X)dt+.15XdW$, $X=80,\Delta t=1/12$.',[
r'$a=4+.2X$, $b=.15X$.',r'Drift $20$.',r'Variance rate $12^2=144$.',
r'Mean change $\approx20/12=1.6667$; variance $\approx12$.',
r'$X_{t+1/12}\approx80+20/12+\sqrt{12}\varepsilon$.'])
ex(15,'GBM: percentages and dollars',r'$S=120,\mu=.09,\sigma=.24$; one month.',[
r'Drift $10.8$; diffusion $28.8$.',r'$dS/S=.09dt+.24dW$.',
r'Proportional mean $\approx.0075=0.75\%$.',r'Proportional SD $\approx.24/\sqrt{12}=.069282=6.9282\%$.',
r'Dollar mean $\approx.9$; SD $\approx8.3138$.'])
prices=[];s=100
for z in [.5,-1.2,.8]:s*=1+.06/12+.2/math.sqrt(12)*z;prices.append(s)
ex(16,'Three Euler steps',r'$S_0=100,\mu=.06,\sigma=.2,\Delta t=1/12$; shocks $.5,-1.2,.8$.',[
r'$S_{i+1}=S_i(1+.06/12+.2\varepsilon_i/\sqrt{12})$.',
'$S_1=$ '+money(prices[0])+'.','$S_2=$ '+money(prices[1])+'; use the updated first price.',
'$S_3=$ '+money(prices[2])+'.','Independent shocks do not imply independent recursively built price levels.'])
ex(17,'Step-size comparison',r'$dS=.07Sdt+.25SdW,S_0=90$; quarter versus month.',[
r'Quarter $S_{i+1}=S_i(1+.0175+.125\varepsilon_i)$.',
r'Month $S_{i+1}=S_i(1+.07/12+.25\varepsilon_i/\sqrt{12})$.',
r'At $90$: quarterly mean $1.575$, variance $126.5625$; monthly mean $.525$, variance $42.1875$ (local).',
r'Quarter the step: SD halves, since $\sqrt{\Delta t/4}=\sqrt{\Delta t}/2$.',
'Smaller steps reduce coefficient-freezing/discretization error at greater computational cost.'])
ex(18,'Correlated increments',r'$dX_1=3dt+5dW_1,dX_2=2dt+7dW_2,\rho=.65,\Delta t=.25$.',[
r'Means $.75,.5$.',r'Variances $6.25,12.25$.',
r'Covariance $.65(5)(7)(.25)=5.6875$.',r'Correlation $.65$.',
r'Changing $\rho$ to $-.65$ reverses covariance/correlation signs; marginal means and variances remain.'])
ex(19,'Correlated shocks',r'Independent $U,V\sim N(0,1)$; $\varepsilon_1=U,\varepsilon_2=\rho U+\sqrt{1-\rho^2}V$.',[
'Both means are zero by linearity.',
r'First variance $1$; second $\rho^2+(1-\rho^2)=1$, using zero covariance of U,V.',
r'$\operatorname{Cov}(\varepsilon_1,\varepsilon_2)=\rho\operatorname{Var}(U)=\rho$.',
r'$\rho=-.4,U=.6,V=-1.1$: $\varepsilon_1=.6$, $\varepsilon_2=-.24-1.1\sqrt{.84}=$ '+money(-.24-1.1*math.sqrt(.84))+'.',
'Fresh independent U,V pair each step; use its correlated shocks in the stock updates.'])
z2=.4-.5*math.sqrt(.75)
ex(20,'Two-stock simulation',r'$S_1=100,S_2=80,\mu_1=.08,\mu_2=.05,\sigma_1=.2,\sigma_2=.3,\rho=.5,\Delta t=1/12$.',[
r'$S_1^+=S_1(1+.08/12+.2\varepsilon_1/\sqrt{12})$; $S_2^+=S_2(1+.05/12+.3\varepsilon_2/\sqrt{12})$.',
r'Local/Euler dollar means $\approx.6667,.3333$.',r'Local/Euler dollar SDs $\approx5.7735,6.9282$.',
r'Local/Euler dollar covariance $\approx.5(.2)(.3)(100)(80)/12=20$.',
r'$U=.8,V=-.5$: $\varepsilon_1=.8$, $\varepsilon_2=.4-.5\sqrt{.75}=$ '+money(z2)+'. Updated prices '+money(100*(1+.08/12+.2/math.sqrt(12)*.8))+', '+money(80*(1+.05/12+.3/math.sqrt(12)*z2))+'.'])
extra=[]
for label,params in [
('1 / 4',dict(S=78,K=80,r=.03,T=4/12,N=2,sigma=.3)),
('2',dict(S=50,K=51,r=.05,T=.5,N=2,u=1.06,d=.95)),
('3 European',dict(S=40,K=42,r=.12,T=.5,N=2,u=1.1,d=.9,put=True)),
('3 American',dict(S=40,K=42,r=.12,T=.5,N=2,u=1.1,d=.9,put=True,american=True)),
('6 call',dict(S=90,K=93,r=.03,T=.75,N=3,sigma=.28,q=.03,american=True)),
('6 put',dict(S=90,K=93,r=.03,T=.75,N=3,sigma=.28,q=.03,american=True,put=True))]:
    result=tree(**params)
    delta=(result['levels'][1]['values'][1]-result['levels'][1]['values'][0])/(result['levels'][1]['stocks'][1]-result['levels'][1]['stocks'][0])
    extra.append(dict(label=label,params=params,result=result,delta=delta))
lectures[0]['sections'].append(dict(title='Lecture contract conventions',body=r'''The slides illustrate January-cycle expiries (Jan/Apr/Jul/Oct), February (Feb/May/Aug/Nov), and March (Mar/Jun/Sep/Dec). They describe third-Friday monthly expiries, additional weekly Fridays, LEAPS maturities up to 39 months and strike spacing of $2.50$, $5$ or $10$. These are the lecture’s examples: verify the specific contract rather than assuming every market follows them. Also check position/exercise limits and corporate-action adjustments. [pp. 19–20]'''))
worked=[]
for label,params in [
 ('American put, p. 22',dict(S=50,K=52,r=.05,T=2,N=2,sigma=.3,put=True,american=True)),
 ('No-dividend call, p. 27',dict(S=50,K=50,r=.05,T=.5,N=2,sigma=.3,american=True)),
 ('2% yield call, pp. 31–32',dict(S=50,K=50,r=.05,T=.5,N=2,sigma=.3,q=.02,american=True)),
 ('Index call, p. 33',dict(S=810,K=800,r=.05,T=.5,N=2,sigma=.2,q=.02)),
 ('FX American call, pp. 35–37',dict(S=.61,K=.60,r=.05,T=.25,N=3,sigma=.12,q=.07,american=True))]:
    result=tree(**params)
    worked.append('<p><b>'+label+':</b> '+', '.join(str(k)+'='+str(v) for k,v in params.items())+'. Value '+money(result['price'])+', probability '+money(result['p'])+'.</p>')
lectures[6]['sections'].insert(-1,dict(title='Lecture numerical examples',body=''.join(worked)+r'''<p>At the upper node of the 2% yield call, continuation is about $8.42$, above exercise $8.09$, so do not exercise. The $4$ cash dividend immediately after $t=.25$ in pp. 28–29 is a separate model: compare exercise before the cash drop, not the continuous-yield example.</p>'''))
lectures[8]['sections'].append(dict(title='Lecture monthly stock example',body=r'''For $S=100$, $\mu=.08$, $\sigma=.20$, one month gives local proportional mean $.08/12=.006667$ and SD $.2/\sqrt{12}=.057735$. Dollar mean is $.6667$ and dollar SD $5.7735$. The local variance is $(.2\cdot100)^2/12=33.3333$, not the SD. [pp. 29–32]'''))
lectures[2]['sections'].append(dict(title='Assumptions behind an arbitrage argument',body=r'''The slides also assume trading profits are taxed consistently and arbitrage opportunities are rapidly exploited. Compare cash flows on the same dates under the same trading constraints; a difference between a model estimate and a quote alone is not a complete arbitrage proof. [L3 p. 10]'''))
lectures[4]['sections'].append(dict(title='Explicit strategy formulas',body=r'''For $K_1<K_2$, the bear-put payoff is $K_2-K_1$ if $S_T\le K_1$, $K_2-S_T$ between strikes, and $0$ if $S_T\ge K_2$. The bull-call payoff is $0$, then $S_T-K_1$, then $K_2-K_1$. An equally spaced butterfly pays $(S_T-K_1)^+-2(S_T-K_2)^++(S_T-K_3)^+$. Strip payoff: $(S_T-K)^++2(K-S_T)^+$. Strap payoff: $2(S_T-K)^++(K-S_T)^+$. Subtract the total net debit for unfinanced profit. [L5 pp. 19–27, 33–34]'''))
lectures[6]['sections'].append(dict(title='Volatility matching: expanded identity',body=r'''Let $R=\Delta S/S$, taking values $u-1$ and $d-1$. Its exact two-point variance is $$\operatorname{Var}(R)=p(u-1)^2+(1-p)(d-1)^2-[p(u-1)+(1-p)(d-1)]^2.$$ With $a=pu+(1-p)d$, this equals $p(1-p)(u-d)^2=a(u+d)-ud-a^2$. The lecture uses the small-step target $\sigma^2\Delta t$. CRR approaches this target as the step shrinks; its factors do not solve that finite-step equation exactly in general. [L7 pp. 14–16]'''))
lectures[6]['sections'].append(dict(title='Physical versus risk-neutral stock dynamics',body=r'''For a non-dividend stock, the lecture writes $$\frac{dS}{S}=\mu\,dt+\sigma\,dW_t\quad\text{under the physical measure},$$ $$\frac{dS}{S}=r\,dt+\sigma\,dW_t^Q\quad\text{under }Q.$$ $W_t^Q$ is Brownian motion under the pricing measure. The drift changes, volatility does not; in the tree the probabilities change while $u,d$ stay the same. The same symbol $W$ without a measure label should not obscure which probability model is being used. [L7 pp. 17–19]'''))
lectures[7]['sections'].append(dict(title='The slides’ z notation and conditional-law formula',body=r'''The slides also use $z(t)$ or $z_t$ for a stochastic process; in the standard Wiener examples, $dz$ plays the same role as $dW$. Always identify whether $z$ is a level or $\Delta z=z(t+\Delta t)-z(t)$ is an increment. The Markov statement is $$\Pr(X_{t+h}\in B\mid\mathcal F_t)=\Pr(X_{t+h}\in B\mid X_t),$$ where $B$ is any set of possible future values. For $N$ independent standard normal shocks and $T=N\Delta t$, $$W_T-W_0=\sum_{i=1}^N\sqrt{\Delta t}\,\varepsilon_i\sim N(0,T).$$ A sum of independent normals is normal; add their variances, not their standard deviations. [L8 pp. 6–14, 20–21]'''))
notation.extend([
 (r'z(t),z_t,Z(t),dz','Alternative process/Wiener notation in the slides; Δz is a change, not the current level.'),
 (r'W_t^Q','Wiener process under the risk-neutral probability measure Q.'),
 (r'F_0','Forward delivery price or current futures quote, according to the contract being discussed.'),
 (r'H,A','H: terminal cash value of the riskless stock–option hedge. A: strategy net debit, or budget in the principal-protection example.'),
 (r'i,j,M','i: time-step index; j: up-move count; M: option units when hedging, or number of simulated paths in a cost calculation.')])
lectures[7]['sections'].append(dict(title='Brownian covariance and correlation: supplement',body=r'''The supplement calls standard Brownian motion $Z(t)$; here $W_t=Z(t)$ denotes the same process. For $s\le t$, write $W_t=W_s+(W_t-W_s)$. The later increment is independent of $W_s$, giving $\operatorname{Cov}(W_s,W_t)=\operatorname{Var}(W_s)=s$. Thus $$\operatorname{Cov}(W_s,W_t)=\min(s,t),\qquad \operatorname{Corr}(W_s,W_t)=\frac{\min(s,t)}{\sqrt{st}}=\sqrt{\frac{\min(s,t)}{\max(s,t)}}\quad(s,t>0).$$ For linear combinations, $$\operatorname{Cov}\left(\sum_i a_iW_{t_i},\sum_j b_jW_{s_j}\right)=\sum_{i,j}a_ib_j\min(t_i,s_j).$$ Use bilinearity to expand first. Joint Gaussianity then permits the zero-covariance independence test; nonlinear functions need a separate justification. [Brownian supplement pp. 1–3]'''))
import re
def safe_math(value):
    if isinstance(value,str):
        return re.sub(r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$',lambda m:m.group(0).replace('<','&lt;').replace('>','&gt;'),value)
    if isinstance(value,list):return [safe_math(v) for v in value]
    if isinstance(value,tuple):return [safe_math(v) for v in value]
    if isinstance(value,dict):return {k:safe_math(v) for k,v in value.items()}
    return value
from coverage_details import complete
complete(lectures,tree)
from question_prompts import attach_prompts
attach_prompts(exercises,extra)
from study_notes import enrich
enrich(lectures,exercises)
from lecture_notation import apply_source_notation
apply_source_notation(lectures,exercises,notation,dependence)
data=safe_math(dict(lectures=lectures,notation=notation,exercises=exercises,dependence=dependence,extra=extra))
(ROOT/'assets/course-data.js').write_text('window.COURSE='+json.dumps(data,ensure_ascii=False)+';\n',encoding='utf-8')
print('Authored',len(lectures),'lectures,',len(exercises),'exercises,',sum(len(e['answers']) for e in exercises),'subparts,',len(dependence),'dependence examples.')
