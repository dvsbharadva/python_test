class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    pass


tommy = Dog()
tommy.walk()