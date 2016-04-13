# 最长上升子序列
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

aList = [5, 3, 4, 8, 6, 7]
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