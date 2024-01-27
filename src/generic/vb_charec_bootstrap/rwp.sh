#!/bin/bash
# must pipe the data to the process.
# to redis.
cp /dev/shm/xvfb/Xvfb_screen0 /dev/shm/xvfb/DOS && cat /dev/shm/xvfb/DOS | pypy3  pypy_xwd.py --raw | python3 rup.py 
# whatever your name is. it gotta be finite.
# must register to something else?
# get recent command?
