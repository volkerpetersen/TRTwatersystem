# see A2 Hosting tutorial
# https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-django-on-linux-shared-hosting
#
# https://www.a2hosting.co.uk/kb/developer-corner/python/using-a-newer-version-of-python

import os
import sys

# to eliminate the A2 Hosting cpanel deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

# Set up paths and environment variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'OSM_website.settings'

# add your project directory to the sys.path
project_home = '/home/southme1/oratorio.org'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set script name for the PATH_INFO fix below
SCRIPT_NAME = os.getcwd()


class PassengerPathInfoFix(object):
    """
        Sets PATH_INFO from REQUEST_URI because Passenger doesn't provide it.
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        from urllib.parse import unquote
        environ['SCRIPT_NAME'] = SCRIPT_NAME
        request_uri = unquote(environ['REQUEST_URI'])
        script_name = unquote(environ.get('SCRIPT_NAME', ''))
        offset = request_uri.startswith(
            script_name) and len(environ['SCRIPT_NAME']) or 0
        environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
        return self.app(environ, start_response)

# Set the application
application = get_wsgi_application()
application = PassengerPathInfoFix(application)
