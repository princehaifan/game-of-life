class Space:
    def __init__(self, space_number, space_type, properties=None):
        self.space_number = space_number
        self.space_type = space_type
        self.properties = properties if properties else {}

class Board:
    def __init__(self):
        self.spaces = self.create_board()
    
    def create_board(self):
        spaces = []
        for i in range(1, 121):
            if i == 1:
                spaces.append(Space(i, "Start", {"message": "Start your journey!"}))
            elif i in {2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 120}:
                spaces.append(Space(i, "Career Choice"))
            elif i in {3, 15, 27, 39, 51, 63, 75, 87, 99, 111}:
                spaces.append(Space(i, "House Choice"))
            elif i in {4, 16, 28, 40, 52, 64, 76, 88, 100, 112}:
                spaces.append(Space(i, "Payday"))
            elif i in {5, 17, 29, 41, 53, 65, 77, 89, 101, 113}:
                spaces.append(Space(i, "Life Event"))
            elif i == 120:
                spaces.append(Space(i, "Retirement", {"message": "You've reached retirement!"}))
            else:
                spaces.append(Space(i, "Regular"))

        return spaces
    
    def get_space_info(self, space_number):
        if 1 <= space_number <= 120:
            return vars(self.spaces[space_number - 1])
        else:
            return None
