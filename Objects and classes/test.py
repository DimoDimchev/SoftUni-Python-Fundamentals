class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(self.name)

    def say_age(self):
        print(self.age)


dimo = Person("Dimo", 17)
dimo.say_name()
dimo.say_age()
