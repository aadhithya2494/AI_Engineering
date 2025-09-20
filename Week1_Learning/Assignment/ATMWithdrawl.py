# Write a Python program to simulate an ATM withdrawal:
# 1. Ask the user to enter a withdrawal amount.
# 2. The ATM only dispenses money in multiples of 100.
# 3. If the entered amount is valid → print "Dispensing <amount>".
# 4. Otherwise → print "Invalid amount".

def atm_withdrawal():
    amount = int(input("Enter the withdrawal amount: "))
    if amount % 100 == 0:
        print(f"Dispensing {amount}")
    else:
        print("Invalid amount")

atm_withdrawal()