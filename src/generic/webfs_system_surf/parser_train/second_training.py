import re

def func0(a,b):
    return False

def func1(a,b):
    return True

def func2(a,b):
    return a+b

def labelcheck(a):
    return not sum([int(a[x]>=0) for x in a.keys()])>0

def filter_function(a):
    sd = [int(x) for x in re.findall(r'\d+',sk)]
    return len(sd)==2
    # it will return the map!
    # not being here?
    # what is that? predetermined things? does it have the weights?

# what if there's solution? you cannot finite the entire search space!
# see what you'll get with these two tokens.
# identifier: None? / transformer?
sk = "1 1"
print("filter function result", filter_function(sk))
sd = [int(x) for x in re.findall(r'\d+',sk)]

# so apply these two things.
# you are gonna map these things. prefilter things out.
# if true then remember to reverse the filter?
sf = {"func0":0,"func1":0,"func2":0}
hopeless = False
roundx=0
maxround = 2
while not hopeless and roundx<maxround:
    for x in sf.keys():
        p = eval(x+"(*sd)")
        if p == 2:
            print("correct!")
            sf[x]+=1
#            hopeless = True
#            break
        else:
            print("false!")
            sf[x]-=1
    print("current score",sf)
    hopeless = labelcheck(sf)
    roundx+=1
# you can simply say that they've found the result.
# print the thing. match all correct things?
print("filter_function -> {} -> answer 2".format(" ".join([y for y in sf.keys() if sf[y]>0])))
