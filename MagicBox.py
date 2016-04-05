#http://hihocoder.com/problemset/problem/1135


def check(x, y, z, colorNum):
    diffRY = abs(colorNum['R'] - colorNum['Y'])
    diffRB = abs(colorNum['R'] - colorNum['B'])
    diffBY = abs(colorNum['B'] - colorNum['Y'])

    if sorted([x, y, z]) == sorted([diffRY, diffRB, diffBY]):
        return True
    else:
        return False

(x, y, z) = (int(i) for i in input().split())
sequence = input()

colorNum = {'R': 0, 'Y': 0, 'B': 0}
maximum = []
tempMaximum = 0

for c in sequence:
    colorNum[c] += 1
    if check(x, y, z, colorNum):
        maximum.append(tempMaximum + 1)
        tempMaximum = 0
        for k in colorNum:
            colorNum[k] = 0
    else:
        tempMaximum += 1
maximum.append(tempMaximum)

print(max(maximum))