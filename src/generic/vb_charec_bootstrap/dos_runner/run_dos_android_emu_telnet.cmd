@echo off
REM do we need latest?
REM "D:\Program Files (x86)\Android\android-sdk\tools\qemu\windows-x86_64\qemu-system-x86_64.exe"  -enable-hax -m 2M,maxmem=5M -mem-path R:\ -hda c.hd -boot d
"D:\Program Files (x86)\Android\android-sdk\tools\qemu\windows-x86_64\qemu-system-x86_64.exe" -L "D:\Program Files (x86)\Android\android-sdk\tools\lib\pc-bios" -L "D:\Android\SDK\emulator\lib\pc-bios"  -m 2M,slots=2,maxmem=5M  -nographic -serial  telnet:localhost:4312,server,nowait -hda c.hd -boot d
REM "D:\Android\SDK\emulator\lib\pc-bios"
REM it is fucked.
REM D:\Program Files (x86)\Android\android-sdk\tools\lib\pc-bios\kvmvapic.bin
REM this is not native one.
REM D:\Program Files\MATLAB\R2018a\toolbox\idelink\foundation\hostapps\PUTTY.EXE
REM "D:\Program Files (x86)\com0com\setupc.exe"