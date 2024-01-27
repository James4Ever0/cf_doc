# make sure the thing is launched.
code = open("../dir_train/third_training.py","r").read()
#code = """print("hello world")"""
# store it into the database, without caring how the fuck it is done.
from nparr_redis import rget, rset
rset("hello_world",code)
rx = rget("hello_world")
print(rx)
exec(rx)
# can you prove there's nothing we can do about self-containing?
# how to get it done? it is my code!
