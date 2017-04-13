"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys, site

site.addsitedir("D:\learning_log\ll_env\Lib\site-packages")
#sys.path.append('d:\learning_log')
#sys.path.append('d:\learning_log\learning_log')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

