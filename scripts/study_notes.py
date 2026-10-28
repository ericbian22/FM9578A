"""Detailed study notes layered onto the original source-aligned content."""
import re

def bullets(items):
    return '<ul class="study-points">'+''.join('<li>'+item+'</li>' for item in items)+'</ul>'

def bulletize(body):
    """Preserve existing content and math while separating dense prose."""
    saved=[]
    def protect(match):
        saved.append(match.group(0))
        return '\ue000'+str(len(saved)-1)+'\ue001'
    protected=re.sub(r'<pre>[\s\S]*?</pre>|<div class="example">[\s\S]*?</div>|\$\$[\s\S]+?\$\$|\$[^$\n]+?\$|<[^>]+>',protect,body)
    sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',protected)
    # Keep related sentences together, instead of turning every clause into a bullet.
    groups=[' '.join(sentences[i:i+2]) for i in range(0,len(sentences),2)]
    def restore(text):
        return re.sub(r'\ue000(\d+)\ue001',lambda m:saved[int(m.group(1))],text)
    return bullets([restore(g) for g in groups if g.strip()])

DETAILS=[
('Reading a position from start to finish',[
r'<b>Identify who has the choice.</b> The call buyer can buy at $K$, so exercising makes sense at expiry only when the market price is above $K$. The put buyer can sell at $K$, so the useful region is below $K$. The writer takes the opposite cash flow; the writer does not choose whether assignment occurs.',
r'<b>Separate three questions.</b> “Is it ITM?” compares $S_T$ with $K$. “What is the payoff?” measures the exercise benefit. “Was the trade profitable?” also includes the premium. These answers can differ: a call with $K=50,c_0=4,S_T=52$ is ITM, pays $2$, but loses $2$ before financing.',
r'<b>Build the graph by regions.</b> For a long call, payoff is zero through $K$ and has slope $+1$ above it. Subtracting the premium shifts the whole graph downward without changing the kink or slope. A short position reflects the long-position payoff or profit across the horizontal axis.',
r'<b>Apply the contract multiplier last.</b> Calculate per underlying unit first, then multiply the payoff and premium by the number of units. A quoted premium of $4$ for a 100-share option contract means $400$, not $4$, paid per contract.',
r'<b>Read the graph below.</b> The call’s payoff starts rising at $50$, while profit reaches zero only at $54$. The put has the opposite slope below $50$ and its profit reaches zero at $46$. These are illustrations with premium $4$ and financing ignored. [L1 pp. 13–17]']),
('Follow the cash through a margin account',[
r'<b>Initial margin is a deposit.</b> It is collateral supporting a position, not the price of the futures contract and not the maximum possible loss. Daily settlements change the balance as market prices move.',
r'<b>Calculate the daily gain or loss.</b> For a long futures position, a price increase produces a gain and a decrease a loss; the short position reverses the sign. Multiply the quoted price change by contract units and number of contracts before updating the balance.',
r'<b>Check the maintenance threshold after settlement.</b> In the authored example, $5{,}000-1{,}800=3{,}200$, which is below $3{,}500$. Restoring the initial balance requires $5{,}000-3{,}200=1{,}800$, not merely the $300$ gap to maintenance.',
r'<b>Distinguish a valuation disagreement from arbitrage.</b> If a model says $96$ and the market says $90$, ask whether an actual replicating portfolio locks in the difference. An uncertain model estimate alone cannot guarantee a riskless $6$ gain.',
r'<b>Source boundary.</b> These steps explain the mechanics from L2 pp. 13–15. The spreadsheet named on p. 16 was not supplied, so this illustration is not claimed to reproduce its numbers.']),
('Prove a bound or parity using a cash-flow table',[
r'<b>Choose portfolios with comparable expiry values.</b> Call plus a bond paying $K$ has payoff $(S_T-K)^++K$. Below $K$ this is $K$; above $K$ it is $S_T$. Stock plus put gives exactly the same two cases, proving European parity.',
r'<b>For a lower bound, dominance is enough.</b> Call plus the bond pays at least $S_T$ in both cases, so it cannot cost less than the stock. Rearranging $c+Ke^{-rT}\ge S_0$ gives the call lower bound; also impose $c\ge0$. The put bound follows from put plus stock dominating the bond.',
r'<b>Discount the strike, not the stock quote.</b> The bond costs $Ke^{-rT}$ today because it must pay $K$ later. Using $K$ instead would mix present and future cash flows. For Q1, $60e^{-.05(.75)}$ is about $57.7917$, giving call lower bound $6.2083$.',
r'<b>State both dates in an arbitrage answer.</b> Buy the cheaper portfolio and sell the expensive one. Show the positive cash receipt at time zero, then show that terminal obligations cancel or leave a nonnegative payoff. This is more convincing than saying only “the option is overpriced.”',
r'<b>Use identical contracts.</b> Parity requires the same underlying, strike and expiry, with the dividend adjustment appropriate to the question. Do not substitute an American option into the European equality. [L3 pp. 11–17; exercises 1–2]']),
('Deciding whether to exercise early',[
r'<b>Compare value now with the value of waiting.</b> Exercise converts an option into its immediate intrinsic cash flow or underlying transaction. Continuation retains the future choices. Being ITM tells you exercise is possible at a positive value, not that it is best.',
r'<b>For a non-dividend call, waiting has two advantages.</b> You postpone paying $K$ and retain protection if the stock later falls. With $r\ge0$ and no dividends to miss, early exercise adds no compensating benefit. Selling the option can recover time value if you want to exit.',
r'<b>A put can benefit from early cash.</b> A deeply ITM put is already close to its maximum exercise payoff. Receiving the strike earlier can outweigh the remaining optionality, especially at higher interest rates. A tree makes that trade-off explicit.',
r'<b>A cash dividend changes the call trade-off.</b> Exercising just before ex-dividend makes you a shareholder entitled to the dividend; continuing as an option holder does not. Compare this benefit with the interest cost of paying the strike and the option value surrendered.',
r'<b>Check the timing of dividends.</b> $D$ in parity is the present value of the cash payments before expiry. $D_{\rm cash}$ in a stock-price jump is the amount paid at that date. They serve different roles. [L4 pp. 6–14]']),
('Construct a strategy rather than memorize its name',[
r'<b>Write each leg with a sign.</b> For a bull call, buying the low-strike call contributes $(S_T-K_1)^+$ and selling the high-strike call contributes $-(S_T-K_2)^+$. This signed sum is the safest starting point.',
r'<b>Split the terminal-price axis at the strikes.</b> Below $K_1$, neither call pays. Between strikes, only the purchased call pays, so the slope is $+1$. Above $K_2$, both calls move dollar-for-dollar and cancel their slopes, leaving the fixed width $K_2-K_1$.',
r'<b>Account for the net premium once.</b> Premiums $8$ paid and $2$ received give a debit of $6$. Profit is payoff minus $6$ everywhere. With strikes $50,70$, the break-even is $56$, max gain $14$ and max loss $6$.',
r'<b>Compare shapes to choose a strategy.</b> A spread limits directional upside and downside. A straddle pays for a sufficiently large move either way. A long butterfly does best near the middle strike and loses its debit outside the wings. The graph below compares payoff shapes before premiums.',
r'<b>Do not combine different expiry payoffs incorrectly.</b> In a calendar spread, the long-dated leg remains an option at the short leg’s expiry. Its remaining time value must be valued; subtracting two intrinsic values at that date is generally wrong. [L5 pp. 17–38]']),
('Why replication and risk-neutral pricing agree',[
r'<b>Start from terminal payoffs.</b> With stock $20\to22$ or $18$ and a call struck at $21$, the call pays $1$ or $0$. The difference between option payoffs is $1$, while the stock difference is $4$.',
r'<b>Choose the stock holding to cancel uncertainty.</b> Hold $\Delta=1/4$ shares and short one call. The up state pays $.25(22)-1=4.5$; the down state pays $.25(18)-0=4.5$. The two equal payoffs are the key check.',
r'<b>Bring the certain amount back to today.</b> The hedge costs $.25(20)-f_0=5-f_0$. Since it pays $4.5$ after one quarter, $5-f_0=4.5e^{-.04(.25)}$, so $f_0=.5448$. No assumption about the stock’s real-world upward probability was needed.',
r'<b>Recover the same value using the pricing probability.</b> Choose $p$ so the expected stock growth equals risk-free growth: $p(22)+(1-p)18=20e^{.01}$. Thus $p=.550251$ and discounted expected call payoff is $e^{-.01}[p(1)+(1-p)0]=.5448$.',
r'<b>For multiple steps, work from right to left.</b> The rightmost option values are known payoffs. Every earlier node is a one-step pricing problem with the two child values as its inputs. Recombination merges up-down and down-up prices; it does not remove either path’s probability. [L6 pp. 4–14]']),
('American exercise: a worked node comparison',[
r'<b>Compute the same continuation value as for a European option.</b> In the lecture put example, $S_0=50,K=52,u=1.2,d=.8,r=.05$, with two one-year steps. The pricing probability is about $.628178$. Terminal stock prices are $72,48,32$, with put payoffs $0,4,20$.',
r'<b>At the low intermediate node, compare two actual numbers.</b> At $S=40$, continuation is $e^{-.05}[p(4)+(1-p)20]=9.4636$. Exercise gives $52-40=12$. The American value there is $12$ because exercising is worth more than waiting.',
r'<b>At the high node, exercise is not attractive.</b> At $S=60$, exercise is zero but continuation is $1.4147$, so keep the option. Roll these selected child values back to obtain root value $5.0894$. Immediate root exercise gives only $2$.',
r'<b>Explain the premium for flexibility.</b> The European put must continue at the low node and is worth $4.1923$ at the root. The American is more valuable because it can avoid that inferior continuation decision. The extra right helps only where exercise beats continuation.',
r'<b>Refining the tree changes opportunities and approximation.</b> CRR recomputes $u,d,p$ using the smaller time step. Check that $0<p<1$, and compare several step counts if assessing convergence; do not assume each refinement moves the price in the same direction. [L7 pp. 3–7, 20–25]']),
('Understand what scales with time',[
r'<b>A level and an increment answer different questions.</b> $W_4$ includes all movement from time 0 to 4. $W_4-W_2$ includes only movement after time 2. It is independent of $W_2$, even though $W_4$ itself is not.',
r'<b>Scale the variance first.</b> A standard Wiener increment over length $h$ has variance $h$, so its standard deviation is $\sqrt h$. If $h$ falls from $1$ to $1/4$, variance becomes $1/4$ and SD becomes $1/2$. Multiplying a normal shock by $h$ instead would give the wrong variance $h^2$.',
r'<b>Add disjoint increments to recover a longer interval.</b> Four independent quarterly increments have total variance $4(1/4)=1$. Their sum is normal because each increment is normal and the increments are independent; their SDs do not add to $2$.',
r'<b>For generalized Wiener motion, separate center and spread.</b> With $X_0=50,a=20,b=30$, six-month mean is $50+20(.5)=60$ while SD is $30\sqrt{.5}=21.2132$. Drift shifts the center; diffusion controls spread around it.',
r'<b>Use overlap to reason about dependence.</b> Increments over [1,3] and [2,4] share the random movement on [2,3], producing covariance $1$. Sharing only an endpoint contributes zero overlap length. The timeline below makes the shared randomness visible. [L8 pp. 8–21, 28–34; Brownian supplement]']),
('From an SDE to a calculation or simulated path',[
r'<b>Identify coefficients before substituting time.</b> For $dX=(4+.2X)dt+.15X\,dW$ at $X=80$, drift is $20$ and diffusion is $12$. The instantaneous variance rate is $12^2=144$, not $12$.',
r'<b>Convert rates to a small-step change.</b> Over $1/12$ year, the frozen-coefficient mean change is $20/12$ and variance is $144/12=12$. The corresponding Euler step is $X^+=80+20/12+\sqrt{12}\varepsilon$. These are local approximations because the coefficients can change as $X$ moves.',
r'<b>For GBM, distinguish dollars from proportions.</b> In $dS/S=\mu dt+\sigma dW$, coefficients describe proportional changes. Multiply by the current stock price to obtain dollar drift $\mu S$ and dollar diffusion $\sigma S$. The dollar variance then contains $S^2$.',
r'<b>Update the state after each shock.</b> Monthly Euler factors for Q16 multiply successively: $S_1=100g_1$, $S_2=S_1g_2$, $S_3=S_2g_3$, where $g_i=1+.06/12+.2\varepsilon_i/\sqrt{12}$. Reusing $100$ for every step would give separate one-step scenarios, not a three-month path.',
r'<b>Build correlated shocks before updating the two stocks.</b> Draw independent $U,V$, then set $\varepsilon_1=U$ and $\varepsilon_2=\rho U+\sqrt{1-\rho^2}V$. This keeps unit marginal variances while controlling covariance. Use a new pair at the next time step; otherwise you introduce unintended dependence across time. [L9 pp. 25–39]'])
]

