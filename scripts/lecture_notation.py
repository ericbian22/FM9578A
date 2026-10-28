"""Keep each supplied source's symbols, instead of normalizing them to one style."""
import re

MATH=r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$'
def in_math(text,fn):
    return re.sub(MATH,lambda m:fn(m.group(0)),text)

def explicit_max(text):
    return re.sub(r'\(([^()]*)\)\^\+',r'\\max(\1,0)',text)

def z_notation(text):
    text=re.sub(r'W_\{([^{}]+)\}',r'z(\1)',text)
    text=re.sub(r'W_([0-9]+|[a-zA-Z])',r'z(\1)',text)
    return text.replace(r'\Delta W',r'\Delta z').replace('dW','dz').replace(r'\varepsilon',r'\epsilon')

def supplement_notation(text):
    text=re.sub(r'W_\{([^{}]+)\}',r'Z(\1)',text)
    return re.sub(r'W_([0-9]+|[a-zA-Z])',r'Z(\1)',text)

def apply_source_notation(lectures,exercises,notation,dependence):
    for l in lectures:
        for s in l['sections']:
            s['body']=explicit_max(s['body'])
            s['body']=s['body'].replace(r'Let $x^+=\max(x,0)$. ','')
            s['body']=s['body'].replace(r'D_{\rm cash}',r'\text{cash dividend}')
    def section(n,title):
        return next(s for s in lectures[n-1]['sections'] if s['title']==title)
    for s in lectures[4]['sections']:
        s['body']=in_math(s['body'],lambda v:re.sub(r'\bA\b',r'\\text{net cost}',v))
    section(5,'Protection and income')['body']=r'''<ul class="study-points"><li>Lecture principal protection starts with $100$: invest $100e^{-rT}$ in a zero-coupon bond paying $100$ at expiry; spend $100-100e^{-rT}$ on calls. The guarantee depends on the bond assumptions. [L5 p. 12]</li><li>Covered call: stock minus call, payoff $S_T-\max(S_T-K,0)=\min(S_T,K)$; capped upside with downside remaining. Protective put: stock plus put, payoff $S_T+\max(K-S_T,0)=\max(S_T,K)$; the premium buys the floor. [L5 pp. 13–16]</li></ul>'''
    section(6,'Hedge one step')['body']=r'''<ul class="study-points"><li>For a non-dividend stock, $S_u=S_0u$, $S_d=S_0d$, with option payoffs $f_u,f_d$. Use the lecture hedge ratio $$\Delta=\frac{f_u-f_d}{S_0(u-d)}.$$</li><li>The portfolio is long $\Delta$ shares and short one option. Equate its terminal values: $\Delta S_0u-f_u=\Delta S_0d-f_d$. Discount that common payoff: $$\Delta S_0-f=e^{-rT}(\Delta S_0u-f_u).$$ Here $T$ is the one-step horizon, as on L6 pp. 3–10; use $\Delta t$ for an individual step in a multi-step tree.</li><li>Delta is shares per option unit. Multiply by the number of option units and any contract multiplier. A negative hedge ratio means a short stock holding. [L6 pp. 3–7; L7 pp. 8–11]</li></ul>'''
    section(6,'One-step example')['body']=section(6,'One-step example')['body'].replace('$H=4.5$','riskless terminal payoff $4.5$')
    # Lecture 8 uses lower-case z(t), x and epsilon, rather than W_t and X_t.
    for s in lectures[7]['sections']:
        if 'supplement' in s['title'].lower() or s['title']=='Which increments overlap?':
            s['body']=supplement_notation(s['body'])
            s['body']=s['body'].replace('here $Z(t)=Z(t)$ denotes the same process.','the formulas below retain that notation.')
            continue
        def l8_math(value):
            value=z_notation(value)
            value=re.sub(r'X_\{([^{}]+)\}',r'x(\1)',value)
            value=re.sub(r'X_([0-9]+|[a-zA-Z])',r'x(\1)',value)
            return value.replace('dX','dx').replace(r'\Delta X',r'\Delta x').replace('w_0','z(0)')
        s['body']=in_math(s['body'],l8_math)
    section(8,'Scaling example')['body']=r'''<ul class="study-points"><li>Lecture 8 cash position: $dx=20dt+30dz$, $x(0)=50$, in thousands of dollars and years. At one year, $x(1)\sim N(70,30^2)$; at six months, $x(0.5)\sim N(60,450)$, with SD $30\sqrt{0.5}=21.2132$. [pp. 32–34]</li><li>Separate Wiener example: $z(0)=25$, so $z(1)\sim N(25,1)$ and $z(5)\sim N(25,5)$. Its five-year SD is $\sqrt5=2.2361$. [pp. 22–23]</li></ul>'''
    s=section(8,'Constant coefficients: exact')
    s['body']=s['body'].replace('x(T)=x(0)+aT+bz(T)','x(T)=x(0)+aT+b[z(T)-z(0)]')
    section(8,'The slides’ z notation and conditional-law formula')['body']=r'''<ul class="study-points"><li>Use the lecture notation $z(t)$ and $\Delta z=z(t+\Delta t)-z(t)$. Lecture 8 pp. 6–7 express Markov dependence as $$P(S_{t+\Delta t}\mid S_t,S_{t-1},S_{t-2},\ldots)=P(S_{t+\Delta t}\mid S_t).$$ Knowing the present makes the earlier path unnecessary for the conditional future law.</li><li>With $T=N\Delta t$, the lecture writes $$z(T)-z(0)=\sum_{i=1}^N\epsilon_i\sqrt{\Delta t}\sim N(0,T).$$ The $\epsilon_i$ are independent standard normals. Add variances, not SDs. [L8 pp. 20–21]</li></ul>'''
    section(9,'Expectation and covariance')['body']=section(9,'Expectation and covariance')['body'].replace('X_i','Y_i').replace('X_j','Y_j')
    section(9,'Local conditional moments')['body']=r'''<ul class="study-points"><li>Lecture 9 p. 25 writes $$dx=a(x,t)dt+b(x,t)dz.$$ Page 26 uses $W_t$ for the Brownian motion and makes the time index explicit: $$dx_t=a(x_t,t)dt+b(x_t,t)dW_t.$$ Both forms are retained here exactly as that page switch requires.</li><li>Freeze coefficients at the current state for a small step: $$E_t[\Delta x]\approx a(x_t,t)\Delta t,$$ $$\operatorname{Var}_t(\Delta x)\approx b^2(x_t,t)\Delta t.$$ These are generally local approximations; constant coefficients give exact finite-step moments.</li><li>As on p. 31, $E_t[Y]=E[Y\mid\mathcal F_t]$: information up to time $t$ is known. State/time coefficients define a Markov diffusion under the usual well-posedness assumptions. [L9 pp. 25–28, 31]</li></ul>'''
    section(9,'Mean reversion')['body']=r'''<ul class="study-points"><li>Lecture 9 p. 28 uses $$dx_t=\kappa(\theta-x_t)dt+\eta dz_t.$$ Here $\kappa>0$ is the speed, $\theta$ is the target and $\eta>0$ is diffusion. Drift is positive below $\theta$, zero at it and negative above it; noise remains.</li><li>For a small step, $E_t[\Delta x]\approx\kappa(\theta-x_t)\Delta t$ and $\operatorname{Var}_t(\Delta x)\approx\eta^2\Delta t$. Suggested Exercise 13 uses capital $X_t$ and $W_t$ instead; its question and solution keep those symbols.</li></ul>'''
    s=section(9,'Local conditional moments')
    s['body']=s['body'].replace('E_t[Y]=E[Y', 'E_t[X]=E[X')
    for title in ['Geometric Brownian motion','Correlated processes','Correlated normals']:
        s=section(9,title)
        def l9_math(value):
            value=value.replace('dW','dz').replace(r'\Delta W',r'\Delta z').replace('dX','dx').replace(r'\Delta X',r'\Delta x')
            if title=='Correlated normals':value=re.sub(r'\bU\b','u',re.sub(r'\bV\b','v',value))
            return value
        s['body']=in_math(s['body'],l9_math)
    s=section(9,'Geometric Brownian motion')
    s['body']=s['body'].replace('dS=\\mu Sdt+\\sigma Sdz','dS_t=\\mu S_tdt+\\sigma S_tdz_t').replace('dS/S=\\mu dt+\\sigma dz','dS_t/S_t=\\mu dt+\\sigma dz_t')
    s=section(9,'Euler simulation')
    s['body']=s['body'].replace(r'S_{i+1}=S_i(1+\mu\Delta t+\sigma\sqrt{\Delta t}\varepsilon_i)',r'S_{t_{k+1}}=S_{t_k}(1+\mu\Delta t+\sigma\sqrt{\Delta t}\varepsilon_k)')
    s['body']=s['body'].replace(r'X_{i+1}=X_i+a(X_i,t_i)\Delta t+b(X_i,t_i)\sqrt{\Delta t}\varepsilon_i',r'x_{t+\Delta t}\approx x_t+a(x_t,t)\Delta t+b(x_t,t)\sqrt{\Delta t}\varepsilon')
    s=section(9,'From an SDE to a calculation or simulated path')
    s['body']=s['body'].replace(r'X^+=',r'X_{t+1/12}\approx')
    s['body']=s['body'].replace(r'Monthly Euler factors for Q16 multiply successively: $S_1=100g_1$, $S_2=S_1g_2$, $S_3=S_2g_3$, where $g_i=1+.06/12+.2\varepsilon_i/\sqrt{12}$.',r'For Suggested Exercise 16, use $S_{i+1}=S_i(1+.06/12+.2\varepsilon_i/\sqrt{12})$ three times, taking the previous result as the next starting price.')
    s['body']=s['body'].replace('For $dX=', 'For Suggested Exercise 14, $dX=').replace('Draw independent $U,V$', 'Using Suggested Exercises 19–20 notation, draw independent $U,V$')
    section(9,'Reading simulation plots and preserving the model assumptions')['body']=section(9,'Reading simulation plots and preserving the model assumptions')['body'].replace('X_t','x_t')
    for e in exercises:
        for answer in e['answers']:
            answer['body']=explicit_max(answer['body']).replace('H=54','54')
    for i,item in enumerate(dependence):
        dependence[i]=tuple(supplement_notation(v) if isinstance(v,str) else v for v in item)
    # Replace glossary entries which previously merged the source conventions.
    replacements={
        r'D,D_{\rm cash}':(r'D,q','D: present value of known cash dividends (L4); q: continuous dividend yield (L7). The actual payment amount is stated separately.'),
        r'W_t,\Delta W,\varepsilon':(r'z(t),\Delta z,\epsilon','Lecture 8: Wiener level, increment, and standard normal shock.'),
        r'a(X,t),b(X,t)':(r'a(x,t),b(x,t)','Lecture 9: drift and diffusion; variance rate b². Its p. 26 writes x_t and W_t.'),
        r'\rho,U,V':(r'\rho,u,v','Lecture 9 p. 38: correlation and independent standard normals. Exercises 19–20 use U,V.'),
        r'x^+,\operatorname{Cov},\operatorname{Corr}':(r'\max(S_T-K,0),\operatorname{Cov},\operatorname{Corr}','Explicit call payoff as in the slides; covariance; covariance divided by both SDs.'),
        r'z(t),z_t,Z(t),dz':(r'W_t,X_t,U,V;\ Z(t)','Suggested exercises use W_t, X_t, U,V. The dependence supplement uses Z(t). Symbols are kept source-specific.'),
        r'H,A':(r'\Pi_u,\Pi_d','L7 p. 10: hedge portfolio values ΔS_u−f_u and ΔS_d−f_d. No extra H variable is required.')
    }
    notation[:]=[replacements.get(symbol,(symbol,meaning)) for symbol,meaning in notation]
    lectures[8]['sections'].insert(0,dict(title='Notation follows the page being reviewed',body=r'''<ul class="study-points"><li>L8 uses $z(t)$, $x$ and $\epsilon$. L9 p. 25 uses $dx=a(x,t)dt+b(x,t)dz$; p. 26 uses $x_t,W_t$; pp. 28–30 use $x_t,S_t,z_t$; p. 38 uses lowercase $u,v$.</li><li>Suggested exercises use $W_t,X_t,U,V$; the Brownian supplement uses $Z(t)$. Those source symbols stay in their own questions. Changing letters does not change the underlying concept, but this review does not substitute a new universal convention.</li></ul>'''))
