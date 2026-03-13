# Game of Life - Game UI


class GameUI:

    def __init__(self):
        self.messages = []

    def display_message(self, message):

        print(message)
        self.messages.append(message)

    def display_player_status(self, player):

        status = f"{player.name} - Position: {player.position}, Cash: ${player.finances:,}"
        self.display_message(status)

    def display_game_status(self, game):

        self.display_message("=" * 50)
        self.display_message("Game Status:")
        for player in game.players:
            self.display_player_status(player)
        self.display_message("=" * 50)

    def get_player_choice(self, options):

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = int(input("Enter your choice: "))
        return choice - 1
