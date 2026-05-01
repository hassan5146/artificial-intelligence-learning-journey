class invlaidAgeError(Exception):
    pass

age =  int(input("Enter your age: "))
if age < 0:
    raise invlaidAgeError(f"Age cannot be negative. Please enter a valid age. , {age}")


try:
    age =  int(input("Enter your age: "))
    if age < 0:
        raise invlaidAgeError(f"Age cannot be negative. Please enter a valid age. , {age}")
    
except invlaidAgeError as e:
    print(e)


