from django.conf import settings
from django.contrib.sites.models import Site

def add_stuff(request):
    return { 'facebook_app_id': settings.FACEBOOK_APP_ID,
             'current_site': Site.objects.get_current() }
