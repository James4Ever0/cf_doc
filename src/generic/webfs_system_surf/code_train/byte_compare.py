def known_bytes(y):
    z=set(y)
    z={k:list(map(lambda f:f==k,y)) for k in z}
    z={k:[f for f in range(len(z[k])) if z[k][f]] for k in z.keys()}
    return z

def given_array(y):
    z=known_bytes(y)
    l=len(y)
    return {k:[y[d:l] for d in z[k]] for k in z.keys()}
