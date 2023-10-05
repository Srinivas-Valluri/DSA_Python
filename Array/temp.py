
from array import *

my_array = array('i', [1,2,3,4,5])

print("Traverse")
for i in my_array:
  print(i, end=" ")

print()
print("Accessing elements by index")
print(my_array[2])

print("Appending an element at end")
my_array.append(6)
print(my_array)

print("Using insert we can add elements at any position")
my_array.insert(0, 11)
print(my_array)

print("Extend Array")
my_array1 = array('i', [7,8,9])
my_array.extend(my_array1)
print(my_array)

print("Adding items from List")
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

print("Remove any element using remove()")
my_array.remove(22)
print(my_array)

print("Remove Last element")
my_array.pop()
print(my_array)

print("Get index of any element by giving its value")
print(my_array.index(20))

print("Revverse an array")
my_array.reverse()
print(my_array)

print("Get buffer_info()")
print(my_array.buffer_info())

print("Check the occurence of an element using count")
my_array.append(11)
print(my_array.count(11))

print("array to List")
#print(my_array.tolist())

print("Slice")
print(my_array[1:4])