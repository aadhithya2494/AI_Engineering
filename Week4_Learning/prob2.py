# Learn how to create a Pandas Series, perform simple analysis, and use loc and iloc.

# Create a Python script named pandas_series_times.py that:
# Creates a Pandas Series representing test execution times:
# [12, 15, 20, 18, 25, 30, 22]
# with labels: ['TC1','TC2','TC3','TC4','TC5','TC6','TC7']
# Prints the Series.
# Displays the first 3 test times.
# Finds the mean execution time.
# Uses iloc to print the 2nd test time.
# Uses loc to print execution time of TC3

import pandas as pd
execution_times = [12, 15, 20, 18, 25, 30, 22]
test_case_labels = ['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6', 'TC7']
series = pd.Series(execution_times, index=test_case_labels)  
print("Test Execution Times Series:")
print(series)   
first_three_times = series.head(3)
print("\nFirst 3 Test Execution Times:")
print(first_three_times)
mean_execution_time = series.mean()
print(f"\nMean Execution Time: {mean_execution_time}")
second_test_time = series.iloc[1]
print(f"2nd Test Execution Time (using iloc): {second_test_time}")
tc3_execution_time = series.loc['TC3']
print(f"Execution Time of TC3 (using loc): {tc3_execution_time}")       