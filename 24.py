from itertools import islice

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# #print([[row[col] for row in a] for col in range(len(a[0]))])
#
# a = [1,2,3,4,5,6]
# print(iter(a))
# print([iter(a)])
# print([iter(a)] * 2)
# print([iter(a), iter(a)])
# print(*([iter(a)] * 2))
# print( list( zip(*([iter(a)] * 2)) ) )
# print( list( zip(*([iter(a), iter(a)])) ) )

a = [1,2,3,4,5,6]
def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    while 1:
        try:
            print(list(z.__next__()))
        except StopIteration:
            break
    #print(list(z)[0])
    return list(zip(*z))

print(n_grams(a, 3))