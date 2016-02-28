import os

"""
    regex explanation by parenthetical clause:
    * first block checks length (minimum of 8)
    * second block checks for at least one lowercase letter
    * third block checks for at least one uppercase letter
    * fourth block checks for at least one number
    * fifth block checks for at least one of !@#$%^&*()
    * sixth block checks to make sure there are no whitespace characters
"""
PASSWORD_REGEX = r'(?=^.{10,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*\(\)])(?=^.*[^\s].*$).*$'
UUID_PATTERN_REGEX = '([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
SITE_NAME = os.path.basename(DJANGO_ROOT)
LOGIN_URL = 'security:login'
LOGOUT_URL = 'security:logout'

# two hours
TEMP_PASSWORD_EXPIRES = 2

SETTINGS_ROOT = os.path.dirname(__file__)
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

GENERIC_ERROR = 'Please correct the error(s) highlighted below.'
GENERIC_DATABASE_ERROR = "We're sorry, an error occurred. Please try your request again in a few minutes. System administrators have been notified."

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 86400

AUTH_USER_MODEL = 'security.CustomUser'
AUTHENTICATION_BACKENDS = ['security.backends.CustomUserAuthBackend', ]

EMAIL_HOST = 'mail.navalsystemsinc.com'
APPLICATION_EMAIL = 'admin@employees.navalsystemsinc.com'
ADMINS = (('Admin', 'admin@navalsystemsinc.com'), )
EMAIL_HOST_USER = APPLICATION_EMAIL
EMAIL_HOST_PASSWORD = 'XgKfQ@Y2waXEo2CM^IOD'
SERVER_EMAIL = APPLICATION_EMAIL


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'stronghold',
]

# Applications
INSTALLED_APPS += [
    'internal',
    'security',
    'shared'
]
MIDDLEWARE_CLASSES = [
    'stronghold.middleware.LoginRequiredMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nsi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nsi.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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
