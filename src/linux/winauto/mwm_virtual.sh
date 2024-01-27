#!/bin/bash
rm -rf /dev/shm/xvfb
mkdir /dev/shm/xvfb
xvfb-run -f ~/.Xauthority -n 7 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb" burpsuite & echo xvfb_session_pid $!
sleep 1
#gnome-shell --display :7
mwm -display :7
#xvfb-run -f ~/.Xauthority -n 1 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -listen tcp " xterm
