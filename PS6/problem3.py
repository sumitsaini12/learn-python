# Write a problem to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")

if(username.isalpha() and len(username) < 10):
    print("Valid username")
else:
    print("Invalid username. Username must contain only letters and be less than 10 characters long.")    