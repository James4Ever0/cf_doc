import redis
import numpy as np
#import struct
import pickle
import random
rng = random.SystemRandom()

# all bytes!
r=redis.StrictRedis(host='localhost', port=6379, decode_responses=False)
#r.set("sample_np_array",arr.tobytes())
for x in r.keys():
    try:
        print("key: ",x)
        f=r.get(x)
    # dump will get unwanted offset.
        print("data: ",f,type(f))
        if "(" in x.decode():
            print("decode_numpy: ",pickle.loads(f))
            break
    except:
        pass
#    else:
#        print(">>>keys compare:",str(x),rail)
