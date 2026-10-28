# FM9578A — Mathematics of Financial Options

Course-specific notes based on supplied Lectures 1–9. Solutions are independently worked, not official. N(m,v) uses variance. Local approximations are marked. Physical PDF page references.


## Lecture 1 · Contracts, payoffs & market language

Separate the contract, its payoff, and the investor’s profit.


### Derivatives and participants

A derivative depends on an underlying stock, index, rate, currency, commodity or other variable. **Hedgers** reduce an existing exposure; **speculators** take a view; **arbitrageurs** exploit inconsistent prices without net risk. Exchange contracts are standardized and cleared; OTC contracts can be customized but introduce counterparty exposure. [pp. 3–10]


### Forward, futures, option

Long forward payoff $S_T-K$; short $K-S_T$. A forward commits both parties. Futures are standardized and marked to market. An option buyer pays a premium for a **right**; the writer has the corresponding obligation. European exercise is only at expiry; American exercise is allowed earlier too. [pp. 6–12]


### Four positions: payoff ≠ profit

Let $x^+=\max(x,0)$. Long call $(S_T-K)^+$; short call $-(S_T-K)^+$; long put $(K-S_T)^+$; short put $-(K-S_T)^+$. Ignoring financing, long-call profit is $(S_T-K)^+-c_0$, long-put profit $(K-S_T)^+-p_0$. Break-evens: $K+c_0$, $K-p_0$. If cash flows are measured at expiry with financing, subtract the future value of the premium instead. [pp. 13–17]Call $K=50$, premium $4$: at $S_T=62$, payoff $12$, profit $8$; at $48$, payoff $0$, profit $-4$. Multiply by 100 for the lecture’s 100-share contract convention.


### Moneyness and time value

Call ITM: $S>K$; put ITM: $S<K$; ATM: $S=K$. Moneyness ignores premium, so ITM does not ensure profit. Intrinsic values: $(S-K)^+$ and $(K-S)^+$. Time value = option price − intrinsic value. American value is at least exercise value. $S=56,K=50,c=9$ gives intrinsic $6$, time value $3$. [pp. 21–22]


### Contract and quote checklist

Check underlying, call/put, strike, expiry, style, settlement and multiplier. A **class** groups calls or puts on an underlying; a **series** fixes strike and expiry. Index options may be cash settled; exercising a futures option creates a futures position. Corporate actions can alter terms. Monthly cycles, strike intervals and LEAPS in the slides are course conventions, not universal specifications. Close a long by selling the same series; close a short by buying it back. Bid $4$, ask $4.50$: spread $.50$, midpoint $4.25$, 100-share immediate round trip costs $50$ before fees. [pp. 18–24]


### Lecture contract conventions

The slides illustrate January-cycle expiries (Jan/Apr/Jul/Oct), February (Feb/May/Aug/Nov), and March (Mar/Jun/Sep/Dec). They describe third-Friday monthly expiries, additional weekly Fridays, LEAPS maturities up to 39 months and strike spacing of $2.50$, $5$ or $10$. These are the lecture’s examples: verify the specific contract rather than assuming every market follows them. Also check position/exercise limits and corporate-action adjustments. [pp. 19–20]


## Lecture 2 · Trading, valuation & margin

A quoted price, model value, premium and collateral are different things.


### Consolidated review

Pages 1–12 repeat Lecture 1’s four positions, contract terms, moneyness, intrinsic/time value and bid–ask conventions. Those explanations are consolidated in L1 rather than silently omitted.


### Market versus model

**Mark to market** uses observable prices; **mark to model** uses model inputs and assumptions. Market $90$ versus model $96$ need not be executable arbitrage: inspect liquidity, trading costs, model assumptions and risk. [p. 13]


### Margin mechanics

Initial margin opens a position; maintenance margin is a minimum balance. Futures mark-to-market losses can trigger a call to restore collateral. Writers can have large future obligations; a fully paid option buyer’s loss is limited to the premium. Margin is collateral, not an option premium. [pp. 14–15]Authored illustration: initial $5,000$, maintenance $3,500$. Loss $1,800$ leaves $3,200$; restoring initial margin needs $1,800$.


### Missing source attachment

Page 16 refers to Future_Margin_Example, a spreadsheet not supplied. Its numerical rows cannot be checked here. The illustration above is authored, not a reconstruction of that workbook.


## Lecture 3 · No-arbitrage bounds & parity

Compare terminal cash flows, then compare their prices today.


### Notation and assumptions

$S_0,S_T$ = stock now/at expiry; $K$ = strike; $T$ = years; $r$ = continuously compounded risk-free rate. $c,p$ are European call/put; $C,P$ American. Parity requires the same underlying, strike and expiry. Proofs assume frictionless trading, short selling and borrowing/lending at $r$. Simplified American bounds and no-early-call results assume $r\ge0$. [pp. 3–4, 9–10]


### Comparative statics

Holding other inputs fixed: $S\uparrow$ raises calls, lowers puts; $K\uparrow$ lowers calls, raises puts; volatility raises both vanilla values in the model; $r\uparrow$ raises calls, lowers puts; dividends lower calls, raise puts. Longer maturity cannot reduce American value, but European maturity effects are not unconditional. $C\ge c$, $P\ge p$. [pp. 3–8]


### Bounds: no dividends

$$\max(0,S_0-Ke^{-rT})\le c\le S_0,\quad \max(0,Ke^{-rT}-S_0)\le p\le Ke^{-rT}.$$ Call + bond paying $K$ dominates stock at expiry; put + stock dominates the bond. American: $C\le S_0$, $P\le K$ for $r\ge0$, and each is at least intrinsic value. [pp. 11–16]Call $S_0=51,K=50,T=.5,r=.12$: lower bound $3.9118$. Put $S_0=38,K=40,T=.25,r=.1$: lower bound $1.0124$.


### Put–call parity

$$c+Ke^{-rT}=p+S_0.$$ Both portfolios pay $\max(S_T,K)$. If prices differ, buy the cheap portfolio and sell the expensive one; terminal obligations cancel. This equality is European, not arbitrary American parity. [p. 17]


### Assumptions behind an arbitrage argument

The slides also assume trading profits are taxed consistently and arbitrage opportunities are rapidly exploited. Compare cash flows on the same dates under the same trading constraints; a difference between a model estimate and a quote alone is not a complete arbitrage proof. [L3 p. 10]


## Lecture 4 · Synthetic positions & early exercise

The timing of cash flows matters.


### Synthetic positions

$c=p+S_0-Ke^{-rT}$; $p=c+Ke^{-rT}-S_0$; $S_0=c-p+Ke^{-rT}$. Negative components mean short/sell or borrow. For arbitrage, compare complete portfolios at time zero and expiry. [pp. 3–5]


### Early call exercise

For a non-dividend stock and $r\ge0$, $C=c$. Early exercise loses remaining optionality and pays $K$ sooner; holding preserves downside protection and delays payment. For positive rates and remaining time, the discounted-strike lower bound exceeds intrinsic value when ITM. Selling can preserve time value when exiting. [pp. 6–7]


### Early put exercise

A deeply ITM put can benefit from receiving $K$ now. Higher rates and little benefit from waiting favor exercise. At each node compare exercise with discounted continuation; “ITM” alone is insufficient. [pp. 8–9]


### American bounds

No dividends, $r\ge0$: $$S_0-K\le C-P\le S_0-Ke^{-rT}.$$ Extra exercise rights prevent a blanket fixed-expiry equality. [pp. 10–11]


### Known cash dividends

$D$ = **present value** of known dividends. $$c\ge(S_0-D-Ke^{-rT})^+,\quad p\ge(D+Ke^{-rT}-S_0)^+,$$ $$c+D+Ke^{-rT}=p+S_0.$$ American: $S_0-D-K\le C-P\le S_0-Ke^{-rT}$. Call exercise may be optimal just before ex-dividend, but not automatically. Distinguish cash dividend from its present value. [pp. 12–14]


## Lecture 5 · Option strategies

Add the legs, then account for the net premium.


### Strategy workflow

Long legs have $+$ signs, short legs $-$. Add terminal payoffs; split the $S_T$ axis at every strike; subtract net debit for profit. State max gain/loss and solve profit $=0$ for break-even. Use consistent cash-flow timing; ignore financing only when the question does. [pp. 2–11, 42]


### Protection and income

Principal protection from budget $A$: bond cost $Ae^{-rT}$ pays $A$ at expiry; remaining $A(1-e^{-rT})$ buys calls when nonnegative. Protection depends on the bond assumptions. Covered call = stock − call, payoff $\min(S_T,K)$: capped upside, downside remains. Protective put = stock + put, payoff $\max(S_T,K)$: floor costs premium. [pp. 12–16]


### Bull and bear spreads

$K_1<K_2$. Bull call: $+c(K_1)-c(K_2)$, payoff $\min((S_T-K_1)^+,K_2-K_1)$. Debit $A$: max loss $A$, max gain $K_2-K_1-A$, BE $K_1+A$. Bear put: $+p(K_2)-p(K_1)$, payoff $\min((K_2-S_T)^+,K_2-K_1)$; BE $K_2-A$. [pp. 17–23]Bull call strikes $50,70$, premiums $8,2$: debit $6$, max loss $6$, max gain $14$, BE $56$.


### Box and butterfly

European box = bull call + bear put at identical strikes/expiry: payoff $K_2-K_1$, value $(K_2-K_1)e^{-rT}$. American early exercise complicates it. Equal-spacing butterfly: $+c(K_1)-2c(K_2)+c(K_3)$; peak payoff $K_2-K_1$ at $K_2$, zero outside wings; a low-movement view. [pp. 24–27]Strikes $90,100,110$, premiums $14.2,8.1,4.3$: debit $2.3$, peak profit $7.7$, BEs $92.3,107.7$. Payoff pieces: $0$, $S_T-90$, $110-S_T$, $0$. [pp. 39–41]


### Calendar and diagonal

Calendar: short near-expiry and long later-expiry at the same strike. At the near expiry, the later leg still has time value: **do not value both legs at intrinsic value**. Diagonal changes both strike and expiry. [pp. 28–29]


### Movement strategies

Straddle = call + put at $K$: payoff $|S_T-K|$, debit $A$, BEs $K\pm A$. Strangle = put $K_1$ + call $K_2>K_1$: payoff $(K_1-S_T)^++(S_T-K_2)^+$; BEs $K_1-A,K_2+A$. Usually cheaper but needs a bigger move. Strip = call + 2 puts (downside emphasis); strap = 2 calls + put (upside emphasis). [pp. 30–38]


### Explicit strategy formulas

For $K_1<K_2$, the bear-put payoff is $K_2-K_1$ if $S_T\le K_1$, $K_2-S_T$ between strikes, and $0$ if $S_T\ge K_2$. The bull-call payoff is $0$, then $S_T-K_1$, then $K_2-K_1$. An equally spaced butterfly pays $(S_T-K_1)^+-2(S_T-K_2)^++(S_T-K_3)^+$. Strip payoff: $(S_T-K)^++2(K-S_T)^+$. Strap payoff: $2(S_T-K)^++(K-S_T)^+$. Subtract the total net debit for unfinanced profit. [L5 pp. 19–27, 33–34]


## Lecture 6 · Binomial pricing I

Replication determines price; risk-neutral expectation computes it.


### Hedge one step

For a non-dividend stock, $S_u=S_0u$, $S_d=S_0d$, payoffs $f_u,f_d$. $$\Delta=\frac{f_u-f_d}{S_u-S_d},\quad H=\Delta S_u-f_u=\Delta S_d-f_d,\quad f_0=\Delta S_0-He^{-r\Delta t}.$$ The portfolio $\Delta S-f$ is riskless. Delta is shares per option unit; multiply by contract multiplier and number of options. [pp. 3–7]


