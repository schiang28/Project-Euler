from math import sqrt
from time import time

start = time()


def prime(n):
    if n == 1:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


side, primes = 3, 0
diagonal = [1]

while True:
    for i in range(4):
        n = diagonal[-1] + (side - 1)
        diagonal.append(n)
        if prime(n):
            primes += 1
    percent = primes / (len(diagonal))
    if percent < 0.1:
        break
    side += 2

print(side)
print("Runtime =", time() - start)