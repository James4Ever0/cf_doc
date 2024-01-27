import redis

r=redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set(2020,2077)
f=r.get(2020)
r.lpush(2033,2)
r.lpush(2033,3)
h=r.lrange(2033,0,-1)
print(f,h)
for x in r.keys():
    print("key: ",x)
