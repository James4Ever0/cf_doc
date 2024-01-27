from nparr_redis import rget
from sm_func import get_table, s2Check, choky , dec_dict
from ms3 import gv1
from id_func import ethic
import matplotlib.pyplot as plt
#import time
# you still need to double-check.
#while True:
# not knowing the length.
# maybe you need to train it though.
# you need to trust something somehow?
pr = rget("recent_keys")
print(pr)
tb = get_table()
#print(len(tb))
keys, cons = dec_dict(tb,flatten = True)
# better walk throuogh.
threash, shp, cod, cov ,jcod = choky(cons,gua = 0.6)

#print(hs)
#print(len(hs))
# not self-repeating.
cod = {k:s2Check(tb[k],cov,jcod,shp,threash) for k in tb.keys()}
col = tuple(cod[k] for k in gv1((25,80)))
#print(col)
cos = ethic(pr,col)[0]
#print(cos)
# they are the same. but getting hash is not enough.
width=5
height=5
rows = 2
cols = 5
axes=[]
fig=plt.figure()
for a in range(rows*cols):
#    b = np.random.randint(7, size=(height,width))
    try:
        print("key",cos[a])
#        b = hs[cos[a]]
        b = cov[cos[a]]
        axes.append( fig.add_subplot(rows, cols, a+1) )
        subplot_title=("Subplot"+str(a))
        axes[-1].set_title("number "+chr(pr[a]))
        plt.imshow(b)
    except:
        print("error on key",cos[a])
fig.tight_layout()    
plt.show()
# print(col)
# so time to get it ordered.
#print(cod)
# this is the code. then find the pattern!
# why that much?
#print(len(tb),type(tb))
# then, get all keys?
# not sure whether we can decode the thing or not? but only targeting readable chars.
# hashing while parsing?
