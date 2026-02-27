class CareerCard:
    def __init__(self, career_name, salary):
        self.career_name = career_name
        self.salary = salary

    def __str__(self):
        return f'Career: {self.career_name}, Salary: {self.salary}'

class HouseCard:
    def __init__(self, house_value):
        self.house_value = house_value

    def __str__(self):
        return f'House Value: {self.house_value}'

class LifeTileCard:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return f'Life Tile: {self.description}'