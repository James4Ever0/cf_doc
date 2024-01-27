import requests
import json
import traceback
import pickle

def poster(s):
    data=None
    try:
        data=json.dumps(s)
    except:
        data=pickle.dumps(s)
#data= json.dumps({"terminal":"terminal"})
    try:
        r=requests.post("http://localhost:8888",data=data)
#        print(type(r),dir(r))
        pr = dir(r)
        for py in pr:
            print("content of {}".format(py))
            print(eval("r."+py))
    except:
        traceback.print_exc()
