class Career:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

class House:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class LifeTile:
    def __init__(self, description):
        self.description = description

class Player:
    def __init__(self, name):
        self.name = name
        self.wealth = 0
        self.career = None
        self.house = None

    def display_status(self):
        return f"{self.name} - Wealth: {self.wealth}, Career: {self.career.title if self.career else 'None'}, House: {self.house.name if self.house else 'None'}"

    def calculate_wealth(self):
        return self.wealth

    def add_money(self, amount):
        self.wealth += amount

    def spend_money(self, amount):
        if amount <= self.wealth:
            self.wealth -= amount
        else:
            raise ValueError("Insufficient funds")

    def assign_career(self, career):
        self.career = career

    def assign_house(self, house):
        self.house = house

# Example instantiation
if __name__ == "__main__":
    player = Player("John")
    career = Career("Engineer", 70000)
    house = House("Villa", 300000)

    player.assign_career(career)
    player.assign_house(house)
    player.add_money(150000)

    print(player.display_status())