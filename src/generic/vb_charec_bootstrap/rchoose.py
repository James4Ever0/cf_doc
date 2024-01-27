import sys
import random

rng=random.SystemRandom()
img=['']

for x in sys.stdin:
    imp+=x.split()
sys.stdout.write(rng.choice(img))
