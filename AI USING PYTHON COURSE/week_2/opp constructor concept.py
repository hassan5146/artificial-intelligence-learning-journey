
#default consturctor
class dog:
    def __init__ (self):
        self.name = "Buddy"
    def bark(self):
        print(f"{self.name} Says Woof!")

dig1 = dog()
dig1.bark()

#parameterize constructor


class car:
    def __init__ (self,brand, color):
        self.brand = brand
        self.color = color

car1 = car("Toyota", "Red")
print(car1.brand)
print(car1.color)

car2 = car("Honda", "Blue")
print(car2.brand)
print(car2.color)
        