imort os,sys
os.environ['DJANGO_SETTTIONS_MODULE']='learning_log.settings'
sys.path.append('d:/learing_log')

import django.core.handers.wsgj
application = django.core.handlers.wsgi.WSGIHandler()
