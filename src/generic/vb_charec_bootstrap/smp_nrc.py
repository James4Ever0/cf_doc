# direct compare or else?
# make these chars unique!
# so you do not use keys?
from charec import s2p

def re2(a):
    l=len(a)
    return sum([a[l-d-1]*(d**2) for d in range(l)])

def spv2(a,b,c=3):
    b0=int(len(b[0])/2)
    x,y = b0,b0
    xd,yd = a.shape[:2]
#    print(a.shape)
    xp,yp=int(xd/x),int(yd/y)
    d={}
    if c == 3:
        for vt in b:
            x0, y0 = s2p(vt)
            x0, y0 = re2(x0), re2(y0)
            x1=x0+1
            y1=y0+1
            xv0,xv1=x0*xp,x1*xp
            yv0,yv1=y0*yp,y1*yp
            d.update({vt:a[xv0:xv1,yv0:yv1,:]})
    elif c == 2:
        for vt in b:
            x0, y0 = s2p(vt)
            x0, y0 = re2(x0), re2(y0)
            x1=x0+1
            y1=y0+1
            xv0,xv1=x0*xp,x1*xp
            yv0,yv1=y0*yp,y1*yp
            d.update({vt:a[xv0:xv1,yv0:yv1]})
    elif c == 4:
        for vt in b:
            x0, y0 = s2p(vt)
            x0, y0 = re2(x0), re2(y0)
            x1=x0+1
            y1=y0+1
            xv0,xv1=x0*xp,x1*xp
            yv0,yv1=y0*yp,y1*yp
            d.update({vt:a[xv0:xv1,yv0:yv1,:,:]})
    elif c == 5:
        for vt in b:
            x0, y0 = s2p(vt)
            x0, y0 = re2(x0), re2(y0)
            x1=x0+1
            y1=y0+1
            xv0,xv1=x0*xp,x1*xp
            yv0,yv1=y0*yp,y1*yp
            d.update({vt:a[xv0:xv1,yv0:yv1,:,:,:]})
    elif c == 6:
        for vt in b:
            x0, y0 = s2p(vt)
            x0, y0 = re2(x0), re2(y0)
            x1=x0+1
            y1=y0+1
            xv0,xv1=x0*xp,x1*xp
            yv0,yv1=y0*yp,y1*yp
            d.update({vt:a[xv0:xv1,yv0:yv1,:,:,:,:]})
    else:
        print("NOT IMPLEMENTED DIMENSION",c)
        # not implemented
        return None
    return d

def verdec(r=0,a=0.98,b=0.01):
    return a-b**(-r)

# collect unique chars first!

import random
rng = random.SystemRandom()


from charec import sparse
import redis
#from charec import cyber_whale 

rsr=redis.StrictRedis(host='localhost', port=6379, decode_responses=False)

import pickle
# must-same: same key with same time?
# but that's deduction.
can=[]
import numpy as np
for x in rsr.keys():
    try:
        pr = pickle.loads(rsr[x])
#        print(x)
#        full = cyber_whale(pr.shape)
#        print(full,np.count_nonzero(pr))
#        print(type(pr),pr.shape,np.max(pr),np.mean(pr),np.count_nonzero(pr)/full)
        can.append(pr)
    except:
        print("wrong keys again")

col = {}
for x in can:
    v=x.shape
    if v in col.keys():
        col.update({v:col[v]+1})
    else:
        col.update({v:1})
px = [(v,col[v]) for v in col.keys()]
#print(px)
from charec import sim
import uuid
def uuid_gen():
    return str(uuid.uuid4())

px = sorted(px,key=lambda x: -x[1])
py = None
for x in px:
    py = x[0]
    break
print(py)
col = list(filter(lambda x: x.shape == py, can))
# use timing.
# there might be hash collisions. so check this.
# hash is not quite sure about this.
def hashy(col,h=True,c=0.9):
    cov = {}
    if h:
        for d in col:
            tr = False
            for z in cov.keys():
                tr = sim(d,cov[z],c=c)
                if tr:
                    break
            if tr:
                continue
            else:
                cov.update({uuid_gen():d})
    else:
        for d in col:
            tr = False
            for z in cov.keys():
                tr = sim(d,cov[z],c=c)
                if tr:
                    break
            if tr:
                continue
            else:
                cov.update({hash(d.tobytes()):d})
    return cov
# this is quick enough, but not there yet.
from ms3 import spilter
# determine the size.
# map to 0 and 1.
import math
def msort(a,b):
    if a>b:
        return (a,b)
    else:
        return (b,a)
# you can use tesseract in the back. hash function as the first step.
# to eliminate uncertainty.
# dl algorithm has that quantum thing. use it as the TRUST thing.
def gaf(n):
    assert type(n)==int and n>0
    factors=[]
    fv = []
    m = math.ceil(math.sqrt(n)+0.1)
    for i in range(1,m+1):
        if n%i == 0:
            p = n//i
            if p > i:
                factors.append(i)
            elif p==i:
                pass
            else:
                continue
            fv[0:0]=[p]
#    print("factors",factors,"fv",fv)
    factors += fv
#            factors.append(msort(n,n/n))
    return factors
#    return list(map(lambda x: x,set(factors)))

def granulizer(s):
    # s is the shape.
    # find something in common?
    # sort those things.
    a,b = s[:2] # 0 for smallest piece, 1 for biggest piece.
    def res0(mp):
        a0,b0=gaf(int(a)),gaf(int(b))
#        print(a0,b0)
        a1,b1=len(a0)-1,len(b0)-1
        return (int(a0[math.ceil(mp*a1)]), int(b0[math.ceil(mp*b1)]))
    return res0

def proadd(a,b,c):
    for k in a.keys():
#        print(k,b)
        b[k][int(a[k])].update([c])
    return b
