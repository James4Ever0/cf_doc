import re
import zlib
import traceback
# so what is the process anyway?
# hit the web, and again?
def getcode(a):
    coder = re.compile(r"<....>",re.S)
    pv = ""
    for s in re.findall(coder,a):
#        pk = int(s[1:-1],base=16)
        print(s)
#        try:
#            pv +=chr(pk)
#        except:
#            traceback.print_exc()
#    print(pv)
pdf = open("cli_text_processing.pdf", "rb").read()
stream = re.compile(b'.*?FlateDecode.*?stream(.*?)endstream', re.S)

for s in re.findall(stream,pdf):
    s = s.strip(b'\r\n')
    try:
        print(zlib.decompress(s).decode('UTF-8'))
        #getcode(zlib.decompress(s).decode('UTF-8'))
    except:
        pass

