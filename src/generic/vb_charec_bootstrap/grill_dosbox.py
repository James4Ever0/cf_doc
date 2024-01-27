# this is recursive programming.
# 25 x 80
import threading
import subprocess
import signal, sys
import time
from nparr_redis import rset
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
def run_main_v2(cmdline,env,callback=None):
    if callback is None:
        callback = lambda x: None
    for x in cmdline:
        subprocess.run(x,env=env)
        callback(x)
        print("completed!",cmdline)

def run_main(cmdline,callback=None):
    if callback is None:
        callback = lambda x: None
    subprocess.run(cmdline)
    callback(cmdline)
    print("completed!",cmdline)

def recent_key_cb(cmdline,callback=None):
#    print("running calback reckeycb")
    if callback is None:
        callback = lambda x: None
    if len(cmdline)==3:
        if cmdline[0]=="xdotool":
            if cmdline[1]=="type":
                callback(cmdline[2])

def rep_main(cmdline,env,delay=0,callback=None):
    time.sleep(delay)
    if callback is None:
        callback = lambda x: None
    if env is not None:
        while True:
            time.sleep(0.5)
#            callback(cmdline)
            run_main_v2(cmdline,env,callback)
    else:
        while True:
            time.sleep(0.5)
#            callback(cmdline)
            run_main(cmdline,callback)
 
    # right into the output.
    #subprocess.run(["./sep_dosbox.sh"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # where's the output?
    # if you cannot count, why bother math?
import os
from mixer import safe_lr as lin_repeat
env = os.environ.copy()
#env = copy.deepcopy(os.environ)
env["DISPLAY"]=":9"
arcade = lin_repeat("0123456789")
al = len(arcade)
craft=arcade*20
t0=threading.Thread(target=rep_main,args=([
["xdotool", "type", craft],
["xdotool", "key", "0xff0d"]
],env,0,lambda x:recent_key_cb(x,lambda y:rset("recent_keys",y[:2*al]))))
t0.setDaemon(True)
t0.start()
# better end this thread? check if properly closed.

t=threading.Thread(target=run_main,args=(["./sep_dosbox.sh"],))
t.setDaemon(True)
t.start()
# better end this thread? check if properly closed.
t1=threading.Thread(target=rep_main,args=(["./rwp.sh"],None,2))
t1.setDaemon(True)
t1.start()
#
while True:
    time.sleep(1)
    print("idle main thread")
