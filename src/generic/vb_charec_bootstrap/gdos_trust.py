# this is recursive programming.
# 25 x 80
import threading
import subprocess
import signal, sys
import time
from nparr_redis import rset
from or_func import trusty
import requests
def repo():
    requests.get("http://localhost:8888/r")

def unwarp(a):
    return [x for y in a for x in y]

def uwp(a,r=1):
    for x in range(r):
        a=unwarp(a)
#    print(a)
    return a
# current_key = None
# use a separate thread to get the image loaded!
# communicate to the thread? bidirectional?
# stdin?
def sigint_handler(signal,frame):
    print("interrupted!")
    time.sleep(0.1)
    sys.exit(0)
def my_except_hook(exctype,value,traceback):
    time.sleep(0.1)
    sys.__excepthook__(exctype,value,traceback)
    sys.exit(0)
    # is it lethal?
sys.excepthook = my_except_hook
signal.signal(signal.SIGINT,sigint_handler)
def run_main_v2(cmdline,env,callback=None,delay_3=None):
    print("started!",cmdline)
    if callback is None:
        callback = lambda x: None
    if delay_3 is None:
        delay_3 = 0
    for x in cmdline:
        time.sleep(delay_3)
        subprocess.run(x,env=env)
        callback(x)

def run_main(cmdline,callback=None):
    print("started!",cmdline)
    if callback is None:
        callback = lambda x: None
    subprocess.run(cmdline)
    callback(cmdline)

def recent_key_cb(cmdline,callback=None,callback_v2=None):
#    print("running callback reckeycb")
    if callback is None:
        callback = lambda x: None
    if callback_v2 is None:
        callback_v2 = lambda : None
    if len(cmdline)==3:
        if cmdline[0]=="xdotool":
            if cmdline[1]=="type":
                callback(cmdline[2])
    elif cmdline[0]=="./trwp.sh":
        callback_v2()

def rep_main(cmdline,env,delay=0,callback=None,delay_2=0.5):
    time.sleep(delay)
    if callback is None:
        callback = lambda x: None
    if env is not None:
        while True:
            time.sleep(delay_2)
#            callback(cmdline)
            run_main_v2(cmdline,env,callback)
    else:
        while True:
            time.sleep(delay_2)
#            callback(cmdline)
            run_main(cmdline,callback)
 
    # right into the output.
    #subprocess.run(["./sep_dosbox.sh"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # where's the output?
    # if you cannot count, why bother math?
import os
env = os.environ.copy()
#env = copy.deepcopy(os.environ)
env["DISPLAY"]=":9"
craft=("0123456789")*20
# this is for cell counting.
# merge the func of checking screen and receiving keys.
# not just rset, but a whole thing.
t0=threading.Thread(target=rep_main,args=([
*uwp([[["xdotool", "type", craft[d]],["./trwp.sh"]] for d in range(len(craft))],r=1),
["xdotool", "key", "0xff0d"],
],env,0.5,lambda x:recent_key_cb(x,lambda y:rset("recent_key",y),repo)))
t0.setDaemon(True)
t0.start()
# better end this thread? check if properly closed.
# this is the launcher.
t=threading.Thread(target=run_main,args=(["./sep_dosbox.sh"],))
t.setDaemon(True)
t.start()
# better end this thread? check if properly closed.
#t1=threading.Thread(target=rep_main,args=(["./rwp.sh"],None,2))
#t1.setDaemon(True)
#t1.start()
#
while True:
    time.sleep(1)
    print("idle main thread")
