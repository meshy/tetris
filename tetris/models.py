import random


pieces = {
    'T': (
        ((-1, 0), (0, 0), (1, 0), (0, -1)),
        ((0, -1), (0, 0), (1, 0), (0, 1)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, -1), (-1, 0), (0, 0), (0, 1)),
    ),
    'J': (
        ((0, -1), (0, 0), (-1, 1), (0, 1)),
        ((-1, -1), (-1, 0), (0, 0), (1, 0)),
        ((0, -1), (1, -1), (0, 0), (0, 1)),
        ((-1, 0), (0, 0), (1, 0), (1, 1)),
    ),
    'Z': (
        ((-1, 0), (0, 0), (0, 1), (1, 1)),
        ((1, -1), (0, 0), (1, 0), (0, 1)),
    ),
    'O': (
        ((-1, 0), (0, 0), (-1, 1), (0, 1)),
    ),
    'S': (
        ((0, 0), (1, 0), (-1, 1), (0, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
    ),
    'L': (
        ((0, -1), (0, 0), (0, 1), (1, 1)),
        ((-1, 0), (0, 0), (1, 0), (-1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (-1, 0), (0, 0), (1, 0)),
    ),
    'I': (
        ((0, -2), (0, -1), (0, 0), (0, 1)),
        ((-2, 0), (-1, 0), (0, 0), (1, 0)),
    ),
}

class Piece:
    def __init__(self, tetrimino, index):
        self.tetrimino = tetrimino
        self.index = index

    def get_matrix(self):
        return pieces[self.tetrimino][self.index]

    def next_piece(self):
        next_index = self.index+1
        next_index %= len(pieces[self.tetrimino])
        return Piece(self.tetrimino, next_index)


class Board:
    def __init__(self, width, height):
        self.startpoint = width/2
        self.pieces = [TPiece, SquarePiece, LLPiece, RLPiece, BarPiece, LSPiece, RSPiece]
        self.current_piece = self.random_piece()
        self.next_piece = self.random_piece()
        self.has_piece = True
        self.height = height
        self.width = width
        self.blocks = [[None for _ in range(width)] for _ in range(height)]

    def step(self):
        if self.has_piece == True:
            self.move(down)
        else:
            self.introduce_piece()

    def rotate(self, rotation):
        if can_rotate(rotation):
            self.current_piece.rotate(rotation)
        else:
            pass

    def move(self, translation):
        if self.can_move(translation):
            self.current_piece.move(translation)

    def slam(self):
        if self.has_piece == True:
            while self.can_move(down):
                self.move(down)
            self.has_piece = False

    def introduce_piece(self):
        self.has_piece = True
        self.current_piece = self.next_piece
        self.next_piece = self.random_piece()

    def can_rotate(self, rotation):
        return True

    def can_move(self, translation):
        return True

    def random_piece(self):
        return random.choice(self.pieces)(self.startpoint)
