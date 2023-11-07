import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.utils.module_loading import import_string

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EDPage.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        import_string('exercises.routing.websocket_urlpatterns')
    ),
})