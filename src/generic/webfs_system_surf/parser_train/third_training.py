import re
import traceback
# a filter is not always true.
# a function is not always false.
# syntax error can cause that.

def func0(a,b):
    return False

def func1(a,b):
    return True

def func2(a,b):
    return a+b

def func3(a):
    return a+"s"

def labelcheck(a):
    return not sum([int(a[x]>=0) for x in a.keys()])>0

def filter_function(a):
    sp = [int(x) for x in re.findall(r'\d+',a)]
#    print(sp)
    return len(sp)==2
# make sure it is independent! even if it has to be verbose.
    # it will return the map!
    # not being here?
    # what is that? predetermined things? does it have the weights?

# i want to double the filters. result is 2 this time.
# have you noticed? that connection is independent on many things. no matter what number is coming in, it always has the result.
def filter2(a):
    return "http" in a
# so http is not in a.
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
        p = None
        try:
            p = eval(x+"(*sd)")
        except:
            traceback.print_exc()
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

sv = "http"
print("f#1 result", filter_function(sv))
print("f#2 result", filter2(sv))

# if true then remember to reverse the filter?
# so do we have any element shifter?
sf = {"func0":0,"func1":0,"func2":0,"func3":0}
sd = [sv]
hopeless = False
roundx = 0
maxround = 2
while not hopeless and roundx<maxround:
    for x in sf.keys():
        p = None
        try:
            p = eval(x+"(*sd)")
        except:
            # this is syntatic error. how to handle it?
            # by feeding it back to the system. clearly there's a way to get the number of arguments.
            traceback.print_exc()
        if p == "https":
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
print("filter2 -> {} -> answer https ".format(" ".join([y for y in sf.keys() if sf[y]>0])))
