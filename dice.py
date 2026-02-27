import logging
import random
from typing import List, Optional

logger = logging.getLogger(__name__)


class Dice:
    """Represents the spinner/dice used in the Game of Life.

    Tracks statistical data across all spins including average, minimum,
    and maximum values.

    Attributes:
        last_spin: The result of the most recent spin.
        spin_history: List of all spin results in order.
    """

    MIN_VALUE: int = 1
    MAX_VALUE: int = 10

    def __init__(self) -> None:
        """Initialize the Dice with no spin history."""
        self.last_spin: int = 0
        self.spin_history: List[int] = []
        logger.debug("Dice initialized")

    def spin(self) -> int:
        """Spin the dice and return a random value between 1 and 10.

        Returns:
            A random integer in [1, 10].
        """
        result = random.randint(self.MIN_VALUE, self.MAX_VALUE)
        self.last_spin = result
        self.spin_history.append(result)
        logger.debug("Dice spun: %d", result)
        return result

    def get_last_spin(self) -> int:
        """Return the result of the most recent spin.

        Returns:
            The last spin value, or 0 if no spins have occurred.
        """
        return self.last_spin

    def get_average(self) -> float:
        """Calculate the average of all spin results.

        Returns:
            The average spin value, or 0.0 if no spins have occurred.
        """
        if not self.spin_history:
            return 0.0
        return sum(self.spin_history) / len(self.spin_history)

    def get_min(self) -> Optional[int]:
        """Return the minimum spin result so far.

        Returns:
            The minimum value, or None if no spins have occurred.
        """
        return min(self.spin_history) if self.spin_history else None

    def get_max(self) -> Optional[int]:
        """Return the maximum spin result so far.

        Returns:
            The maximum value, or None if no spins have occurred.
        """
        return max(self.spin_history) if self.spin_history else None

    def get_spin_count(self) -> int:
        """Return the total number of spins performed.

        Returns:
            Total number of spins.
        """
        return len(self.spin_history)

    def reset(self) -> None:
        """Reset the dice, clearing spin history and last spin value."""
        self.last_spin = 0
        self.spin_history = []
        logger.debug("Dice reset")

    def __repr__(self) -> str:
        return (
            f"Dice(last={self.last_spin}, count={self.get_spin_count()}, "
            f"avg={self.get_average():.2f})"
        )
