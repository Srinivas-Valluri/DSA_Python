import math
def constructProductMatrix(grid):
    dp = [math.inf]
    for i in range(len(grid)):
        for j in range(i+1, len(grid)):
            if grid[j]>grid[i]:
                for k in range(j+1, len(grid)):
                    if grid[i] < grid[j] and grid[j] > grid[k]:
                        if len(dp)!=0 and min(dp)>(grid[i]+grid[j]+grid[k]):
                            dp.clear()
                            dp.append(grid[i]+grid[j]+grid[k])

    return -1 if len(dp)==0 else min(dp)

grid = [8,6,1,5,3]
print(constructProductMatrix(grid))

# TLE 😥