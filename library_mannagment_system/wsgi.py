"""
WSGI config for library_mannagment_system project.

It exposes the WSGI callable as a module-level variable named ``application``.
For Vercel deployment, it also exposes a ``handler`` variable.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_mannagment_system.settings")

# This is the standard Django WSGI application
application = get_wsgi_application()

# This is the handler that Vercel will use
# It's just an alias to the standard Django application
handler = application
