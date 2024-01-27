import difflib
import copy
a = open("anytext.sh","r").read()
b = open("shit.sh","r").read()

#dir(difflib)
#rnd = "round one.                   "*20
rnd = copy.copy(a)
rnd = [x for x in rnd]
# generate some function. this is it. whatever it means.
x0 = [x for x in difflib.ndiff(a,b)]
for xp in range(len(x0)):
    xf = x0[xp]
    if xf[0]==" ":
        pass
    elif xf[0]=="-":
        rnd[xp]=""
    else:
        # this is insertion.
#        rnd[xp]=xf[2]
        rnd[xp:xp]=xf[2]
print("".join(rnd))
