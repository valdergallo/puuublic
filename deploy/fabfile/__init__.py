#!/usr/bin/python
# encoding: utf-8
from __future__ import with_statement
import fabconfig

from fabric.api import *
from fabric.colors import *
from contextlib import contextmanager as _contextmanager


@_contextmanager
def virtualenv():
    with cd(env.path):
        with prefix(env.activate):
            yield

@task
def test():
    with virtualenv():
        "Test connection with server"
        run('echo $PWD')
        run('uptime')
        run('uname -a')
        run('python -V')
        

@task
def install_packages():
    with virtualenv():
        run('pip install -r deploy/requeriments.txt')

@task
def migrate_db():
    with virtualenv():
        run('python manage.py migrate')

@task
def pull():
    with virtualenv():
        run("git pull")

@task
def uninstall(package):
    with virtualenv():
        run('pip uninstall %s' % package)

@task
def deploy():
    with virtualenv():
        print(yellow('Send files'))
        run("git checkout -f")
        run("git pull")
        print(yellow('End'))
    install_packages()
    
@task
def command(command):
    with virtualenv():
        run('python manage.py %s' % command)

@task
def git(command):
    with virtualenv():
        run("git %s" % command)