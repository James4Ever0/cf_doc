#!/bin/bash
# this is a shared jail.
#./loadroot.sh
# you are shitting on me.
# sudo umount /dev/shm/lazero/root
psk=$(sudo mount | grep /dev/shm/lazero/sambaroot | wc -c)
psl=$(sudo mount | grep /dev/shm/lazero/sambaroot | wc -l)
err=0
if [ $psk -eq 0 ]
then
	sudo umount -A -f /dev/shm/lazero/sambaroot
	psk=$(sudo ls /dev/shm/lazero/sambaroot | wc -c)
	if [ $psk -eq 0 ]
	then
		sudo rm -rf /dev/shm/lazero/sambaroot
	fi
	sudo mkdir -p /dev/shm/lazero/sambaroot
	sudo chmod 777 /dev/shm/lazero/sambaroot
	sudo mount --bind -r / /dev/shm/lazero/sambaroot/
else
	psk=$(sudo mount | grep /dev/shm/lazero/sambaroot | grep "errors=remount-ro" | wc -c)
	if [ $psk -eq 0 ]
	then
		err=$(( 1 + $err ))
	fi
	
	if [ $psl -ne 1 ]
	then
		err=$(( 1 + $err ))
	fi
	if [ $err -ne 0 ]
	then
		sudo umount -A -f /dev/shm/lazero/sambaroot
		psk=$(sudo ls /dev/shm/lazero/sambaroot | wc -c)
		if [ $psk -eq 0 ]
		then
			sudo rm -rf /dev/shm/lazero/sambaroot
		fi
#		sudo rm -rf /dev/shm/lazero/root
		sudo mkdir -p /dev/shm/lazero/sambaroot
		sudo chmod 777 /dev/shm/lazero/sambaroot
		sudo mount.cifs -o user=root,pass=password,ro //0.0.0.0/sambashare /dev/shm/lazero/sambaroot/
	fi

fi
err=0
#./loadram.sh
# if umount failed, do not delete shit.
# check lines. if more than one then there must be error.
# sudo umount /dev/shm/lazero/ramdisk
# here's the command! do not do this unless it is necessary.
psk=$(sudo mount | grep /dev/shm/lazero/ramdisk | wc -c)
psl=$(sudo mount | grep /dev/shm/lazero/ramdisk | wc -l)
if [ $psk -eq 0 ]
then
	sudo umount -Afr /dev/shm/lazero/ramdisk
	sudo rm -rf /dev/shm/lazero/ramdisk
	sudo mkdir -p /dev/shm/lazero/ramdisk
	sudo chmod 777 /dev/shm/lazero/ramdisk
	sudo mount -t tmpfs -o size=10m myramdisk /dev/shm/lazero/ramdisk
else
	psk=$(sudo mount | grep /dev/shm/lazero/ramdisk | grep "type tmpfs" | wc -c)
	if [ $psk -eq 0 ]
	then
		err=$(( 1 + $err ))
	fi

	if [ $psl -ne 1 ]
	then
		err=$(( 1 + $err ))
	fi
	if [ $err -ne 0 ]
	then
		sudo umount -Afr /dev/shm/lazero/ramdisk
		sudo rm -rf /dev/shm/lazero/ramdisk
		sudo mkdir -p /dev/shm/lazero/ramdisk
		sudo chmod 777 /dev/shm/lazero/ramdisk
		sudo mount -t tmpfs -o size=10m myramdisk /dev/shm/lazero/ramdisk
	fi
fi
#./loadram.sh
touch /dev/shm/lazero/ramdisk/tmux
# if umount failed, do not delete 
proot -0 -r /dev/shm/lazero/sambaroot -b /dev/shm/lazero/ramdisk:/ramdisk -b /dev/shm/lazero/ramdisk/tmux:$(which tmux) -w /ramdisk
