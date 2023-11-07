from django.urls import re_path

from . import views

websocket_urlpatterns = [
    re_path(r'ws/code_run/$', views.CodeRunnerConsumer.as_asgi()),
]