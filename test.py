
def largestSubmatrix(matrix) -> int:
    m = len(matrix)
    n = len(matrix[0])
    ans = 0
    for i in range(1,m):
        for j in range(n):
            if matrix[i-1][j]>0 and matrix[i][j]!=0:
                matrix[i][j] = matrix[i-1][j]+1
    print(matrix)
    for i in range(m):
        currRow = matrix[i][:]
        currRow.sort(reverse=True)
        base = 1
        currAns = 0
        for j in range(n):
            if currRow[j]==0:
                break
            currAns = currRow[j]*base
            ans = max(currAns, ans)
            base+=1

    return ans

print(largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))

