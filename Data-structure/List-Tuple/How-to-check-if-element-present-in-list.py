#Check if name is present in names list
names1=['Amit','Aditi']

if 'Amit' in names1 : 
    print('Amit is present in the list')

else :
    print('Amit is not present in the list')
    

#Sorting the list 

numbers = [1,2,56,3,8,10]

print(numbers.sort()) # none , as after sort it does not return same list

print(numbers)


#Searching
#How to find index of one items in the list

if 56 in numbers:
    print(numbers.index(56)) #This will return the index

numbers.reverse()

print(numbers)


my_list = [10, 20, 30, 40, 50]
item_to_check = 30

found = False
for index, item in enumerate(my_list):
    if item == item_to_check:
        print(f"{item_to_check} is present at index {index}.")
        found = True
        break

if not found:
    print(f"{item_to_check} is not present in the list.")
    
    
    
#Use the in keyword to check for presence and the index() method to find the first occurrence's index.
#Use enumerate() to loop through the list and find both the index and the item.
#Use a list comprehension to find all indices if the item may appear multiple times


