# starting with hello world, as the aim is to revise.

# Write a program to print something on your mind.

print("Program - 1 \n")
print("Welcome to revision...!")
print(10 * " -")

# Write a program in python to perform addition and subtraction

print("Program - 2 \n")
print("Enter the number on which you want to perform arthimetic operations.")
inputOne = float(input("Please enter the first number  : "))
inputTwo = float(input("Please enter the Second number  : "))


print(f"Addition of the input numbers : {inputOne + inputTwo}" )
print(f"Subtraction of the input numbers : {inputOne - inputTwo}")
if inputTwo == 0:
    print("Division by zero is not allowed")
else :
    print(f"Division of the input numbers : {inputOne/inputTwo}")

# working on the above program using loops

while True:
    print("Welcome to basic calculator..! checkout the options below.")
    print("Select using numbers \n" \
    "Enter 1 to perform Addition operation \n" \
    "Enter 2 to perform Subtraction operation \n" \
    "Enter 3 to perform division opertaion" \
    "Enter 0 to exit the program \n" )
    operationInput = int(input("Which operation would you like to perform choose using numbers "))
    if operationInput == 0:
        print("---- Thanks for using the program ----")
        break
    elif operationInput == 1:
        inputOne = int(input("Enter the first number you want to sum :"))
        inputTwo = int(input("Enter the second number you want to sum :"))
        print(f"Addition of two numbers : {inputOne + inputTwo}")
    elif operationInput == 2:
        inputOne = int(input("Enter the first number from which you want subtract :"))
        inputTwo = int(input("Enter the second number which needs to be subtracted :"))
        print(f"Subtraction of two numbers : {inputOne - inputTwo}")
    elif operationInput == 3:
        inputOne = int(input("Enter the dividend for division :"))
        inputTwo = int(input("Enter the divisor for division :"))
        while inputTwo == 0:
            print("Divisor can't be zero :")
            inputTwo = int(inputTwo("Please enter a vaild divisor :"))
        print(f"Division performed on the numbers is : {inputOne} / {inputTwo}")
    
    print(20 * "-")

    # calulate the area of the triangle using the given inputs

base = int(input("Enter the base of the triangle : "))
height = int(input("Enter the height of the triangle : "))

area = 0.5 * base * height

print(f"Area of the triangle is : {area}")