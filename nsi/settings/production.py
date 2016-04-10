from .base import *


APPLICATION_URL = 'http://employees.n-s-i.us'
PUBLIC_URL = 'http://n-s-i/shared/collect/static/'

DEBUG = False
ALLOWED_HOSTS = ['employees.n-s-i.us']

SECRET_KEY = os.environ['EMP_SECRET_KEY_PROD']

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public/static'))
STATIC_URL = '/static/'

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

IS_PROD = True
IMAGE_PATH = '/home/nsishell/n-s-i/nsi/public/static/img/slides'
DOCUMENT_PATH = '/home/nsishell/n-s-i/nsi/shared/static/documents'
FORM_PATH = '/home/nsishell/employees.n-s-i/nsi-employees/public/static/forms'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME_PROD'],
        'USER': os.environ['DATABASE_USER_PROD'],
        'PASSWORD': os.environ['DATABASE_PASSWORD_PROD'],
        'HOST': os.environ['DATABASE_SERVER_PROD'],
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
