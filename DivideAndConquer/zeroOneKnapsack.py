#Problem: Given weights and profits of N items. Find the maximum profit within given capacity of C. Items cannot be broken.
#Solution: Select first item OR skip the first item and continue to next item

class Item:
  def __init__(self, profit, weight) -> None:
    self.profit = profit
    self.weight = weight

def zoKnapsak(items, capacity, currentIndex):
  if capacity<=0 or currentIndex<0 or currentIndex>=len(items):
    return 0
  elif items[currentIndex].weight<=capacity:
    profit1 = items[currentIndex].profit+zoKnapsak(items, capacity-items[currentIndex].weight, currentIndex+1)
    profit2 = zoKnapsak(items, capacity, currentIndex+1)
    return max(profit1, profit2)
  else:
    return 0
  
mango = Item(31,3)
apple = Item(26,1)
orange = Item(17,2)
banana = Item(72,5)

items = [mango, apple, orange, banana]
print(zoKnapsak(items,7,0))

