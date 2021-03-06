# coding=utf-8
from __future__ import unicode_literals
"""
WSGI config for chishenma_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chishenma_project.settings_production")



from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())


# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
