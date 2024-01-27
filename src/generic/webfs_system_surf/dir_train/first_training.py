#you are gonna ask for the directory.
i=input("where the heck is the dongle?\n")
print(i)
import os
o = os.listdir(i)
print(o)
print("dongle listed!")
