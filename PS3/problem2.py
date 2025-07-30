# Write a program to fill in a letter kemplate givon belaw with name and date
# letter = " Dear LINAME.IZ,
# You are selected!
# <I DATEI>


name = input("Please enter your name :")
letter = '''Dear <|Name|>, 
            You are selected!
            <|Date|> '''

print(letter.replace("<|Name|>" , name).replace("<|Date|>", "30 July 2025 " ))