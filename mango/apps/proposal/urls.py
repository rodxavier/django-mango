from django.conf.urls import patterns, include, url


urlpatterns = patterns('proposal.views',
    url(r'^$', 'proposal_list', name='proposal_list'),
    url(r'^create/$', 'proposal_create', name='proposal_create'),
)
