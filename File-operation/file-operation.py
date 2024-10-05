#--------------------------------Reading a file and printing the file content ----------------------
import json
import pickle
class Person:
    def __init__(self,name,age,country) -> None:
        self.name=name
        self.age=age
        self.country=country
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'country': self.country
        }
    
    def __str__(self):
        return f'Person(Name: {self.name}, Age: {self.age}, Country: {self.country})'
    


file = open('File-operation/message.txt','r')
file_content= file.read()
file_content=file_content.strip()
data=file_content.split('\n',-1)
person_list = []
count=0
for content in data:
    details=content.split('|')
    if(count==0):
        count=count+1
        continue
    else:
       person= Person(details[0],details[1],details[2]) 
       person_list.append(person)

with open('File-operation/person_list.pkl', 'wb') as file2:
    pickle.dump(person_list, file2)

with open('File-operation/person_list.pkl', 'rb') as file5:
    loaded_person_list = pickle.load(file5)
    for person in loaded_person_list:
        print(person) 
    
file.close()

#------------------------------ Modified code with same functionality  ----------------------------------------------

class Person:
    def __init__(self, name, age, country) -> None:
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f'Person(Name: {self.name}, Age: {self.age}, Country: {self.country})'


# Read the file content
with open('File-operation/message.txt', 'r') as file:
    file_content = file.read()

# Trim and split the file content into lines
file_content = file_content.strip()
data = file_content.split('\n')

# Initialize an empty list to store Person objects
person_list = []

# Loop through the data, split by '|' and create Person objects
for idx, content in enumerate(data):
    if idx == 0:
        # Skip the first line (if it's a header)
        continue
    
    details = content.split('|')
    # Create a Person object and append it to the list
    person = Person(details[0], details[1], details[2])
    person_list.append(person)

# Print the list of Person objects
#for person in person_list:
    #print(person)  # This will print the __str__ representation of Person


#---------------------- Write data into file ----------------------------------------------------------

file1= open('File-operation/ack.txt','a')
file1 = open('File-operation/ack.txt','w')
file1.write('Hello, World!\n')     
file1.write('This is a second line.\n')
file1.close()

