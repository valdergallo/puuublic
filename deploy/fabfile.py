#!/usr/bin/python
# encoding: utf-8
from __future__ import with_statement
import os
import sys
from fabric.api import cd, run, prefix, task, env, sudo
from fabric.colors import yellow, green
from contextlib import contextmanager as _contextmanager

BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(BASEDIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'puuublic.settings'

# globals
env.hosts = ['204.62.12.78']
env.port = 70
env.project = 'puuublic'
env.user = 'ellison'
env.password = 'cabeca1985'
#/home/valder/stage.puuublic.com
env.path = '/opt/www/puuublic.com/puuublic/'
env.activate = 'source /home/ellison/envs/puuublic/bin/activate'
env.colors = True
env.format = True


@_contextmanager
def virtualenv():
    with cd(env.path):
        with prefix(env.activate):
            yield


@task
def test():
    "Test connection with server"
    with virtualenv():
        run('echo $PWD')
        run('uptime')
        run('uname -a')
        run('python -V')


@task
def install_packages():
    "Install requeriments packs"
    with virtualenv():
        print(yellow('Install requeriments packs'))
        run('pip install -r deploy/requeriments.txt')
        print(green('Done'))


@task
def reset_db():
    "Reset database"
    with virtualenv():
        run('mysql -u puuublic -p puuublic_p@ss \
            -e "drop database puuublicprod; \
            create database puuublicprod default charset utf8;" ')
        run('python manage.py syncdb')


@task
def sync_and_migrate():
    "Migrate database"
    with virtualenv():
        print(yellow('Migrate database'))
        run('../manage.py syncdb')
        run('../manage.py migrate')
        print(green('Done'))



@task
def collectstatic():
    with virtualenv():
        print(yellow('Running collectstatic'))
        run('../manage.py collectstatic --noinput')
        print(green('Done'))

@task
def pull():
    "Pull files from codebase to server"
    with virtualenv():
        print(yellow('Reset Head'))
        run("git checkout -f")
        print(green('Done'))
        print(yellow('Pull files from server'))
        run("git pull origin master")
        print(green('Done'))
        run("git log -n 1")
        print(green('Done'))


@task
def restart():
    "Restart webserver"
    with virtualenv():
        print(yellow('Restart server'))
        sudo("supervisorctl restart puuublic")
        print(green('Done'))


@task
def uninstall(package):
    "Remove package installed"
    with virtualenv():
        run('pip uninstall %s' % package)


@task
def deploy():
    "Send files to server and restart webserver"
    pull()
    sync_and_migrate()
    collectstatic()
    restart()


@task
def command(command):
    "Send command to manage.py"
    with virtualenv():
        run('python manage.py %s' % command)


@task
def git(command):
    "Run command with git"
    with virtualenv():
        run("git %s" % command)
