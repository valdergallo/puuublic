#!/usr/bin/python
# # encoding: utf-8
from fabric.api import env

# globals
env.hosts = ['stage.puuublic.com']
env.project = 'puuublic'
env.user = 'valder'
#/home/valder/stage.puuublic.com
env.path = '~/stage.puuublic.com/puuublic'
env.activate = 'source ~/.virtualenvs/puuublic-pack/bin/activate'
env.colors = True
env.format = True
