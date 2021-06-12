from math import sqrt


def prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def permutation(a, b):
    if len(str(a)) != len(str(b)):
        return False
    for i in str(b):
        if i not in str(a):
            return False
    return True


for n in range(1001, 10000, 2):
    seq = []
    if prime(n):
        for _ in range(3):
            seq.append(n)
            n1 = n + 3330
            if permutation(n, n1) and prime(n1):
                n = n1
            else:
                break
    if len(seq) == 3:
        print("".join(list(map(str, seq))))
