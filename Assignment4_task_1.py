'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
'''

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            read_file = file.read()
            print(f"Reading file content: \n{read_file}")
            
    except FileNotFoundError:
        print(f'The file {filename} not found')
    

read_file("/home/sunnymhatre/Python/Practice/sample.txt")