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

from charec import sparse

s=sparse(2)
print(s)
import numpy as np
d=np.array([[1,2,3,4],[3,4,2,3],[3,3,2,2],[3,3,2,6]])
dp=np.array([[1,3,3,4],[3,4,2,3],[3,3,1,2],[3,3,2,6]])
# get it checked?
k=spv2(d,s,c=2)
k1=spv2(dp,s,c=2)

# get it ready? a specific thing? equalization?
#for k0 in k.keys():
#    print(k0,k[k0])
