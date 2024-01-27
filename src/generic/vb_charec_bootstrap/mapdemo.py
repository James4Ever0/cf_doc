import numpy as np
# mark with 1d 2d 3d and so on? inter-relationship.
# use eval or nothing will happen.
# extract sparse matrix?
import random
import itertools, time

rng = random.SystemRandom()

def csampler(keys,max_sample=200):
    pm = list(itertools.combinations(keys,r=2))
    if len(pm) > max_sample:
        # use generator instead?
        pm = rng.sample(pm,max_sample)
    return pm

def cprec(lk,l=0):
    if l == 0:
        lk -=1
    if lk>0:
        return cprec(lk-1,l+lk)
    else:
        return l

def tsort(a,b):
    if (hash(a)>hash(b)):
        return (a,b)
    else:
        return (b,a)

def nograt(keys,lk,prev):
    # what about previous permutations?
    # do it later: random pop?
    r = np.random.permutation(keys)
    r = [tsort(tuple(r[x]),keys[x]) for x in range(lk)]
    r = filter(lambda x: not np.array_equal(x[0],x[1]),r)
    prev = prev.union(set(r))
    return prev
# never know the upper bound.

# this is slow.
def cs_mp(keys,max_sample=200):
    # first, calculate the need for doing this.
    lk = len(keys)
    cp = cprec(lk)
    ip = int(2*max_sample/3)
    idx = lk < ip
    if cp > max_sample:
        prev = set([])
        while len(prev)<max_sample:
            if idx:
                prev = nograt(keys,lk,prev)
            else:
                prev = nograt(rng.sample(keys,ip),lk,prev)
        for x in range(len(prev) - max_sample):
            prev.pop()
        return list(prev)
    else:
        return csampler(keys,max_sample)

def genkey(tup):
    # check args length?
    # max recursion 3?
    base_list=[()]
    for x in range(len(tup)):
        base_list = [(*z,y) for z in base_list for y in range(tup[x])]
    return base_list

def recget(a,x):
    tar = a
    for z in x:
        tar = tar[z]
    return tar

# better use this in pypy? but how? use separate process or one single process? 
"""
a = np.array([0,0,0])
b = np.array([0,1,1])
e = np.array([1,1,1])
d = np.array([0,0,1])
c = np.array([0,0,1])
"""


# generate sparse matrix for individual pixels.
# group them together.
def tgen(lst,a):
    shape = a.shape
    keys = genkey(shape)
    typegen= {k:{0:[],1:[]} for k in keys}
    for k in lst.keys():
        f=lst[k]
        for x in keys:
            y=recget(f,x)
            typegen[x][y].append(k)
    return typegen

lst = [np.array([x,y,z,e,f,g,h,i,j,k]) for x in range(2) for y in range(2) for z in range(2) for e in range(2) for f in range(2) for g in range(2) for h in range(2) for i in range(2) for j in range(2) for k in range(2)]
lst = [np.array([x,y]) for x in lst for y in lst]
a=lst[0]
lst = {"a_{}".format(k): lst[k] for k in range(len(lst))}
#lst = {"a":a,"b":b,"c":c,"d":d,"e":e}
typegen=tgen(lst,a)
#print(typegen)
ashp=genkey(a.shape)
t0=time.time()
cs = cs_mp(ashp,max_sample=5000)
# still slower when not big enough.
print(cs,time.time()-t0)
t0=time.time()
# still slow?
cs = csampler(ashp,max_sample=5000)
print(cs,time.time()-t0)
# how do you map the logic? random plots?
"""
print(keys)
# use these keys to get data!
for dx in lst:
    for x in keys:
        print(x,recget(dx,x))
"""
# classify these things by what? better use a dict.
# a recursive function?

