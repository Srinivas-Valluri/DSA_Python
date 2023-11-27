
def linearSearch(customList, value): #Time-O(N) Space-O(1)
  result = -1
  for i in range(len(customList)):
    if customList[i]==value:
      return i
  return result

def binarySearch(customList, value): #Time-O(LogN) Space-O(1)
  l, r = 0, len(customList)-1
  m = (r+l)//2
  while l<=r:
    if customList[m]==value:
      return m
    elif customList[m]>value:
      r = m-1
    else:
      l = m+1
    m = (r+l)//2
  return -1

print(linearSearch([20,30,40,90,50], 90))
print(binarySearch([20,30,40,50,90,100], 1000))