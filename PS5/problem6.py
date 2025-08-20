# if names of 2 friends are same; what will to the program in problem?


friends_languages = {}

for i in range(4):
    name = input("Enter your name:")
    language = input("Enter your favourite programming language:")
    friends_languages[name] = language

print("Friends' favourite languages:", friends_languages) # If two friends have the same name, the second entry will overwrite the first one in the dictionary.