class Student:
    #first method, always
    def __init__(self, name, age, studentID, address):
        self.name = name
        self.age = age
        self.studentID = studentID
        self.__address = address #private attribute

    def __str__(self):
        return f"Name: {self.name}, studentID: {self.studentID}"
    

student1 = Student("John Doe", 20, "S12345", "123 Main St")



        