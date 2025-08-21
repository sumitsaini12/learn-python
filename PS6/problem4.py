# Write a program which finds our whether a given name is present in a list or not.

list = ['saurav', 'sumit', 'neeraj', 'rahul', 'aman', 'akash', 'yogesh']

username = input('Enter your username: ')

if username in list:
    print("Username is present in the list.")
else:
    print("Username is not present in the list.")