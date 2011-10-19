from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('spike.views',
    url(r'^$', 'index', name='index'),
    url(r'^logout/$', 'logout'),
    url(r'^login/$', 'login'),
)
