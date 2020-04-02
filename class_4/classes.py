# Organizing code into classes

#Base Animal definition
class Animal:
    name = "Animal"
    speed = 0
    words = "I am an animal and my name is "


    def talk(self):
        print(self.words + self.name)


# Class definition of a Cat
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.speed = 4
        self.words = "Meow, I am a cat. Call me "


# Class definition of a Dog
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.speed = 8
        self.word = "Woof, woof. My name is "




# a race method

def race(animal1, animal2):
    if animal1.speed > animal2.speed:
        print("The winner is " + animal1.name)
    elif animal1.speed == animal2.speed:
        print("We have a tie between " + animal1.name + " and " + animal2.name)
    else:
        print("The winner is " + animal2.name)


c = Cat("Fluffy")
b = Cat("Mr Biggles")
d = Dog("Fido")

race(c, d)
race(c,b)


#c.talk()
#b.talk()
#d.talk()






# add a constructor init __init__(self, name) method
# extend to have speed
# race method
# dynamically add attributes
# Inherit from a base class





