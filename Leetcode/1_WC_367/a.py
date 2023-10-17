ans = ['11001','10011', '1101','1011']

def sortLen(e):
    return len(e)

ans.sort(key=sortLen)

print(ans)

anss= ['1101','1011']
anss.sort()
print(anss)

print(len(ans[0]))

min_len = len(ans[0])
final_ans = []

for i in ans:
    if len(i)==min_len:
        final_ans.append(i)
    else:
        break
print(final_ans)
final_ans.sort()
print(final_ans)