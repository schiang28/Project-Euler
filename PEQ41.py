from math import sqrt

def pandigital(n):
    for i in range(1, len(str(n))+1):
       if str(i) not in str(n):
           return False
    return True

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = 9999999
while True:
    if pandigital(n) and prime(n):
        break
    n-=2

print(n)