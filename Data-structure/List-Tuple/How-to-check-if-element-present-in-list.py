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

