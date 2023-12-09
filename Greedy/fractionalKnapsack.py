#It is a problem in combinatorial optimization.

#Problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total
#weight is less than or equal to a given limit and the total value is as large as possible. The selectable items can be divided so it is called 
#FRACTIONAL knapsak or else it is Zero One knapsak problem(Divide and Conquer).

class Item:
  def __init__(self, weight, value) -> None:
    self.weight = weight
    self.value = value
    self.ratio = value / weight

def knapsackMethod(items, capacity):
  items.sort(key= lambda x:x.ratio, reverse=True)
  usedCapacity = 0
  totalValue = 0
  for i in items:
    if usedCapacity+i.weight<=capacity:
      usedCapacity+=i.weight
      totalValue+=i.value
    else:
      unusedWeight = capacity-usedCapacity
      value = i.ratio*unusedWeight
      usedCapacity+=unusedWeight
      totalValue+=value
      break
  print("The total value obtained is: "+str(totalValue))

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
items = [item1, item2, item3]

knapsackMethod(items, 50)