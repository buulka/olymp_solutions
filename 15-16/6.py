a = '1111'
b = ''
for n in range(2, 10):
    for i in a:
        b += i + str(int(i) + 1)
        a = b
    b = ''
print(a.count('5'), a.count('7'))