### Pricing probability

$$p=\frac{e^{r\Delta t}-d}{u-d},\quad f_0=e^{-r\Delta t}[pf_u+(1-p)f_d].$$ Check $d<e^{r\Delta t}<u$, hence $0<p<1$. $E^Q[S_{t+\Delta t}\mid S_t]=S_te^{r\Delta t}$. $p$ is not a forecast. Physical expected return $\mu$ instead gives $p^*=(e^{\mu\Delta t}-d)/(u-d)$, if admissible. [pp. 7–10]


### One-step example

$S_0=20,S_u=22,S_d=18,K=21,\Delta t=.25,r=.04$: payoffs $1,0$, $\Delta=.25$, $H=4.5$. Thus $f_0=5-4.5e^{-.01}=.5448$. Also $p=.550251$ and $f_0=e^{-.01}p$. [pp. 4–6, 9]


### Two-step tree

Up-down = down-up for constant factors. Terminal payoff first, then work backward. $$f_0=e^{-2r\Delta t}[p^2f_{uu}+2p(1-p)f_{ud}+(1-p)^2f_{dd}].$$ The 2 counts paths to the middle price. Same call over two steps: prices $24.2,19.8,16.2$, payoffs $3.2,0,0$, upper value $1.7433$, lower $0$, root $.9497$. [pp. 11–14]


### Put and class exercise

$S_0=50,K=52,u=1.2,d=.8,r=.05,\Delta t=1,N=2$: terminal $72,48,32$, put payoffs $0,4,20$, $p=.628178$, European value $4.1923$. [pp. 15–16] Class exercise $S_0=50,S_u=53,S_d=48,K=49,T=2/12,r=.10$: payoffs $4,0$, $\Delta=.8$, $p=.568063$, call $2.2347$. [pp. 17–18]


## Lecture 7 · Binomial pricing II

Exercise, volatility calibration and different underlyings.


### American exercise at every node

At maturity set payoff. Earlier, compute $V=e^{-r\Delta t}[pf_u+(1-p)f_d]$ and $$f_{i,j}=\max(V,\text{exercise value}).$$ Include the root. In L6’s put example, at $S=40$, continuation $9.4636$ versus exercise $12$: exercise. At $60$, continue at $1.4147$. Root American $5.0894$ versus European $4.1923$. [pp. 3–7]


### Dynamic delta and source correction

Recalculate $\Delta=(f_u-f_d)/(S_u-S_d)$ at every node. L6’s two-step call: root delta $.4358$, upper $.7273$, lower $0$. Put deltas are typically negative. **Correction:** L7 p. 13 labels the root $.9334$; the displayed parameters give $.9497$ by backward induction, agreeing with L6. [pp. 8–13]


### CRR factors

$$\Delta t=T/N,\quad u=e^{\sigma\sqrt{\Delta t}},\quad d=1/u,\quad p=(a-d)/(u-d).$$ CRR matches diffusion variance locally as $\Delta t\to0$; it does not exactly match every finite-step variance equation. Exact two-point relative variance is $p(1-p)(u-d)^2$. Check convergence as $N$ grows; it need not be monotonic. The introductory measure-change discussion changes drift to risk-neutral drift but retains volatility, not a full Girsanov proof. [pp. 14–25]


### Growth factor by underlying

Always discount at domestic $r$. Growth $a$: no-dividend stock $e^{r\Delta t}$; continuous-yield stock/index $e^{(r-q)\Delta t}$; FX quoted domestic per foreign unit $e^{(r-r_f)\Delta t}$; futures $1$. In each case $p=(a-d)/(u-d)$. Foreign interest acts like a yield. Non-income forward price $F_0=S_0e^{rT}$. [pp. 26, 33–41]


### Cash dividend caution

At ex-dividend, $S_{\rm after}=S_{\rm before}-D_{\rm cash}$. Compare American exercise immediately before the drop. Replacing discrete cash dividends by continuous $q$ is not an exact cash-dividend tree. The calculator here supports yields, not discrete cash dividends. [pp. 27–32]


### Backward induction pseudocode


```
dt=T/N; set u,d,growth a,p,discount
check d < a < u
for j=0..N: v[j]=payoff(S0*u^j*d^(N-j))
for i=N-1 down to 0:
  for j=0..i:  # ascending: preserve old children
    c=discount*((1-p)*v[j]+p*v[j+1])
    v[j]=c
    if American: v[j]=max(c,payoff(S0*u^j*d^(i-j)))
return v[0]
```
Time $O(N^2)$; rolling memory $O(N)$; full tree memory $O(N^2)$. These cost statements are implementation deductions. [pp. 23–25]


### Lecture numerical examples

**American put, p. 22:** S=50, K=52, r=0.05, T=2, N=2, sigma=0.3, put=True, american=True. Value $7.4284$, probability $0.5097$.**No-dividend call, p. 27:** S=50, K=50, r=0.05, T=0.5, N=2, sigma=0.3, american=True. Value $4.3397$, probability $0.5043$.**2% yield call, pp. 31–32:** S=50, K=50, r=0.05, T=0.5, N=2, sigma=0.3, q=0.02, american=True. Value $4.0558$, probability $0.4876$.**Index call, p. 33:** S=810, K=800, r=0.05, T=0.5, N=2, sigma=0.2, q=0.02. Value $53.3947$, probability $0.5126$.**FX American call, pp. 35–37:** S=0.61, K=0.6, r=0.05, T=0.25, N=3, sigma=0.12, q=0.07, american=True. Value $0.0189$, probability $0.4673$.At the upper node of the 2% yield call, continuation is about $8.42$, above exercise $8.09$, so do not exercise. The $4$ cash dividend immediately after $t=.25$ in pp. 28–29 is a separate model: compare exercise before the cash drop, not the continuous-yield example.


### Practice coverage

Lecture exercises 1–6 on pp. 42–47 are retained below; exercise 4 repeats 1. The supplied material introduces, but does not derive, the continuous-time option-pricing limit. No unprovided Black–Scholes or Itô-lemma chapter is added.


