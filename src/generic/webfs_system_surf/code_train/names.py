import random
# cannot get mysterious names.
def genames(a,b = globals()):
    for x in range(a):
        b.update({"a_"+str(x):random.random()})
if __name__ == "__main__":
    genames(100)
