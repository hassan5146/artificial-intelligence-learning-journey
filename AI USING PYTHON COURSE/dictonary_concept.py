student= { 

    "Name" : "Hassan Shah",
    "Age" : 21,
    "Course" : "PYTHON",
    "Cgpa" : 3.1
} 

print(student)
print(type(student))


#access valus 
print(student["Name"])
print(student["Age"])


#dictonary method
student["Age"]= 23         #update 

student["City"]= "Lahore"  #add

student.pop("Cgpa")      #remove 

print(student)



#Looping Dictionary
for key, value in student.items():
    print(key,  ":", value)