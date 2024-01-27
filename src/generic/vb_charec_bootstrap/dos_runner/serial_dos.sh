#!/bin/bash
qemu-system-i386 -enable-kvm -nographic -serial mon:stdio  -hda c.hd -boot d
# this is unix only.
# qemu-system-i386 -enable-kvm -nographic -serial vc:800x600  -hda c.hd -boot d
# qemu-system-i386 -enable-kvm -nographic -serial /dev/ttyS0 -hda c.hd -boot d
# qemu-system-i386 -enable-kvm -nographic -serial /dev/ttyS0  -hda c.hd -boot d
# qemu-system-i386 -enable-kvm -nographic -serial COM1  -hda c.hd -boot d
# you can use telnet! or unix socket.