from .controllers import Home, WebSocket


handlers = [
    (r'^/$', Home),
    (r'^/ws/$', WebSocket),
]
