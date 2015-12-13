import json

from tornado import web, websocket
from .models import Board, Rotation, Translation


class Home(web.RequestHandler):
    def get(self):
        self.render('home.html')


game_controller = GameController()


class WebSocket(websocket.WebSocketHandler):
    def open(self):
        self.game_controller = game_controller
        self.game_controller.add_client(self)

    def on_message(self, data):
        self.game_controller.handle(data)

    def on_close(self):
        self.game_controller.remove_client(self)


def to_json(board):
    data = {
        'blocks': board.blocks,
        # 'pieces': board.pieces,
    }
    return json.dumps(data)


class GameController:
    def __init__(self):
        self.board = Board(10, 20)

    def add_client(self, client):
        self.clients.append(client)
        self.update()

    def remove_client(self, client):
        self.clients.pop(client)
        self.update()

    def handle(self, message):
        actions = {
            'mleft': lambda: self.board.move(Translation.left),
            'mright': lambda: self.board.move(Translation.right),
            'mdown': lambda: self.board.move(Translation.down),
            'rleft': lambda: self.board.rotate(Rotation.left),
            'rright': lambda: self.board.rotate(Rotation.right),
            'slam': lambda: self.board.slam(),
        }
        action = actions.get(message, None)
        if action:
            action()
        self.update()

    def update(self):
        payload = to_json(self.game_controller.board)
        for client in self.clients:
            self.write_message(payload)
