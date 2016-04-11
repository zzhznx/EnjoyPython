while True:
    try:
        (n, sumTime) = (int(x) for x in raw_input().split())
        minTimeList = []
        maxTimeList = []
        for i in range(n):
            (minTime, maxTime) = (int(x) for x in raw_input().split())
            minTimeList.append(minTime)
            maxTimeList.append(maxTime)
        if sum(maxTimeList) < sumTime:
            print "No"
            continue

        if sum(minTimeList) > sumTime:
            print "No"
            continue

        flag = False
        for i in range(n):
            if not flag:
                timeList = []
                j = i
                for MaxPoint in range(j):
                    timeList.append(maxTimeList[MaxPoint])
                #print "j", j, "timeList", timeList
                jTimeUse = minTimeList[j]
                tempTimeList = []
                while jTimeUse <= maxTimeList[j]:
                    #print "out", sum(timeList) + jTimeUse + sum(minTimeList[j+1:])
                    if (sum(timeList) + jTimeUse + sum(minTimeList[j+1:])) >= sumTime:
                        #print "in", sum(timeList) + jTimeUse + sum(minTimeList[j+1:])
                        timeList.append(jTimeUse)
                        for m in range(j+1, n):
                            timeList.append(minTimeList[m])
                        print "Yes"
                        for t in range(len(timeList) - 1):
                            print timeList[t],
                        print timeList[-1]
                        flag = True
                        break
                    else:
                        jTimeUse += 1
        if not flag:
            print "No"
    except EOFError:
        break
