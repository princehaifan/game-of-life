import logging
from typing import List

logger = logging.getLogger(__name__)


class CareerCard:
    """Represents a career option card in the Game of Life.

    Attributes:
        career_name: The name/title of the career.
        salary: The annual salary for this career.
    """

    def __init__(self, career_name: str, salary: float) -> None:
        """Initialize a CareerCard.

        Args:
            career_name: The career title.
            salary: Annual salary amount.

        Raises:
            ValueError: If salary is negative.
        """
        if salary < 0:
            raise ValueError(f"Salary must be non-negative, got {salary}")
        self.career_name: str = career_name
        self.salary: float = salary
        logger.debug("CareerCard created: %s, salary=%.2f", career_name, salary)

    def __str__(self) -> str:
        return f"Career: {self.career_name}, Salary: {self.salary}"


class HouseCard:
    """Represents a house option card in the Game of Life.

    Attributes:
        house_name: The name or address of the house.
        house_value: The purchase price/value of the house.
    """

    def __init__(self, house_value: float, house_name: str = "") -> None:
        """Initialize a HouseCard.

        Args:
            house_value: The value/price of the house.
            house_name: Optional name or address for the house.

        Raises:
            ValueError: If house_value is not positive.
        """
        if house_value <= 0:
            raise ValueError(f"House value must be positive, got {house_value}")
        self.house_value: float = house_value
        self.house_name: str = house_name
        logger.debug("HouseCard created: value=%.2f", house_value)

    def __str__(self) -> str:
        return f"House Value: {self.house_value}"


class LifeTileCard:
    """Represents a life event tile card in the Game of Life.

    Attributes:
        description: A human-readable description of the life event.
        value: The point value of this tile.
    """

    def __init__(self, description: str, value: int = 0) -> None:
        """Initialize a LifeTileCard.

        Args:
            description: Description of the life event.
            value: Point value of the tile (default 0).
        """
        if not description:
            raise ValueError("LifeTileCard description cannot be empty")
        self.description: str = description
        self.value: int = value
        logger.debug("LifeTileCard created: %s (value=%d)", description, value)

    def __str__(self) -> str:
        return f"Life Tile: {self.description}"


class CardDeck:
    """A generic shuffleable deck of cards.

    Attributes:
        cards: The list of cards currently in the deck.
    """

    def __init__(self, cards: List) -> None:
        """Initialize the deck with a list of cards.

        Args:
            cards: The initial list of card objects.
        """
        self.cards: List = list(cards)
        logger.debug("CardDeck created with %d cards", len(self.cards))

    def draw(self) -> object:
        """Draw the top card from the deck.

        Returns:
            The top card object.

        Raises:
            IndexError: If the deck is empty.
        """
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        card = self.cards.pop(0)
        logger.debug("Card drawn: %s", card)
        return card

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        import random
        random.shuffle(self.cards)
        logger.debug("Deck shuffled (%d cards)", len(self.cards))

    def is_empty(self) -> bool:
        """Return True if the deck has no cards remaining."""
        return len(self.cards) == 0

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f"CardDeck({len(self.cards)} cards)"