import logging
from typing import Optional

logger = logging.getLogger(__name__)


class Space:
    """Represents a single cell/space on the Game of Life board.

    Attributes:
        x: The x-coordinate of this space.
        y: The y-coordinate of this space.
        alive: Whether this space is currently alive/active.
    """

    def __init__(self, x: int, y: int, alive: bool = False) -> None:
        """Initialize a Space at given coordinates.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.
            alive: Initial alive state, defaults to False.
        """
        self.x: int = x
        self.y: int = y
        self.alive: bool = alive
        logger.debug("Space created at (%d, %d), alive=%s", x, y, alive)

    def is_alive(self) -> bool:
        """Return whether this space is alive.

        Returns:
            True if alive, False otherwise.
        """
        return self.alive

    def set_alive(self, state: bool) -> None:
        """Set the alive state of this space.

        Args:
            state: The new alive state.
        """
        self.alive = state
        logger.debug("Space (%d, %d) alive set to %s", self.x, self.y, state)

    def __repr__(self) -> str:
        return f"Space(x={self.x}, y={self.y}, alive={self.alive})"
