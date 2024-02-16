from django.urls import re_path

from .consumers import MeuConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', MeuConsumer.as_asgi()),
]
