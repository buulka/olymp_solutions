def func():
    m = 0
    i = 100000
    a = [0] * 100

    for i in range(100000, 1000000):
        t = i
        k = 0

        while t != 0:
            a[k] = t % 10
            t //= 10
            k += 1

        if a[5] == 5 and a[3] == 3 and a[1] == 2:
            if i % 11 == 0 and i > m:
                m = i

    print(m)

func()


