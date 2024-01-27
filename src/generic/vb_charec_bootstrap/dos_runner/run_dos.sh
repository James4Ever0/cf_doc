#!/bin/bash
./loadram.sh
qemu-system-i386 -enable-kvm -m 5M,maxmem=10M -mem-path $PWD/ramdisk -hda c.hd -boot d
