import numpy as np
# use eval or nothing will happen.
# extract sparse matrix?
def genkey(tup):
    # check args length?
    # max recursion 3?
    base_list=[()]
    for x in range(len(tup)):
        base_list = [(*z,y) for z in base_list for y in range(tup[x])]
    return base_list

def recget(a,x):
    tar = a
    for z in x:
        tar = tar[z]
    return tar

# better use this in pypy? but how? use separate process or one single process? 
a = np.array([0,0,0])
b = np.array([0,1,1])
e = np.array([1,1,1])
d = np.array([0,0,1])
c = np.array([0,0,1])
# generate sparse matrix for individual pixels.
# group them together.
def tgen(lst,a):
    shape = a.shape
    keys = genkey(shape)
    typegen= {k:{0:[],1:[]} for k in keys}
    for k in lst.keys():
        f=lst[k]
        for x in keys:
            y=recget(f,x)
            typegen[x][y].append(k)
    return typegen
lst = {"a":a,"b":b,"c":c,"d":d,"e":e}
typegen=tgen(lst,a)
print(typegen)
# how do you map the logic? random plots?
"""
print(keys)
# use these keys to get data!
for dx in lst:
    for x in keys:
        print(x,recget(dx,x))
"""
# classify these things by what? better use a dict.
# a recursive function?

