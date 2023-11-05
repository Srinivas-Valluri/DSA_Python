class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ans = 0
        minSum = 0
        for i in range(len(grid)):
            temp = sum(grid[i])
            if temp>minSum:
                ans = i
                minSum = temp
            
        return ans