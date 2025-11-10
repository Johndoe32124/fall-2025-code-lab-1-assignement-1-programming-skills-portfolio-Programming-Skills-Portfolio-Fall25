import os, sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dependencies_path = os.path.join(project_dir, "Dependencies")
sys.path.append(dependencies_path)
import Helper

#Exercise 10
def odd_or_even(number):
	if (number % 2) == 0:
		return "Even"
	else:
		return "Odd"
	
def main():
	ask = Helper.input("Input a number ", input_types=(int,))
	answer = odd_or_even(ask)
	print(answer)
	
if __name__ == "__main__":
	main()

#Done on October 8th