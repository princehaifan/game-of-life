# Game of Life - Player


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


class PlayerBase:

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.position = 0
        self.finances = 0
        self.career = None
        self.house = None
        self.family = []
        self.is_retired = False


class PlayerMovement:

    def move(self, steps):
        self.position += steps


class PlayerFinances:

    def add_money(self, amount):
        self.finances += amount

    def spend_money(self, amount):

        if amount <= self.finances:
            self.finances -= amount
        else:
            raise ValueError("Insufficient funds")


class PlayerFamily:

    def add_family_member(self, member):
        self.family.append(member)

    def remove_family_member(self, member):
        self.family.remove(member)


class Player(PlayerBase, PlayerMovement, PlayerFinances, PlayerFamily):

    def __init__(self, name):
        super().__init__(name)

    def assign_career(self, career):
        self.career = career

    def assign_house(self, house):
        self.house = house

    def retire(self):
        self.is_retired = True

    def display_status(self):
        # Returns a summary of the player's current status
        return (
            f"{self.name} - Position: {self.position}, "
            f"Finances: {self.finances}"
        )


# Example instantiation
if __name__ == "__main__":
    player = Player("John")
    career = Career("Engineer", 70000)
    house = House("Villa", 300000)

    player.assign_career(career)
    player.assign_house(house)
    player.add_money(150000)

    print(player.display_status())