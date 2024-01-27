a = open("anytext.sh","r").read()
print(a)
# find and replace? or what?
#print(a.replace("world","fuck"))
# insert a fuck somehow.
import random
a = [x for x in a]
s = random.choice(range(len(a)))
for k in range(4):
    a[s+k]="fuck"[k]
print("".join(a))
