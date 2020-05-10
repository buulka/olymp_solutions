def func(w):
    s = 0
    d = 0
    a = 0
    p = 1
    while w > 0:
        c = w % 10
        k = c + a + d
        s = s + (k % 10) * p
        d = k // 10
        a = c
        p *= 10
        w //= 10
    s += (a + d) * p
    return s


for w in range(10000):
    if func(w) == 96415:
        print(w)
        break
