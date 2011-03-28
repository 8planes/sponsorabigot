import sys, site, os

prev_sys_path = list(sys.path)

site.addsitedir('/home/sab/env/lib/python2.6/site-packages')

sys.path.append('/home/sab/sab')
sys.path.append('/home/sab/sab/sab')

new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'sab-settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
