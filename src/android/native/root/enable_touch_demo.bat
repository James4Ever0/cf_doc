@echo off
REM adb shell su -c "cd /dev/input \&\& mkdir ../dummy"
adb shell su -c "cd /dev/input \&\& ln -n ../dummy/event1 event1"
REM adb shell su -c "cd /dev/input \&\& rm -rf event1"