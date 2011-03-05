import site
site.addsitedir('/home/sab/env/lib/python2.6/site-packages')

import sys
sys.path.append('/home/sab/sab/sab')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'sab-settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
