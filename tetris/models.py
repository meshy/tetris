from enum import Enum


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


class Block:
    def __init__(self, state=State.empty):
        self.state = state


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
        self.rotation +=  rotation.value + limit
        self.rotation %= limit


class TPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 2, 0], [midpoint, 1]],
            [[midpoint, 0], [midpoint, 1], [midpoint, 2], [midpoint + 1, 1]],
            [[midpoint, 0], [midpoint - 1, 1], [midpoint, 1], [midpoint + 1, 1]],
            [[midpoint, 0], [midpoint - 1, 1], [midpoint, 1], [midpoint, 2]],
        ]


class SquarePiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 2, 0], [midpoint, 1]],
        ]

    def rotate(self, direction):
        pass


class LLPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 2, 0], [midpoint + 2, 1]],
            [[midpoint, 2], [midpoint + 1, 0], [midpoint + 1, 1], [midpoint + 1, 2]],
            [[midpoint, 0], [midpoint, 1], [midpoint + 1, 1], [midpoint + 2, 1]],
            [[midpoint, 0], [midpoint + 1, 0], [midpoint, 1], [midpoint, 2]],
        ]


class RLPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 2, 0], [midpoint, 1]],
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 1, 1], [midpoint + 1, 2]],
            [[midpoint + 2, 0], [midpoint, 1], [midpoint + 1, 1], [midpoint + 2, 1]],
            [[midpoint, 0], [midpoint, 1], [midpoint, 2], [midpoint + 1, 2]],
        ]


class BarPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint - 1, 1], [midpoint , 1], [midpoint + 1, 1], [midpoint + 2, 1]],
            [[midpoint, 0], [midpoint, 1], [midpoint, 2], [midpoint, 3]],
        ]


class LSPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint, 0], [midpoint + 1, 0], [midpoint + 1, 1], [midpoint + 2, 1]],
            [[midpoint + 2, 0], [midpoint + 1, 1], [midpoint + 2, 1], [midpoint + 1, 2]],
        ]


class RSPiece(Piece):
    def __init__(self, midpoint):
        self.rotation = 0
        self.orientations = [
            [[midpoint + 1, 0], [midpoint + 2, 0], [midpoint, 1], [midpoint + 1, 1]],
            [[midpoint, 0], [midpoint, 1], [midpoint + 1, 1], [midpoint + 1, 2]],
        ]


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = [[Block() for _ in range(width)] for _ in range(height)]

    def step(self):
        if self.has_falling_blocks():
            pass
            # do_things_n_stuff()
        else:
            # create_new_falling_shape()
            pass

    def rotate(self, direction):
        pass

    def move(self, direction):
        pass

    def slam(self):
        pass

    def has_falling_blocks(self):
        for row in self.blocks:
            for block in row:
                if block.state == State.moving:
                    return True
        return False

    def introduce_piece(self):
        pass
