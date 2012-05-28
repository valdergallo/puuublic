#!/usr/bin/python
# encoding: utf-8

from __future__ import with_statement
from fabconfig import env
from fabric.api import cd, run, prefix, task
from fabric.colors import yellow, green
from contextlib import contextmanager as _contextmanager


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
        print(yellow('Reset Files'))
        run("git checkout -f")
        print(green('Done'))
        print(yellow('Pull files from server'))
        run("git pull")
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
    "Execute command to with git"
    with virtualenv():
        run("git %s" % command)
