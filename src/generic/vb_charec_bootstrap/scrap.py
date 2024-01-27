# if this works?
#import scrapy
import random
rng = random.SystemRandom()
def genchar(a,b):
    return "".join([rng.choice(a) for x in range(b)])
# SELF-SCRAPING.
doers="http://localhost:8888/"
rchar="abcdefg1234567890"
rlink=[doers+genchar(rchar,9) for x in range(9)]
print(rlink)