GRAPH_INFO={
1:('payoff-profit.svg','Long call and put payoff versus profit, strike 50 and premium 4.','Dashed lines show profit after subtracting a premium of 4; solid lines show payoff. The break-even differs from the exercise threshold.'),
3:('parity.svg','Expiry cash flows of call plus bond and stock plus put.','Both European portfolios pay max(S_T, K). The equality of future cash flows explains put–call parity today.'),
5:('strategies.svg','Bull spread, bear spread, butterfly and straddle payoff shapes.','These are payoffs before premiums. Subtract the net debit to obtain a profit graph; do not compare payoff heights as if they were net returns.'),
6:('binomial-tree.svg','Two-step stock and European call tree with node values.','Stock moves forward; option valuation moves backward. Each node shows the stock price S and call value f for the L6 example.'),
7:('american-exercise.svg','American put exercise value versus continuation at intermediate nodes.','At S=40, exercise 12 exceeds continuation 9.4636; at S=60, continuation 1.4147 exceeds exercise 0. Choose the larger value at each node.'),
8:('brownian-scaling.svg','Variance T and standard deviation square root T versus time.','Variance grows linearly, while SD grows as the square root of time. Separate panels avoid treating variance and SD as quantities with the same units.'),
9:('euler-path.svg','Three monthly Euler stock updates using the shocks from exercise 16.','Each point starts from the previous updated stock price. This is one deterministic calculation using the supplied shocks, not an expected-price forecast.')
}

