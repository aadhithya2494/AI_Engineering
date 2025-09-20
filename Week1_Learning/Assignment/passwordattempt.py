 # Write a Python program to implement a password retry system :
# 1. Set the correct password as "openAI123".
# 2. Allow the user 3 attempts to enter the password.
# 3. If the password entered is correct → print "Login Successful".
# 4. If the user fails in all 3 attempts → print "Account Locked".

def password_attempt():
    correct_password = "openAI123"
    max_attempts = 3
    attempts = 0
    for attempts in range(max_attempts):
        entered_password = input("Enter your password: ")
        if entered_password == correct_password:
            print("Login Successful")
            break
        elif attempts < max_attempts - 1:
            print("Incorrect password. Try again.")
    else:
        print("Account Locked")

password_attempt()
