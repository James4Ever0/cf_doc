def combine(b):
    f=list(filter(lambda x:x['fd']==0,b))
    f0=list(filter(lambda x:x['fd']!=0,b))
    return f,f0
#fuck efficiency.
import random
rng=random.SystemRandom()
def still(a):
    return list(map(lambda x:x['data'],a))

def flat(a):
    return "\x00".join([b.decode() for b in a])

def comb(a):
    c,d=combine(a)
    return {flat(still(c)):still(d)}

from byte_compare import given_array as func

def tailer(a):
    t=func(a)
    return t

def reform(h):
    y={}
    for x in h:
        y.update(x)
    return y

def merge_dict(a,b):
    bk=list(b.keys())
    for k in a.keys():
        if k in bk:
            b[k]+=a[k]
        else:
            b.update({k:a[k]})
    return b
import statistics as math

def hascode(a,b):
    return len(a.intersection(b))>0

def getjob(a):
    a0=[a[x] for x in a.keys()]
    a1=set([])
    for x in a0:
        a1.update(x)
    return a1

def hashope(a,b):
    a0,b0=getjob(a),getjob(b)
    return hascode(a0,b0)

def enf(f):
    #print('start',f)
    prev,pk=None,None
    dx,dy=[],[]
    for x in range(len(f)):
        #print('loop',x)
        x0=f[x]
        x0=[(k,x0[k]) for k in x0.keys()]
        if len(x0)==0 or x == len(f)-1:
            #print('here')
            if len(f)==1:
                x0=list(x0)[0]
                pk,prev=x0
                dx+=[pk]
                dy+=[len(prev)]
            return dx,dy
        x0=reversed(sorted(x0))
        if prev is not None:
            if hashope(f[x-1],f[x]):
                i=False
                for k,y in x0:
                    #print(k,y)
                    h=hascode(prev,y)
                    if h:
                        prev,pk=y,k
                        dx+=[k]
                        dy+=[len(y)]
                        #print(dx,dy)
                        i=True
                        continue
                if i:
                    continue
                else:
                    #print('pop')
                    f[x-1].pop(k)
                    return enf(f)
            else:
                #print('hopeless')
                return dx,dy
        else:
            x0=list(x0)[0]
            pk,prev=x0
            dx+=[pk]
            dy+=[len(prev)]
    return dx,dy

def rush(b,enforce=True):
    f=min([len(x) for x in b])
    if not enforce:
        df=[]
        dy=[]
        for x in range(f):
            st=[k[x] for k in b]
            sv=set(st)
            sd={k:st.count(k) for k in sv}
            sm=max([sd[k] for k in sd.keys()])
            dy.append(sm)
            sp=[k for k in sd.keys() if sd[k]==sm]
            sg=len(sp)
            sk=None
            if sg>1:
                sk=rng.choice(sp)
            else:
                sk=sp[0]
            df.append(sk)
        return df, math.mean(dy)
    else:
        f0=[]
        for x in range(f):
            st=[k[x] for k in b]
            sd=set(st)
            sp={k:set([v for v in range(len(st)) if st[v]==k]) for k in sd}
            f0.append(sp)
        df,dy= enf(f0)
        #print(df,dy)
        return df, math.mean(dy)

def pdict(a,enforce=True):
    for k in a.keys():
        b=a[k]
        a[k]=rush(b,enforce)
    return a

def getSingleSession(a):
    fb,bf=[],[]
    for b in a:
        fd=b['fd']
        if fd == 0:
            #print(b)
            if bf!=[]:
                fb.append(bf)
            bf=[b]
        else:
            bf.append(b)
    fb.append(bf)
    # here.
    h=list(map(lambda x:comb(x),fb))
    h=reform(h)
    #print(h)
    for x in h.keys():
        dx=h[x]
        hd={}
        #print(dx)
        for z in dx:
            t=tailer(z)
            merge_dict(t,hd)
        #phd=pdict(hd,enforce=False)
        phd=pdict(hd,enforce=True)
        print(phd)
            #print(t)
        '''t=tailer(dx)
        print(t)'''
    return fb
# logical cluster.
# do we need time cluster?

