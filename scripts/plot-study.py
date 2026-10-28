"""Regenerate labelled lecture graphs (Matplotlib; SVG assets are committed)."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/plotting'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from content import tree

OUT=ROOT/'assets/graphs';OUT.mkdir(parents=True,exist_ok=True)
GREEN='#276a57';AMBER='#bf812a';BLUE='#426f9a';INK='#183f35'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.color':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#a3b7aa','axes.grid':True,'grid.color':'#e2e9df','grid.alpha':.8,'svg.fonttype':'none','savefig.facecolor':'white'})
def save(fig,name):
    fig.savefig(OUT/name,format='svg',bbox_inches='tight',metadata={'Creator':'FM9578A course review','Date':None})
    plt.close(fig)
def labels(ax,x='Terminal stock price',y='Payoff per unit'):
    ax.set_xlabel(x);ax.set_ylabel(y);ax.axhline(0,color='#8a9d90',lw=.8);ax.set_axisbelow(True)

s=np.linspace(20,80,401);K=50
fig,axes=plt.subplots(1,2,figsize=(10,3.4),layout='constrained')
for ax,title,pay,be in [(axes[0],'Long call',np.maximum(s-K,0),54),(axes[1],'Long put',np.maximum(K-s,0),46)]:
    ax.plot(s,pay,color=GREEN,lw=2.4,label='Payoff');ax.plot(s,pay-4,color=AMBER,lw=2.4,ls='--',label='Profit (premium 4)')
    ax.axvline(K,color='#b8c5b8',ls=':',lw=1);ax.scatter([be],[0],color=AMBER,zorder=4);ax.annotate('Break-even '+str(be),(be,0),xytext=(be+2,6),arrowprops={'arrowstyle':'->','color':AMBER},fontsize=9)
    ax.set_title(title+' · K = 50');labels(ax,y='Payoff / profit');ax.legend(fontsize=9)
save(fig,'payoff-profit.svg')
fig,ax=plt.subplots(figsize=(8,3.6),layout='constrained')
ax.plot(s,np.maximum(s-50,0)+50,color=GREEN,lw=4,label='Call + bond paying 50')
ax.plot(s,s+np.maximum(50-s,0),color=AMBER,lw=2,ls='--',label='Stock + put')
ax.axvline(50,color='#b8c5b8',ls=':');ax.annotate('Same payoff in every state',(60,60),xytext=(24,73),arrowprops={'arrowstyle':'->','color':INK},fontsize=10)
labels(ax,y='Portfolio value at expiry');ax.set_ylim(43,83);ax.legend(loc='lower right',fontsize=9)
save(fig,'parity.svg')
s=np.linspace(30,90,501)
fig,axes=plt.subplots(2,2,figsize=(10,6),layout='constrained')
payoffs=[('Bull call: strikes 50, 70',np.minimum(np.maximum(s-50,0),20)),('Bear put: strikes 50, 70',np.minimum(np.maximum(70-s,0),20)),('Butterfly: strikes 50, 60, 70',np.maximum(s-50,0)-2*np.maximum(s-60,0)+np.maximum(s-70,0)),('Straddle: strike 60',abs(s-60))]
for ax,(title,pay) in zip(axes.flat,payoffs):
    ax.plot(s,pay,color=GREEN,lw=2.5);ax.set_title(title,fontsize=11);labels(ax);ax.set_xticks([30,50,60,70,90])
save(fig,'strategies.svg')
r=tree(20,21,.04,.5,2,u=1.1,d=.9)
fig,ax=plt.subplots(figsize=(9,4.1),layout='constrained')
for i in range(2):
    for j in range(i+1):
        for nxt in [j,j+1]:
            ax.annotate('',xy=(i+1,2*nxt-(i+1)),xytext=(i,2*j-i),arrowprops={'arrowstyle':'->','color':'#a6b9ac','lw':1.5,'shrinkA':45,'shrinkB':45})
for level in r['levels']:
    i=level['i']
    for j,(stock,value) in enumerate(zip(level['stocks'],level['values'])):
        ax.text(i,2*j-i,'S = '+format(stock,'.2f')+'\nf = '+format(value,'.4f'),ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.55','facecolor':'#edf3e8','edgecolor':GREEN})
ax.set_xlim(-.45,2.55);ax.set_ylim(-2.65,2.65);ax.set_xticks([0,1,2],['Today','3 months','6 months']);ax.set_yticks([]);ax.grid(False)
ax.set_title('Two-step European call · K = 21, r = 4%, p = 0.550251',pad=14)
ax.set_xlabel('Underlying moves →     •     ← Value the option backward')
save(fig,'binomial-tree.svg')
r=tree(50,52,.05,2,2,u=1.2,d=.8,put=True,american=True)
level=r['levels'][1];x=np.arange(2);fig,ax=plt.subplots(figsize=(8,3.6),layout='constrained')
a=ax.bar(x-.18,level['continuation'],width=.36,color=GREEN,label='Continue');b=ax.bar(x+.18,level['exercise'],width=.36,color=AMBER,label='Exercise')
ax.bar_label(a,fmt='%.4f',padding=4,fontsize=10);ax.bar_label(b,fmt='%.0f',padding=4,fontsize=10);ax.set_xticks(x,['Stock = 40\nChoose exercise','Stock = 60\nChoose continuation']);ax.set_ylabel('Put value at the intermediate node');ax.set_ylim(0,14);ax.legend();ax.set_axisbelow(True)
save(fig,'american-exercise.svg')
t=np.linspace(0,4,301);fig,axes=plt.subplots(1,2,figsize=(10,3.4),layout='constrained')
for ax,y,title,col in [(axes[0],t,'Variance = T',GREEN),(axes[1],np.sqrt(t),'Standard deviation = √T',AMBER)]:
    ax.plot(t,y,color=col,lw=2.5);ax.set_title(title);ax.set_xlabel('Time T (years)');ax.set_ylabel('Variance' if col==GREEN else 'Standard deviation');ax.scatter([.25,1,4],[.25,1,4] if col==GREEN else [.5,1,2],color=col)
save(fig,'brownian-scaling.svg')
fig,ax=plt.subplots(figsize=(8,2.8),layout='constrained')
ax.axvspan(2,3,color='#f3dfb5',alpha=.9,label='Shared interval: length 1')
ax.plot([1,3],[1,1],color=GREEN,lw=9,solid_capstyle='round')
ax.plot([2,4],[0,0],color=BLUE,lw=9,solid_capstyle='round')
ax.set_yticks([0,1],['W₄ − W₂','W₃ − W₁']);ax.set_xticks(range(6));ax.set_xlim(0,5);ax.set_ylim(-.5,1.8);ax.set_xlabel('Time');ax.set_title('Overlap produces covariance: Cov = 1');ax.legend(loc='upper right',fontsize=9)
save(fig,'increment-overlap.svg')
vals=[100.]
for z in [.5,-1.2,.8]:vals.append(vals[-1]*(1+.06/12+.2/np.sqrt(12)*z))
fig,ax=plt.subplots(figsize=(8,3.8),layout='constrained');ax.plot(range(4),vals,'o-',color=GREEN,lw=2.3)
for i,v in enumerate(vals):ax.annotate(format(v,'.4f'),(i,v),xytext=(0,12),textcoords='offset points',ha='center',fontsize=10)
for i,z in enumerate([.5,-1.2,.8]):ax.text(i+.5,(vals[i]+vals[i+1])/2-1,'ε = '+str(z),ha='center',color=AMBER,fontsize=10)
ax.set_xticks(range(4));ax.set_xlabel('Month');ax.set_ylabel('Stock price');ax.set_ylim(93.5,107);ax.set_title('Q16 · Monthly Euler path with the supplied shocks')
save(fig,'euler-path.svg')
print('Generated 8 labelled SVG study graphs.')