REASONS=[
['Compare today’s stock quote with the present value of the strike; then apply nonnegativity to the lower bounds.','To prove the call arbitrage, verify both the initial receipt and terminal payoff in the regions below and above the strike.'],
['Solve parity algebraically for the unknown put before comparing it with the market quote.','The short put and short stock fund the long call and bond. At expiry the whole position cancels for every terminal stock price.'],
['The call pays only above 75 and the put only below 75; adding them produces an absolute-value payoff.','Both premiums are paid, so subtract 10 everywhere. The two break-evens are where the payoff rises back to 10.'],
['More exercise rights cannot reduce value because the American holder can always wait until expiry.','For the non-dividend call, paying the strike early gives up financing value without receiving a dividend benefit.'],
['Choose delta to make the up-minus-down change in the hedged portfolio zero.','Check both terminal states explicitly, then discount the common hedge payoff. Risk-neutral valuation is a second route to the same price.'],
['The two probabilities solve different expected-growth equations, one with r and one with mu.','Only the pricing probability is used with risk-free discounting in this replication model; mixing physical expectation with risk-free discounting generally gives the wrong value.'],
['Build stock nodes by multiplying factors; the middle price can be reached by two paths.','The two-step direct formula includes the factor 2 on p(1−p) because both middle paths count.'],
['A put is worth more at low terminal stock prices, so compute K−S separately at each terminal node.','Price the two intermediate nodes first, then use those option values—not their stock prices—in the root expectation.'],
['CRR uses the square root of the half-year step in u and d.','At intermediate nodes and at the root, compare exercise with continuation before selecting the American value; a positive intrinsic value alone does not establish optimal exercise.'],
['Use domestic minus foreign interest for currency growth, but the domestic rate alone for discounting.','The exchange-rate quote is domestic currency per foreign unit, so all payoffs are expressed in domestic currency per option unit.'],
['The normal variance of an increment is the length of its interval: 5−2=3.','For the tail probability, W1 is already standard normal. A level at time 4 would need division by its SD, 2, before using the standard normal CDF.'],
['Constant coefficients permit an exact normal distribution at the stated horizon, rather than a local approximation.','Standardize 25 by subtracting the one-year mean 38 and dividing by SD 12, not variance 144.'],
['The sign of theta minus X determines which direction the drift pulls.','The local variance uses eta squared times the step; the state-dependent drift does not make these frozen finite-step moments exact.'],
['Substitute X=80 before evaluating drift and diffusion.','The Euler shock coefficient is b times square root dt; equivalently it is the square root of the local variance.'],
['Start with percentage mean and SD, then multiply each by the current price to convert to dollar changes.','Converting a dollar SD to variance requires squaring the full product sigma times S.'],
['Calculate the first multiplier, multiply the current price, and carry that updated price into the next calculation.','Do not round intermediate prices too early; later results use those prices as inputs.'],
['Drift accumulates in proportion to dt while the random shock coefficient scales with square root dt.','A smaller step reduces local approximation error but still contains randomness and requires more steps for a fixed horizon.'],
['The deterministic drift terms contribute to means, not covariance.','Multiply the two diffusion coefficients, their Brownian correlation, and the interval length to obtain covariance.'],
['Independence makes Cov(U,V)=0, eliminating the cross term from the variance calculation.','The shared U component creates correlation, while the independent V component restores unit variance.'],
['Construct both correlated shocks before evaluating either monthly stock update.','Use the current prices and each stock’s own drift and volatility. The stated means, SDs and covariance are local/Euler quantities, not exact long-horizon GBM formulas.']
]

