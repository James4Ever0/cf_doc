#!/bin/bash
#qemu-system-i386 -nographic  -serial telnet:localhost:4312,server,nowait  -hda c.hd -boot d
qemu-system-i386 -nographic -enable-kvm -serial telnet:localhost:4312,server,nowait  -hda c.hd -boot d
