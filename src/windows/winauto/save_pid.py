import sys
s=""
def writeOn(a):
    with open("pidfile","w+") as f:
        f.write(a)

for x in sys.stdin:
    s+=x+"\n"
writeOn(s)