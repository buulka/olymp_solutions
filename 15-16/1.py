kolvo = 0
for i in range(1, 8192):
    temp = i
    sum1 = ''
    final1 = 0
    while temp > 0:
        sum1 += str(temp % 2)
        temp //= 2
    for k in sum1:
        final1 += int(k)
    temp = i + 1
    sum2 = ''
    final2 = 0
    while temp > 0:
        sum2 += str(temp % 2)
        temp //= 2
    for k in sum2:
        final2 += int(k)
    if final1 / final2 == 3:
        kolvo += 1
    final1 = 0
    final2 = 0
    sum1 = ''
    sum2 = ''

print(kolvo)
