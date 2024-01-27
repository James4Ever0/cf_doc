from nparr_redis import rget
import time
while True:
    print(rget("recent_keys"))
    time.sleep(1.5)
