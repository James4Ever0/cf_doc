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
        return r.content
#        print(type(r),dir(r))
    except:
        traceback.print_exc()

def termControl(s):
    try:
        r=requests.post("http://localhost:8888",data=s)
        return r.content
    except:
        traceback.print_exc()

def anyControl(p,s,a=True):
    try:
        if a:
            r=requests.post("http://localhost:{}".format(p),data=s)
            return r.content
        else:
            r=requests.get("http://localhost:{}".format(p))
            return r.content
    except:
        traceback.print_exc()
