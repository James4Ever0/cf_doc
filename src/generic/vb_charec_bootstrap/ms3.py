import numpy as np
#from numba import jit
# just an example.
#arr = np.array([[[0 for x in range(3)] for y in range(500)] for x in range(300)])
#@jit(nogil=True)
# there's no speedup.
def gv1(b,binary=True):
    if binary:
        return (str((x,y)).encode() for x in range(b[0]) for y in range(b[1]))
    return ((x,y) for x in range(b[0]) for y in range(b[1]))

def gv2(b,binary=True):
    if binary:
        return ((str((x,y)).encode() for x in range(b[0])) for y in range(b[1]))
    return (((x,y) for x in range(b[0])) for y in range(b[1]))

def gv3(b,binary=True):
    if binary:
        return ((str((x,y)).encode() for y in range(b[1])) for x in range(b[0]))
    return (((x,y) for y in range(b[1])) for x in range(b[0]))

def spilter(a,b):
    x,y=b
    xd,yd,_=a.shape
#    print(a.shape)
    xp,yp=int(xd/x),int(yd/y)
    d={}
    for x0 in range(x):
        x1=x0+1
        xv0,xv1=x0*xp,x1*xp
        for y0 in range(y):
            y1=y0+1
            yv0,yv1=y0*yp,y1*yp
            d.update({(x0,y0):a[xv0:xv1,yv0:yv1,:]})
    return d
#dp=spilter(arr,(10,10))
#for x in dp.keys():
#    print("key",x,"slice",dp[x].shape)
