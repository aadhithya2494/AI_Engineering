# create series - scalar - 1.     Creates a Pandas Series representing test execution times: 
# 2.  [12, 15, 20, 18, 25, 30, 22]

# slice the midle three execution times

import pandas as pd

execution_times = [12, 15, 20, 18, 25, 30, 22]
series = pd.Series(execution_times)
print("Full Series:")
print(series)   
print("\nSliced Series:")
sliced_series = series[2:5]
print(sliced_series)


# 2.⁠ ⁠Create with numpy array of number of defects [10,20,23,45,50] convert to series
import numpy as np
defects_array = np.array([10, 20, 23, 45, 50])
defects_series = pd.Series(defects_array)
print("\nDefects Series from NumPy array:")
print(defects_series)

# 3.⁠ ⁠Create series with the help of dictionary for the foll test cases executed by Engineers as key
# Alex - 500 Steve 200 Bob 300

dict = {'Alex': 500, 'Steve': 200, 'Bob': 300}
serie = pd.Series(dict)
print("\nTest Cases Series from dictionary:")
print(serie)

