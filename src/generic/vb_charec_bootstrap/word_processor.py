import sys
import random

rng = random.SystemRandom()
maxToken=5

for x in sys.stdin:
    z=len(x) # remaining.
    f=z
    print("input: ",x)
    while (z>0):
        k=f-z
        s=range(1,min(maxToken,1+z))
        s=rng.choice(s)
        y=x[k:k+s]
        z-=s
        print("output:",y)
