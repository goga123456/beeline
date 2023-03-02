"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import threading

from core.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
print(BASE_DIR)


def start():
    os.system(f'python {BASE_DIR}/bbb.py')


threading.Thread(target=start).start()

application = get_wsgi_application()
