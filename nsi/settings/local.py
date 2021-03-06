from .base import *


APPLICATION_URL = 'http://employees.nsilocal:8889'
PUBLIC_URL = 'http://nsilocal:8890/shared/collect/static/'

DEBUG = True
ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = os.environ['SECRET_KEY_EMPLOYEES']

STATIC_ROOT = os.path.dirname(BASE_DIR) + '/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

IS_PROD = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nsi',
        'USER': 'nsi',
        'PASSWORD': 'nsi',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# DJANGO-STRONGHOLD
STRONGHOLD_DEFAULTS = False
STRONGHOLD_PUBLIC_URLS = (
    r'^%s.+$' % STATIC_URL,
    r'^/__debug__/.+$',  # needed for django debug toolbar
    r'^/security/(.+)?$',
)