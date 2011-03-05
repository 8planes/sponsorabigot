from settings import *

SITE_ID = 2
SITE_NAME = 'sponsorabigot'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Adam Duston', 'adam@sponsorabigot.com'),
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
