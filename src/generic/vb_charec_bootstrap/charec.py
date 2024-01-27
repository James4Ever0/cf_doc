# charec stub. for quickly parsing console optical chars.
#     
#      [console chars] -----------------
#      /            \                   \
# [inside-chars]   [outside-chars]   [ASCII/Console Art]
#     |                        |              |
# [can be gen with keyboard] [non-ascii?]  [Merge ROI] 
#     |                        |              |
# [type/store/rec]  <-     [DL/tesseract]-----/

# when name is unknown, we can use statistics to find similarities.
# we'll assign random name to random templates.
# or just a special name. even hash.

import redis
import numpy as np
from ms3 import spilter

# similarity check
# maybe shall know about the location of chars?
# or recheck?

def cyber_whale(a,s=1):
    # the shape.
    s*=a[0]
    if len(a)==1:
        return s 
    else:
        return cyber_whale(a[1:],s)

def sum_all(n):
    l = len(n.shape)
    for x in range(l):
        n=sum(n)
    return n

def fsum(n):
    return np.sum(n.flatten())

def sim(a,b,c=0.998):
    nr = fsum(a == b)
    cy = cyber_whale(a.shape)
    return np.all((nr/cy) > c)
"""
def checkCode(y):
    return tuple(int(x) for x in bin(y)[2:])
"""
def checkCode(y):
    base_list=[()]
    for d in range(y):
        base_list=[(*z,x) for z in base_list for x in range(2)]
    return base_list

def sparse(x):
    base_list=[()]
    blist = checkCode(x)
    # this is not the way to do it?
    # nope this is not.
    for d in range(2):
        # it is about y.
        base_list = [(*z,*y) for z in base_list for y in blist]
    return base_list

def roundme(a,x):
    return a[:x]

def rcomp(a,b):
    x=min(len(a),len(b))
    return roundme(a,x)==roundme(b,x)

def s2p(a):
    s=int(len(a)/2)
    return a[:s],a[s:]

def r2comp(a,b):
    a0,a1 = s2p(a)
    b0,b1 = s2p(b)
    return rcomp(a0,b0) and rcomp(a1,b1)

# rounding algorithm.
# check and update? assign random names? randomly picking shits up?
# you can have microname.
