# # Write a Python program to :
# 1. Maintain a list of 5 employee names.
# 2. Print each employee name in order, numbered as:
# 1. Name
# 2. Name
# 3. Name

employees = ["Danger", "Alert", "Siren", "Warning", "Caution"]
for i in range(len(employees)):
    print(f"{i+1}. {employees[i]}")

    