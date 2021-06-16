from math import factorial


def combinatoric(n, r):
    ans = factorial(n) / (factorial(r) * factorial(n - r))
    return ans


count = 0
for r in range(1, 101):
    for n in range(r, 101):
        if combinatoric(n, r) > 1000000:
            count += 1

print(count)