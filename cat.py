class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # This an instance method and only works on instances
    def description(self):
        return "{} is {}".format(self.name, self.age)
gus = Cat("Gus", 9)
print(gus.description())

