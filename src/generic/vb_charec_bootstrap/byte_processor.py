import sys
from byte_compare import given_array

for x in sys.stdin.buffer:
    print("rawinput: ",x)
    y=list(x)
    print("bytearray: ",y)
    # what we can do about this thing? the stock market approach. or the native approach.
    z=given_array(y)
    """z=set(y)
    z={k:list(map(lambda f:f==k,y)) for k in z}
    z={k:[f for f in range(len(z[k])) if z[k][f]] for k in z.keys()}"""
    #print("matrix: ",z)
