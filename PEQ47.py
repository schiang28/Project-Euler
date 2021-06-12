from math import sqrt


def tree(n):
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = n / 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = n / i
    if n > 2:
        pf.append(int(n))
    return pf


con = 0
for n in range(100000, 1000000):
    pf = tree(n)
    l = len(set(pf))
    if l == 4:
        con += 1
        if con == 4:
            print(n - 3)
            break
    else:
        con = 0
