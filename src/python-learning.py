import calendar

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

# 6. Write a Python program to convert kilometers to miles.
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"The {kilometers} kilometers is {miles} miles.")

# 7. Write a Python program to convert Celsius to Fahrenheit.
celsius = float(input("Enter the temperature in celsius degrees: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = celsius * 9 / 5 + 32
print(f"The {celsius} temperature in Celsius is {fahrenheit} in Fahrenheit")

# 8. Write a Python program to display calendar.
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
cal = calendar.month(year, month)
print(cal)

# 9. Write a Python program to solve quadratic equation.
# ax^2+bx+c=0
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + np.sqrt(delta)) / 2 * a
    x2 = (-b - np.sqrt(delta)) / 2 * a
    print(
        f"The delta is greater than 0. The equation has 2 real roots.\nThe roots are {x1} and {x2}"
    )
elif delta == 0:
    x0 = -b / 2 * a
    print(f"The delta is equal to 0. The equation has 1 real root.\nThe root is {x0}")
else:
    real = -b / 2 * a
    img = np.sqrt(abs(delta)) / 2 * a
    print(
        f"The delta is less than 0. The equation has complex roots.\nThe roots are {real} + {img}i and {real} - {img}i."
    )

# 10. Write a Python program to swap two variables without temp variable.
a = float(input("Please enter the first variable: "))
b = float(input("Please enter the second variable: "))
print(f"The original variables are: a = {a} and b = {b}")
a, b = b, a
print(f"The swapped variables are: a = {a}, b = {b}")

# 11. Write a Python Program to Check if a Number is Positive, Negative or Zero.
a = float(input("Please enter your number: "))
if a > 0:
    print("The entered number is positive.")
elif a == 0:
    print("The entered number is 0.")
else:
    print("The entered number is negative.")

# 12. Write a Python Program to Check if a Number is Odd or Even.
a = float(input("Please enter a number: "))
if a % 2 == 0:
    print("The entered number is even.")
else:
    print("The entered number is odd.")
