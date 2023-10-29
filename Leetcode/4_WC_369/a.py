class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        p = [0]* 31

        for i in nums:
            for j in range(0,31):
                temp = i & pow(2, j)
                if temp>0:
                      p[j]+=1

        for i in range(0,31):
              if p[i]>=k:
                ans+=pow(2,i)
        return ans