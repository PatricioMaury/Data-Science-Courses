# Creating Classes and Objects
name = 'Pato'
age = 25

print(type(name))
print(type(age))
print(name.upper())

class Dog:
    def bark(self):
        print('Whoof whoof')

dog1 = Dog()
dog1.bark()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('Whoof whoof')

dog1 = Dog('Bruce', 'Labrador')
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog('Freya', 'Greyhound')
dog2.bark()
print(dog2.name)
print(dog2.breed)