def jit_inv(a):
    bitch = {}
    # x in the location.
    for x in a.keys():
        for y in (0,1):
            if len(a[x][y])>0:
                c,d = frozenset(a[x][y]) , [(x,y)]
                try:
                    bitch[c]+=d
                except:
                    bitch[c]=d
    return bitch

def tst_m(a,b,m=3):
    l = len(b)
    if l<m:
        return sum([a[x[0]] == x[1] for x in b]) == l
    else:
        c = rng.sample(b,m)
        return sum([a[x[0]] == x[1] for x in c]) == m

def dream_func(a,b,m = 3):
    # b is the inv_dict.
    # generate relationships between these keys?
    bk = [frozenset(x) for x in b.keys()]
    rng.shuffle(bk)
    #print("bk",bk)
    # remove the non-key.
    # these are all sets.
    fk = None
#    while len(bk)>0:
    for fc in bk:
#        fc = rng.choice(range(len(bk)))
#        fc = bk.pop(0)
#        fc = frozenset(fc)
        if fk is None:
            if tst_m(a,b[fc],m):
        # passed!
                if len(fc)==1:
                    return set(fc).pop()
                else:
                    fk = fc
            else:
                pass
        else:
            fd = fk.intersection(fc)
            if len(fd)==0:
                continue
            elif tst_m(a,b[fc],m):
                # must check.
                if len(fd)==1:
                    return set(fd).pop()
                else:
                    fk = fd
    return fk
        # get all possible sections.
        # careful about impossible things.
            # test both?
            # must exist.
    # a must be inverted.
#    inv = jit_inv(a)

def choky(col,gua=0.3, snach=0.5, min_try = 3,h0=True ,c0=0.9):
    bk = np.array(col).flatten()
    mx,mn = max(bk), min(bk)
    threash = snach*mx + mn
    shp = granulizer(col[0].shape)(gua)
    cod = {}
    cov = {}
    jcod = None
#    changed = False
#    buf_new = None
#    buf_init = None
    for x in col:
#        print(shp)
        sk = spilter(x,shp)
        sk = {k:np.mean(sk[k].flatten())>threash for k in sk.keys()}
        if cov == {}:
            # init the thing!
            ky = hash(x.tobytes())
            cov.update({ky:x})
            cod = {k:{0:set([]),1:set([])} for k in sk.keys()}
            cod = proadd(sk,cod,ky)
            jcod = jit_inv(cod)
            # there's a buffer.
            # got to buffer this?
            # this is predefined thing?
#            buf_init = x.copy()
#            buf_new = (ky,sk)
# do not hash small pieces?
        else:
            drm = dream_func(sk,jcod,3)
            if drm is None:
                ky = hash(x.tobytes())
                # but we're using hash!
                cov.update({ky:x})
#                sk = spilter(x,shp)
                cod = proadd(sk,cod,ky)
                jcod = jit_inv(cod)
                # add new things here.
            else:
                if type(drm) == frozenset:
                    drm = list(drm)
                else:
                    drm = [drm]
                tr = False
                for drx in drm:
                    buf_init = cov[drx]
#                print("closet approach", drm)
                # there's no such thing.
                # or yes? get the closet approach.
                    # add things here.
                    tr = sim(buf_init,x,c0)
                    if tr:
#                        print("duplication found!")
                        # still inaccurate!
                        # and slow as hell!
                    # duplicate.
                    # trust the first deduction.
                    # conflict? then either error or add to registry.
                        break
                if not tr:
                    ky = hash(x.tobytes())
                    cov.update({ky:x})
#                    sk = spilter(x,shp)
                    cod = proadd(sk,cod,ky)
                    jcod = jit_inv(cod)
    return threash, shp, cod, cov ,jcod
                    # non-zero filter?
                    # not!
                # use base compare? or use buffer. verify from three pieces?
            # do the thing. checking?
            # this is really weird. damn.
import time
g0 = time.time()
g = hashy(col,h=False)
print("hashy:",time.time()-g0,len(g))
g1 = time.time()
threash,shp,cod,cov,jcod= choky(col,gua =0.6)
# this is a bad choice. better not to write anything from scratch. train a network instead. see if new candidates are welcomed.
print("chocky:",time.time()-g1,len(cov))

# get hash first, then we get the code.
def hashCheck(a,b):
    try:
        k = hash(a.tobytes())
        # do hash.
        for x in b.keys():
            if x == k:
                return k
        # not return shit.
    except:
        return None

def simCheck(a,b):
    for k in b.keys():
        b0 = b[k]
        s=sim(a,b0)
        if s:
            return k
    return None
#import numba
#@numba.jit
def s2Check(a,cov,jcod,shp,threash):
    sk = spilter(a,shp)
    sk = {k:np.mean(sk[k].flatten())>threash for k in sk.keys()}
    b = dream_func(sk,jcod,3)
    if b is None:
        return None
    else:
        if not type(b) == frozenset:
            b=[b]
        print("len of candidates",len(b))
        # how the fuck?
        for x in b:
#            print("x",x)
            s=sim(a,cov[x])
            if s:
                return x
    return None

rk = rng.choice(col)
t0 = time.time()
x = hashCheck(rk,g)
print("hashCheck",time.time()-t0,x)
t0 = time.time()
x = simCheck(rk,g)
print("simCheck",time.time()-t0,x)
t0 = time.time()
x = s2Check(rk,cov,jcod,shp,threash)
print("s2Check",time.time()-t0,x)
# so my method is the worst one. I've got it.
    # naive approach
    # hash is fast. anyway do that if you can?
# but we are going to check the thing!
#for x in col:
#    if x.shape == py:
        # do work?
# i know there are shits.
    # collect default shape.
    # no cannot use something like that.
    # check these things.
# what to do after loading?

