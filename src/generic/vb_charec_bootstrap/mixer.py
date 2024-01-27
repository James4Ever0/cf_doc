import random
from id_func import ethic
rng = random.SystemRandom()

def lin_repeat(a,b=3):
    # this is pattern.
    f=""
    for x in a:
        f+=x*rng.choice(range(1,b+1))
    return f

def safe_lr(a,b=3):
    while True:
        c = lin_repeat(a,b)
        c2 = c*2
        e = ethic(c,c2,c=True,mix=1)
        if len(e) == 0:
            return c
