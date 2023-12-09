#Problem: Given N, find the number of ways to express N as a sum of 1, 3 and 4.
#Solution: Find solution of subproblem for f(N-1), f(N-3) and f(N-4) cuz the will build the solution of f(N).
#Do a dry run for finding f(4) and use f(0), f(1) and f(3) to again find f(4).

#added memoization personally. 🐍
ans = [None]*1500
def numberFactor(n):
  if n in [0,1,2]:
    return 1
  elif n==3:
    return 2
  else:
    subP1 = ans[n-1] if ans[n-1] else numberFactor(n-1)
    subP2 = ans[n-3] if ans[n-3] else numberFactor(n-3)
    subP3 = ans[n-4] if ans[n-4] else numberFactor(n-4)
    ans[n-1], ans[n-3], ans[n-4] = subP1, subP2, subP3
    return subP1+subP2+subP3

print(numberFactor(1000))