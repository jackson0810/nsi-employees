from .base import *

DEBUG = True
ALLOWED_HOSTS = ['employees.navalsystemsinc.com']
URL_HOME = 'external'
URL_HOME_NAME = 'external'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY_EMPLOYEES']
