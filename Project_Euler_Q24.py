import itertools

ls = [0,1,2,3,4,5,6,7,8,9]
x = list(itertools.permutations(ls)) # finds all the permutations of ls
print(''.join(map(str, x[999999])))  # maps all values to string then joins as you can't use join() with integers