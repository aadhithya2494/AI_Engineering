print("Welcome to testing for AI")

# Practise Problem 1: Eligibility Check for Job Application
# You are given two inputs: age and years of experience (yoe).
# Write a program that checks if a person is eligible to apply for a job.
# Eligibility criteria:
# 1. Age must be at least 22 years.
# 2. Years of experience must be at least 2 years.

age = int(input("Press Enter your age"))
yoe = int(input("Press Enter your years of experience"))
if(age >= 22 and yoe >= 2):
    print("Access Granted")
else:
    print("Access Denied")