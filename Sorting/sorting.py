import math

def bubbleSort(customList): #Time-O(N*N) Space-O(1)
  for i in range(len(customList)-1):
    for j in range(len(customList)-i-1):
      if customList[j]>customList[j+1]:
        customList[j], customList[j+1] = customList[j+1], customList[j]

  print("Bubble Sort",customList)

def selectionSort(customList): #Time-O(N*N) Space-O(1)
  for i in range(len(customList)):
    min_index = i
    for j in range(i+1, len(customList)):
      if customList[min_index]>customList[j]:
        min_index=j
    customList[i], customList[min_index] = customList[min_index], customList[i]
  print("Selection Sort", customList)

def insertionSort(customList): #Time-O(N*N) Space-O(1)
  for i in range(1, len(customList)):
    key = customList[i]
    j = i-1
    while j>=0 and key<customList[j]:
      customList[j+1] = customList[j]
      j-=1
    customList[j+1] = key
  return customList

def bucketSort(customList): #Time-O(N*N) Space-O(N)
  numberOfBuckets = round(math.sqrt(len(customList)))
  maxValue = max(customList)
  arr = []

  for i in range(numberOfBuckets):
    arr.append([])
  for i in customList:
    index_b = math.ceil(i*numberOfBuckets/maxValue)
    arr[index_b-1].append(i)
  for i in range(numberOfBuckets):
    arr[i] = insertionSort(arr[i])

  k = 0
  for i in range(numberOfBuckets):
    for j in range(len(arr[i])):
      customList[k] = arr[i][j]
      k+=1
  return customList
  
def merge(customList, l, m, r):
  n1 = m-l+1
  n2 = r-m

  L = [0]*n1
  R = [0]*n2

  for i in range(n1):
    L[i] = customList[l+i]
  for i in range(n2):
    R[i]=customList[m+1+i]

  i = 0
  j = 0
  k = l
  while i<n1 and j<n2:
    if L[i]<=R[j]:
      customList[k]=L[i]
      i+=1
    else:
      customList[k]=R[j]
      j+=1
    k+=1
  while i<n1:
    customList[k]=L[i]
    i+=1
    k+=1
  while j<n2:
    customList[k]=R[j]
    j+=1
    k+=1

def mergeSort(customList, l, r): #Time-O(N*LogN) Space-O(N)
  if l<r:
    m = (l+(r-1))//2
    mergeSort(customList, l, m)
    mergeSort(customList, m+1, r)
    merge(customList, l, m ,r)
  return customList

def swap(my_list, index1, index2):
  my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
  swap_index = pivot_index
  for i in range(pivot_index+1, end_index+1):
    if my_list[i]<my_list[pivot_index]:
      swap_index+=1
      swap(my_list, swap_index, i)
  swap(my_list, pivot_index, swap_index)
  return swap_index

def quicksort_helper(my_list, left, right):
  if left<right:
    pivot_index = pivot(my_list, left, right)
    quicksort_helper(my_list, left, pivot_index-1)
    quicksort_helper(my_list, pivot_index+1, right)
  return my_list

def quicksort(my_list): #Time-O(N*LogN) Space-O(N)
  return quicksort_helper(my_list, 0, len(my_list)-1)

def heapify(customList, n, i):
  smallest = i
  l = 2*i+1
  r = 2*i+2
  if l<n and customList[l]<customList[smallest]:
    smallest=l
  if r<n and customList[r]<customList[smallest]:
    smallest=r

  if smallest!=i:
    customList[i], customList[smallest] = customList[smallest], customList[i]
    heapify(customList, n, smallest)


def heapsort(customList): #Time-O(N*LogN) Space-O(1)
  n = len(customList)
  for i in range(int(n/2)-1, -1, -1):
    heapify(customList, n, i)

  for i in range(n-1, 0, -1):
    customList[i], customList[0] = customList[0], customList[i]
    heapify(customList, i, 0)
  customList.reverse()
  return customList




cList = [2,1,7,6,5,3,4,9,8] 
bubbleSort([2,1,7,6,5,3,4,9,8])
selectionSort([2,1,7,6,5,3,4,9,8])
print("Insertion Sort", insertionSort([2,1,7,6,5,3,4,9,8]))
print("Bucket Sort", bucketSort([2,1,7,6,5,3,4,9,8]))
print("Merge Sort", mergeSort([2,1,7,6,5,3,4,9,8], 0, 8))
print("Quick Sort",quicksort([2,1,7,6,5,3,4,9,8]))
print("Heap Sort", heapsort([2,1,7,6,5,3,4,9,8]))
