while True:
    try:
        (R, x1, y1, x2, y2, x3, y3, x0, y0) = (int(x) for x in input().split())
        count = 0
        if (x1 - x0) ** 2 + (y1 - y0) ** 2 <= R ** 2:
            count += 1
        if (x2 - x0) ** 2 + (y2 - y0) ** 2 <= R ** 2:
            count += 1
        if (x3 - x0) ** 2 + (y3 - y0) ** 2 <= R ** 2:
            count += 1

        print(str(count) + 'x')
    except EOFError:
        break