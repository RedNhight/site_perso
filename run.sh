#!/bin/bash

cleanup() {
	processes=$(ps ax | grep "python3 manage.py" | grep -v grep | awk '{print $1}')
	for pid in $processes; do
		echo "Closing the script"
	        kill -9 $pid
	done
	exit 1

}

trap cleanup SIGINT

pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver &
PID=$!
echo $PID
google-chrome http://127.0.0.1:8000/
wait $PID

