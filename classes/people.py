
class Father:

    def __init__(self, name, surname, eye_color):
        self.name = name
        self.surname = surname
        self.eye_color = eye_color

class Mother:

    def __init__(self, name, surname, hair_color):
        self.name = name
        self.surname = surname
        self.hair_color = hair_color

class Child(Father, Mother):

    def __init__(self, name):
        Father.__init__(self, "John", "Smith", "blue")
        Mother.__init__(self, "Jane", "Doe", "brown")
        self.name = name

husband = Father("John", "Smith", "blue")
wife = Mother("Jane", "Doe", "brown")
first_born = Child("Bheki")
second_born = Child("Lerato")

print(f"{first_born.name} is the child of {husband.name} and {wife.name}. He has {husband.eye_color} eyes and {wife.hair_color} hair.")