### Volatility matching: expanded identity

Let $R=\Delta S/S$, taking values $u-1$ and $d-1$. Its exact two-point variance is $$\operatorname{Var}(R)=p(u-1)^2+(1-p)(d-1)^2-[p(u-1)+(1-p)(d-1)]^2.$$ With $a=pu+(1-p)d$, this equals $p(1-p)(u-d)^2=a(u+d)-ud-a^2$. The lecture uses the small-step target $\sigma^2\Delta t$. CRR approaches this target as the step shrinks; its factors do not solve that finite-step equation exactly in general. [L7 pp. 14–16]


### Physical versus risk-neutral stock dynamics

For a non-dividend stock, the lecture writes $$\frac{dS}{S}=\mu\,dt+\sigma\,dW_t\quad\text{under the physical measure},$$ $$\frac{dS}{S}=r\,dt+\sigma\,dW_t^Q\quad\text{under }Q.$$ $W_t^Q$ is Brownian motion under the pricing measure. The drift changes, volatility does not; in the tree the probabilities change while $u,d$ stay the same. The same symbol $W$ without a measure label should not obscure which probability model is being used. [L7 pp. 17–19]


## Lecture 8 · Wiener processes

Variance grows with time; SD grows with its square root.


### Processes and Markov property

Time and state can each be discrete or continuous. Markov means the conditional future given the present does not need the earlier path. It does **not** mean successive levels are independent. [pp. 2–7]


### Standard Brownian motion

$W_0=0$, continuous paths, independent increments over non-overlapping intervals, and $$W_t-W_s\sim N(0,t-s)\quad(s<t).$$ $N(m,v)$ uses **variance**, not SD, as its second parameter. $E[W_T]=0$, variance $T$, SD $\sqrt T$. A process started at $w_0$ instead has mean $w_0$. [pp. 8–18]


### Increment simulation

$$\Delta W=\sqrt{\Delta t}\,\varepsilon,\quad\varepsilon\sim N(0,1).$$ Fresh independent shocks for disjoint steps. At $\Delta t=.01$, use $.1\varepsilon$, not $.01\varepsilon$. Over $N$ steps, variances add to $N\Delta t=T$; SDs do not add. Brownian paths are continuous but not ordinarily differentiable; $dW$ is not an ordinary derivative. [pp. 19–27]


### Constant coefficients: exact

$$dX=a\,dt+b\,dW,\quad X_T=X_0+aT+bW_T,$$ $$X_T\sim N(X_0+aT,b^2T),\quad\Delta X\sim N(a\Delta t,b^2\Delta t).$$ Drift $a$: value/time; diffusion $b$: value/$\sqrt{\rm time}$; variance rate $b^2$; SD $|b|\sqrt T$. Exact finite-horizon results for constant coefficients. [pp. 28–31]


### Scaling example

$X_0=50,a=20,b=30$, thousands and years. At one year: mean $70$, variance $900$, SD $30$; six months: mean $60$, variance $450$, SD $21.2132$. A Wiener process started at $25$ has $X_1\sim N(25,1)$ and $X_5\sim N(25,5)$. [pp. 22–23, 32–34]


### The slides’ z notation and conditional-law formula

The slides also use $z(t)$ or $z_t$ for a stochastic process; in the standard Wiener examples, $dz$ plays the same role as $dW$. Always identify whether $z$ is a level or $\Delta z=z(t+\Delta t)-z(t)$ is an increment. The Markov statement is $$\Pr(X_{t+h}\in B\mid\mathcal F_t)=\Pr(X_{t+h}\in B\mid X_t),$$ where $B$ is any set of possible future values. For $N$ independent standard normal shocks and $T=N\Delta t$, $$W_T-W_0=\sum_{i=1}^N\sqrt{\Delta t}\,\varepsilon_i\sim N(0,T).$$ A sum of independent normals is normal; add their variances, not their standard deviations. [L8 pp. 6–14, 20–21]


### Brownian covariance and correlation: supplement

The supplement calls standard Brownian motion $Z(t)$; here $W_t=Z(t)$ denotes the same process. For $s\le t$, write $W_t=W_s+(W_t-W_s)$. The later increment is independent of $W_s$, giving $\operatorname{Cov}(W_s,W_t)=\operatorname{Var}(W_s)=s$. Thus $$\operatorname{Cov}(W_s,W_t)=\min(s,t),\qquad \operatorname{Corr}(W_s,W_t)=\frac{\min(s,t)}{\sqrt{st}}=\sqrt{\frac{\min(s,t)}{\max(s,t)}}\quad(s,t>0).$$ For linear combinations, $$\operatorname{Cov}\left(\sum_i a_iW_{t_i},\sum_j b_jW_{s_j}\right)=\sum_{i,j}a_ib_j\min(t_i,s_j).$$ Use bilinearity to expand first. Joint Gaussianity then permits the zero-covariance independence test; nonlinear functions need a separate justification. [Brownian supplement pp. 1–3]


## Lecture 9 · Itô processes, stock models & correlation

Distinguish exact distributions from local approximations.


### Expectation and covariance

Expectation is linear without independence. $$\operatorname{Var}\left(\sum_iX_i\right)=\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$ Independence implies zero covariance (when moments exist), not conversely in general. Pages 2–24 review L8; p. 6 explicitly gives the variance rule.


### Local conditional moments

$$dX_t=a(X_t,t)dt+b(X_t,t)dW_t.$$ Freeze current coefficients for a small step: $$E_t[\Delta X]\approx a(X_t,t)\Delta t,\quad\operatorname{Var}_t(\Delta X)\approx b(X_t,t)^2\Delta t.$$ $E_t$ conditions on information $\mathcal F_t$. Unlike constant coefficients, frozen finite-step moments are approximate. State/time coefficients define a Markov diffusion under usual well-posedness assumptions. [pp. 25–28]


### Mean reversion

