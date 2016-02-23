from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('internal.urls', namespace='internal')),
    url(r'^security/', include('security.urls', namespace='security')),
    url(r'^admin/', admin.site.urls),

    # Shared Application
    url(r'^shared/', include('shared.urls', namespace='shared')),
]
