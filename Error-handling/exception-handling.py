#----------------------------------- Basic Exception Handling -------------------------------------------------------#

try:
    result = 10/0
except Exception as e :
    print('some issue there')
else:
    print(result)
finally:
    print("This is the 'finally' block, always executed.")
    
#------------------------------------ Throw(Raise) exception from method -------------------------------------------------#

def divide_numbers(a, b):
    if b == 0:
        # Raise an exception when trying to divide by zero
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide_numbers(10, 0)  # This will raise an exception
except ValueError as e:
    print(f"Error: {e}")
    
    

#------------------------------------ Create custom Exception  -------------------------------------------------#

class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number<0:
        raise NegativeNumberError('Negative Number')
    else:
        print('Positive number')

try:
    check_positive(-3)
except NegativeNumberError as e:
     print(f"Error: {e}")
     

#---------------------------------------------------------------------------------------------------------------#