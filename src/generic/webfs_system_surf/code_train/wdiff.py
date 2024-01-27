import requests
import json
import traceback
def poster(s):
    data=json.dumps(s)
#data= json.dumps({"terminal":"terminal"})
    try:
        requests.post("http://localhost:8888",data=data)
    except:
        traceback.print_exc()