def enrich(lectures,exercises):
    for lecture,(title,items) in zip(lectures,DETAILS):
        # Verify every old math expression survives the formatting change.
        for section in lecture['sections']:
            before=section['body']
            after=bulletize(before)
            pattern=r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$'
            assert re.findall(pattern,before)==re.findall(pattern,after)
            plain=lambda value:re.sub(r'\s+','',re.sub(r'<[^>]*>','',re.sub(pattern,lambda m:m.group(0).replace('<','&lt;').replace('>','&gt;'),value)))
            assert plain(before)==plain(after),section['title']
            section['body']=after
        lecture['sections'].append(dict(title=title,body=bullets(items)))
        n=lecture['number']
        if n in GRAPH_INFO:
            file,alt,caption=GRAPH_INFO[n]
            lecture['sections'].append(dict(title='See the idea',body='<figure class="study-figure"><a href="assets/graphs/'+file+'" target="_blank" rel="noopener"><img src="assets/graphs/'+file+'" alt="'+alt+'" loading="lazy"></a><figcaption>'+caption+' Open the image for a larger view.</figcaption></figure>'))
    lectures[7]['sections'].append(dict(title='Which increments overlap?',body='<figure class="study-figure"><a href="assets/graphs/increment-overlap.svg" target="_blank" rel="noopener"><img src="assets/graphs/increment-overlap.svg" alt="Intervals from 1 to 3 and 2 to 4 overlap from 2 to 3, giving Brownian covariance 1." loading="lazy"></a><figcaption>The shared interval has length 1, so the two increments have covariance 1. Disjoint intervals, including ones that only touch at an endpoint, have covariance zero.</figcaption></figure>'))
    for e,reasons in zip(exercises,REASONS):
        e['reasoning']=bullets(reasons)

