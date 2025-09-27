#  Pandas Series – Test Pass Rate %
# Create a Python script named pandas_series_passrate.py that:
# Creates a Series for test pass percentage across 5 builds:
# [80, 85, 78, 90, 88]
# with labels: ['B1','B2','B3','B4','B5']
# Prints the Series.
# Calculates and prints the average pass rate.
# Finds which build had the highest pass rate.
# Uses iloc to print pass rate of the last build.
# Uses loc to print pass rate of Build B3.
# Normalizes values by subtracting average from each pass rate.

import pandas as pd
import numpy as np
pass_rates = [80, 85, 78, 90, 88]
build_labels = ['B1', 'B2', 'B3', 'B4', 'B5']
series = pd.Series(pass_rates, index=build_labels)  
print("Pass Rate Series:")
print(series)   
average_pass_rate = series.mean()
print(f"\nAverage Pass Rate: {average_pass_rate}%")
highest_pass_rate_build = series.idxmax()
highest_pass_rate_value = series.max()
print(f"Highest Pass Rate: {highest_pass_rate_value}% in {highest_pass_rate_build}")
last_build_pass_rate = series.iloc[-1]
print(f"Pass Rate of the last build (B5): {last_build_pass_rate}%")
b3_pass_rate = series.loc['B3']
print(f"Pass Rate of Build B3: {b3_pass_rate}%")
normalized_series = series - average_pass_rate
print("\nNormalized Pass Rate Series (Pass Rate - Average):")
print(normalized_series)        
