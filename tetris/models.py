from enum import Enum


class State(Enum):
    empty = 0
    stationary = 1
    moving = 2


class Block:
    def __init__(self, state=State.empty):
        self.state = state


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
