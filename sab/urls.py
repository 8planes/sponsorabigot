from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import redirect_to

admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'', include('main.urls', namespace='main')),
    url(r'^robots.txt', 'django.views.generic.simple.direct_to_template', 
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^favicon\.ico$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 
          'path': 'images/favicon.ico', 
          'show_indexes': True}))
