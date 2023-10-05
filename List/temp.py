my_List = [1,2,3,4]

def traversal(arr, val):
  for i, item in enumerate(arr):
    if item==val:
      print(item, i)

traversal(my_List, 2)

a=[1,2,3,4]
c= a
c = c+[1]
print(a,c)

a = a*3
print(a)

a = "spam"
b = list(a)
print(a,b)

a = "spam spam spam"
b = a.split(" ")
print(a, b)

new_b=" ".join(b)
print(new_b)

#list comprehension
a = [1,2,3,4]
new_a = [x*2 for x in a if x%2==0]
print(a, new_a )