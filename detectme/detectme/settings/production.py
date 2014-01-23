"""Production settings and globals."""


from os import environ

from base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 25)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'detectmedb',
        'USER': 'detectmeuser',
        'PASSWORD': 'detectme',
        'HOST': 'localhost', 
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION



#TODO: Configure caches for production!!

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
#SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION



########## TOOLBAR CONFIGURATION
# NOTE: FOR DEBUGGING PURPOSES
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG = True
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1','128.30.99.198')

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END TOOLBAR CONFIGURATION


########## SENTRY CONFIGURATION
# See http://sentry.readthedocs.org/en/latest/quickstart/index.html
# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'http://890fed90c14e467ebcdf00971fd4d2e2:14719749a32d4910b3714c099608c4a4@128.52.160.245:9000/1',
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
)
########## SENTRY CONFIGURATION