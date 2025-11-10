import os, sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dependencies_path = os.path.join(project_dir, "Dependencies")
sys.path.append(dependencies_path)
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