import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


class GameUI:
    """User-interface helper for displaying game information.

    Attributes:
        messages: History of all messages displayed.
    """

    def __init__(self) -> None:
        """Initialize GameUI with empty message history."""
        self.messages: List[str] = []
        logger.debug("GameUI initialized")

    def display_message(self, message: str) -> None:
        """Print and record a message.

        Args:
            message: The message to display.
        """
        print(message)
        self.messages.append(message)

    def display_player_status(self, player) -> None:
        """Display the current status of a player.

        Args:
            player: A Player object with name, position, and finances attributes.
        """
        status = (
            f"{player.name} - "
            f"Position: {player.position}, "
            f"Cash: ${player.finances:,}"
        )
        self.display_message(status)

    def display_game_status(self, game) -> None:
        """Display the status of all players in the game.

        Args:
            game: A GameManager (or Game) object with a players list.
        """
        self.display_message("=" * 50)
        self.display_message("Game Status:")
        for player in game.players:
            self.display_player_status(player)
        self.display_message("=" * 50)

    def get_player_choice(self, options: List[str]) -> int:
        """Prompt the player to choose from a numbered list of options.

        Args:
            options: List of option strings to display.

        Returns:
            Zero-based index of the chosen option.
        """
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter your choice: "))
            return choice - 1
        except ValueError:
            logger.warning("Invalid choice entered; defaulting to 0")
            return 0
