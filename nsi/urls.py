from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^', include('{}.urls'.format(settings.URL_HOME), namespace=settings.URL_HOME_NAME)),

    url(r'^admin/', admin.site.urls),

    # Shared Application
    url(r'^shared/', include('shared.urls', namespace='shared')),
]
