from itertools import *

# count(start[, step])
# (以start为首项, step为公差的等差数列, step默认为1)
arithmetic = count(5, 3)
print(next(arithmetic))
print(next(arithmetic))
for n in arithmetic:
    if n > 15:
        break
    else:
        print(n)

# cycle(p)
# 对序列循环遍历
cycleSeq = cycle('xyz')
print(next(cycleSeq))
print(next(cycleSeq))
i = 0
for c in cycleSeq:
    if i > 4:
        break
    else:
        print(c)
    i += 1

# repeat(elem[, n])
# elem, elem, elem...( 重复n次或者无限下去)
repeatSeq = repeat("zzhznx", 2)
print(next(repeatSeq))
print(next(repeatSeq))
# print(next(repeatSeq))

# chain(p, q, ...)
# 一个一个地遍历这些序列的, 不必生成大序列即可这样遍历
chainSeq = chain("zzh", "znx")
for c in chainSeq:
    print(c)

# compress(data d, selector s)
# (d[0] if s[0]), (d[1] if s[1]), ...
for c in compress("abcdef", [1, 1, 0, 1, 0, 1]):
    print(c)

# dropwhile(func f, seq q)
# 当函数f执行返回假时, 开始迭代序列
for n in dropwhile(lambda x: x < 5, [1, 2, 6, 4, 3]):#6, 4, 3
    print(n)

# takewhile(func, seq)
# 从序列的头开始, 直到执行函数func失败.
for n in takewhile(lambda x: x < 5, [1, 2, 6, 4, 3]):#1, 2
    print(n)

# groupby(iterable[, keyfunc])
# 按照keyfunc函数对序列每个元素执行后的结果分组(每个分组是一个迭代器), 返回这些分组的迭代器
a = ['aa', 'ab', 'abc', 'bcd', 'abcde']
for i, k in groupby(a, len):
    for m in k:
        print(m, end=" ")
    print(i)

# islice(seq[, start], stop[, step])
# 返回序列seq的从start开始到stop结束(不包括stop)的步长为step的元素的迭代器
for c in islice("abcdefg", 0, 4, 2):
    print(c)

# starmap(func[, iterable])
# 对序列seq的每个元素作为func的参数列表执行, 返回执行结果的迭代器
for n in starmap(pow, [(2, 3), (3, 4), (5, 2)]):
    print(n)

# tee(iterable[, n = 2])
# 把一个迭代器分为n个迭代器, 返回一个元组.默认是两个
a = "hello"
c, d = tee(a, 2)
for i, j in zip(c, d):
    print(i, j)

# permutations(iterable[, r])
# 排列
# 创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同
for i in permutations([1, 2, 3], 3):
    print(i)

# product(iter1, iter2, ... iterN [, repeat = 1])
# 创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数
for i in product([1, 2, 3], [4, 5], [6]):
    print(i)
for i in product([1, 3], repeat=3):
    print(i)
for i in product([1, 5], [2, 4], repeat=2): #等同于product([1, 5], [2, 4], [1, 5], [2, 4])
    print(i)

# combinations(iterable, r)
# 组合（不重复）
# 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序
for i in combinations([1, 2, 3], 2):
    print(i)

# combinations_with_replacement(iterable, r)
# 组合（不重复）
for i in combinations_with_replacement([1, 2, 3], 2):
    print(i)