$dX=\kappa(\theta-X)dt+\eta dW$, $\kappa>0$: positive drift below $\theta$, negative above. Noise remains, so attraction is not a guaranteed path. Variance rate $\eta^2$. [pp. 25–28; exercise 13]


### Geometric Brownian motion

$$dS=\mu Sdt+\sigma SdW,\quad dS/S=\mu dt+\sigma dW.$$ Dollar drift $\mu S$, diffusion $\sigma S$, variance rate $\sigma^2S^2$. Locally proportional mean $\approx\mu\Delta t$, SD $\approx\sigma\sqrt{\Delta t}$; multiply by current $S$ for dollar changes. If $\sigma=0$, exact $S_t=S_0e^{\mu t}$. Do not claim local normal returns are the exact long-horizon GBM distribution. [pp. 29–32, 36]


### Euler simulation

$$S_{i+1}=S_i(1+\mu\Delta t+\sigma\sqrt{\Delta t}\varepsilon_i).$$ Use the **updated** state and fresh shocks. Independent shocks do not imply independent prices. Euler can produce negative prices for sufficiently negative shocks: an approximation artifact. Smaller steps reduce discretization error but cost more work. General update: $X_{i+1}=X_i+a(X_i,t_i)\Delta t+b(X_i,t_i)\sqrt{\Delta t}\varepsilon_i$. [pp. 33–36]


### Correlated processes

$\operatorname{Cov}(\Delta W_1,\Delta W_2)=\rho\Delta t$ implies local $\operatorname{Cov}_t(\Delta X_1,\Delta X_2)\approx\rho b_1b_2\Delta t$. For stocks: $\rho\sigma_1\sigma_2S_1S_2\Delta t$. Constant coefficients make the relation exact. Local/instantaneous increment correlation is $\rho$ for positive diffusion coefficients; this is exact over finite intervals for constant coefficients. State-dependent finite-horizon changes need not have correlation $\rho$. [p. 37]


### Correlated normals

Independent $U,V\sim N(0,1)$: $$\varepsilon_1=U,\quad\varepsilon_2=\rho U+\sqrt{1-\rho^2}V.$$ Means $0$, variances $1$, covariance $\rho$. Reuse $U$ within a pair, generate a fresh independent pair each step. At $\rho=0$ jointly normal shocks are independent; $\rho=\pm1$ gives degenerate perfect dependence. [pp. 38–39]


### Lecture monthly stock example

For $S=100$, $\mu=.08$, $\sigma=.20$, one month gives local proportional mean $.08/12=.006667$ and SD $.2/\sqrt{12}=.057735$. Dollar mean is $.6667$ and dollar SD $5.7735$. The local variance is $(.2\cdot100)^2/12=33.3333$, not the SD. [pp. 29–32]


## Notation

| Symbol | Meaning |

|---|---|

| $S_0,S_t,S_T$ | Underlying price now, at time t, and at expiry; FX quote is domestic per foreign unit. |

| $K$ | Strike / exercise price. |

| $c,p;\ C,P$ | European call/put; American call/put prices. |

| $f_{i,j}$ | Option value at step i after j up moves. |

| $T,t,\Delta t,N$ | Expiry in years; current time; step T/N; number of tree/simulation steps. |

| $r,r_f,q$ | Continuous domestic rate, foreign rate, and dividend yield. |

| $D,D_{\rm cash}$ | Present value of dividends; actual cash amount at the payment date. |

| $u,d,a$ | Tree up/down multipliers and risk-neutral one-step growth factor. |

| $p,p^*,Q$ | Risk-neutral up probability, physical up probability, pricing measure. p also denotes a put price: use context. |

| $\Delta$ | Hedge ratio, shares per option unit. Δt is a time interval. |

| $\mu,\sigma$ | Annual proportional drift and annualized volatility. |

| $W_t,\Delta W,\varepsilon$ | Wiener level, increment and standard normal shock. |

| $a(X,t),b(X,t)$ | Itô drift and diffusion; variance rate b². This a is not tree growth. |

| $\mathcal F_t,E_t,\operatorname{Var}_t$ | Information at t; expectation/variance conditional on it. |

| $\rho,U,V$ | Correlation and independent standard normal variables. |

| $\kappa,\theta,\eta$ | Mean-reversion speed, target and diffusion coefficient. |

| $N(m,v),\Phi(z)$ | Normal with mean m and variance v; standard normal CDF. |

| $x^+,\operatorname{Cov},\operatorname{Corr}$ | max(x,0); covariance; covariance divided by both SDs. |

| $z(t),z_t,Z(t),dz$ | Alternative process/Wiener notation in the slides; Δz is a change, not the current level. |

| $W_t^Q$ | Wiener process under the risk-neutral probability measure Q. |

| $F_0$ | Forward delivery price or current futures quote, according to the contract being discussed. |

| $H,A$ | H: terminal cash value of the riskless stock–option hedge. A: strategy net debit, or budget in the principal-protection example. |

| $i,j,M$ | i: time-step index; j: up-move count; M: option units when hedging, or number of simulated paths in a cost calculation. |


## Suggested exercises — all 20 / 97 subparts


### Q1 · No-arbitrage bounds

$S_0=64,K=60,T=.75,r=.05$, no dividends. Find both bounds, test call $4.50$, construct arbitrage.


(a) Call lower $6.2083$, upper $64$.


(b) Put lower $0$, upper $57.7917$.


(c) Call quote violates the lower bound.


(d) Buy call and bond paying $60$; short stock. Initial receipt $64-4.5-60e^{-.0375}=$ $1.7083$. Terminal payoff $(S_T-60)^++60-S_T=(60-S_T)^+\ge0$. Invest the initial receipt.


### Q2 · Parity arbitrage

$S_0=82,K=85,T=.5,r=.04,c=5.20$; test market put $9$.


(a) $c+Ke^{-rT}=p+S_0$.


(b) $p=5.2+85e^{-.02}-82=$ $6.5169$.


