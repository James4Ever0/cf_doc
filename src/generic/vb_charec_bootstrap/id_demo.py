a,b = "abcde", "bcdef"
a,b = a*20, b*20
b = "random stuff of unrelated shits"+b
b = b*2
# fuzzy logic.
# what is repeating anyway?
import numpy as np
def uniq(a):
    # start with 0.
    i = 0
    d={}
    k=[]
    for x in a:
        if x in d.keys():
            pass
        else:
            d.update({x:i})
            i+=1
        k.append(d[x])
    return np.array(k),d

def du(a):
    return np.diff(a)

def ethic(a,b,c=True):
    # slide the b.
    ad, _ = uniq(a)
    N = len(a)
    N0 = N-1
    ln = len(b)-N0
    if not c:
        for x in range(ln):
            bn = b[x:x+N]
            bd, _ = uniq(bn)
#            print("x",x,"bd",bd)
            if np.all(ad == bd):
            # check all possible match? maybe later.
                return bn
        return None
    else:
        can = []
        preb = 0
        for x in range(ln):
            xpreb = x+preb
            if xpreb<ln:
                bn = b[xpreb:xpreb+N]
                bd, _ = uniq(bn)
                if np.all(ad == bd):
                # must skip.
                    preb+=N0
                    can.append(bn)
            else:
                break
        return can 

print(ethic(a,b,False))
print(ethic(a,b))
# find the exact match. using what?
# i mean it is what? learning to forget?
