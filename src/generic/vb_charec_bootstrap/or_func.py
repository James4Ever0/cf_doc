from nparr_redis import rget, rsetex
from sm_func import get_table
from ms3 import gv1
# get bytes to string and to tuple?
# use eval? or safe eval.
from id_func import ethic
#import time
import ast
import numpy as np
import pickle, os
rph = "/dev/shm/ocf.pickle"
# get it into the pickle.
# use some magic.
def seval(a):
    try:
        if type(a)==bytes:
            a = a.decode()
            return ast.literal_eval(a)
        elif type(a) == str:
            return ast.literal_eval(a)
        else:
            return a
    except:
        return None
def rlogic(a,c,b=False):
    if b:
        if a > c:
            return a
        else:
            return c
    else:
        if a > c:
            return c 
        else:
            return a

def atrange(a,stdrange,b=5):
    xv=set([])
    c,d = a
    e,f = stdrange
    c0, d0 = rlogic(c-b,0,True),rlogic(d-b,0,True)
    c1, d1 = rlogic(c+b,e),rlogic(d+b,f)
    for x0 in range(c0,c1):
        for y0 in range(d0,d1):
            xv.add((x0,y0))
    return xv

def attension(a,stdrange,b = 5):
    # return candidates.
    f=set([])
    for x in a:
        x = seval(x)
#        c,d = x
        cd = atrange(x,stdrange,b)
        f = f.union(cd)
    return f

def getbuff():
    if os.path.exists(rph):
        with open(rph,"rb") as f:
            return pickle.loads(f.read())
    return None

def savebuff(a):
    with open(rph,"wb+") as f:
        f.write(pickle.dumps(a))
# you still need to double-check.

def strify(a,b=False):
    a=str(a)
    if b:
        return a
    else:
        return a.encode()

def ddiff(a,b,c,d=None):
    if d is None:
        d = lambda x: x
    e={}
    for x in c:
        if np.all(d(a[x]) == d(b[x])):
            pass
        else:
                # append that thing?
            e.update({x:(a[x],b[x])})
    return e if e != {} else None

def atdic(d,stdrange,b=5):
    ex = d.keys()
    ef = attension(ex,stdrange,b)
    return ef

# save to ram buffer.
def trusty(stdrange):
    # both are bytes. do not worry.
    k = rget("recent_key")
    tb = get_table()
    buff = getbuff()
    rp = buff is not None
    rg = rget("raw_reign")
    if not rp:
        rg = b"None"
    elif rg is None:
        rg = b"None"
    else:
        rg = pickle.loads(rg)
#    if len(buff) == 1:
#    print("rp",rp)
# use another range?
# you'd better see it all. otherwise you have to clean the reign.
# set it into the redis.
    if rp:
        if rg == b"None":
            k0 = ddiff(tb,buff,gv1(stdrange))
            #k0 = ddiff(tb,buff,gv1((25,80)))
        else:
            k0 = ddiff(tb,buff,[strify(xb) for xb in rg])
        if k0 is None:
            rg = b"None"
        else:
            rg = atdic(k0,stdrange)
            #print("roi",rg)
        #rg = atdic(k0,(25,80))
        # do things here.
    else:
        pass
    savebuff(tb)
    rg = pickle.dumps(rg)
    rsetex("raw_reign",rg)
#    print("k",k,"k0",k0)
        # it is saved. but this rp is what?
    if rp:
        return k,k0
    return None,None
# still need to store at somewhere?
# may you call me from the web?
#    keys, cons = dec_dict(tb)
#    hs = hashy(cons,h=False)
#    cod = {k:simCheck(tb[k],hs) for k in tb.keys()}
#    col = tuple(cod[k] for k in gv1((25,80)))
#    cos = ethic(pr,col)[0]
