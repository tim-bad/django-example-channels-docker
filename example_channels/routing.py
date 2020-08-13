# example_channels/routing.py
#from channels.routing import route
#from example.consumers import ws_connect, ws_disconnect

# channel_routing = [ route('websocket.connect', ws_connect), route('websocket.disconnect',ws_disconnect), ]
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import example.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            example.routing.websocket_urlpatterns
            )
        ),
    })
