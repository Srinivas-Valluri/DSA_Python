#Given different denominations and total amount. Find minimum number of coins to make amount.

denominations = [1, 20, 50]

def coinChange(denominations, amount):
  ans = 0
  denominations.sort()
  n = len(denominations)
  for i in range(n-1, -1, -1):
    ans+=amount//denominations[i]
    amount%=denominations[i]
    if amount==0:
      break
  print(ans)

coinChange(denominations, 110)
