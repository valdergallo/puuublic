#!/usr/bin/python
# # encoding: utf-8
from fabric.api import env

# globals
env.hosts = ['puuublic.com']
env.project = 'puuublic'
env.user = 'valder'
env.path = '~/puuublic-pack/puuublic'
env.activate = 'source ~/puuublic-pack/bin/activate'
env.colors = True
env.format = True