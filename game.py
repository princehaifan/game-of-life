import logging
from typing import List, Optional

from player import Player
from board import Board, BoardSpace, SpaceType
from dice import Dice

logger = logging.getLogger(__name__)


class GameManager:
    """Centralized orchestration for the Game of Life.

    Manages turn order, player state, score calculation, and winner
    determination.

    Attributes:
        players: Ordered list of players in the game.
        board: The game board.
        dice: The shared dice/spinner.
        current_turn: Index of the player whose turn it is.
        turn_number: Cumulative turn counter.
        game_over: Whether the game has ended.
        winner: The winning player, or None.
    """

    def __init__(self) -> None:
        """Initialize the GameManager with a fresh board and dice."""
        self.players: List[Player] = []
        self.board: Board = Board()
        self.dice: Dice = Dice()
        self.current_turn: int = 0
        self.turn_number: int = 0
        self.game_over: bool = False
        self.winner: Optional[Player] = None
        logger.debug("GameManager initialized")

    def add_player(self, player: Player) -> None:
        """Add a player to the game.

        Args:
            player: The Player to add.

        Raises:
            ValueError: If the player is already in the game.
        """
        if player in self.players:
            raise ValueError(f"Player '{player.name}' is already in the game")
        self.players.append(player)
        logger.debug("Player '%s' added to game", player.name)

    def get_current_player(self) -> Optional[Player]:
        """Return the player whose turn it currently is.

        Returns:
            The current Player, or None if no players exist.
        """
        if not self.players:
            return None
        return self.players[self.current_turn]

    def next_turn(self) -> None:
        """Advance to the next player's turn."""
        if not self.players:
            return
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.turn_number += 1
        logger.debug("Advanced to turn %d, player index %d", self.turn_number, self.current_turn)

    def take_turn(self) -> int:
        """Execute the current player's turn: spin and move.

        Returns:
            The spin result.

        Raises:
            RuntimeError: If the game is already over.
        """
        if self.game_over:
            raise RuntimeError("Game is already over")
        player = self.get_current_player()
        if player is None:
            raise RuntimeError("No players in the game")
        spin = self.dice.spin()
        player.move(spin)
        logger.debug("Player '%s' spun %d, moved to position %d", player.name, spin, player.position)
        self._apply_space_effect(player)
        self.check_win_condition()
        if not self.game_over:
            self.next_turn()
        return spin

    def _apply_space_effect(self, player: Player) -> None:
        """Apply the effect of the player's current board space.

        Args:
            player: The player who just moved.
        """
        board_space = self.board.get_track_space(player.position)
        if board_space is None:
            return
        space_type = board_space.space_type
        if space_type == SpaceType.PAYDAY.value:
            player.add_money(10_000)
            logger.debug("Player '%s' collected payday: $10,000", player.name)
        elif space_type == SpaceType.RETIREMENT.value:
            player.retire()
            logger.debug("Player '%s' reached retirement", player.name)

    def check_win_condition(self) -> bool:
        """Check whether any player has won.

        A player wins by reaching or passing the Retirement space (position 120).

        Returns:
            True if a winner has been found, False otherwise.
        """
        for player in self.players:
            if player.position >= 120:
                self.game_over = True
                self.winner = player
                player.retire()
                logger.debug("Player '%s' has won the game", player.name)
                return True
        return False

    def calculate_score(self, player: Player) -> int:
        """Calculate a player's total score.

        Score = finances + sum of life tile values.

        Args:
            player: The player to score.

        Returns:
            The player's total score.
        """
        return player.calculate_wealth()

    def determine_winner(self) -> Optional[Player]:
        """Determine the winner based on highest score among all players.

        Returns:
            The Player with the highest score, or None if no players.
        """
        if not self.players:
            return None
        winner = max(self.players, key=self.calculate_score)
        logger.debug("Winner determined: '%s' with score %d", winner.name, self.calculate_score(winner))
        return winner

    def get_rankings(self) -> List[Player]:
        """Return players sorted by score descending.

        Returns:
            List of players ordered from highest to lowest score.
        """
        return sorted(self.players, key=self.calculate_score, reverse=True)

    # Legacy interface for backward compatibility
    def select_career(self, player_name: str, career: str) -> None:
        """Assign a career to a named player.

        Args:
            player_name: The name of the player.
            career: The career title to assign.
        """
        for player in self.players:
            if player.name == player_name:
                player.assign_career(career)
                return
        raise ValueError(f"Player '{player_name}' not found")

    def play(self) -> None:
        """Run the game loop until a winner is found."""
        while not self.game_over:
            self.take_turn()

    def __repr__(self) -> str:
        return (
            f"GameManager(players={len(self.players)}, "
            f"turn={self.turn_number}, over={self.game_over})"
        )
