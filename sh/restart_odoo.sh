#!/bin/sh
# check parameter input
if [ $1 ]; then
	echo "odoo-restart.sh does not need any parameter"
	exit 1
fi

# set parameter
loc=$(pwd)						# store current directory name
pid_file=my-odoo.pid			# store process id
exe_file=start_odoo.sh			# store execute file name
last_cfg=server.cfg				# store last used configuration file path, used by restart_odoo.sh

if [ -f "$loc"/"$pid_file" ]; then
	read pid < "$loc"/"$pid_file"
	ps -p $pid > /dev/null
	r=$?
	if [ $r -eq 0 ]; then
    	echo "Odoo-server is currently running, Stopping odoo-server now..."
		kill -9 $pid
		rm "$loc"/"$pid_file"
		sleep 1
		echo "Odoo-server stoped."
		echo "Restarting odoo-server now..."
		if [ -f "$loc/$last_cfg" ]; then
			read cfg < "$loc"/"$last_cfg"
			if [ ! -f "$loc/$exe_file" ]; then
				if [ -f "$loc/$last_cfg" ]; then
					rm $loc/$last_cfg
				fi
				echo "$exe_file not found, odoo-server not started."
				exit 1
			fi
			exec sh "$loc"/$exe_file "$cfg"
			rc=$?
			if [ $rc !=0 ]; then
				if [ -f "$loc/$last_cfg" ]; then
					rm $loc/$last_cfg
				fi
			fi
		else
			sleep 1
			echo "Cannot restart odoo-server, server.cfg not found."
			echo "Please use $exe_file to run odoo-server."
			exit 1
		fi
	else
		if [ -f "$loc/$pid_file" ]; then
			rm "$loc"/"$pid_file"
		fi
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
