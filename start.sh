uwsgi \
--chdir /www/webapp/ \
-M --pidfile var/uwsgi.pid \
-L -s var/uwsgi.sock \
-p 4 --uid nobody \
--env "DJANGO_SETTINGS_MODULE=webapp.settings" \
-w "django.core.handlers.wsgi:WSGIHandler()" \
-d var/uwsgi.log