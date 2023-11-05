#0 1 1 2 3 5 8....

def fib(n):
  assert n>=0 and int(n)==n, "Input should be positive integer!"
  if n==0:
    return 0
  elif n==1:
    return 1
  return fib(n-1)+fib(n-2)

print(fib(10))