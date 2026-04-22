# write a python program to check if a number is odd or even

# num = int(input("Enter a number you want to check  :"))

# if num%2 == 0:
#     print("This is even number")
# else :
#     print("This is odd number")

# write a program to check if the given year is leap year

year = int(input("Enter the year you want to check : "))

if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not leap year")