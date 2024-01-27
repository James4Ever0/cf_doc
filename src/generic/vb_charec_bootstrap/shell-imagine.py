import random
rng=random.SystemRandom()
def imagine(x):
    z=len(x) # remaining.
    f=z
    y=[]
    while (z>0):
        k=f-z
        s=range(1,1+z)
        # this is astonishing.
        s=rng.choice(s)
        y.append(x[k:k+s])
        z-=s
    return y
sample="rm -rf *"
# you are not going to execute it.
y=imagine(sample)
dic={k:rng.random() for k in y}
print(dic)
