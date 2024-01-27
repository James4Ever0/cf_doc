s0 = open("fdecode.log","r").read().split()
# get the shift.
# major shift: 29
def shifter(s,k):
    f=[]
    for x in s:
        if len(x)==6:
            f+=[chr(eval("0x"+x[1:-1])+k)]
    print("".join(f))

p = [29,30,49]
for x in p:
    shifter(s0,x)
