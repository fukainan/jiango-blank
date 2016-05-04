PROJECT_DIR=/data/www
USER=nobody
PROCESSES=1
SOCK=$PROJECT_DIR/var/uwsgi.sock

chown $USER $PROJECT_DIR

uwsgi \
--chdir $PROJECT_DIR \
--module=webapp.wsgi:application \
--master --pidfile=$PROJECT_DIR/var/uwsgi.pid \
--processes=$PROCESSES --enable-threads \
--disable-logging \
--daemonize=$PROJECT_DIR/var/uwsgi.log \
--socket=$SOCK \
--uid $USER
