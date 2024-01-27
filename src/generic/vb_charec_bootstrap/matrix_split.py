import numpy as np
# just an example.
arr = np.array([[0 for x in range(300)] for y in range(500)])
def spilter(a,b):
    x,y=b
    xd,yd=a.shape
    xp,yp=int(xd/x),int(yd/y)
    d={}
    for x0 in range(x):
        x1=x0+1
        xv0,xv1=x0*xp,x1*xp
        for y0 in range(y):
            y1=y0+1
            yv0,yv1=y0*yp,y1*yp
            d.update({(x0,y0):arr[xv0:xv1,yv0:yv1]})
    return d
dp=spilter(arr,(10,10))
for x in dp.keys():
    print("key",x,"slice",dp[x].shape)
