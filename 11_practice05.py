from functools import reduce
l = [3, 8, 4, 2, 56, 57, 67, 78, 2]

a = reduce(max, l)
print(a)