(c) Market put is overpriced relative to its replication.


(d) Buy call and bond paying $85$; short put and stock. Initial receipt $9+82-5.2-85e^{-.02}=$ $2.4831$. Terminal $(S_T-85)^++85-(85-S_T)^+-S_T=0$. Invest the receipt.


### Q3 · Long straddle

Buy call $K=75$ for $6$ and put $K=75$ for $4$. Payoffs, profits at $60,75,95$, break-evens and sketch; ignore financing.


(a) Call $(S_T-75)^+$; put $(75-S_T)^+$.


(b) Combined payoff $|S_T-75|$.


(c) Profit $|S_T-75|-10$: $5,-10,10$ respectively.


(d) Break-evens $65,85$.


(e) V-shaped profit: slope $-1$ below $75$, $+1$ above; vertex $(75,-10)$, zero at $65,85$. See payoff explorer.


### Q4 · American and European calls

Compare exercise rights, values and early exercise, with and without dividends.


(a) European: only at expiry. American: any allowed time through expiry.


(b) $C\ge c$: more rights cannot reduce value.


(c) No dividends and $r\ge0$: early exercise sacrifices optionality and pays the strike sooner; $C=c$.


(d) Dividends may justify exercise immediately before ex-dividend; compare the benefit with lost time value and early strike payment.


### Q5 · One-step replication

$S_0=48,S_u=54,S_d=43,K=49,T=.25,r=.06$. Payoffs, hedge, price and probability.


(a) $f_u=5,f_d=0$.


(b) $\Delta=5/11=.454545$.


(c) Long $5/11$ shares, short one call: both states pay $H=54(5/11)-5=43(5/11)=215/11$.


(d) $f_0=48(5/11)-(215/11)e^{-.015}=$ $2.5637$.


(e) $p=(48e^{.015}-43)/11=$ $0.5205$; $e^{-.015}(5p)=$ $2.5637$.


### Q6 · Pricing versus physical probability

$S_0=100,u=1.15,d=.9,r=.05,T=.25,\mu=.12$.


(a) $p_Q=(e^{.0125}-.9)/.25=$ $0.4503$.


(b) $p_Q115+(1-p_Q)90=100e^{.0125}=$ $101.2578$.


(c) $p^*=(e^{.03}-.9)/.25=$ $0.5218$.


(d) Physical probability matches expected return $\mu$; pricing probability matches $r$. Replication prices the option without the investor’s return forecast.


### Q7 · Two-step European call

$S_0=60,u=1.12,d=.9,r=.04,\Delta t=.25,N=2,K=62$.


(a) $60\to(67.2,54)\to(75.264,60.48,48.6)$ (high to low).


(b) $p=(e^{.01}-.9)/.22=$ $0.5002$.


(c) Payoffs $13.264,0,0$.


(d) Upper intermediate $6.5690$, lower $0$; root $3.2533$.


(e) $e^{-.02}[p^2(13.264)+2p(1-p)0+(1-p)^2 0]=$ $3.2533$.


### Q8 · Two-step European put

$S_0=75,K=78,u=1.25,d=.8,r=.05,\Delta t=1,N=2$.


(a) $75\to(93.75,60)\to(117.1875,75,48)$.


(b) $p=(e^{.05}-.8)/.45=$ $0.5584$.


(c) Payoffs $0,3,30$.


(d) Upper intermediate $1.2602$, lower $14.1959$, root $6.6328$.


(e) Discount the risk-neutral expected payoff. This is valuation, not a real-world forecast.


### Q9 · American put: exercise decisions

$S_0=45,K=48,r=.05,\sigma=.3,T=1,N=2$; CRR.


(a) $\Delta t=.5$.


(b) $u=e^{.3\sqrt{.5}}=$ $1.2363$, $d=1/u=$ $0.8089$.


(c) $p=(e^{.025}-d)/(u-d)=$ $0.5064$.


(d) Intermediate high-to-low: $55.6340$, $36.3986$. Terminal prices: $68.7809$, $45.0000$, $29.4413$. Put payoffs: $0.0000$, $3.0000$, $18.5587$.


(e) Upper: continuation $1.4443$ exceeds exercise $0$. Lower: continuation $10.4163$ below exercise $11.6014$: exercise.


(f) Root $6.2985$ exceeds immediate exercise $3$: continue. Early exercise at the low intermediate node.


### Q10 · FX call

$S_0=.72,K=.73,r=.05,r_f=.03,\sigma=.15,T=.5,N=2$. Domestic per foreign unit.


(a) $u=e^{.15\sqrt{.25}}=$ $1.0779$, $d=$ $0.9277$.


(b) $p=(e^{(.05-.03).25}-d)/(u-d)=$ $0.5146$.


(c) $S_{i,j}=.72u^jd^{i-j}$. Intermediate low-to-high: $0.6680$, $0.7761$; terminal: $0.6197$, $0.7200$, $0.8365$.


(d) Terminal payoffs low-to-high: $0.0000$, $0.0000$, $0.1065$.


(e) Discount at domestic r: call $0.0275$.


(f) Foreign interest acts as yield, reducing growth to $r-r_f$, not replacing domestic discounting.


### Q11 · Wiener distributions and tails

Standard $W_0=0$: distributions at 2 and over [2,5], moments at 4, tail at 1.5, independence.


(a) $W_2\sim N(0,2)$.


(b) $W_5-W_2\sim N(0,3)$.


(c) $E[W_4]=0$, variance $4$, SD $2$.


(d) $P(W_1>1.5)=1-\Phi(1.5)\approx.066807$.


(e) Independent non-overlapping increments are a defining property. Levels are not generally independent.


### Q12 · Generalized Wiener process

$dX=8dt+12dW,X_0=30$ million; years.


(a) Drift $8$, variance rate $144$; diffusion $12$.


(b) $X_1\sim N(38,144)$.


(c) $E[X_{.5}]=34$ million.


(d) SD at two years $12\sqrt2=16.9706$ million.


