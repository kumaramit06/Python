"""
Dictionary is a key,value pair like map in java. 
This data structure is mutable. 

Creating the Dictionary: 
        Curly brackets are the simplest way to generate a Python dictionary
        It is also possible to use the dict() constructor to make a dictionary.

"""

dict = {"Name": "Gayle", "Age": 25, "Profession": "Engineer"}   
print(dict)

#traversing a dictionary 

for key, value in dict.items():
    print(f"Key: {key}, Value: {value}")
    

#Fetch all the key items 

for key in dict:
    print(key)
    

#fetch all the values 

for values in dict.values():
  print(values)


#Traversing a dictionary with index 

for index,(key,value) in enumerate(dict.items()):
      print(f"{index}: {key} -> {value}")
      

#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


