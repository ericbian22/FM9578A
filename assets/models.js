(function(root){
function binomial(o){
 const {S,K,r,q=0,T,N,sigma,kind='call',style='european',underlying='stock'}=o;
 if(![S,K,r,q,T,N,sigma].every(Number.isFinite)||S<=0||K<=0||T<=0||sigma<=0||N<1||N>200||!Number.isInteger(N))throw Error('Use positive prices, volatility and time, with an integer N from 1 to 200.');
 const dt=T/N,u=Math.exp(sigma*Math.sqrt(dt)),d=1/u,a=underlying==='future'?1:Math.exp((r-q)*dt),p=(a-d)/(u-d),disc=Math.exp(-r*dt);
 if(!(p>0&&p<1))throw Error('No-arbitrage condition fails: require d < growth < u. Increase N or check inputs.');
 const payoff=s=>Math.max(kind==='put'?K-s:s-K,0),stocks=i=>Array.from({length:i+1},(_,j)=>S*u**j*d**(i-j));
 let s=stocks(N);
 if(s.some(x=>!Number.isFinite(x)||x<=0)||!Number.isFinite(disc))throw Error('Inputs exceed the numerical range of this tree. Reduce volatility, horizon or rate magnitude.');
 let v=s.map(payoff),levels=[{i:N,stocks:s,values:[...v]}];
 for(let i=N-1;i>=0;i--){s=stocks(i);const continuation=Array.from({length:i+1},(_,j)=>disc*((1-p)*v[j]+p*v[j+1]));const exercise=s.map(payoff);v=continuation.map((c,j)=>style==='american'?Math.max(c,exercise[j]):c);levels.push({i,stocks:s,values:[...v],continuation,exercise});}
 levels.reverse();const slope=(levels[1].values[1]-levels[1].values[0])/(levels[1].stocks[1]-levels[1].stocks[0]);
 const delta=slope*(underlying==='future'?1:Math.exp(-q*dt));
 const exerciseNow=style==='american'&&levels[0].exercise[0]>levels[0].continuation[0]+1e-10;
 if(![v[0],slope,delta].every(Number.isFinite))throw Error('Inputs exceed the numerical range of this tree.');
 return {price:v[0],p,u,d,a,dt,delta,slope,exerciseNow,levels};
}
function payoff(s,k,w,kind){const c=x=>Math.max(s-x,0),p=x=>Math.max(x-s,0);
 return ({call:()=>c(k),put:()=>p(k),straddle:()=>c(k)+p(k),bull:()=>c(k)-c(k+w),bear:()=>p(k+w)-p(k),strangle:()=>p(k)+c(k+w),butterfly:()=>c(k)-2*c(k+w)+c(k+2*w),covered:()=>s-c(k),protective:()=>s+p(k),strip:()=>c(k)+2*p(k),strap:()=>2*c(k)+p(k)})[kind]();
}
function brownian(T,rho,seed,N=160){
 if(![T,rho,seed].every(Number.isFinite)||T<=0||T>20||Math.abs(rho)>1)throw Error('Use 0 < T ≤ 20 and −1 ≤ correlation ≤ 1.');
 let state=seed>>>0;const uniform=()=>{state=(1664525*state+1013904223)>>>0;return (state+.5)/4294967296};
 const normal=()=>Math.sqrt(-2*Math.log(uniform()))*Math.cos(2*Math.PI*uniform());
 let x=0,y=0;const rows=[[0,0,0]],dt=T/N;
 for(let i=1;i<=N;i++){const u=normal(),v=normal();x+=Math.sqrt(dt)*u;y+=Math.sqrt(dt)*(rho*u+Math.sqrt(1-rho*rho)*v);rows.push([i*dt,x,y]);}return rows;
}
const api={binomial,payoff,brownian};root.Models=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
