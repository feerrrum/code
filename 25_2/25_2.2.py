for x in range(1234490, 1234520):
    p = 0
    f = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            if not p:
                p = i
            else:
                f = 0
                break
    if f and p:
        print(x, x // p)
