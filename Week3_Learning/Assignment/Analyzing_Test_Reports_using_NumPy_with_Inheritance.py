# You are working on a QA analytics system. The system stores test execution times (in seconds) using NumPy arrays.

# # a) Create a base class TestReport with an attribute execution_times (NumPy array). b) In TestReport, implement methods:
# 1. average_time() → returns the mean execution time. 2. max_time() → returns the maximum execution time.
# c) Create a subclass RegressionReport that inherits from TestReport.
#  Add a method slow_tests(threshold) that returns all test cases taking more than the threshold time.
# d) In the main section:
#  Create a NumPy array with 10 execution times.
#  Create a RegressionReport object using this array.
#  Display average, max, and slow tests using the implemented methods.

import numpy as np
class TestReport:
    def __init__(self, execution_times):
        self.execution_times = np.array(execution_times)

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)

class RegressionReport(TestReport):
    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]

if __name__ == "__main__":
    ex_time = [12.5, 15.3, 9.8, 20.1, 7.6, 14.2, 18.4, 11.0, 16.5, 13.7]
    report = RegressionReport(ex_time)
    
    print(f"Average Execution Time: {report.average_time()} seconds")
    print(f"Maximum Execution Time: {report.max_time()} seconds")
    
    threshold = 15.0
    slow_tests = report.slow_tests(threshold)
    print(f"Tests taking more than {threshold} seconds: {slow_tests} seconds")
