import logging
from enum import Enum
from typing import List, Optional

from space import Space

logger = logging.getLogger(__name__)


class SpaceType(Enum):
    """Enumeration of all space types on the Game of Life board."""

    START = "Start"
    CAREER_CHOICE = "Career Choice"
    HOUSE_CHOICE = "House Choice"
    PAYDAY = "Payday"
    LIFE_EVENT = "Life Event"
    RETIREMENT = "Retirement"
    REGULAR = "Regular"


class BoardSpace:
    """Represents a numbered space on the Game of Life track board.

    Attributes:
        space_number: The sequential position number on the board track.
        space_type: The type of action this space triggers.
    """

    def __init__(self, space_number: int, space_type: str) -> None:
        """Initialize a BoardSpace.

        Args:
            space_number: The position number on the board.
            space_type: The type string for this space.
        """
        self.space_number: int = space_number
        self.space_type: str = space_type
        logger.debug("BoardSpace created: #%d (%s)", space_number, space_type)

    def __repr__(self) -> str:
        return f"BoardSpace({self.space_number}, {self.space_type})"


class Board:
    """Represents the Game of Life board.

    Can be used as a 2D grid board (width x height) for Conway-style play,
    or as a 120-space track board via the track_spaces attribute.

    Attributes:
        width: The width of the grid board.
        height: The height of the grid board.
        spaces: List of Space objects for grid-mode play.
        track_spaces: List of BoardSpace objects for track-mode play.
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initialize the Board.

        Args:
            width: Grid width. If both width and height are 0, the 120-space
                   track board is initialized instead.
            height: Grid height.

        Raises:
            ValueError: If width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Board dimensions must be non-negative")
        self.width: int = width
        self.height: int = height
        self.spaces: List[Space] = []
        self.track_spaces: List[BoardSpace] = []
        if width == 0 and height == 0:
            self._initialize_track()
        logger.debug("Board created: %dx%d", width, height)

    def _initialize_track(self) -> None:
        """Build the 120-space track board with typed spaces."""
        for i in range(1, 121):
            if i == 1:
                space_type = SpaceType.START.value
            elif i == 120:
                space_type = SpaceType.RETIREMENT.value
            elif i % 12 == 2:
                space_type = SpaceType.CAREER_CHOICE.value
            elif i % 12 == 3:
                space_type = SpaceType.HOUSE_CHOICE.value
            elif i % 12 == 4:
                space_type = SpaceType.PAYDAY.value
            elif i % 12 == 5:
                space_type = SpaceType.LIFE_EVENT.value
            else:
                space_type = SpaceType.REGULAR.value
            self.track_spaces.append(BoardSpace(i, space_type))
        logger.debug("Track board initialized with %d spaces", len(self.track_spaces))

    def add_space(self, space: Space) -> None:
        """Add a Space to the grid board.

        Args:
            space: The Space object to add.
        """
        self.spaces.append(space)
        logger.debug("Space added at (%d, %d)", space.x, space.y)

    def remove_space(self, space: Space) -> None:
        """Remove a Space from the grid board.

        Args:
            space: The Space object to remove.

        Raises:
            ValueError: If the space is not on the board.
        """
        if space not in self.spaces:
            raise ValueError(f"Space at ({space.x}, {space.y}) not found on board")
        self.spaces.remove(space)
        logger.debug("Space removed at (%d, %d)", space.x, space.y)

    def get_track_space(self, position: int) -> Optional[BoardSpace]:
        """Get a track space by 1-indexed position.

        Args:
            position: The 1-indexed position number (1-120).

        Returns:
            The BoardSpace at that position, or None if out of range.
        """
        if 1 <= position <= len(self.track_spaces):
            return self.track_spaces[position - 1]
        return None

    def __repr__(self) -> str:
        return f"Board(width={self.width}, height={self.height}, spaces={len(self.spaces)})"