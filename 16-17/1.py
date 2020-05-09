def convfromdec():
    sum = ""
    tempsum = ""
    for i in range(1, 1024):
        temp = i
        while temp > 0:
            tempsum += str(temp % 4)
            temp //= 4
        sum += tempsum[::-1]
        tempsum = ""
    return convtodec(sum)


def convtodec(sum):
    answ = 0
    sum = sum[::-1]
    for i in range(len(sum)):
        answ += int(sum[i]) * (4 ** i)
    return convto16(answ)


def convto16(answ):
    abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    final = ""
    while answ > 0:
        final += abc[answ % 16]
        answ //= 16
    final = final[::-1]
    return final


number = convfromdec()
print(number)
if number[59] in number:
    print(number[59], end=" ")
if number[999] in number:
    print(number[999])
