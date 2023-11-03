x = [1,2,3]
values = reversed(x)
strValues = [str(i) for i in values]
club = "\n".join(strValues)

print(club)

for i in range(1,10):
  print(i, end=" ")