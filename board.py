class Space:
    def __init__(self, space_number, space_type):
        self.space_number = space_number
        self.space_type = space_type

class Board:
    def __init__(self):
        self.spaces = []
        self._initialize_board()
    
    def _initialize_board(self):
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