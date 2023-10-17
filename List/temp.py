def getWordsInLongestSubsequence(n: int, words, groups):
    max_len = 1
    start = [0]
    temp_len = 1
    
    if n==1:
        return words

    for i in range(len(groups)-1):
      if groups[i]!=groups[i+1]:
        temp_len+=1
      else:
        if temp_len>max_len:
          max_len=temp_len
          start.append(i-temp_len+1)
        temp_len=1


    if temp_len>max_len:
          max_len=temp_len
          start.append(len(groups)-temp_len)
        
    if max_len==1 and n==1:
        return words[0:1]
    if max_len==1:
        return words[0:0]
    
    return words[start[-1]:start[-1]+max_len]

print(getWordsInLongestSubsequence(2, ["d","a","v","b"], [1,0,0,1]))
