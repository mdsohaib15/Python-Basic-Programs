# Student Age Calculation using datetime module
from datetime import date  

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Student's name is {self.name} and Age is {self.age}")

    @classmethod
    def initFromBirthYear(cls, name, birth_year):
        # Calculate age based on birth year and the current year
        today_year = date.today().year
        age = today_year - birth_year
        return cls(name, age)


student1 = Student("Sohaib", 19)
#creating object for class method t
student2 = Student.initFromBirthYear("Hammad", 2003)
student3 = Student.initFromBirthYear("Basit",2004)

student1.describe()
student2.describe()
student3.describe()

