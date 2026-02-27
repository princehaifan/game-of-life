import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LifeTile:
    """Represents a life tile event card in the Game of Life."""

    def __init__(self, name: str, value: int) -> None:
        """Initialize a LifeTile with a name and point value.

        Args:
            name: The name/description of the life event.
            value: The point value of this life tile.
        """
        if not name:
            raise ValueError("LifeTile name cannot be empty")
        self.name = name
        self.value = value
        logger.debug("LifeTile created: %s with value %d", self.name, self.value)

    def __str__(self) -> str:
        return f"LifeTile({self.name}, value={self.value})"


class Career:
    """Represents a career card in the Game of Life."""

    def __init__(self, title: str, salary: float) -> None:
        """Initialize a Career with a title and salary.

        Args:
            title: The job title.
            salary: The annual salary amount.

        Raises:
            ValueError: If salary is negative.
        """
        if salary < 0:
            raise ValueError(f"Salary must be non-negative, got {salary}")
        self.title = title
        self.salary = salary
        logger.debug("Career created: %s with salary %.2f", self.title, self.salary)

    def __str__(self) -> str:
        return f"Career({self.title}, salary={self.salary})"


class House:
    """Represents a house card in the Game of Life."""

    def __init__(self, address: str, price: float) -> None:
        """Initialize a House with an address and price.

        Args:
            address: The address or name of the house.
            price: The purchase price of the house.

        Raises:
            ValueError: If price is not positive.
        """
        if price <= 0:
            raise ValueError(f"House price must be greater than zero, got {price}")
        self.address = address
        self.price = price
        logger.debug("House created: %s with price %.2f", self.address, self.price)

    def __str__(self) -> str:
        return f"House({self.address}, price={self.price})"


class Player:
    """Represents a player in the Game of Life.

    Attributes:
        name: The player's name.
        position: Current board position (0-indexed).
        finances: Current cash/financial balance.
        career: The player's current career, or None.
        house: The player's current house, or None.
        family: List of family members.
        life_tiles: Collected life tile events.
        is_retired: Whether the player has retired.
    """

    def __init__(self, name: str) -> None:
        """Initialize a Player.

        Args:
            name: The player's name.

        Raises:
            ValueError: If name is empty.
        """
        if not name or not name.strip():
            raise ValueError("Player name cannot be empty")
        self.name: str = name
        self.position: int = 0
        self.finances: int = 0
        self.career: Optional[str] = None
        self.house: Optional[str] = None
        self.family: List[str] = []
        self.life_tiles: List[LifeTile] = []
        self.is_retired: bool = False
        logger.debug("Player created: %s", self.name)

    @property
    def cash(self) -> int:
        """Alias for finances for backward compatibility."""
        return self.finances

    def move(self, spaces: int) -> None:
        """Move the player by the given number of spaces.

        Args:
            spaces: Number of spaces to move (can be negative).
        """
        self.position += spaces
        logger.debug("Player %s moved by %d to position %d", self.name, spaces, self.position)

    def add_money(self, amount: int) -> None:
        """Add money to the player's finances.

        Args:
            amount: Amount to add.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError(f"Amount to add must be non-negative, got {amount}")
        self.finances += amount
        logger.debug("Player %s received $%d, total: $%d", self.name, amount, self.finances)

    def spend_money(self, amount: int) -> None:
        """Deduct money from the player's finances.

        Args:
            amount: Amount to spend.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError(f"Amount to spend must be non-negative, got {amount}")
        self.finances -= amount
        logger.debug("Player %s spent $%d, total: $%d", self.name, amount, self.finances)

    def assign_career(self, career: str) -> None:
        """Assign a career to the player.

        Args:
            career: The career title to assign.
        """
        self.career = career
        logger.debug("Player %s assigned career: %s", self.name, career)

    def assign_house(self, house: str) -> None:
        """Assign a house to the player.

        Args:
            house: The house name/address to assign.
        """
        self.house = house
        logger.debug("Player %s assigned house: %s", self.name, house)

    def add_family_member(self, member: str) -> None:
        """Add a family member to the player's family.

        Args:
            member: The family member's name/relation.
        """
        self.family.append(member)
        logger.debug("Player %s added family member: %s", self.name, member)

    def remove_family_member(self, member: str) -> None:
        """Remove a family member from the player's family.

        Args:
            member: The family member's name/relation to remove.

        Raises:
            ValueError: If the family member is not found.
        """
        if member not in self.family:
            raise ValueError(f"Family member '{member}' not found")
        self.family.remove(member)
        logger.debug("Player %s removed family member: %s", self.name, member)

    def retire(self) -> None:
        """Mark the player as retired."""
        self.is_retired = True
        logger.debug("Player %s has retired", self.name)

    def add_life_tile(self, name: str, value: int) -> None:
        """Add a life tile event to the player's collection.

        Args:
            name: Name of the life event.
            value: Point value of the tile.
        """
        self.life_tiles.append(LifeTile(name, value))
        logger.debug("Player %s added life tile: %s", self.name, name)

    def choose_career(self, title: str, salary: float) -> None:
        """Choose a career with a title and salary, validating the salary.

        Args:
            title: The job title.
            salary: The annual salary.
        """
        Career(title, salary)  # validate via Career's constructor
        self.assign_career(title)

    def buy_house(self, address: str, price: float) -> None:
        """Purchase a house, validating the price.

        Args:
            address: The house address.
            price: The purchase price.
        """
        House(address, price)  # validate via House's constructor
        self.assign_house(address)

    def calculate_wealth(self) -> int:
        """Calculate the player's total wealth including life tile values.

        Returns:
            Total wealth as an integer.
        """
        tile_value = sum(tile.value for tile in self.life_tiles)
        return self.finances + tile_value

    def display_status(self) -> str:
        """Return a human-readable string of the player's current status.

        Returns:
            Status string containing name, position, and finances.
        """
        return (
            f"Player: {self.name} | "
            f"Position: {self.position} | "
            f"Finances: {self.finances} | "
            f"Career: {self.career or 'None'} | "
            f"Retired: {self.is_retired}"
        )

    def __str__(self) -> str:
        return f"Player({self.name}, pos={self.position}, $={self.finances})"
