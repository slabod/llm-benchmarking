# Synthetic A/B task with a hidden SRM + Simpson's paradox (seeded, reproducible).
import numpy as np, pandas as pd, math
rng=np.random.default_rng(20261020)
N=400_000
strata=[('android','old',0.30,0.020),('android','new',0.40,0.050),('ios','any',0.30,0.060)]
EFFECT=-0.02      # true relative effect of the new checkout screen in every stratum
DROP_TEST_ANDROID_OLD=0.30   # exposure-logging bug: 30% of test users on old Android versions are not logged
rows=[]
uid=0
for plat,ver,share,base in strata:
    n=int(N*share)
    grp=rng.integers(0,2,n)            # 0 control, 1 test (50/50 by user hash)
    p=np.where(grp==1, base*(1+EFFECT), base)
    sessions=rng.poisson(3.0,n)+1
    orders=rng.binomial(1,p)
    keep=~((grp==1)&(rng.random(n)<DROP_TEST_ANDROID_OLD)) if (plat,ver)==('android','old') else np.ones(n,bool)
    if plat=='android':
        vers=np.where(ver=='old', rng.choice(['6.8','6.9','7.0'],n), rng.choice(['7.1','7.2','7.3'],n))
    else:
        vers=rng.choice(['7.1','7.2','7.3'],n)
    for g,s,o,v,k in zip(grp,sessions,orders,vers,keep):
        if k:
            rows.append((uid,'test' if g else 'control',plat,v,int(s),int(o)))
        uid+=1
df=pd.DataFrame(rows,columns=['user_id','group','platform','app_version','sessions','converted'])
df=df.sample(frac=1,random_state=7).reset_index(drop=True)
df.to_csv('experiment_users.csv',index=False)
def z2(a,b):
    p1=a.converted.mean();p2=b.converted.mean();n1=len(a);n2=len(b);p=(a.converted.sum()+b.converted.sum())/(n1+n2)
    se=math.sqrt(p*(1-p)*(1/n1+1/n2));z=(p2-p1)/se;pv=math.erfc(abs(z)/math.sqrt(2))
    return p1,p2,(p2/p1-1),z,pv
c=df[df.group=='control'];t=df[df.group=='test']
print('n control',len(c),'n test',len(t),'test share',len(t)/len(df))
chi=( (len(c)-len(df)/2)**2+(len(t)-len(df)/2)**2 )/(len(df)/2); print('SRM chi2',chi,'p',math.erfc(math.sqrt(chi/2)))
print('aggregate: ctl %.4f test %.4f rel %+.3f z %.2f p %.4f'%z2(c,t))
for (plat,old),g in df.assign(old=df.app_version.isin(['6.8','6.9','7.0'])).groupby(['platform','old']):
    cc=g[g.group=='control'];tt=g[g.group=='test']
    print(plat,'old' if old else 'new', len(cc),len(tt),'ctl %.4f test %.4f rel %+.3f z %.2f p %.3f'%z2(cc,tt))
