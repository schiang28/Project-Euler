from math import sqrt

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    num = []
    for digit in str(n):
        num.append(digit)
    for _ in range(len(num)):
        if not prime(int(''.join(num))):
            return False
        del num[0]
    return True

def truncate_right(n):
    num = []
    for digit in str(n):
        num.append(digit)
    for _ in range(len(num)):
        if not prime(int(''.join(num))):
            return False
        del num[-1]
    return True

ans = 0
for n in range(21, 1000000, 2):
    if truncate_right(n) and truncate_left(n):
        ans += n

print(ans)