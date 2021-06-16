n, d = [3], [2]
for i in range(1, 999):
    n.append(n[i - 1] + d[i - 1] * 2)
    d.append(n[i - 1] + d[i - 1])

ans = 0
for i in range(len(n)):
    if len(str(n[i])) > len(str(d[i])):
        ans += 1

print(ans)