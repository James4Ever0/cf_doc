# this is recursive programming.
# 25 x 80
import threading
import subprocess
import signal, sys
import time

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
def run_main_v2(cmdline,env):
    for x in cmdline:
        subprocess.run(x,env=env)
        print("completed!",cmdline)


def run_main(cmdline):
    subprocess.run(cmdline)
    print("completed!",cmdline)

def rep_main(cmdline,env):
    while True:
        time.sleep(0.5)
        run_main_v2(cmdline,env)
    # right into the output.
    #subprocess.run(["./sep_dosbox.sh"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # where's the output?
    # if you cannot count, why bother math?
import os
env = os.environ.copy()
#env = copy.deepcopy(os.environ)
env["DISPLAY"]=":9"
craft=("0123456789")*20
t0=threading.Thread(target=rep_main,args=([
["xdotool", "type", craft],
["xdotool", "key", "0xff0d"]
    ],env))
t0.setDaemon(True)
t0.start()
# better end this thread? check if properly closed.

t=threading.Thread(target=run_main,args=(["./sep_dosbox.sh"],))
t.setDaemon(True)
t.start()
# better end this thread? check if properly closed.

while True:
    time.sleep(1)
    print("idle main thread")
