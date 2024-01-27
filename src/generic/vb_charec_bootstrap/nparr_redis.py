import redis
import numpy as np
import pickle
import threading

r=redis.StrictRedis(host='localhost', port=6379, decode_responses=False)
#r.set("sample_np_array",arr.tobytes())
def npset(x,arr):
    # use batch mode.
    # and with expiration.
    try:
        orig = pickle.dumps(arr)
        r.set(x,orig)
        return True
    except:
        return False

def rset(k,x):
    try:
        r.set(k,x)
#        print("setting",k,x)
        return True
    except:
#        print("error setting",k,x)
        return False

def rsetex(k,x,ex=1):
    try:
        r.setex(k,ex,x)
#        print("setting",k,x)
        return True
    except:
#        print("error setting",k,x)
        return False

def rget(k):
    try:
        return r[k]
    except:
        return None
# learning one by one.
def sov(dic,key,gple):
    dic[key] = pickle.dumps(dic[key])
    gple[0]+=1

def sod(dic,key,gple):
    dic[key] = pickle.loads(dic[key])
    gple[0]+=1

def bp_changer(x_arr):
    lst,i=[0],len(list(x_arr.keys()))
    for k in x_arr.keys():
        tx = threading.Thread(target = sov,args=(x_arr,k,lst))
        tx.setDaemon(True)
        tx.start()
    while True:
        if lst[0] == i:
            break
        time.sleep(0.001)
#    print("conv complete!")
#    print(x_arr)
    return x_arr

def npbset(x_arr,exp=2):
    pipe = r.pipeline()
    # use batch mode.
    # and with expiration.
    # threading?
    x_arr = bp_changer(x_arr)
    if exp == 0:
        for key in x_arr.keys():
            pipe.set(key, x_arr[key])
        pipe.execute()
    elif exp > 0 and type(exp) == int:
        for key in x_arr.keys():
            pipe.setex(key, exp, x_arr[key])
        pipe.execute()
    else:
        print("invalid expire time!")
        return False
#    print("execution done!")
# check keys then.
#        orig = pickle.dumps(arr)
#       r.set(x,orig)
    return True
#    except:
#        return False

def npret(x):
    try:
        f=r.get(x)
        return pickle.loads(f)
    except:
        return None
#    else:
