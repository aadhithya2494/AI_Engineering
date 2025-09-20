# You are simulating different QA roles analyzing test cycle data using NumPy.
# # a) Create three classes: ManualTester, AutomationTester, and PerformanceTester.
# b) Each class should have a method analyze(data) that takes a NumPy array of test execution times.
#  ManualTester → prints the first 5 test execution times (data[:5]).
#  AutomationTester → prints the fastest test case (data.min()).
#  PerformanceTester → prints the 95th percentile execution time (np.percentile(data,
# 95)).
# c) Write a function show_analysis(tester, data) that calls the analyze() method. d) In the main section:
#  Create a NumPy array with at least 12 execution times.
#  Create objects of all three tester roles.
#  Call show_analysis() for each tester object.

import numpy as np
class ManualTester:
    def analyze(self, data):
        print("Manual Tester - First 5 execution times:", data[:5])

class AutomationTester:
    def analyze(self, data):
        print("Automation Tester - Fastest execution time:", data.min())

class PerformanceTester:
    def analyze(self, data):
        print("Performance Tester - 95th percentile execution time:", np.percentile(data, 95))

def show_analysis(tester, data):
    tester.analyze(data)

if __name__ == "__main__":
    execution_times = np.array([12.5, 15.3, 9.8, 20.1, 7.6, 14.2, 18.4, 11.0, 16.5, 13.7, 22.3, 10.5])
    
    manual_tester = ManualTester()
    automation_tester = AutomationTester()
    performance_tester = PerformanceTester()
    
    show_analysis(manual_tester, execution_times)
    show_analysis(automation_tester, execution_times)
    show_analysis(performance_tester, execution_times)