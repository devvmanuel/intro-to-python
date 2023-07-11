class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("meowwww")


cat1 = Cat("Tom")
cat1.make_sound()
