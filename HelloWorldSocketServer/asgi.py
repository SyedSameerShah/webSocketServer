"""
ASGI config for HelloWorldSocketServer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from SocketServer_app.consumers import HelloConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloWorldSocketServer.settings')


# application = get_asgi_application()

# asgi.py

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("wss://hello/", HelloConsumer.as_asgi()),
        ])
    ),
})