(e) $P(X_1<25)=\Phi(-13/12)\approx.1393$.


### Q13 · Mean reversion

$dX=.6(50-X)dt+8dW$; drift at $40,50,65$; local moments at $40,\Delta t=.1$.


(a) $a=.6(50-X)$, $b=8$.


(b) Drifts $6,0,-9$.


(c) Drift pulls toward $50$, proportional to distance; noise remains.


(d) $E_t[\Delta X]\approx.6$, variance $\approx6.4$. Local, not exact finite-time mean-reversion moments.


### Q14 · Local Itô moments

$dX=(4+.2X)dt+.15XdW$, $X=80,\Delta t=1/12$.


(a) $a=4+.2X$, $b=.15X$.


(b) Drift $20$.


(c) Variance rate $12^2=144$.


(d) Mean change $\approx20/12=1.6667$; variance $\approx12$.


(e) $X_{t+1/12}\approx80+20/12+\sqrt{12}\varepsilon$.


### Q15 · GBM: percentages and dollars

$S=120,\mu=.09,\sigma=.24$; one month.


(a) Drift $10.8$; diffusion $28.8$.


(b) $dS/S=.09dt+.24dW$.


(c) Proportional mean $\approx.0075=0.75\%$.


(d) Proportional SD $\approx.24/\sqrt{12}=.069282=6.9282\%$.


(e) Dollar mean $\approx.9$; SD $\approx8.3138$.


### Q16 · Three Euler steps

$S_0=100,\mu=.06,\sigma=.2,\Delta t=1/12$; shocks $.5,-1.2,.8$.


(a) $S_{i+1}=S_i(1+.06/12+.2\varepsilon_i/\sqrt{12})$.


(b) $S_1=$ $103.3868$.


(c) $S_2=$ $96.7408$; use the updated first price.


(d) $S_3=$ $101.6928$.


(e) Independent shocks do not imply independent recursively built price levels.


### Q17 · Step-size comparison

$dS=.07Sdt+.25SdW,S_0=90$; quarter versus month.


(a) Quarter $S_{i+1}=S_i(1+.0175+.125\varepsilon_i)$.


(b) Month $S_{i+1}=S_i(1+.07/12+.25\varepsilon_i/\sqrt{12})$.


(c) At $90$: quarterly mean $1.575$, variance $126.5625$; monthly mean $.525$, variance $42.1875$ (local).


(d) Quarter the step: SD halves, since $\sqrt{\Delta t/4}=\sqrt{\Delta t}/2$.


(e) Smaller steps reduce coefficient-freezing/discretization error at greater computational cost.


### Q18 · Correlated increments

$dX_1=3dt+5dW_1,dX_2=2dt+7dW_2,\rho=.65,\Delta t=.25$.


(a) Means $.75,.5$.


(b) Variances $6.25,12.25$.


(c) Covariance $.65(5)(7)(.25)=5.6875$.


(d) Correlation $.65$.


(e) Changing $\rho$ to $-.65$ reverses covariance/correlation signs; marginal means and variances remain.


### Q19 · Correlated shocks

Independent $U,V\sim N(0,1)$; $\varepsilon_1=U,\varepsilon_2=\rho U+\sqrt{1-\rho^2}V$.


(a) Both means are zero by linearity.


(b) First variance $1$; second $\rho^2+(1-\rho^2)=1$, using zero covariance of U,V.


(c) $\operatorname{Cov}(\varepsilon_1,\varepsilon_2)=\rho\operatorname{Var}(U)=\rho$.


(d) $\rho=-.4,U=.6,V=-1.1$: $\varepsilon_1=.6$, $\varepsilon_2=-.24-1.1\sqrt{.84}=$ $-1.2482$.


(e) Fresh independent U,V pair each step; use its correlated shocks in the stock updates.


### Q20 · Two-stock simulation

$S_1=100,S_2=80,\mu_1=.08,\mu_2=.05,\sigma_1=.2,\sigma_2=.3,\rho=.5,\Delta t=1/12$.


(a) $S_1^+=S_1(1+.08/12+.2\varepsilon_1/\sqrt{12})$; $S_2^+=S_2(1+.05/12+.3\varepsilon_2/\sqrt{12})$.


(b) Local/Euler dollar means $\approx.6667,.3333$.


(c) Local/Euler dollar SDs $\approx5.7735,6.9282$.


(d) Local/Euler dollar covariance $\approx.5(.2)(.3)(100)(80)/12=20$.


(e) $U=.8,V=-.5$: $\varepsilon_1=.8$, $\varepsilon_2=.4-.5\sqrt{.75}=$ $-0.0330$. Updated prices $105.2855$, $80.1046$.


## Brownian dependence supplement


### (a) $W_2\quad\text{and}\quad W_4-W_2$
Independent. Disjoint intervals [0,2] and [2,4]; covariance 0.


### (b) $W_2\quad\text{and}\quad W_4$
Dependent. Covariance $\min(2,4)=2$. The later level contains the earlier increment.


### (c) $W_3-W_1\quad\text{and}\quad W_5-W_3$
Independent. Disjoint increments; covariance 0. A shared endpoint adds no overlap length.


### (d) $W_3-W_1\quad\text{and}\quad W_4-W_2$
Dependent. Overlap [2,3] has length 1: covariance 1.


### (e) $W_5-W_2\quad\text{and}\quad W_2-W_1$
Independent. Disjoint increments; covariance 0.


### (f) $W_4+W_2\quad\text{and}\quad W_4-W_2$
Dependent. Covariance $\operatorname{Var}(W_4)-\operatorname{Var}(W_2)=4-2=2$.


### (g) $W_3-2W_2+W_1\quad\text{and}\quad W_3-W_1$
Independent. Let $X=W_2-W_1$, $Y=W_3-W_2$, independent $N(0,1)$. Pair $Y-X,Y+X$ has covariance $1-1=0$ and is jointly Gaussian, hence independent.


