import redis
import numpy as np
#import struct
import pickle

arr = np.array([1,2])
# all bytes!
rail="sample_np_array"
r=redis.StrictRedis(host='localhost', port=6379, decode_responses=False)
orig = pickle.dumps(arr)
print("original: ",orig)
r.set(rail,orig)
#r.set("sample_np_array",arr.tobytes())
for x in r.keys():
    print("key: ",x)
    f=r.get(x)
    # dump will get unwanted offset.
    print("data: ",f,type(f))
    if x.decode() == rail:
        print("decode_numpy: ",pickle.loads(f))
#    else:
#        print(">>>keys compare:",str(x),rail)
