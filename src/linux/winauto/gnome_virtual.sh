#!/bin/bash
rm -rf /dev/shm/xvfb
mkdir /dev/shm/xvfb
xvfb-run -f ~/.Xauthority -n 7 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -reset -terminate" gnome-shell --replace 
#echo xvfb_session_pid $!
#mwm -display :7
#xvfb-run -f ~/.Xauthority -n 1 -s "-pixdepths 3 27 -fbdir /dev/shm/xvfb -listen tcp " xterm
