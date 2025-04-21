### Assignment 3 
'''
Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

'''
n = int(input("Enter a number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*(factorial(n-1))

result = factorial(n)
print(f"Factorial of {n} is: {result}")