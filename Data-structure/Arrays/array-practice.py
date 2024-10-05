
import array

#In python the most common use of data structure in List , Below is one - 
names=['Amit','Aditi','Ajit']

print(names)

print(type(names)) #List 

for name in names:
    print(name)

#But there is a array module which can also be used to create a array 

arr = array.array('i',[1,2,3])

print(arr)

arr.append(6)

print(arr)

arr.insert(1,45)

print(arr)

sliceArray= arr[1:3]

print(sliceArray)



for num in arr:
    print(num)

