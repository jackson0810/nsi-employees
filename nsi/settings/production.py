from .base import *


APPLICATION_URL = 'https://employees.navalsystemsinc.com'
DEBUG = True
ALLOWED_HOSTS = ['navalsystemsinc.com']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

STATIC_ROOT = os.path.dirname(BASE_DIR) + '/public/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '/public/media/')
MEDIA_URL = '/media/'

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
