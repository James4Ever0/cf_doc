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

def ethic(a,b,c=True,mix=0.7,filter_num = 3):
    # slide the b.
    ad, _ = uniq(a)
    N = len(a)
    N0 = N-1
    ln = len(b)-N0
    if not c:
        for x in range(ln):
#            print("iteration",x)
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
#            print("iteration",x)
            xpreb = x+preb
            if xpreb<ln:
                bn = b[xpreb:xpreb+N]
                bd, _ = uniq(bn)
                nr = (ad == bd)
                snr = sum(nr)
#                if snr > N*0.7:
#                    print("expected",N,"actual",snr,"max",len(nr))
                if snr > N*mix:
                # must skip.
                    preb+=N0
                    # append the value instead? floating point.
                    can.append((bn,-snr/N))
            else:
                break
        fn = sorted(can,key = lambda x: x[1])
        kan = []
        for x in fn:
            if filter_num>0:
                kan.append(x[0])
                filter_num-=1
            else:
                break
        return kan
