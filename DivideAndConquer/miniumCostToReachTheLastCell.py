#Problem: Given 2D matrix. find the least possible way of reaching other corner.

def MinCLC(arr, row, col):
  if row==-1 or col==-1:
    return float('inf')
  if row==0 and col==0:
    return arr[0][0]
  else:
    op1 = MinCLC(arr, row-1, col)
    op2 = MinCLC(arr, row, col-1)
    return arr[row][col] + min(op1, op2)
  
arr = [
  [4,7,8,6,4],
  [6,7,3,9,2],
  [3,8,1,2,4],
  [7,1,7,3,7],
  [2,9,8,9,3],
]

print(MinCLC(arr, 4, 4))