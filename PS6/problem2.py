# Write a program to find out whether a student is pass or fail, if it requires total 40% 
# and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from 
# the user

marks = {}

for i in range(3): 
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    if(i == 0): 
        marks["hindi"] = mark
    elif(i == 1): 
        marks["english"] = mark
    else:
        marks["maths"] = mark 

print("Marks entered:", marks)


if(marks.get("hindi") >= 33 and 
   marks.get("english") >= 33 and 
   marks.get("maths") >= 33 and 
   (marks.get("hindi") + marks.get("english") + marks.get("maths")) / 3 >= 40):
    print("The student is pass")
else:
    print("The student is fail")
    if(marks.get("hindi") < 33):
        print("Failed in Hindi", marks.get("hindi"))
    if(marks.get("english") < 33):
        print("Failed in English", marks.get("english"))   
    if(marks.get("maths") < 33): 
        print("Failed in Maths", marks.get("maths"))  