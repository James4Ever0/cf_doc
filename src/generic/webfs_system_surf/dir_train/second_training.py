#you are gonna ask for the directory.
i=input("where the heck is the dongle?\n")
# so this time a single input with typo!
# can you fix it?
# the way you use a function, the way you handle the source code.

def singleShot(i):
    import os
    o = os.listdir(i)
    return o

# multiple workable ways?
def dis(a,b):
    import Levenshtein
    return Levenshtein.distance(a,b)

def trim(a,b):
    return dis(a[:len(b)],b)
#    print(o)
def lowtrim(a,b):
    return dis(a[:len(b)].lower(),b.lower())

#    print("dongle listed!")
fx = "/"
for x in i.split():
    print(x)
    s = singleShot(fx)
    for sx in s:
        # so make summary: the lowest thing adding up altogether is true. the rule forms?
        print(sx,"distance",dis(sx,x),"trim_distance",trim(sx,x),"lower_trim",lowtrim(sx,x))
    print("directory listed!")
    # how's it going?
    # assume it is started from the ground level.
