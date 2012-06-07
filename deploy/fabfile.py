#!/usr/bin/python
# encoding: utf-8
from __future__ import with_statement
import os
import sys
from fabric.api import cd, run, prefix, task, env
from fabric.colors import yellow, green
from contextlib import contextmanager as _contextmanager

BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(BASEDIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'puuublic.settings'

# globals
env.hosts = ['stage.puuublic.com']
env.project = 'puuublic'
env.user = 'valder'
env.password = 'v11a82'
#/home/valder/stage.puuublic.com
env.path = '~/stage.puuublic.com/puuublic/'
env.activate = 'source ~/.virtualenvs/puuublic-pack/bin/activate'
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
        dabase_path = os.path.join(env.path, 'db', 'puuublic.sqlite')
        try:
            run("rm %s" % dabase_path)
        except:
            print green('Database File doest not exist')
        run('python manage.py syncdb')


@task
def migrate_db():
    "Migrate database"
    with virtualenv():
        print(yellow('Migrate database'))
        run('python manage.py migrate')
        print(green('Done'))


@task
def pull():
    "Pull files from codebase to server"
    with virtualenv():
        print(green('Done'))
        print(yellow('Pull files from server'))
        run("git fetch")
        print(yellow('Reset Head'))
        run("git checkout master -f")
        run("git log -n 1")
        print(green('Done'))


@task
def restart():
    "Restart webserver"
    with virtualenv():
        print(yellow('Restart server'))
        run("touch ../tmp/restart.txt")
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
