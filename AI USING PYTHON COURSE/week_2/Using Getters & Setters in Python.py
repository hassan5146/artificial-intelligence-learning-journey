#Using Getters & Setters in Python

class Student:
    @property
    def grade(self):
        return self.__grade
    def __init__ (self , name, grade):
        self.__grade = grade 
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

Student = Student("Alice", 85)
Student.set_grade(-90)
print(Student.get_grade())