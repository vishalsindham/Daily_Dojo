# program 4 to swap two variables

# a = input("Enter value of the first value :  ")
# b = input("Enter value of the second value :  ")

# print(f"Original values that need to be swapned : a : {a} b : {b}")

# temp = a 
# a = b 
# b = temp

# print(f"Swapped values: a : {a}  b : {b}")

# Program 5 to generate a random number

# import random

# print(f"Random number : {random.randint(1, 100)}")

# Program 6 write a program to convert kilometers to miles

# kilometers = float(input("Enter the distance in kilometers : "))

# # Conversion factor : 1 kilometer = 0.621371

# conversion_factor = 0.621371

# miles = kilometers * conversion_factor

# print(f"{kilometers} kilometers is equal to {miles} miles.")

# Program to convert Celsius to Fahrenheit

# celsius = float(input("Enter temperature in Celsius : "))

# # Conversion formula: Fahrenheit = (Celsius * 9/5) + 32

# fahrenheit = (celsius * (9/5)) + 32

# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degree Fahrenheit")

# Write a program to to display calendar1

# import calendar

# year = int(input("Enter year : "))
# month = int(input("Enter month : "))

# cal = calendar.month(year,month)
# print(cal)

# Write a python program to solve quadratic equation

# import math

# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# discriminant = b**2 - 4*a*c

# if discriminant > 0:

#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"Root 1: {root1}")
#     print(f"Root 2: {root2}")

# elif discriminant == 0 :
#     root = -b / (2*a)
#     print(f"Root: {root}")

# else :
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#     print(f"Root 1 : {real_part} + {imaginary_part}i")
#     print(f"Root 2 : {real_part} - {imaginary_part}i")

# Write a python program to swap two variables without temp variables

# a = int(input("Enter a value for the first variable : "))
# b = int(input("Enter a value for the second variable : "))

# # swapping without a temporary variable
# print(f"Values of variables before swapping a :{a}, b :{b}")

# a, b = b, a

# print(f"Values of variables after swapping a :{a}, b :{b}")

# Write a python program to check if a number is positive, negative or zero.

# input_number = float(input("Enter a number you want to check : "))

# if  input_number > 0:
#     print("Enterted number is positive.")

# elif input_number == 0:
#     print("Entered number is zero.")
# else :
#     print("Entered number is negative.")