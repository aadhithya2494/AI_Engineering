# You are analyzing execution durations (in seconds) for 50 automated test cases across 5 cycles.

# b) Perform the following analyses:
# 1. Statistical Analysis
# o Calculate the average execution time per cycle.
# o Identify the test case with the maximum execution time in the entire dataset. o Find the standard deviation of execution times for each cycle to measure
# consistency. 2. Slicing Operations
# o Extract the first 10 test execution times from Cycle 1. o Extract the last 5 test execution times from Cycle 5. o Extract every alternate test from Cycle 3.
# 3. Arithmetic Operations
# o Perform element-wise addition and subtraction between Cycle 1 and Cycle 2.
# o Perform element-wise multiplication and division between Cycle 4 and Cycle 5.
# 4. Power Functions
# o Square and cube all execution times.
# o Apply a square root transformation on the dataset.
# o Apply logarithmic transformation (np.log(array+1)) to normalize skewed data.
# 5. Copy Operations
# o Create a shallow copy of the dataset and modify one cycle. Observe if the original
# changes.
# o Create a deep copy using .copy() and modify it. Confirm the original remains
# unchanged.
# 6. Filtering with Conditions
# o Extract all test cases in Cycle 2 that take more than 30 seconds.
# o Identify tests that consistently (in every cycle) take more than 25 seconds.
# Replace all execution times below 10 seconds with 10 (minimum thresholding).

import numpy as np

np.random.seed(0)  # For reproducibility
data = np.random.randint(5, 60, size=(5, 50))
print("Dataset (5 cycles, 50 test cases each):\n", data)


avg = np.mean(data, axis=1)
print("\nAverage execution time per cycle:", avg)

max_time = np.max(data)
max_index = np.unravel_index(np.argmax(data, axis=None), data.shape)
print(f"Maximum execution time in the dataset: {max_time} seconds (Cycle {max_index[0]+1}, Test Case {max_index[1]+1})")

std_dev = np.std(data, axis=1)
print("\nStandard deviation of execution times per cycle:", std_dev)

first_10_cycle1 = data[0, :10]
print("\nFirst 10 test execution times from Cycle 1:", first_10_cycle1)

last_5_cycle5 = data[4, -5:]
print("\nLast 5 test execution times from Cycle 5:", last_5_cycle5)

alternate_cycle3 = data[2, ::2]
print("\nEvery alternate test from Cycle 3:", alternate_cycle3)

add_cycle1_cycle2 = data[0] + data[1]
sub_cycle1_cycle2 = data[0] - data[1]
print("\nElement-wise addition between Cycle 1 and Cycle 2:", add_cycle1_cycle2)
print("Element-wise subtraction between Cycle 1 and Cycle 2:", sub_cycle1_cycle2)

mul_cycle4_cycle5 = data[3] * data[4]
div_cycle4_cycle5 = np.divide(data[3], data[4], out=np.zeros_like(data[3], dtype=float), where=data[4]!=0)
print("\nElement-wise multiplication between Cycle 4 and Cycle 5:", mul_cycle4_cycle5)
print("Element-wise division between Cycle 4 and Cycle 5:", div_cycle4_cycle5)

squared = np.power(data, 2)
cubed = np.power(data, 3)
print("\nSquared execution times:\n", squared)
print("\nCubed execution times:\n", cubed)


sqrt_data = np.sqrt(data)
log_data = np.log(data + 1)
print("\nSquare root transformation of execution times:\n", sqrt_data)
print("\nLogarithmic transformation of execution times:\n", log_data)

shallow_copy = data
shallow_copy[0, 0] = 999
print("\nAfter modifying shallow copy (Cycle 1, Test Case 1 to 999):")
print("Original dataset:\n", data)
deep_copy = data.copy()
deep_copy[0, 0] = 5
print("\nAfter modifying deep copy (Cycle 1, Test Case 1 to 5):")
print("Original dataset remains unchanged:\n", data)
filtered_cycle2 = data[1, data[1] > 30]
print("\nTest cases in Cycle 2 taking more than 30 seconds:", filtered_cycle2)

consistent_above_25 = np.all(data > 25, axis=0)
tests_consistently_above_25 = np.where(consistent_above_25)[0]
print("\nTests that consistently take more than 25 seconds (Test Case indices):", tests_consistently_above_25)

data[data < 10] = 10
print("\nDataset after replacing execution times below 10 seconds with 10:\n", data)

