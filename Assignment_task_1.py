### Task 1: Perform Basic Mathematical Operations
'''
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

addition = num1 + num2
sub = num1 - num2
division = num1 / num2
multiply = num1 * num2

print(f"Addition : {addition}")
print(f"Substraction : {sub}")
print(f"Division : {division}")
print(f"Multiplication : {multiply}")
