'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

x= int(input("Enter a number : "))
# print(x)

if x%2:
    print(f"{x} is an even number.")
else:
    print(f"{x} is an odd number.")

