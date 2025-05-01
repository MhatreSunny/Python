'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.H
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''

# input_text = input("Enter text to write to the file : ")
# # print(input_text)


def append_text(filename):
    try:
        with open(filename, 'w') as file_text:
            user_input = input("Enter text to write to the file : ")
            file_text.write(user_input + '\n')
            print(f"Data got successfully written to {filename}")
        
        with open(filename, 'a') as addtional_txt:
            additional_input = input("Enter additional text to append : ")
            addtional_txt.write(additional_input + '\n')
            print(f"Data successfully appended.")

        print(f"Final content of {filename}: ")
        with open(filename, 'r') as file:
            for i in file:
                print(i)
    
    except FileNotFoundError:
        print(f"The file {filename} not found")


append_text("/home/sunnymhatre/Python/Practice/output.txt")
           
    
