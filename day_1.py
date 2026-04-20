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