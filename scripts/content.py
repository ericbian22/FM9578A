"""FM9578A authored content; physical PDF page references."""
import json,pathlib,math
ROOT=pathlib.Path(__file__).resolve().parents[1]
lectures=[]
def lecture(n,title,pages,subtitle,sections):
    lectures.append(dict(id=f'l{n}',number=n,title=title,pages=pages,subtitle=subtitle,sections=[dict(title=t,body=b) for t,b in sections]))
lecture(1,'Contracts, payoffs & market language',24,'Separate the contract, its payoff, and the investor’s profit.',[
('Derivatives and participants',r'''A derivative depends on an underlying stock, index, rate, currency, commodity or other variable. <b>Hedgers</b> reduce an existing exposure; <b>speculators</b> take a view; <b>arbitrageurs</b> exploit inconsistent prices without net risk. Exchange contracts are standardized and cleared; OTC contracts can be customized but introduce counterparty exposure. [pp. 3–10]'''),
('Forward, futures, option',r'''Long forward payoff $S_T-K$; short $K-S_T$. A forward commits both parties. Futures are standardized and marked to market. An option buyer pays a premium for a <b>right</b>; the writer has the corresponding obligation. European exercise is only at expiry; American exercise is allowed earlier too. [pp. 6–12]'''),
('Four positions: payoff ≠ profit',r'''Let $x^+=\max(x,0)$. Long call $(S_T-K)^+$; short call $-(S_T-K)^+$; long put $(K-S_T)^+$; short put $-(K-S_T)^+$. Ignoring financing, long-call profit is $(S_T-K)^+-c_0$, long-put profit $(K-S_T)^+-p_0$. Break-evens: $K+c_0$, $K-p_0$. If cash flows are measured at expiry with financing, subtract the future value of the premium instead. [pp. 13–17]<div class="example">Call $K=50$, premium $4$: at $S_T=62$, payoff $12$, profit $8$; at $48$, payoff $0$, profit $-4$. Multiply by 100 for the lecture’s 100-share contract convention.</div>'''),
('Moneyness and time value',r'''Call ITM: $S>K$; put ITM: $S<K$; ATM: $S=K$. Moneyness ignores premium, so ITM does not ensure profit. Intrinsic values: $(S-K)^+$ and $(K-S)^+$. Time value = option price − intrinsic value. American value is at least exercise value. $S=56,K=50,c=9$ gives intrinsic $6$, time value $3$. [pp. 21–22]'''),
('Contract and quote checklist',r'''Check underlying, call/put, strike, expiry, style, settlement and multiplier. A <b>class</b> groups calls or puts on an underlying; a <b>series</b> fixes strike and expiry. Index options may be cash settled; exercising a futures option creates a futures position. Corporate actions can alter terms. Monthly cycles, strike intervals and LEAPS in the slides are course conventions, not universal specifications. Close a long by selling the same series; close a short by buying it back. Bid $4$, ask $4.50$: spread $.50$, midpoint $4.25$, 100-share immediate round trip costs $50$ before fees. [pp. 18–24]''')])
lecture(2,'Trading, valuation & margin',16,'A quoted price, model value, premium and collateral are different things.',[
('Consolidated review',r'''Pages 1–12 repeat Lecture 1’s four positions, contract terms, moneyness, intrinsic/time value and bid–ask conventions. Those explanations are consolidated in L1 rather than silently omitted.'''),
('Market versus model',r'''<b>Mark to market</b> uses observable prices; <b>mark to model</b> uses model inputs and assumptions. Market $90$ versus model $96$ need not be executable arbitrage: inspect liquidity, trading costs, model assumptions and risk. [p. 13]'''),
('Margin mechanics',r'''Initial margin opens a position; maintenance margin is a minimum balance. Futures mark-to-market losses can trigger a call to restore collateral. Writers can have large future obligations; a fully paid option buyer’s loss is limited to the premium. Margin is collateral, not an option premium. [pp. 14–15]<div class="example">Authored illustration: initial $5,000$, maintenance $3,500$. Loss $1,800$ leaves $3,200$; restoring initial margin needs $1,800$.</div>'''),
('Missing source attachment',r'''Page 16 refers to <code>Future_Margin_Example</code>, a spreadsheet not supplied. Its numerical rows cannot be checked here. The illustration above is authored, not a reconstruction of that workbook.''')])
lecture(3,'No-arbitrage bounds & parity',17,'Compare terminal cash flows, then compare their prices today.',[
('Notation and assumptions',r'''$S_0,S_T$ = stock now/at expiry; $K$ = strike; $T$ = years; $r$ = continuously compounded risk-free rate. $c,p$ are European call/put; $C,P$ American. Parity requires the same underlying, strike and expiry. Proofs assume frictionless trading, short selling and borrowing/lending at $r$. Simplified American bounds and no-early-call results assume $r\ge0$. [pp. 3–4, 9–10]'''),
('Comparative statics',r'''Holding other inputs fixed: $S\uparrow$ raises calls, lowers puts; $K\uparrow$ lowers calls, raises puts; volatility raises both vanilla values in the model; $r\uparrow$ raises calls, lowers puts; dividends lower calls, raise puts. Longer maturity cannot reduce American value, but European maturity effects are not unconditional. $C\ge c$, $P\ge p$. [pp. 3–8]'''),
('Bounds: no dividends',r'''$$\max(0,S_0-Ke^{-rT})\le c\le S_0,\quad \max(0,Ke^{-rT}-S_0)\le p\le Ke^{-rT}.$$ Call + bond paying $K$ dominates stock at expiry; put + stock dominates the bond. American: $C\le S_0$, $P\le K$ for $r\ge0$, and each is at least intrinsic value. [pp. 11–16]<div class="example">Call $S_0=51,K=50,T=.5,r=.12$: lower bound $3.9118$. Put $S_0=38,K=40,T=.25,r=.1$: lower bound $1.0124$.</div>'''),
('Put–call parity',r'''$$c+Ke^{-rT}=p+S_0.$$ Both portfolios pay $\max(S_T,K)$. If prices differ, buy the cheap portfolio and sell the expensive one; terminal obligations cancel. This equality is European, not arbitrary American parity. [p. 17]''')])
lecture(4,'Synthetic positions & early exercise',14,'The timing of cash flows matters.',[
('Synthetic positions',r'''$c=p+S_0-Ke^{-rT}$; $p=c+Ke^{-rT}-S_0$; $S_0=c-p+Ke^{-rT}$. Negative components mean short/sell or borrow. For arbitrage, compare complete portfolios at time zero and expiry. [pp. 3–5]'''),
('Early call exercise',r'''For a non-dividend stock and $r\ge0$, $C=c$. Early exercise loses remaining optionality and pays $K$ sooner; holding preserves downside protection and delays payment. For positive rates and remaining time, the discounted-strike lower bound exceeds intrinsic value when ITM. Selling can preserve time value when exiting. [pp. 6–7]'''),
('Early put exercise',r'''A deeply ITM put can benefit from receiving $K$ now. Higher rates and little benefit from waiting favor exercise. At each node compare exercise with discounted continuation; “ITM” alone is insufficient. [pp. 8–9]'''),
('American bounds',r'''No dividends, $r\ge0$: $$S_0-K\le C-P\le S_0-Ke^{-rT}.$$ Extra exercise rights prevent a blanket fixed-expiry equality. [pp. 10–11]'''),
('Known cash dividends',r'''$D$ = <b>present value</b> of known dividends. $$c\ge(S_0-D-Ke^{-rT})^+,\quad p\ge(D+Ke^{-rT}-S_0)^+,$$ $$c+D+Ke^{-rT}=p+S_0.$$ American: $S_0-D-K\le C-P\le S_0-Ke^{-rT}$. Call exercise may be optimal just before ex-dividend, but not automatically. Distinguish cash dividend from its present value. [pp. 12–14]''')])
lecture(5,'Option strategies',42,'Add the legs, then account for the net premium.',[
('Strategy workflow',r'''Long legs have $+$ signs, short legs $-$. Add terminal payoffs; split the $S_T$ axis at every strike; subtract net debit for profit. State max gain/loss and solve profit $=0$ for break-even. Use consistent cash-flow timing; ignore financing only when the question does. [pp. 2–11, 42]'''),
('Protection and income',r'''Principal protection from budget $A$: bond cost $Ae^{-rT}$ pays $A$ at expiry; remaining $A(1-e^{-rT})$ buys calls when nonnegative. Protection depends on the bond assumptions. Covered call = stock − call, payoff $\min(S_T,K)$: capped upside, downside remains. Protective put = stock + put, payoff $\max(S_T,K)$: floor costs premium. [pp. 12–16]'''),
('Bull and bear spreads',r'''$K_1<K_2$. Bull call: $+c(K_1)-c(K_2)$, payoff $\min((S_T-K_1)^+,K_2-K_1)$. Debit $A$: max loss $A$, max gain $K_2-K_1-A$, BE $K_1+A$. Bear put: $+p(K_2)-p(K_1)$, payoff $\min((K_2-S_T)^+,K_2-K_1)$; BE $K_2-A$. [pp. 17–23]<div class="example">Bull call strikes $50,70$, premiums $8,2$: debit $6$, max loss $6$, max gain $14$, BE $56$.</div>'''),
('Box and butterfly',r'''European box = bull call + bear put at identical strikes/expiry: payoff $K_2-K_1$, value $(K_2-K_1)e^{-rT}$. American early exercise complicates it. Equal-spacing butterfly: $+c(K_1)-2c(K_2)+c(K_3)$; peak payoff $K_2-K_1$ at $K_2$, zero outside wings; a low-movement view. [pp. 24–27]<div class="example">Strikes $90,100,110$, premiums $14.2,8.1,4.3$: debit $2.3$, peak profit $7.7$, BEs $92.3,107.7$. Payoff pieces: $0$, $S_T-90$, $110-S_T$, $0$. [pp. 39–41]</div>'''),
('Calendar and diagonal',r'''Calendar: short near-expiry and long later-expiry at the same strike. At the near expiry, the later leg still has time value: <b>do not value both legs at intrinsic value</b>. Diagonal changes both strike and expiry. [pp. 28–29]'''),
('Movement strategies',r'''Straddle = call + put at $K$: payoff $|S_T-K|$, debit $A$, BEs $K\pm A$. Strangle = put $K_1$ + call $K_2>K_1$: payoff $(K_1-S_T)^++(S_T-K_2)^+$; BEs $K_1-A,K_2+A$. Usually cheaper but needs a bigger move. Strip = call + 2 puts (downside emphasis); strap = 2 calls + put (upside emphasis). [pp. 30–38]''')])
lecture(6,'Binomial pricing I',18,'Replication determines price; risk-neutral expectation computes it.',[
('Hedge one step',r'''For a non-dividend stock, $S_u=S_0u$, $S_d=S_0d$, payoffs $f_u,f_d$. $$\Delta=\frac{f_u-f_d}{S_u-S_d},\quad H=\Delta S_u-f_u=\Delta S_d-f_d,\quad f_0=\Delta S_0-He^{-r\Delta t}.$$ The portfolio $\Delta S-f$ is riskless. Delta is shares per option unit; multiply by contract multiplier and number of options. [pp. 3–7]'''),
('Pricing probability',r'''$$p=\frac{e^{r\Delta t}-d}{u-d},\quad f_0=e^{-r\Delta t}[pf_u+(1-p)f_d].$$ Check $d<e^{r\Delta t}<u$, hence $0<p<1$. $E^Q[S_{t+\Delta t}\mid S_t]=S_te^{r\Delta t}$. $p$ is not a forecast. Physical expected return $\mu$ instead gives $p^*=(e^{\mu\Delta t}-d)/(u-d)$, if admissible. [pp. 7–10]'''),
('One-step example',r'''$S_0=20,S_u=22,S_d=18,K=21,\Delta t=.25,r=.04$: payoffs $1,0$, $\Delta=.25$, $H=4.5$. Thus $f_0=5-4.5e^{-.01}=.5448$. Also $p=.550251$ and $f_0=e^{-.01}p$. [pp. 4–6, 9]'''),
('Two-step tree',r'''Up-down = down-up for constant factors. Terminal payoff first, then work backward. $$f_0=e^{-2r\Delta t}[p^2f_{uu}+2p(1-p)f_{ud}+(1-p)^2f_{dd}].$$ The 2 counts paths to the middle price. Same call over two steps: prices $24.2,19.8,16.2$, payoffs $3.2,0,0$, upper value $1.7433$, lower $0$, root $.9497$. [pp. 11–14]'''),
('Put and class exercise',r'''$S_0=50,K=52,u=1.2,d=.8,r=.05,\Delta t=1,N=2$: terminal $72,48,32$, put payoffs $0,4,20$, $p=.628178$, European value $4.1923$. [pp. 15–16] Class exercise $S_0=50,S_u=53,S_d=48,K=49,T=2/12,r=.10$: payoffs $4,0$, $\Delta=.8$, $p=.568063$, call $2.2347$. [pp. 17–18]''')])
lecture(7,'Binomial pricing II',47,'Exercise, volatility calibration and different underlyings.',[
('American exercise at every node',r'''At maturity set payoff. Earlier, compute $V=e^{-r\Delta t}[pf_u+(1-p)f_d]$ and $$f_{i,j}=\max(V,\text{exercise value}).$$ Include the root. In L6’s put example, at $S=40$, continuation $9.4636$ versus exercise $12$: exercise. At $60$, continue at $1.4147$. Root American $5.0894$ versus European $4.1923$. [pp. 3–7]'''),
('Dynamic delta and source correction',r'''Recalculate $\Delta=(f_u-f_d)/(S_u-S_d)$ at every node. L6’s two-step call: root delta $.4358$, upper $.7273$, lower $0$. Put deltas are typically negative. <b>Correction:</b> L7 p. 13 labels the root $.9334$; the displayed parameters give $.9497$ by backward induction, agreeing with L6. [pp. 8–13]'''),
('CRR factors',r'''$$\Delta t=T/N,\quad u=e^{\sigma\sqrt{\Delta t}},\quad d=1/u,\quad p=(a-d)/(u-d).$$ CRR matches diffusion variance locally as $\Delta t\to0$; it does not exactly match every finite-step variance equation. Exact two-point relative variance is $p(1-p)(u-d)^2$. Check convergence as $N$ grows; it need not be monotonic. The introductory measure-change discussion changes drift to risk-neutral drift but retains volatility, not a full Girsanov proof. [pp. 14–25]'''),
('Growth factor by underlying',r'''Always discount at domestic $r$. Growth $a$: no-dividend stock $e^{r\Delta t}$; continuous-yield stock/index $e^{(r-q)\Delta t}$; FX quoted domestic per foreign unit $e^{(r-r_f)\Delta t}$; futures $1$. In each case $p=(a-d)/(u-d)$. Foreign interest acts like a yield. Non-income forward price $F_0=S_0e^{rT}$. [pp. 26, 33–41]'''),
('Cash dividend caution',r'''At ex-dividend, $S_{\rm after}=S_{\rm before}-D_{\rm cash}$. Compare American exercise immediately before the drop. Replacing discrete cash dividends by continuous $q$ is not an exact cash-dividend tree. The calculator here supports yields, not discrete cash dividends. [pp. 27–32]'''),
('Backward induction pseudocode',r'''<pre>dt=T/N; set u,d,growth a,p,discount
check d &lt; a &lt; u
for j=0..N: v[j]=payoff(S0*u^j*d^(N-j))
for i=N-1 down to 0:
  for j=0..i:  # ascending: preserve old children
    c=discount*((1-p)*v[j]+p*v[j+1])
    v[j]=c
    if American: v[j]=max(c,payoff(S0*u^j*d^(i-j)))
return v[0]</pre>Time $O(N^2)$; rolling memory $O(N)$; full tree memory $O(N^2)$. These cost statements are implementation deductions. [pp. 23–25]'''),
('Practice coverage',r'''Lecture exercises 1–6 on pp. 42–47 are retained below; exercise 4 repeats 1. The supplied material introduces, but does not derive, the continuous-time option-pricing limit. No unprovided Black–Scholes or Itô-lemma chapter is added.''')])
lecture(8,'Wiener processes',34,'Variance grows with time; SD grows with its square root.',[
('Processes and Markov property',r'''Time and state can each be discrete or continuous. Markov means the conditional future given the present does not need the earlier path. It does <b>not</b> mean successive levels are independent. [pp. 2–7]'''),
('Standard Brownian motion',r'''$W_0=0$, continuous paths, independent increments over non-overlapping intervals, and $$W_t-W_s\sim N(0,t-s)\quad(s<t).$$ $N(m,v)$ uses <b>variance</b>, not SD, as its second parameter. $E[W_T]=0$, variance $T$, SD $\sqrt T$. A process started at $w_0$ instead has mean $w_0$. [pp. 8–18]'''),
('Increment simulation',r'''$$\Delta W=\sqrt{\Delta t}\,\varepsilon,\quad\varepsilon\sim N(0,1).$$ Fresh independent shocks for disjoint steps. At $\Delta t=.01$, use $.1\varepsilon$, not $.01\varepsilon$. Over $N$ steps, variances add to $N\Delta t=T$; SDs do not add. Brownian paths are continuous but not ordinarily differentiable; $dW$ is not an ordinary derivative. [pp. 19–27]'''),
('Constant coefficients: exact',r'''$$dX=a\,dt+b\,dW,\quad X_T=X_0+aT+bW_T,$$ $$X_T\sim N(X_0+aT,b^2T),\quad\Delta X\sim N(a\Delta t,b^2\Delta t).$$ Drift $a$: value/time; diffusion $b$: value/$\sqrt{\rm time}$; variance rate $b^2$; SD $|b|\sqrt T$. Exact finite-horizon results for constant coefficients. [pp. 28–31]'''),
('Scaling example',r'''$X_0=50,a=20,b=30$, thousands and years. At one year: mean $70$, variance $900$, SD $30$; six months: mean $60$, variance $450$, SD $21.2132$. A Wiener process started at $25$ has $X_1\sim N(25,1)$ and $X_5\sim N(25,5)$. [pp. 22–23, 32–34]''')])
lecture(9,'Itô processes, stock models & correlation',39,'Distinguish exact distributions from local approximations.',[
('Expectation and covariance',r'''Expectation is linear without independence. $$\operatorname{Var}\left(\sum_iX_i\right)=\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$ Independence implies zero covariance (when moments exist), not conversely in general. Pages 2–24 review L8; p. 6 explicitly gives the variance rule.'''),
('Local conditional moments',r'''$$dX_t=a(X_t,t)dt+b(X_t,t)dW_t.$$ Freeze current coefficients for a small step: $$E_t[\Delta X]\approx a(X_t,t)\Delta t,$$ $$\operatorname{Var}_t(\Delta X)\approx b(X_t,t)^2\Delta t.$$ $E_t$ conditions on information $\mathcal F_t$. Unlike constant coefficients, frozen finite-step moments are approximate. State/time coefficients define a Markov diffusion under usual well-posedness assumptions. [pp. 25–28]'''),
('Mean reversion',r'''$dX=\kappa(\theta-X)dt+\eta dW$, $\kappa>0$: positive drift below $\theta$, negative above. Noise remains, so attraction is not a guaranteed path. Variance rate $\eta^2$. [pp. 25–28; exercise 13]'''),
('Geometric Brownian motion',r'''$$dS=\mu Sdt+\sigma SdW,$$ $$dS/S=\mu dt+\sigma dW.$$ Dollar drift $\mu S$, diffusion $\sigma S$, variance rate $\sigma^2S^2$. Locally proportional mean $\approx\mu\Delta t$, SD $\approx\sigma\sqrt{\Delta t}$; multiply by current $S$ for dollar changes. If $\sigma=0$, exact $S_t=S_0e^{\mu t}$. Do not claim local normal returns are the exact long-horizon GBM distribution. [pp. 29–32, 36]'''),
('Euler simulation',r'''$$S_{i+1}=S_i(1+\mu\Delta t+\sigma\sqrt{\Delta t}\varepsilon_i).$$ Use the <b>updated</b> state and fresh shocks. Independent shocks do not imply independent prices. Euler can produce negative prices for sufficiently negative shocks: an approximation artifact. Smaller steps reduce discretization error but cost more work. General update: $X_{i+1}=X_i+a(X_i,t_i)\Delta t+b(X_i,t_i)\sqrt{\Delta t}\varepsilon_i$. [pp. 33–36]'''),
('Correlated processes',r'''$\operatorname{Cov}(\Delta W_1,\Delta W_2)=\rho\Delta t$ implies local $\operatorname{Cov}_t(\Delta X_1,\Delta X_2)\approx\rho b_1b_2\Delta t$. For stocks: $\rho\sigma_1\sigma_2S_1S_2\Delta t$. Constant coefficients make the relation exact. Local/instantaneous increment correlation is $\rho$ for positive diffusion coefficients; this is exact over finite intervals for constant coefficients. State-dependent finite-horizon changes need not have correlation $\rho$. [p. 37]'''),
('Correlated normals',r'''Independent $U,V\sim N(0,1)$: $$\varepsilon_1=U,\quad\varepsilon_2=\rho U+\sqrt{1-\rho^2}V.$$ Means $0$, variances $1$, covariance $\rho$. Reuse $U$ within a pair, generate a fresh independent pair each step. At $\rho=0$ jointly normal shocks are independent; $\rho=\pm1$ gives degenerate perfect dependence. [pp. 38–39]''')])
notation=[
(r'S_0,S_t,S_T','Underlying price now, at time t, and at expiry; FX quote is domestic per foreign unit.'),
(r'K','Strike / exercise price.'),(r'c,p;\ C,P','European call/put; American call/put prices.'),
(r'f_{i,j}','Option value at step i after j up moves.'),
(r'T,t,\Delta t,N','Expiry in years; current time; step T/N; number of tree/simulation steps.'),
(r'r,r_f,q','Continuous domestic rate, foreign rate, and dividend yield.'),
(r'D,D_{\rm cash}','Present value of dividends; actual cash amount at the payment date.'),
(r'u,d,a','Tree up/down multipliers and risk-neutral one-step growth factor.'),
(r'p,p^*,Q','Risk-neutral up probability, physical up probability, pricing measure. p also denotes a put price: use context.'),
(r'\Delta','Hedge ratio, shares per option unit. Δt is a time interval.'),
(r'\mu,\sigma','Annual proportional drift and annualized volatility.'),
(r'W_t,\Delta W,\varepsilon','Wiener level, increment and standard normal shock.'),
(r'a(X,t),b(X,t)','Itô drift and diffusion; variance rate b². This a is not tree growth.'),
(r'\mathcal F_t,E_t,\operatorname{Var}_t','Information at t; expectation/variance conditional on it.'),
(r'\rho,U,V','Correlation and independent standard normal variables.'),
(r'\kappa,\theta,\eta','Mean-reversion speed, target and diffusion coefficient.'),
(r'N(m,v),\Phi(z)','Normal with mean m and variance v; standard normal CDF.'),
(r'x^+,\operatorname{Cov},\operatorname{Corr}','max(x,0); covariance; covariance divided by both SDs.')]
dependence=[
('a',r'W_2\quad\text{and}\quad W_4-W_2','Independent','Disjoint intervals [0,2] and [2,4]; covariance 0.'),
('b',r'W_2\quad\text{and}\quad W_4','Dependent',r'Covariance $\min(2,4)=2$. The later level contains the earlier increment.'),
('c',r'W_3-W_1\quad\text{and}\quad W_5-W_3','Independent','Disjoint increments; covariance 0. A shared endpoint adds no overlap length.'),
('d',r'W_3-W_1\quad\text{and}\quad W_4-W_2','Dependent','Overlap [2,3] has length 1: covariance 1.'),
('e',r'W_5-W_2\quad\text{and}\quad W_2-W_1','Independent','Disjoint increments; covariance 0.'),
('f',r'W_4+W_2\quad\text{and}\quad W_4-W_2','Dependent',r'Covariance $\operatorname{Var}(W_4)-\operatorname{Var}(W_2)=4-2=2$.'),
('g',r'W_3-2W_2+W_1\quad\text{and}\quad W_3-W_1','Independent',r'Let $X=W_2-W_1$, $Y=W_3-W_2$, independent $N(0,1)$. Pair $Y-X,Y+X$ has covariance $1-1=0$ and is jointly Gaussian, hence independent.'),
('h',r'W_2^2\quad\text{and}\quad W_4-W_2','Independent',r'$W_2$ is independent of the later increment; squaring preserves independence. The square is not Gaussian: do not justify this solely with zero covariance.'),
('i',r'W_4-2W_2\quad\text{and}\quad W_2','Dependent',r'Covariance $2-2(2)=-2$.')]
def tree(S,K,r,T,N,u=None,d=None,sigma=.3,q=0,put=False,american=False):
    dt=T/N;u=u or math.exp(sigma*math.sqrt(dt));d=d or 1/u;p=(math.exp((r-q)*dt)-d)/(u-d);disc=math.exp(-r*dt)
    stocks=lambda i:[S*u**j*d**(i-j) for j in range(i+1)]
    payoff=lambda s:max(K-s if put else s-K,0)
    vals=list(map(payoff,stocks(N)));levels=[dict(i=N,stocks=stocks(N),values=vals[:])]
    for i in range(N-1,-1,-1):
        c=[disc*((1-p)*vals[j]+p*vals[j+1]) for j in range(i+1)];s=stocks(i);e=list(map(payoff,s));vals=[max(x,y) if american else x for x,y in zip(c,e)]
        levels.append(dict(i=i,stocks=s,values=vals[:],continuation=c,exercise=e))
    return dict(price=vals[0],p=p,u=u,d=d,levels=levels[::-1])
exercises=[]
def ex(n,title,question,answers):exercises.append(dict(number=n,title=title,question=question,answers=[dict(part=chr(97+i),body=a) for i,a in enumerate(answers)]))
fmt=lambda x:f'{x:.4f}'
