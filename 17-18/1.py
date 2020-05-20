import math

a = '0.'
for i in range(100):
    a += '41'
print(a)

b = '0.'
for i in range(100):
    b += '25'
print(b)

# c = float(a) * float(b)
# print(c)

# suma = ''
# for i in range(10):
#     a *= 8
#     suma += str(int(a - a % 1))
#     a = a % 1
# suma = a[::-1]
# print(suma)
a = a[0:1] + a[2:]
deca = 0.0
for i in range(len(a)):
    deca += float(a[i]) * (8 ** -i)
print(deca)


b = b[2:]
decb = 0.0
for i in range(1, len(b)+1):
    decb += float(b[i-1]) * (8 ** -i)
print(decb)