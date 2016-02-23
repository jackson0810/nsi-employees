from django.conf.urls import patterns, url

urlpatterns = patterns(
    'internal.views',
    url(r'^$', 'home', name='home'),
)