### (h) $W_2^2\quad\text{and}\quad W_4-W_2$
Independent. $W_2$ is independent of the later increment; squaring preserves independence. The square is not Gaussian: do not justify this solely with zero covariance.


### (i) $W_4-2W_2\quad\text{and}\quad W_2$
Dependent. Covariance $2-2(2)=-2$.


## Lecture 7 exercise answers


### Exercise 1 / 4

{'S': 78, 'K': 80, 'r': 0.03, 'T': 0.3333333333333333, 'N': 2, 'sigma': 0.3}

Value 4.6677; next-node value slope 0.5000; u 1.1303; d 0.8847; p 0.4898

To hedge 1000 short option units, buy 499.9990 shares initially; multiply again if contracts have a multiplier.

Step 0: stock [78.0]; option [4.667671238835645]

Continuation [4.667671238835645]; immediate exercise [0]

Step 1: stock [69.00882117558425, 88.16264205586167]; option [0.0, 9.57689066307579]

Continuation [0.0, 9.57689066307579]; immediate exercise [0, 8.162642055861667]

Step 2: stock [61.0540692313303, 78.0, 99.64937761884599]; option [0, 0, 19.64937761884599]


### Exercise 2

{'S': 50, 'K': 51, 'r': 0.05, 'T': 0.5, 'N': 2, 'u': 1.06, 'd': 0.95}

Value 1.6351; next-node value slope 0.5291; u 1.0600; d 0.9500; p 0.5689

Step 0: stock [50.0]; option [1.6350711385184167]

Continuation [1.6350711385184167]; immediate exercise [0]

Step 1: stock [47.5, 53.0]; option [0.0, 2.910269488814637]

Continuation [0.0, 2.910269488814637]; immediate exercise [0, 2.0]

Step 2: stock [45.125, 50.349999999999994, 56.18000000000001]; option [0, 0, 5.180000000000007]


### Exercise 3 European

{'S': 40, 'K': 42, 'r': 0.12, 'T': 0.5, 'N': 2, 'u': 1.1, 'd': 0.9, 'put': True}

Value 2.1185; next-node value slope -0.4936; u 1.1000; d 0.9000; p 0.6523

Step 0: stock [40.0]; option [2.1184803010867217]

Continuation [2.1184803010867217]; immediate exercise [2.0]

Step 1: stock [36.0, 44.0]; option [4.758712409037339, 0.8098810428403073]

Continuation [4.758712409037339, 0.8098810428403073]; immediate exercise [6.0, 0]

Step 2: stock [32.400000000000006, 39.6, 48.400000000000006]; option [9.599999999999994, 2.3999999999999986, 0]


### Exercise 3 American

{'S': 40, 'K': 42, 'r': 0.12, 'T': 0.5, 'N': 2, 'u': 1.1, 'd': 0.9, 'put': True, 'american': True}

Value 2.5374; next-node value slope -0.6488; u 1.1000; d 0.9000; p 0.6523

Step 0: stock [40.0]; option [2.5373533380173767]

Continuation [2.5373533380173767]; immediate exercise [2.0]

Step 1: stock [36.0, 44.0]; option [6.0, 0.8098810428403073]

Continuation [4.758712409037339, 0.8098810428403073]; immediate exercise [6.0, 0]

Step 2: stock [32.400000000000006, 39.6, 48.400000000000006]; option [9.599999999999994, 2.3999999999999986, 0]


### Exercise 6 call

{'S': 90, 'K': 93, 'r': 0.03, 'T': 0.75, 'N': 3, 'sigma': 0.28, 'q': 0.03, 'american': True}

Value 7.9381; next-node value slope 0.4895; u 1.1503; d 0.8694; p 0.4651

Step 0: stock [90.0]; option [7.938057803090932]

Continuation [7.938057803090932]; immediate exercise [0]

Step 1: stock [78.24224118589251, 103.52464189715046]; option [2.2423602413069705, 14.618168225412642]

Continuation [2.2423602413069705, 14.618168225412642]; immediate exercise [0, 10.52464189715046]

Step 2: stock [68.02053673101528, 90.0, 119.08168311036934]; option [0.0, 4.857987087690102, 26.08168311036934]

Continuation [0.0, 4.857987087690102, 25.886802203944054]; immediate exercise [0, 0, 26.08168311036934]

Step 3: stock [59.1342137833551, 78.24224118589251, 103.52464189715046, 136.97654000567707]; option [0, 0, 10.52464189715046, 43.976540005677066]


### Exercise 6 put

{'S': 90, 'K': 93, 'r': 0.03, 'T': 0.75, 'N': 3, 'sigma': 0.28, 'q': 0.03, 'american': True, 'put': True}

Value 10.8824; next-node value slope -0.5031; u 1.1503; d 0.8694; p 0.4651

Step 0: stock [90.0]; option [10.882406493207252]

Continuation [10.882406493207252]; immediate exercise [3.0]

Step 1: stock [78.24224118589251, 103.52464189715046]; option [16.879503140460802, 4.1602642800199305]

Continuation [16.879503140460802, 4.1602642800199305]; immediate exercise [14.75775881410749, 0]

Step 2: stock [68.02053673101528, 90.0, 119.08168311036934]; option [24.979463268984716, 7.835571252147521, 0.0]

Continuation [24.79281808879152, 7.835571252147521, 0.0]; immediate exercise [24.979463268984716, 3.0, 0]

Step 3: stock [59.1342137833551, 78.24224118589251, 103.52464189715046, 136.97654000567707]; option [33.8657862166449, 14.75775881410749, 0, 0]


Exercise 5: dt=1/12, r=.05, rf=.08, sigma=.12. u=exp(.12/sqrt(12)), d=1/u, a=exp(-.03/12), p=(a-d)/(u-d). Values: u=1.035248, d=0.965952, a=0.997503, p=0.455308.


## Limitations and corrections

L2 margin spreadsheet not supplied. L7 p13 root .9334 is inconsistent: parameters give .9497. CRR variance matching is local/asymptotic. Original source PDFs are not republished.