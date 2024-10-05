import datetime

date = datetime.datetime.now()

print(date)

#format-date 

print(date.strftime('%B'))

#How to parse a string to date in python

from datetime import datetime

date_string = "2024-90-05"

try:
    date_object = datetime.strptime(date_string, "%Y-%m-%d")   
    print(date_object)  # Output: 2024-10-05 00:00:00
except ValueError as e :
    print('Date format is wrong')
except Exception as e :
    print('Some issue converting date')
    


    
    
    

    



