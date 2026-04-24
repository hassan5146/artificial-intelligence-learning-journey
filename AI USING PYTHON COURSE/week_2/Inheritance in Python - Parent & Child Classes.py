class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.speak()  # Output: Some sound

class Dog(Animal):
    def bark(self):
        print("Woof!")

childdog = Dog()
childdog.bark()  # Output: Woof!
childdog .speak()  # Output: Some sound