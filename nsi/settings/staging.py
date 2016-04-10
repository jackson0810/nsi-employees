from .base import *


APPLICATION_URL = 'http://employees.navalsystemsinc.com'
PUBLIC_URL = 'http://navalsystemsinc.com/shared/collect/static/'

DEBUG = False
ALLOWED_HOSTS = ['employees.navalsystemsinc.com']

SECRET_KEY = os.environ['SECRET_KEY_EMPLOYEES']

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public/static'))
STATIC_URL = '/static/'

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

IS_PROD = True
IMAGE_PATH = '/home/nsishell/navalsystemsinc/nsi/public/static/img/slides'
DOCUMENT_PATH = '/home/nsishell/navalsystemsinc/nsi/shared/static/documents'
FORM_PATH = '/home/nsishell/employees.navalsystemsinc.com/nsi-employees/public/static/forms'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_SERVER'],
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
