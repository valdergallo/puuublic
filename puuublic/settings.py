# -*- coding: utf8 -*-
import os
BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
SITE_URL = 'http://puuublic.com'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Ellison Leao', 'ellisonleao@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'puuublicprod',
        'USER': 'puuublic',  # Not used with sqlite3.
        'PASSWORD': 'puuublic_p@ss',  # Not used with sqlite3.
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
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT
CKEDITOR_RESTRICT_BY_USER = True

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
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.DeleteSessionOnLogoutMiddleware',
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
    "website.context_processors.global_includes",
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
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #admin
    #'grappelli',
    'filebrowser',
    'taggit',
    'ckeditor',
    #admin default
    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    #projet apps
    'puuublic',
    'core',
    'gunicorn',
    'publication',
    'friendship',
    'website',
    #plugins
    'sorl.thumbnail',
    'endless_pagination',
    'captcha',
    #'debug_toolbar',
    'south',
)

AUTHENTICATION_BACKENDS = (
    'puuublic.backends.EmailAuth',
)

CAPTCHA_NOISE_FUNCTIONS = None
#SENTRY_DSN = 'https://00b195f8daa041e9a8a704f1857a43c0:db2564599ed345f798ecc8fc0882e024@app.getsentry.com/3344'

AUTH_PROFILE_MODULE = 'friendship.UserProfile'

#CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink',
              '-', 'Youtube', 'Vimeo',
              '-', 'Preview',
            ],
        ],
        'width': 945,
        'height': 350,
        'toolbarCanCollapse': False,
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,
        'extraPlugins': 'youtube,vimeo',
        'language': 'pt-br',
    }
}


#EMAIL_HOST = 'localhost'
NO_REPLY_EMAIL = 'noreply@puuublic.com'

#SMTP Definitions
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@puuublic.com'
EMAIL_HOST_PASSWORD = 'tchuca32'
EMAIL_PORT = 587


DEFAULT_FROM_EMAIL = 'noreply@puuublic.com'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'

MAX_UPLOAD_SIZE = 3 * 1024 * 1024 # 3MB
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#LOGGING                                                                        
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

DDF_DEFAULT_DATA_FIXTURE = 'sequential'
DDF_NUMBER_OF_LAPS = 1
DDF_USE_LIBRARY = False
DDF_VALIDATE_ARGS = True

try:
    execfile(os.path.join(BASEDIR, 'puuublic/settings_local.py'))
except IOError:
    pass
