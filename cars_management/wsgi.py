"""
WSGI config for cars_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars_management.settings')
os.environ["AUTO_DEV"] = "ZrQEPSkKYWxleHN0ZWV2ZUBnbWFpbC5jb20="

application = get_wsgi_application()
