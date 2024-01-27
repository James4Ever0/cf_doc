import threading
import time

MAX_IDLE=3
MIN_COLLECT=1
MAX_COLLECT=10
col=[]
def listen(a):
    with open(a,'r') as f:
        while True:
            r=f.readline()
            if len(r)==0:
                pass
            else:
#                print(a,r,type(r),len(r))
                col.append(r)
            time.sleep(0.1)
# what if not sleeping?
# then things will go shit.

t=threading.Thread(target=listen,args=('stdout',))
t1=threading.Thread(target=listen,args=('stderr',))
t.setDaemon(True)
t1.setDaemon(True)

t.start()
t1.start()
# guess on windows there are pipe apis. offtopic!
# self-init.
counter=0
while True:
    l=len(col)
    #print('idle main thread',l,counter)
    # max idle time 5
    if l<MIN_COLLECT:
        pass
    else:
        if l >= MAX_COLLECT:
            break
        elif counter>=MAX_IDLE:
            break
        counter+=1
    time.sleep(0.1)
# do random choice here?
print(" ".join(col))
