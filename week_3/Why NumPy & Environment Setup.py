import numpy as np
import time

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (arr.shape)
print (arr.ndim)
print (arr.dtype)

print("==========================================================")
print ("list time :")

#list vs numpy array performance comparison

py_list = list (range(1_000_000)) # Create a list of 1 million integers
py_result = []                    
start_time = time.time()          # Start time measurement
for  i in py_list:                # Iterate through the list and perform an operation (e.g., adding 5)
    py_result.append(i + 5)       
end_time = time.time()            # End time measurement
print ("python list time :", end_time - start_time)   # Print the time taken for the list operation




print("==========================================================")
print ("numpy array time :")


# Create a NumPy array of 1 million integers

np_array = np.arange (1_000_000)   # Create a NumPy array of 1 million integers
start_time = time.time()            # Start time measurement
np_result = np_array + 5            # Perform the same operation (adding 5)
end_time = time.time()              # End time measurement
print(f"NumPy operation took {end_time - start_time:.6f} seconds")  # Print the time taken for NumPy operation


print("==========================================================")

