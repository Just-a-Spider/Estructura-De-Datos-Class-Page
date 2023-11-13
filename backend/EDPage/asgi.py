import os
from django.core.asgi import get_asgi_application
from django.utils.module_loading import import_string

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EDPage.settings')

application = get_asgi_application()