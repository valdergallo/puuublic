import sys, os
 
INTERP = os.path.join(os.environ['HOME'], 'puuublic-pack', 'bin', 'python')
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
 
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/puuublic')
os.environ['DJANGO_SETTINGS_MODULE'] = "puuublic.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
