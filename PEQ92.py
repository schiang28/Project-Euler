def chain(n):
    ans = 0
    for i in str(n):
        ans += int(i) ** 2
    return ans


t = 0
for n in range(1, 10000000):
    while True:
        num = chain(n)
        if num == 89:
            t += 1
            break
        if num == 1:
            break
        n = num

print(t)