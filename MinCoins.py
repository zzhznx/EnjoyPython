
# 效率极差
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins

print(recMC([1, 5, 10, 21, 25], 27))


# 保存中间结果
# 如果查看一下knownResults列表，会发现有太多的洞（0值），
# 事实上不能称之为动态规划，只是利用了记忆或缓冲的做法优化了我们程序的性能
def recDc(coinValueList, change, knowResult):
    minCoins = change
    if change in coinValueList:
        knowResult[change] = 1
        return 1
    elif knowResult[change] > 0:
        return knowResult[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDc(coinValueList, change - i, knowResult)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResult[change] = minCoins
    return minCoins

print(recDc([1, 5, 10, 21, 25], 63, [0]*64))

# 函数计算完成后，minCoin将包括小于找钱的所有找零值所需要的最小硬币数量
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

print(dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64))


# 打印结果
def dpMakeChange_2(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin

change = 11
coinUsed = [0] * (change + 1)
minCoins = [0] * (change + 1)
print(dpMakeChange_2([1, 5, 10, 21, 25], change, minCoins, coinUsed))
printCoins(coinUsed, change)