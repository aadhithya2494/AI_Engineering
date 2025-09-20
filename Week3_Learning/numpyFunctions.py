import numpy as np

nparray = np.array([10, 15, 20, 25, 30, 35, 40, 45])

# Indexing & Shaping
# Access the first, last, and 3rd element of the array.
print("First:", nparray[0])
print("Last:", nparray[-1])
print("3rd element:", nparray[2])
# Print the shape of the array.
print("Shape:", nparray.shape)

# Slicing
# Print execution times of the first 3 tests.
print("First 3 elements:", nparray[:3])

# Print every alternate test time.
print("Every alternate element:", nparray[::2])

# Iteration
# Iterate through the array and print each execution time with a message: "Test X execution time: Y seconds".

for i, time in enumerate(nparray):
    print(f"Test {i+1} execution time: {time} seconds")

# Reshaping
# Reshape the 1D array (8 elements) into a 2D array of shape (2,4).
# Print the reshaped array.
print("Reshaped array (2x4):\n", nparray.reshape(2, 4))

# Joining
# Create another NumPy array with 4 more execution times:
# [50, 55, 60, 65]
# Join (concatenate) this with the first array to form a longer array.
another_array = np.array([50, 55, 60, 65])
joined_array = np.concatenate((nparray, another_array))
print("Joined array:", joined_array)

# Splitting
# Split the final array into 3 smaller arrays (equal parts if possible).
# Print each split.
split_arrays = np.array_split(joined_array, 3)
for i, arr in enumerate(split_arrays):
    print(f"Split array {i+1}:", arr)