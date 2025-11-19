#pylint:disable=W0201
#pylint:disable=E1101
#pylint:disable=E0401
#pylint:disable=W0718
import time, os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Dependencies"))
import Helper

# Exercise 6
class Login:
    def __init__(self, **kwargs):
    	self.__dict__.update(kwargs)

passwords = Login(
	passcode = [12345] # passcodes, more can be added like (12345, 1234, 123)
)

password_attempts = Login(
	current = 0, # current amount of passwords attempted
	max = 3, # maximum amount of password attempts before timeout
)

failed_attempts = Login(
	current = 0, # current failed attempts
	max = 3, # maximum failed attempts allowed
	timeout = 0, # current timeout
	timeout_previous = 0, # previous timeout
	timeout_increment = 2 # timeout incremental increase
)

def compare_passwords(password):
    password = str(password).strip()
    # if password is a integer find if it exists in the password list and compare
    # if password is a string find if it exists in the password list and compare
    return any(
        int(password) == int(pc) # if the entered password is a digit do this
        if password.isdigit() and str(pc).isdigit()
        else password == str(pc).strip() # otherwise do this if it is a string
        for pc in passwords.passcode # for all passwords in the passcode table
    )

def setup_timeout():
	if password_attempts.current >= password_attempts.max: # if the current attempts are over or equal to the max amounts of attempts
		password_attempts.current, failed_attempts.current = 0, failed_attempts.current + 1 # set the current attempt count to 0 and increase curent fail count by 1
		
		# if previous time is 0, use time increment to determine initial timeout by multiplying time increment with current fail attempt otherwise default to previous time. 
		failed_attempts.timeout = (
		failed_attempts.timeout_increment * failed_attempts.current
		if failed_attempts.timeout_previous < 1
		else failed_attempts.timeout_previous * failed_attempts.current
		)
		
		failed_attempts.timeout_previous = failed_attempts.timeout # update previous timeout
		
		print(f"Timeout for {failed_attempts.timeout} second{'s' if failed_attempts.timeout != 1 else ''}") # print the current timeout time
		print(f"Previous timeout: {failed_attempts.timeout_previous} second{'s' if failed_attempts.timeout_previous != 1 else ''}") # print the previous timeout time
		print(f"Failed attempts: {failed_attempts.current}\n") # print current failed attempts
		
		while failed_attempts.timeout > 0:
			print(f"Please wait {failed_attempts.timeout} second{'s' if failed_attempts.timeout != 1 else ''} before next try...")
			time.sleep(1)
			failed_attempts.timeout -= 1
			Helper.clear()
		
def enter_password(password):
	if failed_attempts.current >= failed_attempts.max: # if current fail attempts exceeds the maximum return nothing
		print("Too many failed attempts. Access locked.\n") # prints that the user can not enter anymore
		return False

	if compare_passwords(password):
		password_attempts.current, failed_attempts.current, failed_attempts.timeout, failed_attempts.timeout_previous = (0,0,0,0) # reset all variables to 0
		print("Correct password.\n")
		return True
	else:	
		password_attempts.current += 1 # increase attempt count by 1
		print("Incorrect password.")
		print(f"Attempt {password_attempts.current} of {password_attempts.max}\n") # prints current failed attempt amounts
		
		if password_attempts.current >= password_attempts.max:
			setup_timeout()
		return False
		
while True:
	try:
		if failed_attempts.timeout <= 0:
			Helper.flush_input()
			pw = Helper.input("Enter password ", input_types=(str, int))
			enter_password(pw)
	except Exception as e:
		print(f"Error: {e}") # if it somehow errors it will print the error

#Done on October 8th
#this was hell by the way.