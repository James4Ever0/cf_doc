#!/bin/bash
# you should only observe attached session only.
#rpd=""
pwx=$( screen -ls | grep jailscreen | grep Detached | wc -l )
if [ $pwx -eq 1 ]
then
	./reattach_nocreate.sh
	# there's the x command. what is that?
	# it won't change shit. always need to reconsider.
else
	pwy=$( screen -ls | grep Detached | grep -Eo "[0-9]+\.jailscreen" | wc -l)
	#pwy=$( echo $pwx | wc -l )
#	echo $pwy
#	echo $pwx
	pwz=$( fish -c "random 0 $(( $pwy - 1 ))" )
	rz=0
	screen -ls | grep Detached | grep -Eo "[0-9]+\.jailscreen" | while read F;	do
		if [ $rz -eq $pwz ]
		then
			echo $F > /dev/shm/tmp_store
#			echo $F
#			screen -r $F
#			echo bingo $F
		fi
#		echo $rz
		rz=$(( 1 + $rz ))
	done
#	echo $arr
#	echo $pwz
#	rpd= ${arr[$pwz]}
# i have to say that this is shit.
	screen -r $( cat /dev/shm/tmp_store )
fi
	# feed arbitrary shit and use option -x.
# tmux capture-pane -epJ -t 0
# search it in pip packages.
