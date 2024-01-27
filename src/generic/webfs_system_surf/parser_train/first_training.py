# no time to use ANTLR, right?
# that's because the architecture is simply not right.
# it can only become a submodule, and that's it.
a = open("rbh.log","r").read()
#import parse
from parse import *
#print(a)
print(parse("It's {}, I love it!", "It's spam, I love it!"))
print([x for x in findall("-{} ",a)])
r = parse("My quest is {quest[name]}", "My quest is to seek the holy grail!")
print(r)
