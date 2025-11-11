import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper

#Exercise 8
list_of_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave", "Dove"]

def search(query):
	matches = [name for name in list_of_names if name.lower().startswith(query.lower())]
	if matches:
	   	print("Found matches:")
	   	for match in matches:
	   		print(f"- {match}")
	else:
		print("No matches found.")

print("Available names: ", list_of_names)
while True:
	name = Helper.input("Who do you want to search for? ", input_types=(str,))
	search(name)

#Done on October 8th