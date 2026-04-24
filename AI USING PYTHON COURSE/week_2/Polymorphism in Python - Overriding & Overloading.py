
#Polymorphism in Python - Overriding
class dog:
    def speak(self):
        print("Woof!")
    
class cat:
    def speak (self):
        print("Meow!")
    
for  animal in [dog(), cat()]:
     animal.speak()




class Vehicle:
    def move(self):
        print("Vehicle Is Moving")

class car(Vehicle):
    def move(self):
        print("Car Is Moving") #

car1 = car()
car1.move()  # Output: Car Is Moving



#Polymorphism in Python - Overloading

class Calulator:
    def add(self, a, b=0, c=0):      #a is a required parameter, b and c are optional parameters with default values of 0
        return a + b + c
    
calc = Calulator()
# print(calc.add())                 # This will raise an error because the required argument 'a' is missing
print(calc.add (5))                 #argument a is 5, b and c are default to 0
print(calc.add(7, 13))              #argument a is 7, b is 13, c is default to 0
print(calc.add(5, 55, 23))          #argument a is 5, b is 55, c is 23