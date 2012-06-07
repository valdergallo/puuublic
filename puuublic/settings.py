# -*- coding: utf-8 -*-
import os, sys
BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))

print BASEDIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Valder Gallo', 'valdergallo@gmail.com'),
    ('Ellison Leão', 'ellisonleao@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'db', 'puuublic.sqlite'),
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    },
}

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-BR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASEDIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASEDIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    MEDIA_ROOT,
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
FILEBROWSER_DIRECTORY = 'filebrowser/'
GRAPPELLI_ADMIN_TITLE = 'Puuublic Admin'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2l+i-5to%g7l-5t3j*#uc7uu#iudn8zf+h0u=f@nzpy4%jfj-%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'puuublic.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'puuublic.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASEDIR, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #admin
    'grappelli',
    'tinymce',
    'filebrowser',
    #admin default
    'django.contrib.admin',
    'django.contrib.admindocs',
    #projet apps
    'puuublic',
    'core',
    'publication',
    'friendship',
    'website',
    #plugins
    'sorl.thumbnail',
    'endless_pagination',
    'debug_toolbar',
    'django_dynamic_fixture',
    'coverage',
    #'south',
    #'registration', #TODO: make this work
)

AUTH_PROFILE_MODULE = 'friendship.UserProfile'

#registration
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'valdergallo@gmail.com'
LOGIN_REDIRECT_URL = '/'

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS':False
}

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

COVERAGE_MODULES = (
                    'Publication',
                    'core',
                    'friendship',
                    'website',
                    )


DDF_DEFAULT_DATA_FIXTURE = 'sequential'
DDF_NUMBER_OF_LAPS = 1
DDF_USE_LIBRARY = False
DDF_VALIDATE_ARGS = True

TINYMCE_JS_URL = MEDIA_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_URL + 'tiny_mce'
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = True
TINYMCE_GZ = True

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': '::memory::'}
    del AUTH_PROFILE_MODULE

