# Game of Life - Board

from space import Space


class BoardBase:

    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
        self.spaces = []

    def build(self):
        pass


class BoardLayout(BoardBase):

    def build(self):

        for i in range(1, 121):
            if i == 1:
                self.spaces.append(Space(i, "Start"))
            elif i == 120:
                self.spaces.append(Space(i, "Retirement"))
            elif i % 12 == 2:
                self.spaces.append(Space(i, "Career Choice"))
            elif i % 12 == 3:
                self.spaces.append(Space(i, "House Choice"))
            elif i % 12 == 4:
                self.spaces.append(Space(i, "Payday"))
            elif i % 12 == 5:
                self.spaces.append(Space(i, "Life Event"))
            else:
                self.spaces.append(Space(i, "Regular"))


class BoardActions:

    def add_space(self, space):
        self.spaces.append(space)

    def remove_space(self, space):
        self.spaces.remove(space)


class Board(BoardLayout, BoardActions):

    def __init__(self, width=0, height=0):
        super().__init__(width, height)
        self.build()