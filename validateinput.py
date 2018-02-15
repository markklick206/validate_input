# mk
# validate_input
# Simple validate_input function using regex patterns to detect numeric or string input.

# import the python regular expression package
import re

def numericValuesValidation(input_numeric):
	# use re.compile for clarity. This is a pattern for any numeric. \d for float and + for as many times up to a decimal point 
    # \. then \d+ again for any number of numbers after the decimal point
    pattern = re.compile('\d+(\.\d+)?')
    # re.match function on a compiled regex object will check to see if this input_numeric variable matches the numeric pattern
    while pattern.match(input_numeric) == None:
        input_numeric = input("Bad input: ")
    # convert to float before returning
    return float(input_numeric)

def stringValuesValidation(input_string):
    # custom string matching regex
    pattern = re.compile('[a-zA-Z1-9]+')
	# check to see if input matches your desired string pattern
    while pattern.match(input_string) == None:
        input_string = input("Bad input: ")
    
    return input_string