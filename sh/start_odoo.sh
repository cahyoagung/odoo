#!/bin/sh
# check parameter
: '
if [ ! $1 ]; then
	echo "odoo-start.sh need 1 parameter like 'openerp_server.conf'"
	echo "that was located in 'odoo_conf' folder inside odoo source folder"
	echo "e.g: /home/user_name/odoo/odoo_conf/openerp_server.conf"
	exit 1
fi'

if [ $2 ]; then
	echo "odoo-start.sh can only get 1 parameter"
	echo "odoo-start.sh need 1 parameter like 'openerp_server.conf'"
	echo "that was located in 'odoo_conf' folder inside odoo source folder"
	echo "e.g: /home/user_name/odoo/odoo_conf/openerp_server.conf"
	exit 1
fi

# Better OS/400 detection: see Bugzilla 31132
os400=false
case "`uname`" in
OS400*) os400=true;;
esac

# set parameter
loc=$(pwd)					# store current directory name
exe_file=odoo.py			# store exe file name
pid_file=my-odoo.pid		# store process id
cfg_file=$loc/odoo_conf		# store configuration file name
last_cfg=server.cfg			# store last used configuration file name, used by odoo-restart.sh

# check configuration file exists
if [ $1 ]; then
	cfg_file=$cfg_file/$1
else
	cfg_file=$cfg_file/openerp_server.conf
fi
if [ ! -f "$cfg_file" ]; then
	echo "Cannot found $cfg_file"
	echo "No such file or directory"
	exit 1
fi

# check config
if [ -f "$loc/check_config.sh" ]; then
	exec sh $loc/check_config.sh $cfg_file
else
	echo "Cannot found check_config.sh"
	echo "No such file or directory."
	exit 1
fi

# Check that target executable exists
if $os400; then
  # -x will Only work on the os400 if the files are:
  # 1. owned by the user
  # 2. owned by the PRIMARY group of the user
  # this will not work if the user belongs in secondary groups
  eval
else
  if [ ! -x "$loc"/"$exe_file" ]; then
    echo "Cannot find $loc/$exe_file"
    echo "The file is absent or does not have execute permission"
    echo "This file is needed to run this program"
    exit 1
  fi
fi

# execute commands
if [ ! -f "$loc"/"$pid_file" ]; then
	echo "Starting odoo-server..."
	if [ -f "$loc"/"$exe_file" ]; then
		python "$loc/$exe_file" -c $cfg_file & echo $! >"$loc/$pid_file"
		rc=$?
		
    	if [ $rc != 0 ]; then
			if [ -f "$loc"/"$pid_file" ]; then
				rm "$loc"/"$pid_file"
			fi
			if [ -f "$loc/$last_cfg" ]; then
				rm $loc/$last_cfg
			fi
			sleep 1
			echo "Error when starting odoo-server"
			echo "Odoo-server not started."
		else
			echo $1 >"$loc/$last_cfg"
			sleep 1
			echo "Odoo-server started."
		fi
	else
		sleep 1
		echo "Cannot found odoo.py"
		echo "Odoo-server not started."
	fi
else
	read pid < "$loc"/"$pid_file"
	ps -p $pid > /dev/null
	r=$?
	if [ $r -eq 0 ]; then
    	echo "Odoo-server is currently running, not executing twice, exiting now..."
    	exit 1
	else
		rm "$loc"/"$pid_file"
		if [ -f "$loc/$last_cfg" ]; then
			rm $loc/$last_cfg
		fi
		sleep 1
		echo "Odoo-server is not running."
	fi
fi

exit 0
