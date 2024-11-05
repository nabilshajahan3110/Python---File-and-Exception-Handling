
# ASSIGNMENT - FILE & EXCEPTION HANDLING

# Exercise 1: (score : 1)
# Write a Python program to read a file and display its contents

file1=open("C:\\Users\\nms31\\OneDrive\\Desktop\\File Handling\\Hello.txt",'r') # r = read
print(file1.read())

# Exercise 2: (score : 1)
# Write a Python program to copy the contents of one file to another file

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError:
        print("An error occurred while copying the file.")
    finally:
        print("The function has completed the task")

source_file = "C:\\Users\\nms31\\OneDrive\\Desktop\\File Handling\\Read file.txt"
destination_file = "C:\\Users\\nms31\\OneDrive\\Desktop\\File Handling\\Write file.txt"
copy_file("C:\\Users\\nms31\\OneDrive\\Desktop\\File Handling\\Read file.txt",
          "C:\\Users\\nms31\\OneDrive\\Desktop\\File Handling\\Write file.txt")

# Exercise 3: (score : 2)
# Write a Python program to read the content of a file and count the total number of words in that file.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        print(f"The total number of words in '{filename}' is: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print("An error occurred while reading the file.")
    finally:
        print("The word count has been done successfully")

filename = "C:\\Users\\nms31\\OneDrive\\Downloads\\File Handling\\Read file.txt"
count_words_in_file(filename)

# Exercise 4: (score : 1)
# Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur

a=input("the string which is to be converted to int: ")
try:
     b=int(a)
     print(b,"the string converted to integer")
except ValueError:
     print("This string cannot be converted to integer")

# Exercise 5: (score : 1)
# Write a Python program that prompts the user to input a list of integers and raises an exception if any of the
# integers in the list are negative.

def get_positive_integers():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers, separated by spaces: ")

        # Convert the input string to a list of integers
        int_list = [int(num) for num in user_input.split()]

        # Check for any negative integers
        for num in int_list:
            if num < 0:
                raise ValueError("Negative numbers are not allowed.")

        print("All numbers are non-negative:", int_list)

    except ValueError as e:
        print("Error:", e)

# Run the function
get_positive_integers()

# Exercise 6: (score : 2)
# Write a Python program that prompts the user to input a list of integers and computes the average of those integers.
# Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message
# indicating that the program has finished running.

def compute_average():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers, separated by spaces: ")

        # Convert the input string to a list of integers
        int_list = [int(num) for num in user_input.split()]

        # Calculate the average
        average = sum(int_list) / len(int_list)

        print("The average of the entered integers is:", average)

    except ValueError:
        print("Error: Please enter only integers.")
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list.")
    finally:
        print("Program has finished running.")

# Run the function
compute_average()

# Exercise 7 : (score : 2)
# Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no
# exception occurred.

def write_to_file():
    try:
        # Prompt the user to input a filename
        filename = input("Enter the filename to write to: ")

        # Specify the string to write to the file
        content = "Hello! My name is Nabil."

        # Open the file in write mode and write the string
        with open(filename, 'w') as file:
            file.write(content)

        # Print a welcome message if writing succeeds
        print("Welcome! The text has been successfully written to the file.")

    except Exception as e:
        # Handle any exception that may occur
        print("An error occurred:", e)

# Run the function
write_to_file()