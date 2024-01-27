# remember or get some code.
import requests
import time
def mix_and_eval(*args):
    for x in args:
        r = requests.post("http://localhost:8888",x)
        print("data received:",r.content)
        time.sleep(0.1)
    r=requests.get("http://localhost:8888")
    print(r.content)

f = ["1","+","1"]
mix_and_eval(*f)
f0 = ["1","-","1"]
mix_and_eval(*f0)
f1 = ["1","1"]
mix_and_eval(*f1)
