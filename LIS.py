'''
最长上升子序列
'''

def lis(aList, pre):
    d = [0] * len(aList)
    longest = 1
    global longestPoint

    for p, n in enumerate(aList):
        pre[p] = n

    for i in range(0, len(aList)):
        d[i] = 1
        for j in range(0, i):
            if aList[i] >= aList[j] and (d[j] + 1) > d[i]:
                d[i] = d[j] + 1
                pre[i] = j
        if d[i] > longest:
            longest = d[i]
            longestPoint = i
    return longest

aList = [5, 3, 4, 8, 6, 7, 8, 5, 4, 9]
pre = [0] * len(aList)
longestPoint = 0

print("result:", lis(aList, pre))

print("longestPoint:", longestPoint)
print(aList)
print(pre)

point = longestPoint

resultList = list([])

resultList.append(aList[point])
while pre[point] != aList[point]:
    point = pre[point]
    resultList.append(aList[point])

while len(resultList) > 1:
    print(resultList.pop(), end="->")
print(resultList.pop())


'''
O(nlogn)的动态规划+二分方法
开一个栈，每次取栈顶元素top和读到的元素temp做比较，如果temp > top 则将temp入栈；
如果temp < top则二分查找栈中的比temp大的第1个数，并用temp替换它。 最长序列长度即为栈的大小top。
这也是很好理解的，对于x和y，如果x < y且Stack[y] < Stack[x],用Stack[x]替换Stack[y]，此时的最长序列长度没有改变但序列Q的”潜力”增大了。
举例：原序列为1，5，8，3，6，7
栈为1，5，8，此时读到3，用3替换5，得到1，3，8； 再读6，用6替换8，得到1，3，6；再读7，得到最终栈为1，3，6，7。最长递增子序列为长度4。

注意：当出现1，5，8，2这种情况时，栈内最后的数是1，2，8不是正确的序列，难道错了？
分析一下，我们可以看出，虽然有些时候这样得不到正确的序列，但最后算出来的个数是没错的，为什么呢？
想想，当a[i]>top时，总个数直接加1，这肯定没错；但当a[i]<top时呢？ 这时a[i]会替换栈里面的某一个元素，大小不变，就是说一个小于栈顶的元素加入时，总个数不变。
这两种情况的分析可以看出，如果只求个数的话，这个算法比较高效；但如果要求打印出序列时，就只能用动态规划了
'''
print("################")

def binarySearch(dp, target):
    low = 0
    high = len(dp)
    mid = 0
    while low < high:
        mid = (low + high) // 2
        if target > dp[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

def lis2(aList):
    dp = []
    dp.append(aList[0])
    for i in range(1, len(aList)):
        if aList[i] > dp[-1]:
            dp.append(aList[i])
        else:
            targetIndex = binarySearch(dp, aList[i])
            dp[targetIndex] = aList[i]
    return len(dp)

print(lis2(aList))