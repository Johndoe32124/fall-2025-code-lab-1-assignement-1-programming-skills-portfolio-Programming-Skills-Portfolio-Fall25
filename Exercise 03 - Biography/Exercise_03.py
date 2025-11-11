import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper
# ^^^^^ Imports instead of using the same code over and over you'll see this in the other exercises that require user input'

#Exercise 3
name = Helper.input("What is your name? ", input_types=(str,))
age = Helper.input("How old are you? ", input_types=(int,))
hometown = Helper.input("What is the name of your hometown? ", input_types=(str,))

print(f"Name: {name}\nAge: {age}\nHome Town: {hometown}")

#Done on October 8th