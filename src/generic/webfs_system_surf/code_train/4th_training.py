# make sure the thing is launched.
from names import genames
# design a keyword.
import re
code = """print"""
# store it into the database, without caring how the fuck it is done.
from nparr_redis import rget, rset
rset("hello_world",code)
rx = rget("hello_world")
print(rx)
#ry = rx.split(b"\n")
#print(ry)
# what type?
genames(100,globals())
keys = list(globals().keys())
for x in keys:
#    esc = re.escape(str(globals()[x])).encode()
    esc = globals()[x]
    es = rx+b"(esc)"
    print(es)
    # cannot execute the thing.
    # rename it. do the hack.
    exec(es)
# nothing in return.
# now you need to change, or execute it one by one?
# can you prove there's nothing we can do about self-containing?
# how to get it done? it is my code!
