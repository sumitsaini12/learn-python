# Write a program to accept marks of 6 students any display them in a sorted manner

marks = []

s1 = int(input("Enter first student marks "))
marks.append(s1)

s2 = int(input("Enter second student marks "))
marks.append(s2)

s3 = int(input("Enter third student marks "))
marks.append(s3)

s4 = int(input("Enter forth student marks "))
marks.append(s4)

s5 = int(input("Enter fifth student marks "))
marks.append(s5)

s6 = int(input("Enter six student marks "))

marks.append(s6)

marks.sort()

print("student marks in sort order", marks)