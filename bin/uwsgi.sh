#!/bin/sh

USER=nobody
PROCESSES=1
THREADS=200

PROJDIR="$( cd "$(dirname "$0")"/.. && pwd )"
PIDFILE=$PROJDIR/var/uwsgi.pid
SOCKET=$PROJDIR/var/uwsgi.sock
LOGFILE=$PROJDIR/var/uwsgi.log

case $1 in
	start)
		if [ -f $PIDFILE ]; then
			echo "Stop uWSGI"
		    uwsgi --stop $PIDFILE
		    rm -f -- $PIDFILE
		fi
		
		echo "Start uWSGI"
		
		uwsgi \
			--chdir $PROJDIR \
			--module=webapp.wsgi:application \
			--master --pidfile=$PIDFILE \
			--processes=$PROCESSES --enable-threads --threads $THREADS \
			--disable-logging \
			--daemonize=$LOGFILE \
			--socket=$SOCKET --chown-socket $USER \
			--uid $USER
		;;
	
	stop)
		echo "Stop uWSGI"
		uwsgi --stop $PIDFILE
		rm -f -- $PIDFILE
		;;
	
	reload)
		echo "Reload uWSGI"
		uwsgi --reload $PIDFILE
		;;
	
	*)
		echo "Using uwsgi.sh start|stop|reload"
esac
