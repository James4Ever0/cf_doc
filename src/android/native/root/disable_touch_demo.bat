@echo off
adb shell su -c "cd /dev/input \&\& mkdir ../dummy"
adb shell su -c "cd /dev/input \&\& ln -n event1 ../dummy/event1"
adb shell su -c "cd /dev/input \&\& rm -rf event1"