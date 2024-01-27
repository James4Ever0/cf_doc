# execute the command. see if it works?
from tcx import reset, scommand
import itertools
import traceback
import time

cmd = ["ruby","hello.rb"]
# new stuff! irb.
def mix_and_eval(*args):
    for x in itertools.permutations(args):
        try:
            print(scommand(" ".join(x)+"\n"))
            print("success",x)
        except:
            traceback.print_exc()
            print("error",x)
        finally:
            reset()
            time.sleep(1)
mix_and_eval(*cmd)
# so which is first?
