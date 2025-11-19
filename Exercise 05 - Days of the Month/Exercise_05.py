import calendar, os, sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper

#Exercise 5 without needing a table or asking the user
def get_days_in_month(year, month):
	return calendar.month_name[month], calendar.monthrange(year, month)[1]

year = Helper.input("Insert a year number: ", input_types=(int,))
month = Helper.input("Insert a month number: ", input_types=(int,), min_value=1, max_value=12)
name, days = get_days_in_month(year, month)

print(f"Number of days in {name} {year}: {days}")


#Exercise 5 with a table and asks the user
months = {
    1:31, 
    2: 28, 
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }

month = Helper.input("Insert month: ", input_types=(int,), min_value=1, max_value=12)
if month == 2:
	leap_year = Helper.input("Is the year a leap year? (yes/no) ", input_types=(str,)).lower()
	if leap_year == "yes":
		months[2] = 29
	print(f"Numbers of days: {months[month]}")

#Done on October 8th
#Automatically adjusts for leap years so incase human error occurs for example you enter 2025 as a leap year and it agreeing and just returning wrong info, it just does it for you without any extra input!