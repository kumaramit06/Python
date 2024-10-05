from collections import Counter


names1=['Amit','Aditi']

names2= ['Amit','Aditi','Ajit']

names3=['Amit','Aditi']

names4= ['Amit','Ajit','Aditi']

names5 = ['Amit','Aditi','Amit']

#Using the Equality Operator (==)
#If you want to check if two lists contain the same elements in the same order, you can use the equality operator:

are_equal = names1 == names2 
print(are_equal) #false

are_equl2= names1 == names3
print(are_equl2) #True 

are_equal3= names2 == names4
print(are_equal3) #False , even though same data is there , as the order is different so , the comparison is not working with this 


# Using Sets
#If you want to check if both lists contain the same unique elements regardless of order and duplicates, you can convert them to sets:

print(set(names3) == set(names5)) #True , with set the dupliacte gets removed and comparison is then happen with this 


#Using the collections.Counter
#f you need to consider duplicates but do not care about the order, you can use collections.Counter, which counts the occurrences of each element

print(Counter(names3) == Counter(names5)) #False , as counter check duplicate as well 



#4. Using a Loop

are_equal4 = len(names1) == len(names3) and all(name in names1 for name in names3 )

print(are_equal4) #True


#Use the == operator to check for equality with order sensitivity.
#Convert lists to sets to check for unique elements, ignoring order and duplicates.
#Use Counter to consider duplicates but ignore order.
#Use loops for custom comparison logic.