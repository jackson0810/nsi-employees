from django.conf import settings
from django.conf.urls import patterns, url


urlpatterns = patterns('security.views',
    url(r'^login/$', 'login_form', name='login'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^password/reset/$', 'reset_password', name='reset_password'),
    url(r'^password/create/{uuid_pattern}/{uuid_pattern}/$'.format(uuid_pattern=settings.UUID_PATTERN_REGEX), 'create_new_password',
        name='create_new_password'),
    url(r'^team/members/$', 'team_members', name='team_members'),
    url(r'^team/member/{}/$'.format(settings.UUID_PATTERN_REGEX), 'team_members', name='edit_team_member')

)
