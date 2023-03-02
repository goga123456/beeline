"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
print(BASE_DIR)
os.system(f'python {BASE_DIR}/bbb.py')
application = get_wsgi_application()
