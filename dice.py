# Game of Life - Dice

import random


class Dice:

    def __init__(self):
        self.last_spin = 0

    def spin(self):

        self.last_spin = random.randint(1, 10)
        return self.last_spin

    def get_last_spin(self):
        return self.last_spin

    def reset(self):
        self.last_spin = 0
