
def zoKnapsack(items, capacity, currentIndex, dp):
  dictKey = str(currentIndex)+str(capacity)
  if currentIndex<0 or currentIndex>=len(items) or capacity<=0:
    return 0
  elif dictKey in dp:
    return dp[dictKey]
  elif items[currentIndex].weight<=capacity:
    profit1 = items[currentIndex].weight + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1, dp)
    profit2 = zoKnapsack(items, capacity, currentIndex+1, dp)
    dp[dictKey]=max(profit1, profit2)
    return dp[dictKey]
  else:
    return 0

