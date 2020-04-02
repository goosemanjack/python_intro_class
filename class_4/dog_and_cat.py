# Example of using classes


class Cat:
    """A furry cat"""
    name = "Tabby"
    # tricks = []

    def rename(self, new_name):
        self.name = new_name

    def speak(self):
        print("Meow. My name is " + self.name)

"""
    def add_trick(self, trick):
        self.tricks.append(trick)

    def list_tricks(self):
        print("My tricks")
        for t in self.tricks:
            print(t)
"""


class Dog:
    """A barky dog"""
    name = "Dog"


    def rename(self, new_name):
        self.name = new_name

    def speak(self):
        print("Woof woof woof. And bark yip! My name is " + self.name)


# add a constructor init __init__(self, name) method
# extend to have speed
# race method
# dynamically add attributes
# Inherit from a base class



c = Cat()
c.rename("Mr Biggles")
b = Cat()
b.rename("SDF")
c.speak()
b.speak()

# c.add_trick("Roll")
# b.add_trick("Sit")
# c.list_tricks()

