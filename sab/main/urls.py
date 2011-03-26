from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    url(r'^$',
        'django.views.generic.simple.direct_to_template', 
        {'template': 'index.html'}),
    url(r'^0/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'index0.html'}),
    url(r'^1/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'index1.html'}),
    url(r'^2/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'index2.html'}),
    url(r'^3/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'index3.html'}),        
    url(r'^donate/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'donate.html'}, name="donate"),
)
