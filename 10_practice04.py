l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 55, 60, 70, 80]

a = list(filter(lambda a: a%5==0 , l ))
print(a)