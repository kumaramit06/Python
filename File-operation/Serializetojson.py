#--------------------------------- Serialize & Deserialize the objects to JSON  --------------------------------------
import json
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
    


person_list = [
    Person("John", 30, "USA"),
    Person("Alice", 25, "Canada"),
    Person("Bob", 28, "UK")
]

person_dicts = [person.to_dict() for person in person_list]

with open('person_list.json', 'w') as json_file:
    json.dump(person_dicts, json_file, indent=4)
