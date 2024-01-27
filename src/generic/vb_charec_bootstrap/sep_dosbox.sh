#!/bin/bash
# do it in xvfb.
mkdir /dev/shm/xvfb
# value found on internet.
xvfb-run -f ~/.Xauthority -n 9 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -screen 0 640x400x24 -nocursor" dosbox
#xvfb-run -f ~/.Xauthority -n 9 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -screen 0 500x500x24" dosbox
#xvfb-run -f ~/.Xauthority -n 9 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -screen 300x300x27" dosbox
