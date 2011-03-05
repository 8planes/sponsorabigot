from fabric.api import run, put, sudo, env, cd, local
import os

env.hosts = ['8planes.com']
env.user = 'sab'
env.base_dir = '/home/sab'

def update():
    with cd('{0}/sab/deploy'.format(env.base_dir)):
        run('git pull')
        env.warn_only = True
        run("find . -name '*.pyc' -print0 | xargs -0 rm")
        env.warn_only = False
        run('touch {0}.wsgi'.format(env.user))

def syncdb(app_name=''):
    with cd('{0}/sab/sab'.format(env.base_dir)):
        run('{0}/env/bin/python manage.py syncdb {1} --settings=sab-settings'.format(env.base_dir, app_name))
