for x in range(int('a0ded', 16), 16**6):
    n = x
    x = hex(x)[2:]
    if x[0] == 'a' and x[2:5] == 'ded' and n % int('19', 16) == 0:
        print(n, n // int('19', 16))
