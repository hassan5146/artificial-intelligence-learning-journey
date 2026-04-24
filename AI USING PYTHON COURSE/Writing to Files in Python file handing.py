

file = open("example.txt", "r")  # Open the file in read mode

print(file.read())  # This will raise an error because the file is opened in write mode

file.close()  # Close the file

file = open("example.txt", "w")  # Open the file in write mode

file.write("change Hello, World!")  # Write a string to the file

file.close()  # Close the file




