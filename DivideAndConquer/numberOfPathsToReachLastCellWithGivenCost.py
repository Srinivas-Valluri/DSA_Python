#Problem: Find the number of ways to reach corner of matrix with given fixed cost.

def numberOfPaths(arr, row, col, capacity):
  if capacity<0:
    return 0
  elif row==0 and col==0:
    if arr[row][col]-capacity==0:
      return 1
    else:
      return 0
  elif row==0:
    return numberOfPaths(arr, row, col-1, capacity-arr[row][col])
  elif col==0:
    return numberOfPaths(arr, row-1, col, capacity-arr[row][col])
  else:
    op1 = numberOfPaths(arr, row-1, col, capacity-arr[row][col])
    op2 = numberOfPaths(arr, row, col-1, capacity-arr[row][col])
    return op1+op2
  
arr = [
  [4,7,1,6],
  [5,7,3,9],
  [3,2,1,2],
  [7,1,6,3]
]
print(numberOfPaths(arr, 3, 3, 20))