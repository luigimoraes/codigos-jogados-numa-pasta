#!/bin/bash

process=`ps -e | grep mysqld`

if [[ -z $process ]]
then
	echo "MySQLd process not found"
else
	kill -15 ${process::5}
fi
