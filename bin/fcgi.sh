#!/bin/sh

THREADS=200

PROJDIR="$( cd "$(dirname "$0")"/.. && pwd )"
PIDFILE=$PROJDIR/var/fcgi.pid
SOCKET=$PROJDIR/var/fcgi.sock
OUTLOG=$PROJDIR/var/fcgi.log
ERRLOG=$PROJDIR/var/fcgi-error.log
MANAGEFILE=$PROJDIR/manage.py

case $1 in
	start)
		if [ -f $PIDFILE ]; then
			echo "Stop Fcgi"
		    kill `cat $PIDFILE`
		    rm -f -- $PIDFILE
		fi
		
		echo "Start Fcgi"
		
		python $MANAGEFILE runfcgi \
			method=threaded \
			maxspare=$THREADS maxchildren=$THREADS \
			daemonize=true \
			pidfile=$PIDFILE \
			socket=$SOCKET umask=000 \
			workdir=$PROJDIR \
			outlog=$OUTLOG \
			errlog=$ERRLOG
		;;
	
	stop)
		echo "Stop Fcgi"
		kill `cat $PIDFILE`
		rm -f -- $PIDFILE
		;;
	
	*)
		echo "Using fcgi.sh start|stop"
esac
