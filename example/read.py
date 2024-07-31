from stdio import read
from stdio import readint
from stdio import readfloat
from stdio import clear
from stdio import write
from stdio import skipline

# Usage examples:
clear()         # Clears the terminal

# Prompt user for name, age, and height
name = read("Enter your name: ")            # Example input: "Thiago"
age = readint("Enter your age: ")           # Example input: "26"
height = readfloat("Enter your height: ")   # Example input: "1.8"

clear()         # Clears the terminal

# Writes the collected information to the terminal
write(f"Your name is {name}, your age is {age}, and height is {height}")
skipline(2)

# Output

'''
Your name is Thiago, your age is 26, and height is 1.8

'''
