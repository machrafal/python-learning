import numpy as np

# 1. Write a Python program to print "Hello Python".
print("Hello Python")


# 2. Write a Python program to do arithmetical operations addition and division.
def add(a, b):
    return a + b


def div(a, b):
    if b == 0:
        print("Cannot divide by 0!!!")
    else:
        return a / b


# Addition
num1 = float(input("Enter the first for addition: "))
num2 = float(input("Enter the second for addition: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} equals: {sum_result}")

# Division
num3 = float(input("Enter the first for division: "))
num4 = float(input("Enter the second for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed!")
else:
    div_result = num3 / num4
    print(f"The division of {num3} by {num4} equals: {div_result}")

# 3. Write a Python program to find the area of a triangle.
base = float(input("Please enter the base length: "))
heigth = float(input("Please enter the height length: "))
triangle_area = 1 / 2 * base * heigth
print(
    f"The area of a triangle with a base of {base} and a height of {heigth} is: {triangle_area}"
)

# 4. Write a Python program to swap two variables.
a = float(input("Please enter the first variable: "))
b = float(input("Please enter the second variable: "))
print(f"The original variables are: a = {a} and b = {b}")
temp = a
a = b
b = temp
print(f"The swapped variables are: a = {a}, b = {b}")

# 5. Write a Python program to generate a random number
a = np.random.randint(1, 100)
