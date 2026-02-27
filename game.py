class Game:
    def __init__(self):
        self.players = []  # List to store player information
        self.current_turn = 0  # To track whose turn it is
        self.winner = None  # To store the winner of the game

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

    def play(self):
        while not self.winner:
            current_player = self.players[self.current_turn]
            # Logic for player to take their turn
            self.next_turn()
