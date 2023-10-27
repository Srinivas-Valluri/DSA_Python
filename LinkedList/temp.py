s = "srinivas"
n = len(s)


for window in range(n,1,-1):
    for i in range(n-window+1):
        subString = s[i:i+window]
        print(subString, i, window)