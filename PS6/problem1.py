# Write a program to find greatest of four numbers entered by the user.

number = []

for i in range(4):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)

def max(numbers):
    greatest = numbers[0]
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest

print("The greatest number is:", max(number))    