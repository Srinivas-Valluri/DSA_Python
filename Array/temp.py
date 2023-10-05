import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def traverse(arr):
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      print(arr[i][j], end=" ")
    print()

traverse(twoDArray)

newTwoDArray = np.delete(twoDArray, 1, axis=0)
print(newTwoDArray)