from django.conf.urls.defaults import *
from main import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
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
    url(r'^4/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'index4.html'}),
    url(r'^donate/$', views.donate, name="donate"),
    url(r'^pledge/$', views.pledge, name="pledge"),
    url(r'^confirm_pledge/(?P<confirm_code>\w+)/$', 
        views.confirm_pledge, name="confirm_pledge"),
    url(r'^confirm_fail/(?P<confirm_code>\w+)/$', 
        views.confirm_fail, name="confirm_fail"),
    url(r'^closewindow/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'closewindow.html'}, name='closewindow')
)
