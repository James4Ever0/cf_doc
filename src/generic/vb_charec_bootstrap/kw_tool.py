import os
import random
import threading, time
from colorama import Fore, Style

rng = random.SystemRandom()

def rdk(a):
    cl=[Fore.RED,Fore.GREEN,Fore.BLUE]
    return " ".join([rng.choice(cl)+x+Style.RESET_ALL for x in a])

def nb_read(a,b,c):
    try:
        c[0] = open(a,b)
        return c
    except:
        return None

max_read = 5
for x in os.listdir("."):
    #try:
    f=[None]
    t=threading.Thread(target=nb_read,args=(x,"r",f))
    t.setDaemon(True)
    t.start()
    time.sleep(0.001)
    if f[0] is not None:
        try:
            f=f[0]
            k = set(f.read().split())
            if len(k)<=max_read:
                pass
            else:
                k = rng.sample(k,max_read)
                print(Fore.YELLOW+"file name: "+Style.RESET_ALL,x)
                print(">>>keywords: ",rdk(k))
        except:
            pass
    #except:
    #    print("error opening",x)
