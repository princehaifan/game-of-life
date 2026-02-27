"""
Dice/Spinner class for random movement
Simulates the spinner in The Game of Life
"""

import random


class Dice:
    """
    Simulates a spinner with values 1-10
    Used to determine how many spaces a player moves each turn
    
    Attributes:
        last_spin (int): Result of the most recent spin
    """
    
    MIN_VALUE = 1
    MAX_VALUE = 10
    
    def __init__(self, seed=None):
        """
        Initialize the dice
        
        Args:
            seed (int, optional): Random seed for reproducible tests
        """
        self.last_spin = 0
        if seed is not None:
            random.seed(seed)
        
    def spin(self):
        """
        Spin the spinner
        
        Returns:
            int: Random number between 1 and 10
        """
        self.last_spin = random.randint(self.MIN_VALUE, self.MAX_VALUE)
        return self.last_spin
    
    def get_last_spin(self):
        """
        Get the result of the last spin
        
        Returns:
            int: Last spin result
        """
        return self.last_spin