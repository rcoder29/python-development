'''
Code sample for Handling Exception
'''

# global min, max
MIN_NUMBER=1
MAX_NUMBER=100000

#declare variables to hold the numbers
num1=None
num2=None

# custom exception class
class InvalidInputNumberError(Exception):
    '''
    Custom exception class to raise when input number entered is not with in range
    '''

class StringInputError(Exception):
    '''
    Custom exception class to raise when input is string instead of number
    '''


# get two input numbers and divide first number by second number
#while(True):
try:
    num1=input("Enter first number:")
    num1=int(num1)
    if num1 < MIN_NUMBER or num1 > MAX_NUMBER:
        print("Invalid number entered, it should be between ", MIN_NUMBER, MAX_NUMBER)
        #raise ValueError("Invalid number entered")
        raise InvalidInputNumberError("Invalid number entered")
        #print("try again...")
    #else:
    #    break
except ValueError as e:
    # check if value type is string
    print(type(num1))
    if type(num1) is str :
        raise StringInputError("String entered as input instead of a number!!")
    else:
        raise e
else:
    print("No Exceptions reading Input number1")
finally:
    print("reached end of read first input...")

try:
    #while(True):
    num2=input("Enter second number:")
    num2 = int(num2)
    if num2 < MIN_NUMBER or num2-1 > MAX_NUMBER:
        print("Invalid number entered, it should be between ", MIN_NUMBER, MAX_NUMBER)
        #raise ValueError("Invalid number entered")
        raise InvalidInputNumberError("Invalid number entered")
        #print("try again...")
    #else:
    #    break
except ValueError as e: # comes here on value error
    # check if value type is string
    print(type(num2))
    if type(num2) is str :
        raise StringInputError("String entered as input instead of a number!!")
    else:
        raise e
else: # comes here if no exceptions
    print("No Exceptions reading Input number2")
finally: # comes here every time
    print("reached end of read second input...")

# perform division
result=num1/num2
print("Result of division - ",result)
