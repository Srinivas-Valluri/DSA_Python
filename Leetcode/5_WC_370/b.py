from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges) -> int:
        ans = -1
        if n==1:
            return 0
        d = defaultdict(lambda: 0)
        
        for [i,j] in edges:
            d[j]+=1
            
        print(d)
        print(len(d))
        if len(d)==n-1:
            for i in range(0,n):
                if i not in d.keys():
                    return i
        return ans