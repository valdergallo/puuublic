#!/usr/bin/python
# # encoding: utf-8
from fabric.api import env

# globals
env.hosts = ['puuublic.com']
env.project = 'puuublic'
env.user = 'valder'
#/home/valder/www/puuublic/
env.path = '~/www/puuublic'
env.activate = 'source ~/.virtualenvs/puuublic-pack/bin/activate'
env.colors = True
env.format = True
