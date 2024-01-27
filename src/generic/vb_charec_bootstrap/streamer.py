# check the reoccurance of every phrase.
def occur(a,b):
    return not a==b

def reoccur(a,b):
    return occur(a,b) and a>1

def xoccur(a,b,x):
    return occur(a,b) and a>x
"

"""
def readict(a,d):
    for x in d.keys():
        if a==x:
            return d[a]
    return 0
"""
def refdict(a,d):
    for x in d.keys():
        if a==x:
            d[a]+=1
            return d[a]-1,d[a],d
    d.update({a:1})
    return 0,1,d

# some actions must be taken.
sample="this is a part of sample text."
dic={}
for k in sample:
    a,b,dic=refdict(k,dic)
    o,r=occur(a,b),reoccur(a,b)
    print("{} occur: ".format(k),o)
    print("{} reoccur: ".format(k),r)
