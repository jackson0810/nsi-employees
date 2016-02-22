from django.conf.urls import patterns, url

urlpatterns = patterns(
    'external.views',
    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'about_us', name='about_us'),
    url(r'^services/$', 'services', name="services"),
    url(r'^clients/partners/$', 'clients_partners', name="clients_partners"),
    url(r'^locations/china/lake/$', 'china_lake', name='china_lake'),
    url(r'^contract/vehicles/seaport-e/$', 'seaporte', name='seaporte'),
    url(r'^careers/$', 'careers', name='careers'),
    url(r'^news/$', 'news', name='news'),
)

