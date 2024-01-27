# to prove something has a thing or to.
    # wow but this is useless. only a proof of legit grammar.
# so we want to find something in common.
def try_decode(a):
    try:
        return chr(a)
    except:
        print("unable to decode.")
a = open("cli_text_processing.pdf","rb").read()
buf=""
for x in a:
    td = try_decode(x)
    if td is None:
        if buf !="":
            print(buf)
            buf = ""
    else:
        buf+=td
if buf !="":
    print(buf)
#print(a)
#for x in a.split():
#    try_decode(x)
#    print(x)
