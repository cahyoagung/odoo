#!/bin/sh
loc=$(pwd)						# store current directory name
pid_file=my-odoo.pid			# store process id
last_cfg=server.cfg				# store last used configuration file path, used by odoo-restart.sh

if [ -f "$loc"/"$pid_file" ]; then
	read pid < "$loc"/"$pid_file"
	ps -p $pid > /dev/null
	r=$?
	if [ $r -eq 0 ]; then
		echo "Stopping odoo-server now..."
		kill -9 $pid
		rm "$loc"/"$pid_file"
		if [ -f "$loc/$last_cfg" ]; then
			rm $loc/$last_cfg
		fi
		sleep 1
		echo "Odoo-server stoped."
	else
		rm "$loc"/"$pid_file"
		if [ -f "$loc/$last_cfg" ]; then
			rm $loc/$last_cfg
		fi
		sleep 1
		echo "Odoo-server is curently stoped."
	fi
else
	echo "Odoo-server is curently stoped."
fi

exit 0
