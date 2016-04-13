'''
Created on 2016年4月1日

@author: betterSN

  蘑菇街2016实习生招聘大数据工程师笔试题：给定9个数字，分别代表书写1-9的每个数字需要用的墨水量，并且给出总墨水量，请求出能书写出的最大数字为多少
即 输入：总墨水两vol
         书写1-9分别用的墨水两（a1,a2,...,a9）
   输出：得到的最大数字
例如：输入vol=5，  （a1,a2,...,a9） = （5，4，3，2，1，2，3，4，5） 输出 55555
      输入vol=5，  （a1,a2,...,a9） = （5，4，3，2，2，2，3，4，5） 输出 76
'''
from _functools import reduce


'''
输入（a1,a2,...,a9）得到按照墨水量排序的（a,v）的组合形成的list
'''
def voldata_sorted(n, input):
    dict = {}

    for i in range(n):
        dict[i+1] = input[i]
    dictSorted = sorted(dict.items(), key=lambda d: d[1])
    print("dictSorted:")
    print(dictSorted)
    return dictSorted


'''
得到最终答案的备选，即墨水量的总和为vol,并且局部最大
例如（a1,a2,...,a9） = （5，4，3，2，1，2，3，4，5）的情况下
[[5, 5, 5, 5, 5], [4, 4, 5], [6, 6, 5], [3, 6], [7, 6], [2, 5], [8, 5], [1], [9]]
'''
def getCandidateLoveNumbers(sum, n, input):
    dataList = voldataSorted(n, input)


def getLoveNumber(sum, data):
    l = list(map(buildMax, getCandidateLoveNumbers(sum, len(data), data))) # 得到每个备选的最大数字排序
    candidateLoveNumbers = []

    for item in l:
        num = reduce(lambda x, y: x*10 + y, item)
        candidateLoveNumbers.append(num)

    return max(candidateLoveNumbers)


if __name__ == '__main__':
    print(getLoveNumber(5, [5,4,3,2,2,2,3,4,5]))