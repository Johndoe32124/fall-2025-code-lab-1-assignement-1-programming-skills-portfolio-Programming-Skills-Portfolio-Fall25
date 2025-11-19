#pylint:disable=W0622
#pylint:disable=W0702
#module for every script in the assessment
#ID: 01-25-476
import sys, os, builtins
msvcrt = __import__('msvcrt') if os.name == 'nt' else None
termios = __import__('termios') if os.name != 'nt' else None

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def flush_input():
    if os.name == "nt":
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

# does not work with negatives
def input(message, input_types=(str,), min_value=None, max_value=None):
    # just checks that check if you entered the input I wanted you to input so it doesnt crash.
    while not (user_input := builtins.input(message).strip()) or not any(
        # checks if its a string if so it must not be numerical
        (input_type == str and not user_input.lstrip('-').replace('.', '', 1).isdigit()) or
        # checks if its an integer if so it must be a number and not a float or string
        (input_type == int and user_input.lstrip('-').isdigit()) or
        # checks if its a float if so it must be a decimel and not a integer or strint
        (input_type == float and user_input.lstrip('-').replace('.', '', 1).isdigit() and user_input.count('.') <= 1)
        for input_type in input_types
    ):
    	pass

    for input_type in input_types:
        try:
            value = input_type(user_input)
            # if set does a range check from the given values, allows extra flexability and helps me be sane knowing that I dont have to keep doing the same checks over and over.
            if input_type in (int, float):
                if (min_value is not None and value < min_value) or \
                   (max_value is not None and value > max_value):
                    print(f"Value must be between {min_value} and {max_value}.")
                    return input(message, input_types=input_types, min_value=min_value, max_value=max_value)
                    # pretty much annoys you until you give it the right input lol.
            return value
        except:
        	pass