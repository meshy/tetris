from enum import Enum
import random


class State(Enum):
    empty = 0
    stationary = 1
    moving = 2


class Translation(Enum):
    left = (-1, 0)
    right = (1, 0)
    down = (0, 1)


class Rotation(Enum):
    left = -1
    right = 1


class Piece:
    def move(self, translation):
        transform = translation.value
        for orientation in self.orientations:
            for coordinate in orientation:
                coordinate[0] += transform[0]
                coordinate[1] += transform[1]

    def get_coords(self):
        return self.orientations[self.rotation]

    def rotate(self, rotation):
        limit = len(self.orientations) + 1
        self.rotation += rotation.value + limit
        self.rotation %= limit


class TPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 2, 0], [startpoint, 1]],
            [[startpoint, 0], [startpoint, 1], [startpoint, 2], [startpoint + 1, 1]],
            [[startpoint, 0], [startpoint - 1, 1], [startpoint, 1], [startpoint + 1, 1]],
            [[startpoint, 0], [startpoint - 1, 1], [startpoint, 1], [startpoint, 2]],
        ]


class SquarePiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 2, 0], [startpoint, 1]],
        ]

    def rotate(self, rotation):
        pass


class LLPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 2, 0], [startpoint + 2, 1]],
            [[startpoint, 2], [startpoint + 1, 0], [startpoint + 1, 1], [startpoint + 1, 2]],
            [[startpoint, 0], [startpoint, 1], [startpoint + 1, 1], [startpoint + 2, 1]],
            [[startpoint, 0], [startpoint + 1, 0], [startpoint, 1], [startpoint, 2]],
        ]


class RLPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 2, 0], [startpoint, 1]],
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 1, 1], [startpoint + 1, 2]],
            [[startpoint + 2, 0], [startpoint, 1], [startpoint + 1, 1], [startpoint + 2, 1]],
            [[startpoint, 0], [startpoint, 1], [startpoint, 2], [startpoint + 1, 2]],
        ]


class BarPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint - 1, 1], [startpoint , 1], [startpoint + 1, 1], [startpoint + 2, 1]],
            [[startpoint, 0], [startpoint, 1], [startpoint, 2], [startpoint, 3]],
        ]


class LSPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint, 0], [startpoint + 1, 0], [startpoint + 1, 1], [startpoint + 2, 1]],
            [[startpoint + 2, 0], [startpoint + 1, 1], [startpoint + 2, 1], [startpoint + 1, 2]],
        ]


class RSPiece(Piece):
    def __init__(self, startpoint):
        self.rotation = 0
        self.orientations = [
            [[startpoint + 1, 0], [startpoint + 2, 0], [startpoint, 1], [startpoint + 1, 1]],
            [[startpoint, 0], [startpoint, 1], [startpoint + 1, 1], [startpoint + 1, 2]],
        ]


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
