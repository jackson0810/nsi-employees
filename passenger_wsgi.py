import sys
import os


INTERP = "/home/nsishell/navalsystemsinc/env/bin/python"

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/nsi')

sys.path.insert(0, cwd + '/env/bin')

os.environ['DJANGO_SETTINGS_MODULE'] = "nsi.settings.production"

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
