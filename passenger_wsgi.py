# passenger_wsgi.py

import sys, os

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/chishenma_django')

if sys.version < "2.7.1": os.execl("$HOME/app.chishen.ma/venv/bin/python", "python2.7.1", *sys.argv)

sys.path.insert(0, '/Users/michelleglauser/Desktop/mobile/chishenma/app.chishen.ma/venv/bin')
sys.path.insert(0, '/Users/michelleglauser/Desktop/mobile/chishenma/app.chishen.ma/venv/lib/python2.7/site-packages')


os.environ['DJANGO_SETTINGS_MODULE'] = "chishenma_django.settings_production"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
