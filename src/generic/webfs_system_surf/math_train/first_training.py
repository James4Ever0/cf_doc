# remember or get some code.
import itertools

def mix_and_eval(*args):
    for x in itertools.permutations(args):
        try:
            print(eval("".join(x)))
            print("success",x)
        except:
            print("error",x)

f = ["1","+","1"]
mix_and_eval(*f)
