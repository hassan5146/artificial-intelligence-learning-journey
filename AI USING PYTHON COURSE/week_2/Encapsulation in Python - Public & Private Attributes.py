#create class with private attribute
class Student:
    def __init__ (self, name , age , grade):
        self.name = name
        self.age = age
        self.__grade = grade # Private attribute
    
    # Getter method to access private attribute
    def get_grade(self):
        return self.__grade


student1 = Student("Hassan", 22, "A")
print(student1.name)  # Accessing public attribute
print(student1.age)   # Accessing public attribute
print(student1.get_grade())  # Accessing private attribute through getter method







