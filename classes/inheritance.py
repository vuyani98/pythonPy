
#parent class
class Animal:

    def __init__ (self, name, species):
        self.name = name
        self.species = species

    def speak (self):
        print(f"{self.name} makes a sound.")
    
#child class
class Dog (Animal): 

    def __init__ (self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    #method overriding
    def speak(self):
        print(f"{self.name} barks.")
        


dog1 = Animal("Spotty", "Dog")
dog1.speak()

dog2 = Dog("Rex", "Dog", "German Shepherd")
dog2.speak()
print(f"{dog2.name} is a {dog2.breed}.")



