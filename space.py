# Game of Life - Space


class Space:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.alive = False

    def is_alive(self):
        return self.alive
