# Analyze defect counts logged per day using a Pandas Series.

# Create a Python script named pandas_series_defects.py that:
# Creates a Pandas Series for defects logged across 7 days:
# [5, 8, 3, 6, 10, 2, 7]
# with labels: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# Prints the Series.
# Prints the maximum defects logged in a single day.
# Prints the day with minimum defects.
# Uses iloc to print defect count of Day5.
# Uses loc to print defect count on "Wed".
# Prints the total defects logged in the week.

import pandas as pd
defect_counts = [5, 8, 3, 6, 10, 2, 7]
day_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
series = pd.Series(defect_counts, index=day_labels)  
print("Defect Counts Series:")
print(series)   
max_defects = series.max()
print(f"\nMaximum Defects Logged in a Single Day: {max_defects}")
min_defects_day = series.idxmin()
min_defects_value = series.min()
print(f"Day with Minimum Defects: {min_defects_day} ({min_defects_value} defects)")
day5_defects = series.iloc[4]
print(f"Defect Count on Day5 (using iloc): {day5_defects}")
wed_defects = series.loc['Wed']
print(f"Defect Count on Wed (using loc): {wed_defects}")
total_defects = series.sum()
print(f"Total Defects Logged in the Week: {total_defects}") 

