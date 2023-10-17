my_dict = {'a': 1, 'b': 2, 'c': 3}

rev_dict = dict.fromkeys(my_dict.values())

for key, value in my_dict.items():
  rev_dict[value] = key
  

print(rev_dict)
