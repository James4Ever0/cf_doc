import requests
import json
data= json.dumps({"terminal":"terminal"})
requests.post("http://localhost:8888",data=data)
