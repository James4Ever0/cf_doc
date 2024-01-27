import virtualbox
import time
import signal, sys
#from gevent import monkey
#monkey.patch_all()
# consider taking that too.
# the pipe must be initialized. use another thread to initialize the pipe.
import threading
import subprocess
# or you can be careless anyway.
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
machine=vbox.find_machine("TinyPlus")
def sigint_handler(signal,frame):
    print("interrupted!")
    session.console.power_down()
    time.sleep(0.1)
    sys.exit(0)
signal.signal(signal.SIGINT,sigint_handler)
#virtualbox.library_ext.machine.IMachine
#print(dir(machine),type(machine))
# you can close this window anyway, or minimize it using another thread?
progress=machine.launch_vm_process(session,"gui","")
progress.wait_for_completion()
# how to pass it around?
# must be keys. but what is keys?
time.sleep(5)
# not receiving shit.
# connect to existing session if possible? or close that thing.
# the virtualbox can get separate input while dosbox cannot. if want to must use a separate screen. xdotool.
def init():
    time.sleep(0.2)
    subprocess.run(["./init.sh"])

"""def shot(sess):
    s=sess.console.display"""
def typekey(key):
    session.console.keyboard.put_keys(key)

t=threading.Thread(target=init)
t.setDaemon(True)
t.start()

buff=["passwd","root","root","su - tc","passwd","tinypluscore","tinypluscore","exit","clear","stty size"]
#buff=["passwd","root","root","su - tc","passwd","tinypluscore","tinypluscore","exit","clear","bash","echo $LINES","echo $COLUMNS"]
for x in buff:
    time.sleep(0.2)
    typekey(x+"\n")
with open("lazero","r") as f:
    while True:
        r=f.readline()
        # be properly decoded.
        # return included.
        if len(r)==0:
            pass
        else:
            session.console.keyboard.put_keys(r)
        time.sleep(0.1)
        print(">>> visible delay?",time.time())
#session.console.keyboard.put_keys("Hello, world!")
# maybe a dedicated image for dos and more.
# first we have to check how to read chars from the canvas or something.
# remember that is way too slow to parse info from console. i mean THAT.
