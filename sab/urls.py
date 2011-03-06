from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    (r'', include('main.urls', namespace='main')),
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
