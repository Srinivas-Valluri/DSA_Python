def constructProductMatrix(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Initialize the product matrix p with all elements set to 1
    p = [[1] * m for _ in range(n)]
    
    # Calculate the product of all elements in the same row and column for each element
    for i in range(n):
        for j in range(m):
            row_product = 1
            col_product = 1
            
            # Calculate product of elements in the same row excluding grid[i][j]
            for k in range(m):
                if k != j:
                    row_product = (row_product * grid[i][k]) % 12345
            
            # Calculate product of elements in the same column excluding grid[i][j]
            for k in range(n):
                if k != i:
                    col_product = (col_product * grid[k][j]) % 12345
            
            # Calculate the element for p[i][j]
            p[i][j] = (row_product * col_product) % 12345
    
    return p

# Example usage
grid = [[8,18],[24,20],[9,5],[26,26],[19,19],[20,1],[20,23],[15,19],[24,14],[12,15],[22,3],[22,11],[9,25]]
print(constructProductMatrix(grid))