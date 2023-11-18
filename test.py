def merge(intervals):
    def helper(item):
            return item[0], item[1]
    intervals.sort(key=helper)
    #print(intervals)
    
    ans, n = [], len(intervals)
    temp = 0
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(n-1):
        # print(start, end)
        if end>=intervals[i+1][0]:
            if end>intervals[i+1][1]:
                continue
            end = intervals[i+1][1]
            continue
        else:
            ans.append([start, end])
            start = intervals[i+1][0]
            end = intervals[i+1][1]
    ans.append([start, end])
    

    return ans

print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
        