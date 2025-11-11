import calendar, os, sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper

#Exercise 5
def get_days_in_month(year, month=1):
	return calendar.monthrange(year, month)[1]

year = Helper.input("Insert a year number: ", input_types=(int,))
month = Helper.input("Insert a month number: ", input_types=(int,), min_value=1, max_value=12)
print(f"Number of days in {calendar.month_name[month]} {year}: {get_days_in_month(year, month)}")

#Done on October 8th
#Automatically adjusts for leap years so incase human error occurs for example you enter 2025 as a leap year and it agreeing and just returning wrong info, it just does it for you without any extra input!