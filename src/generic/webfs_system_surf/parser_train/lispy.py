# so how do you get the number 2?
import re
import subprocess
from subprocess import PIPE
exp = "(+ 1 1)"
def func(a,b):
    print(eval("{}+{}".format(a,b)))

def lispRunner(a):
    f = subprocess.Popen(["./lisprunner.sh"],stdout=PIPE,stderr=PIPE)
    f = f.communicate()
    print(f)

def filter_out(a):
    return [x for x in a if len(x)>0]

lispRunner(exp)
sv = [x for x in re.findall(r'\d?',exp)]
#print(sv)
sv = filter_out(sv)
#print(sv)
func(*sv)
