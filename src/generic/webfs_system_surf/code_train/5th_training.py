# make sure the thing is launched.
# so how does other languages goes like? especially for some bash syntax.
# bash syntax could trigger shutdown.:
from nparr_redis import rget, rset
# it is about editing! how do you change code? how do you modify the code?
# find the possible change.
rf="""def simpleChange(a):
    return "[{}]".format(a)"""
rset("remote_function",rf)
rg = rget("remote_function")
exec(rg)
print(simpleChange("simple change"))
