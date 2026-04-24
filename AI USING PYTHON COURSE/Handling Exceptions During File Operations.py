
try:  
    with open("missing.txt", "r") as file:  # Attempt to open the file in read mode
        print(file.read())  # Read and print the contents of the file

except FileNotFoundError:  # Handle the case where the file is not found
    print("The file 'missing.txt' was not found. Please check the file name and try again.")


filename = "missing.txt"
name = "Alice"
age = 27

try:
    with open(filename, "r") as fin:  # Attempt to open the file in read mode
        print(fin.read())  # Read and print the contents of the file

except FileNotFoundError:  # Handle the case where the file is not found
    with open(filename, "w") as fout:  # Open the file in write mode to create it
        fout.write(f"Name: {name}\nAge: {age}")  # Write the name and age to the file
    with open(filename, "r") as fin: # Open the file in read mode to verify its contents
        print(fin.read())  # Read and print the contents of the file to verify it was created successfully