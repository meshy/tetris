from tornado import web, websocket


class Home(web.RequestHandler):
    def get(self):
        self.render('home.html')


class WebSocket(websocket.WebSocketHandler):
    def open(self):
        self.write_message('Connection OPEN!')

    def on_message(self, data):
        self.write_message('Got message:')
        self.write_message(data)

    def on_close(self):
        pass
