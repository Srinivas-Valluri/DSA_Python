def constructProductMatrix(grid):
    dp = []
    min_val = min(grid)
    for i in range(len(grid)):
        for j in range(i+1, len(grid)):
            for k in range(j+1, len(grid)):
                if grid[i] < grid[j] and grid[j] > grid[k]:
                    dp.append(grid[i]+grid[j]+grid[k])
    
    return -1 if len(dp)==0 else min(dp)
                       
      

grid = [6,10,4]
print(constructProductMatrix(grid))