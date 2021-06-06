def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

ans = 0
for x in range(145, 50000):
    su = 0
    for digit in str(x):
        digit = int(digit)
        f = factorial(digit)
        su += f

    if su == x:
        ans += x

print(ans)