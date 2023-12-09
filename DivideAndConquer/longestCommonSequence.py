#Problem: Given String S1 and S2. Find the length of the longest subsequence. Subsequence is obtained by deleting some elements but retaining order.
#Solution: See the sub-problems.


def findLCS(s1, s2, index1, index2):
  if index1==len(s1) or index2 == len(s2):
    return 0
  if s1[index1]==s2[index2]:
    return 1+findLCS(s1, s2, index1+1, index2+1)
  else:
    subP1 = findLCS(s1, s2, index1+1, index2)
    subP2 = findLCS(s1, s2, index1, index2+1)
    return max(subP1, subP2)
  
print(findLCS("elephant", "eretpat", 0, 0))