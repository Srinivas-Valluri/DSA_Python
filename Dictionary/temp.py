myDict = {
  "Miller": "Ownes a Mill",
  "Programmer": "Owner a computer", 
}
print(myDict["Miller"]) 

tuple_to_dict = [('one','uno'), ('two','dos')]
myDict2 = dict(tuple_to_dict)
print(myDict2)

myDict3 = dict(one="uno", two="dos")
print(myDict3)

a = [1,2,3,4]
name = "Srinivas"
myDict4 = dict.fromkeys(a,name)
print(myDict4)

del myDict4[1]
print(myDict4)

popped = myDict4.pop(2, "dwag")
print(myDict4)
print(popped)

item_pop = myDict4.get(2)
print(item_pop)