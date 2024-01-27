# make sure the thing is launched.
# so how does other languages goes like? especially for some bash syntax.
# bash syntax could trigger shutdown.:
from nparr_redis import rget, rset
# it is about editing! how do you change code? how do you modify the code?
# find the possible change.
rf="""def simpleChange(a):
    return "[{}]".format(a)"""
rd="""def smc(a):
    return "{"+a+"}" """

rset("remote_function",rf)
rset("rm_f",rd)
rg = rget("remote_function")
exec(rg)
rg = rget("rm_f")
exec(rg)
# do a smart exec, change the name before execute!
pc = simpleChange(smc("simple_change"))
pr = smc(simpleChange("simple_change"))
print(pc)
print(pr)
