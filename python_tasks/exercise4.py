# excercise_4:Password checker. Looping concept with while loop applied
correct_password = "xxxx"
users_password = input(("Enter your password: "))
while users_password != correct_password :
    users_password = input(("Invalid password. Try again: "))
print("Access Granted!")  