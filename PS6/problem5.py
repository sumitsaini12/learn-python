# Write a program to calculate the grade of a student from his marks from 
# the following scheme : 
"""
90 -- 100 --> A+
80 -- 89  --> A
70 -- 79  --> B+
60 -- 69  --> B
50 -- 59  --> C
33 -- 49  --> D
0 -- 32  --> F
"""

marks = int(input("Enter your marks: "))

if(marks >= 90 and marks <= 100):
    print("Grade: A+")
elif(marks >= 80 and marks < 90):
    print("Grade: A")
elif(marks >= 70 and marks < 80):   
    print("Grade: B+")
elif(marks >= 60 and marks < 70): 
    print("Grade: B")
elif(marks >= 50 and marks < 60):
    print("Grade: C")
elif(marks >= 33 and marks < 50):
    print("Grade: D")
elif(marks >= 0 and marks < 33):
    print("Grade: F")