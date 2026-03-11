# Combining Objects
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print('Whoof whoof')
class Owner:
    def __init__(self, name, adress, contact_number):
        self.name = name
        self.adress = adress
        self.phone_number = contact_number

owner1 = Owner('John', '123 5th Ave', '999-930-1234')
dog1 = Dog('Bruce', 'Labrador', owner1)
print(dog1.owner.name)
print(dog1.owner.adress)
print(dog1.owner.phone_number)

print('--------------------------------')

owner2 = Owner('Mary', '456 6th St', '981-123-2030')
dog2 = Dog('Freya', 'Greyhound', owner2)
print(dog2.owner.name)
print(dog2.owner.adress)
print(dog2.owner.phone_number)
