class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age  =  age
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    def is_eligible(self):
        if self.age >= 15 and self.grade in ["A", "A-","B+","B","B-", "C+", "C"]:
            print(f"{self.name} is  eligible for Admission.")
        else:
            print(f"{self.name} is not eligible for Admission.")


s1 = student("Hassan", 22, "A")
s2 = student("Ali", 14, "B")
s3 = student("Sara", 16, "B-")
s4 = student("Aisha", 13, "A")
s5 = student("Ahmed", 17, "C-")
s6 = student("Fatima", 18, "D")

# Instance methods 
s1.display_info()
s1.is_eligible()


s2.display_info()
s2.is_eligible()

s3.display_info()
s3.is_eligible()

s4.display_info()
s4.is_eligible()    

s5.display_info()
s5.is_eligible()


s6.display_info()
s6.is_eligible()