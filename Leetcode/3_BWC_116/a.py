class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i,n):
                temp = len(set(nums[i:j+1]))
                ans+=(temp*temp)
                
        return ans