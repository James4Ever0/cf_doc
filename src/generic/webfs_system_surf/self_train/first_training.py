# to prove something has a thing or to.
import numpy
def prove_add(s):
    assert eval("1"+s+"1") == 2
    # wow but this is useless. only a proof of legit grammar.
# so we want to find something in common.
def process_tool(c,d):
#    e = [x for x in d]
    e = d
    f = numpy.diff([x for x in c.encode()])
    if len(f)==0:
        return False
    counter = 0
    max_counter = 0
    for x in e:
        if x == f[counter]:
            if counter < len(f)-1:
                counter +=1
            else:
                return True
        else:
            max_counter = max([max_counter,counter])
            counter = 0
    print("max_counter",max_counter)
    return False

a = open("cli_text_processing.pdf","rb").read()
#print(a)
b = open("out.txt","r").read()
#print(b)
nd=numpy.diff([x for x in a])
# type matched. then what?
# so we're gonna find the commondities.
for x in b.split():
    print(x,type(x),type(a),process_tool(x,nd))
