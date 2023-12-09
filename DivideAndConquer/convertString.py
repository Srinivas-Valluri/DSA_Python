#Problem: S1 and S2 are given strings. Convert S2 to S1 using delete, insert or replace operations. Findthe minimum count of edit operations.

def findMinOperation(s1, s2, index1, index2):
  if index1==len(s1):
    return len(s2)-index2
  if index2==len(s2):
    return len(s1)-index1
  if s1[index1]==s2[index2]:
    return findMinOperation(s1, s2, index1+1, index2+1)
  
  else:
    deleteOp = 1+findMinOperation(s1,s2, index1, index2+1)
    insertOp = 1+findMinOperation(s1,s2, index1+1, index2)
    replaceOp = 1+findMinOperation(s1,s2, index1+1, index2+1)
    return min(deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrles",0,0))
