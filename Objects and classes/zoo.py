class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fish = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fish.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
            print(f"Total animals: {Zoo.__animals}")
        elif species == "bird":
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
            print(f"Total animals: {Zoo.__animals}")
        if species == "fish":
            print(f"Fishes in {self.name}: {', '.join(self.fish)}")
            print(f"Total animals: {Zoo.__animals}")


zoo_name = Zoo(input())
number = int(input())


for index in range(number):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo_name.add_animal(species, name)

info = input()
zoo_name.get_info(info)
