# Game of Life - Game


class GameBase:

    def __init__(self):
        super().__init__()
        self.players = []  # List to store player information
        self.current_turn = 0  # Track whose turn it is
        self.winner = None  # Store the winner of the game


class GameLogic(GameBase):

    def add_player(self, player_name):
        self.players.append(player_name)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def select_career(self, player_name, career):
        # Logic to assign a career/house
        pass  # Placeholder for career selection logic

    def check_win_condition(self):
        # Logic to check if a player has met the win conditions
        pass  # Placeholder for win condition logic


class Game(GameLogic):

    def __init__(self):
        super().__init__()

    def play(self):

        while not self.winner:
            current_player = self.players[self.current_turn]
            # Logic for player to take their turn
            self.next_turn()
