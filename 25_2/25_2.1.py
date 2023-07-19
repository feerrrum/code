def div(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return ans

def prime(x):
    if x == 2:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for x in range(1234490, 1234520):
    d = div(x)
    f = 1
    for i in d:
        if not prime(i):
            f = 0
    if f == 1 and len(d) > 0:
        print(x, max(d))
