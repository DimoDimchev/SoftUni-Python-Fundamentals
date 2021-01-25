class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price:
            if self.owner is None:
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
            else:
                return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"
