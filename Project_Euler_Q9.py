import math
a = []
b = []
c = []

for a1 in range(1,1000):
    for b1 in range(1,1000):
        numc = a1*a1 + b1*b1
        c1 = math.sqrt(numc)
        if c1.is_integer() == True and a1 < b1:
            a.append(a1)
            b.append(b1)
            c.append(c1)

for i in range(0, len(a)):
    if  a[i] + b[i] + c[i] == 1000:
        print(a[i], b[i], c[i])
        print(int(a[i] * b[i] * c[i]))
