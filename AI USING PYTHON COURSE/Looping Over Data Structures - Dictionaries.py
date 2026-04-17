#Looping Over Data Structures - Dictionaries

print("==========================================================")
print("1st concept")
print("==========================================================")

student ={"Name " : "HASSAN", "Age " : 21, "Grade" : "A"}

for key in student:
    print(key)
print("==========================================================")
print("2nd concept")
print("==========================================================")


student ={"Name " : "HASSAN", "Age " : 21, "Grade" : "A"}

for key in student:
    print(student[key])


print("==========================================================")
print("3nd concept")
print("==========================================================")


student ={"Name " : "HASSAN", "Age " : 21, "Grade" : "A"}

for key in student:
    print(key , ":" , student[key])

print("==========================================================")
print("4nd concept")
print("==========================================================")

student_list =[
    {"Name " : "AHMAD", "Age " : 25, "Grade" : "A"},
    {"Name " : "SARA", "Age " : 28, "Grade" : "B"},
]
for student  in student_list:
    print(f"Name:  {student.get('Name','')} | Grade: {student.get('Grade','')} ")