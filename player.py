"""
Player class representing each participant in the game
Handles player state, movement, and financial transactions
"""


class Player:
    """
    Manages individual player state and actions in The Game of Life
    
    Attributes:
        name (str): Player's name
        position (int): Current position on the board
        cash (int): Current cash amount
        career (dict): Current career information
        house (dict): Current house information
        life_tiles (int): Number of life tiles collected
        is_retired (bool): Whether player has retired
        salary (int): Current salary per turn
        children (int): Number of children
        spouse (bool): Whether player is married
    """
    
    STARTING_CASH = 100000
    STARTING_POSITION = 0
    PAYDAY_AMOUNT = 50000
    
    def __init__(self, name):
        """
        Initialize a new player
        
        Args:
            name (str): Player's name
        """
        self.name = name
        self.position = self.STARTING_POSITION
        self.cash = self.STARTING_CASH
        self.career = None
        self.house = None
        self.life_tiles = 0
        self.is_retired = False
        self.salary = 0
        self.children = 0
        self.spouse = False
        self.career_choice_made = False
        self.house_choice_made = False
        
    def move(self, spaces):
        """
        Move the player forward on the board
        
        Args:
            spaces (int): Number of spaces to move
        """
        if spaces < 0:
            raise ValueError("Cannot move negative spaces")
        self.position += spaces
        
    def earn_money(self, amount):
        """
        Add money to player's cash
        
        Args:
            amount (int): Amount to earn
        """
        if amount < 0:
            raise ValueError("Cannot earn negative money")
        self.cash += amount
        
    def pay_money(self, amount):
        """
        Remove money from player's cash
        
        Args:
            amount (int): Amount to pay
            
        Returns:
            bool: True if successful, False if insufficient funds
        """
        if amount < 0:
            raise ValueError("Cannot pay negative money")
        if self.cash >= amount:
            self.cash -= amount
            return True
        return False
        
    def set_career(self, career):
        """
        Set player's career and salary
        
        Args:
            career (dict): Career information with 'name' and 'salary' keys
        """
        if not isinstance(career, dict):
            raise TypeError("Career must be a dictionary")
        self.career = career
        self.salary = career.get('salary', 0)
        self.career_choice_made = True
        
    def set_house(self, house):
        """
        Set player's house
        
        Args:
            house (dict): House information with 'name' and 'price' keys
        """
        if not isinstance(house, dict):
            raise TypeError("House must be a dictionary")
        self.house = house
        self.house_choice_made = True
        
    def add_child(self):
        """Add a child to the player's family"""
        self.children += 1
        
def marry(self):
        """Set player as married"""
        self.spouse = True
        
def collect_life_tile(self):
        """Collect a life tile"""
        self.life_tiles += 1
        
def collect_salary(self):
        """Collect salary based on current career"""
        if self.salary > 0:
            self.earn_money(self.salary)
            return self.salary
        return 0
        
def retire(self):
        """Mark player as retired"""
        self.is_retired = True
        
def get_status(self):
        """
        Return a string summary of player's current status
        
        Returns:
            str: Formatted status string
        """
        status = f"\n{'='*50}\n"
        status += f"Player: {self.name}\n"
        status += f"{'='*50}\n"
        status += f"Position: {self.position}\n"
        status += f"Cash: ${self.cash:,}\n"
        status += f"Career: {self.career.get('name', 'Not chosen') if self.career else 'Not chosen'}\n"
        if self.career:
            status += f"  Salary: ${self.salary:,} per payday\n"
        status += f"House: {self.house.get('name', 'Not chosen') if self.house else 'Not chosen'}\n"
        if self.house:
            status += f"  Price: ${self.house.get('price', 0):,}\n"
        status += f"Family: {self.children} children, {'Married' if self.spouse else 'Single'}\n"
        status += f"Life Tiles: {self.life_tiles}\n"
        status += f"Status: {'Retired' if self.is_retired else 'Working'}\n"
        status += f"{'='*50}\n"
        return status