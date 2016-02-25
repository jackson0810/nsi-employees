from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns(
    'internal.views',
    url(r'^$', 'home', name='home'),
    url(r'^news/items/$', 'news_items', name='news_items'),
    url(r'^process/news/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'news_items', name='edit_news_items'),
)

