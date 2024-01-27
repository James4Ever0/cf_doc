import numpy as np
s = open("fdecode.log","r").read().split()
v = open("out.txt","r").read().split()
# get the shift.
# major shift: 29
def process_tool(c,d,mv,mn):
#    e = [x for x in d]
    e = d
    f = np.diff([x for x in c.encode()])
    if len(f)==0:
        return False
    counter = 0
    max_counter = 0
    for x in range(len(e)):
        if e[x] == f[counter]:
            if counter < len(f)-1:
                counter +=1
            else:
#                print("shift",mv[x-len(mn)]-ord(mn[0]))
                print("scene",e[2+x-len(mn):x+1],f)
                print("real",mv[2+x-len(mn):x+2],[ord(y) for y in mn],mv[2+x-len(mn)])
                print("shift",mv[2+x-len(mn)]-ord(mn[0]))
                # how to get the shift?
                return True
        else:
            max_counter = max([max_counter,counter])
            counter = 0
    print("max_counter",max_counter)
    return False

f=[]
for x in s:
    if len(x)==6:
        print(x[1:-1])
        f+=[eval("0x"+x[1:-1])]
#print(f)
f0 = np.diff(f)
for x in v:
    print(x,process_tool(x,f0,f,x))
