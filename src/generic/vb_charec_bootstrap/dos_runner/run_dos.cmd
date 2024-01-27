@echo off
REM do we need latest?
REM "D:\Program Files (x86)\Android\android-sdk\tools\qemu\windows-x86_64\qemu-system-x86_64.exe"  -enable-hax -m 2M,maxmem=5M -mem-path R:\ -hda c.hd -boot d
"E:\Program Files\qemu\qemu-system-x86_64.exe" -accel hax -m 2M,slots=2,maxmem=5M  -hda c.hd -boot d
REM "D:\Android\SDK\emulator\lib\pc-bios"
REM D:\Program Files (x86)\Android\android-sdk\tools\lib\pc-bios\kvmvapic.bin
REM this is not native one.