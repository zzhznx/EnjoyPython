'''
stopWord = ''
str = ''
for line in iter(input, stopWord):
    print(line)
'''


def gy(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

while True:
     try:
        inability = [int(i) for i in input().split()]
        guaiwu = [int(i) for i in input().split()]
        if len(guaiwu) == 1:
            for i in range(inability[0]-1):
                guaiwu.append(input())
        for i in range(inability[0]):
            if inability[1] >= guaiwu[i]:
                inability[1] += guaiwu[i]
            else:
                inability[1] += gy(inability[1], guaiwu[i])

        print(inability[1])
     except EOFError:
        break