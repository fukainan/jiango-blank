# -*- coding: utf-8 -*-
# Django settings for webapp project.
# @author: Yefei
# @version: $Id:$
import os
from django.template.base import add_to_builtins

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 调试模式
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# 错误收集邮件
ADMINS = (
    ('Yefei', '316606233@qq.com'),
)

MANAGERS = ADMINS

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jiango-blank',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

DATETIME_FORMAT = 'y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'upload')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/upload/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

PUBLIC_ROOT = os.path.join(BASE_DIR, 'public')
PUBLIC_URL = '/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '##SECRET_KEY##'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'webapp.context_processors.config',
)

ROOT_URLCONF = 'webapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'webapp.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jiango',
    'jiango.bootstrap',
    'jiango.pagination',
    'jiango.admin',
#    'jiango.captcha',
#    'jiango.cms',
)

JIANGO_CMS_MODELS = {
#    'article': {
#        'name': u'文章',
#        'model': 'webapp.cms.models.Article',
#        'form': 'webapp.cms.forms.ArticleForm',
#        'index_view': 'path.to.views.index',
#        'list_view': 'path.to.views.list',
#        'content_view': 'path.to.views.content',
#    },
}

ROOT_DOMAIN = '.lvh.me'
SESSION_COOKIE_DOMAIN = ROOT_DOMAIN
CSRF_COOKIE_DOMAIN = ROOT_DOMAIN

# 调试配置
if DEBUG:
    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    MIDDLEWARE_CLASSES.append('jiango.debug.middleware.SQLDebugMiddleware')
    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS.append('jiango.debug')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

add_to_builtins('jiango.bootstrap.templatetags.bootstrap')
add_to_builtins('jiango.pagination.templatetags.pagination')
add_to_builtins('jiango.serializers.templatetags.serializers')
