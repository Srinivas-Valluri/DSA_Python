#Top Down Approach

def houseRobberTD(arr, index, dp):
  if index>=len(arr):
    return 0
  if index not in dp:
    subP1 = arr[index] + houseRobberTD(arr, index+2, dp)
    subP2 = houseRobberTD(arr, index+1, dp)
    dp[index] = max(subP1, subP2)
  return dp[index]


#Bottom Up Approach

def houseRobberBU(arr):
  dp = [0]*(len(arr)+2)
  for i in range(len(arr)-1, -1, -1):
    dp[i]=max(arr[i]+dp[i+2], dp[i+1])
  return dp[0]

print(houseRobberTD([6,7,1,30,8,2,4], 0, {}))
print(houseRobberBU([6,7,1,30,8,2,4]))