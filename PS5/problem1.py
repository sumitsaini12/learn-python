# Write a program to create a dictionary of Hindi words with values as their english translation.
# privide user with an option to look it up!


d = {}

key1 = input("Enter a Hindi word: ")
value1 = input("Enter the English translation: ")
d[key1] = value1   # store key-value pair

key2 = input("Enter a Hindi word: ")
value2 = input("Enter the English translation: ")
d[key2] = value2   # store key-value pair

print("Dictionary created successfully! ", d)