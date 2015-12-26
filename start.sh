uwsgi \
--plugin python \
--chdir /data/www/ \
--module=webapp.wsgi:application \
--master --pidfile=var/uwsgi.pid \
--processes=4 --enable-threads \
--disable-logging \
--daemonize=var/uwsgi.log \
--socket=/tmp/uwsgi-www.sock \
--uid nobody
