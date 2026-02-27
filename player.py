import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class LifeTile:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        logging.debug(f"LifeTile created: {self.name} with value {self.value}")


class Career:
    def __init__(self, title: str, salary: float):
        self.title = title
        self.salary = salary
        logging.debug(f"Career created: {self.title} with salary {self.salary}")


class House:
    def __init__(self, address: str, price: float):
        self.address = address
        self.price = price
        logging.debug(f"House created: {self.address} with price {self.price}")


class Player:
    def __init__(self, name: str):
        self.name = name
        self.career: Optional[Career] = None
        self.house: Optional[House] = None
        self.life_tiles: List[LifeTile] = []
        logging.debug(f"Player created: {self.name}")

    def choose_career(self, title: str, salary: float):
        if salary < 0:
            logging.error(f"Invalid salary: {salary}")
            raise ValueError("Salary must be a positive number")
        self.career = Career(title, salary)

    def buy_house(self, address: str, price: float):
        if price <= 0:
            logging.error(f"Invalid house price: {price}")
            raise ValueError("House price must be greater than zero")
        self.house = House(address, price)

    def add_life_tile(self, name: str, value: int):
        self.life_tiles.append(LifeTile(name, value))

    def __str__(self):
        return f"Player {self.name} with career {self.career.title if self.career else 'None'}"
