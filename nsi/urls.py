from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^', include('internal.urls', namespace='internal')),
    url(r'^security/', include('security.urls', namespace='security')),
    url(r'^admin/', admin.site.urls),

    # Shared Application
    url(r'^shared/', include('shared.urls', namespace='shared')),

    url(r'^404/$', TemplateView.as_view(template_name='404.html',)),
    url(r'^500/$', TemplateView.as_view(template_name='500.html',)),
]
