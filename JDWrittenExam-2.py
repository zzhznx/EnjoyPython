
def solution(n, target, player):
    count = 0
    while True:
        if target > max(player):
            return count
        else:
            maxPlayer = max(player)
            for point, c in enumerate(player):
                if c == maxPlayer:
                    target += 1
                    player[point] -= 1
                    count += 1
                    break

while True:
    try:
        n = int(raw_input())
        temp = (int(x) for x in raw_input().split())
        player = []
        for i in temp:
            player.append(i)
        print solution(n, player[0], player[1:])

    except EOFError:
        break
