#from xwd_func import mainConv
from ms3 import spilter
# does this work in pypy? no?
import numpy as np
import sys, pickle, time
from nparr_redis import npbset
# i guess python is full of translation here. translating calls into simple reusable stubs.
# to redis.
def concat(a,b,c):
    # c is glue.
    n=np.concatenate((a,c),axis=0)
    n=np.concatenate((n,b),axis=0)
    return n

def concat_h(a,b,c):
    # c is glue.
    n=np.concatenate((a,c),axis=1)
    n=np.concatenate((n,b),axis=1)
    return n

def genline_h(a,b):
    return np.ones((a,1,b))

def genline(a,b):
    return np.ones((1,a,b))

with sys.stdin.buffer as f:
    # reading from stdin.
    img = np.array(pickle.load(f))
    x,_ = img.shape
    img = img.reshape(x,-1,3)    
#    img=mainConv(f)
    t0=time.time()
    s=spilter(img,(25,80))
    print("spilt timing: ",time.time()-t0)
    s0={str(k):s[k].copy() for k in s.keys()}
    npbset(s0,0)
