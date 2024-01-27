from ms3 import spilter
import cv2
import numpy as np
import time
# i guess python is full of translation here. translating calls into simple reusable stubs.
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

def grill(img,t0):
    s=spilter(img,(25,80))
    # same config for that tinycore.
    rk=list(s.keys())[0]
    rk=s[rk]
    _,y,x = rk.shape
    base_t=None
    # this is vertical alignment. but what is vertical?
    # not happy with raw key input.
    for x0 in range(80):
        base = genline(y,x)
        for y0 in range(25):
            base=concat(base,genline(y,x),s[(y0,x0)])
        if base_t is None:
#            print("init",base.shape)
            base_t = base.copy()
        else:
            z,_,_=base.shape
#            print("looping",base_t.shape,base.shape)
            base_t = concat_h(base_t,base,genline_h(z,x))
    #input class: <class '_io.BufferedReader'>    
    # paint multiple images onto the same window.
    cv2.imshow("sample",base_t)
    print("timing: ",time.time()-t0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
