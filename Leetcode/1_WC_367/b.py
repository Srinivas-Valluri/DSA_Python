def shortestBeautifulSubstring(s, k):
        
    if s.count("1") < k:
        print("skip")
        return ""
    
    start, end = 0,0
    one_index = []
    ans = []
    
    for i in range(len(s)):
        if s[i]=="1":
            one_index.append(i)
    
    for i in range(len(one_index)-k+1):
        ans.append(s[one_index[i]:one_index[i+k-1]+1])
    print(ans)  
    ans.sort()
    print("this is ans")
    print(ans, "this is ans")
    return ans[0]

print(shortestBeautifulSubstring("100011001", 3))