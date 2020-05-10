a = [-1] * 10


def func(w):
    k = 0
    a[k] = w
    while w != 85:
        s = 0
        while w != 0:
            c = w % 10
            s += c * c
            w //= 10
        w = s
        k += 1
        a[k] = w
    return k + 1


summa = 0
for w in range(1000000):
    try:
        k = func(w)
        istrue = True
        for i in a:
            if 10 <= i < 100 or i == -1:
                istrue = True
            else:
                istrue = False
                break
        if k == 5:
            istue = True
        else:
            istrue = False

        if istrue:
           summa += w
    except:
        pass
    a = [-1] * 10

print(summa)