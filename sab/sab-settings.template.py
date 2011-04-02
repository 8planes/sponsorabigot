from settings import *

SITE_ID = 2
SITE_NAME = 'sponsorabigot'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Adam Duston', 'adam@sponsorabigot.org'),
)

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'sab',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT' : ''
        }
    }

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

MEDIA_URL = 'http://sponsorabigot.org/site_media/'
