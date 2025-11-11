import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper

#Exercise 4
Quiz = Helper.input("What is the capital of France? ", input_types=(str,))
Countries = [
    {"Country": "Germany", "Capital": "Berlin"},
    {"Country": "Italy", "Capital": "Rome"},
    {"Country": "Spain", "Capital": "Madrid"},
    {"Country": "Portugal", "Capital": "Lisbon"},
    {"Country": "Netherlands", "Capital": "Amsterdam"},
    {"Country": "Belgium", "Capital": "Brussels"},
    {"Country": "Austria", "Capital": "Vienna"},
    {"Country": "Finland", "Capital": "Helsinki"},
    {"Country": "Ireland", "Capital": "Dublin"},
    {"Country": "France", "Capital": "Paris"}
]

if (Quiz.lower() == "paris"):
	print("Correct") 
else:
	print("Incorrect, the answer is paris.")

for Country in Countries:
	Answer = Helper.input(f"What is the capital of {Country['Country']}? ", input_types=(str,)).lower()
	if Answer == Country["Capital"].lower():
		print("Correct")
	else:
		print(f"Incorrect, the answer is {Country['Capital']}.")

#Done on October 8th