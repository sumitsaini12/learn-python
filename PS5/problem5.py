# Create an empty dictionary. Allow 4 friends to enter their facourite language as values and 
# their names as keys. Print the dictionary. Assume that the names are unique. 

friends_languages = {}

for i in range(4):
    name = input("Enter your name:")
    language = input("Enter your favourite programming language:")
    friends_languages[name] = language

print("Friends' favourite languages:", friends_languages)