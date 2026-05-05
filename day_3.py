# write a python program to check if a number is odd or even

# num = int(input("Enter a number you want to check  :"))

# if num%2 == 0:
#     print("This is even number")
# else :
#     print("This is odd number")

# write a program to check if the given year is leap year

# year = int(input("Enter the year you want to check : "))

# if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
#     print(f"{year} is a leap year.")
# else :
#     print(f"{year} is not leap year")

# write a program to check prime numbers

# num = int(input("Enter a number : "))

# # keep a flag to check and update in loop
# prime = False

# if num == 1:
#     print(f"{num} is not a prime number.")
# elif num > 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             prime = True
#             break
# if prime:
#     print(f"{num} is not a prime number")
# else :
#     print(f"{num} is a prime number")

# write a python program to print all prime numbers in an interval of 1-10

# lower = int(input("Enter the lower range of input : "))
# upper = int(input("Enter the upper range of input : "))

# print(f"Printing prime numbers in between the range {lower} to {upper}")

# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else :
#             print(num)

# write a python program to find the factorial of a number

# num = int(input("Enter a number : "))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("Factorial of 0 in 1")
# else:
#     for i in range(1, num+1):
#         factorial = factorial*i
#     print(f"The factorial of {num} is {factorial}")

# write a python program to display the multiplication table

# num = int(input("Display the multiplication table of : "))

# for i in range(1, 11):
#     print(f"{num} X {i} = {num*i}") 

# write a python program to print the fibonacci sequence.

# nterms = int(input("How many terms? "))

# n1, n2 = 0, 1
# count = 0

# if nterms <= 0:
#     print("Please enter a positive number.")
# elif nterms == 1:
#     print(f" Fibonacci sequence upto {nterms} : ")
#     print(n1)
# else :
#     print(f" Fibonacci sequence upto {nterms} : ")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1


# nterms = int(input("How many terms ..?"))

# n1, n2 = 0, 1
# count = 0

# if nterms <= 0:
#     print("Please enter a positive number.")
# elif nterms == 1:
#     print(f"Fibonacci sequence up to {nterms} : {n1}")
# else :
#     print(f"Fibonacci sequence upto {nterms} :")
#     while count < nterms :
#         print(n1, end=", ")
#         nth  = n1 + n2
#         n1, n2 = n2, nth
#         count += 1
#     print()

