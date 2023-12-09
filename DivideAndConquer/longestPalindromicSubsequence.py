#Problem: Given S string. Find longest palindromic subsequence(LPS).

def longPS(word, start, end):
  if start>end:
    return 0
  elif start==end:
    return 1
  elif word[start]==word[end]:
    return 2+longPS(word, start+1, end-1)
  else:
    subP1 = longPS(word, start+1, end)
    subP2 = longPS(word, start, end-1)
    return max(subP1, subP2)
  
print(longPS("ELRMENMET", 0, 8))