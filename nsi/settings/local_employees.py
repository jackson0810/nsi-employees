from .base import *

DEBUG = True
ALLOWED_HOSTS = []
URL_HOME = 'internal'
URL_HOME_NAME = 'internal'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY_EMPLOYEES']


