ans = 0
for a in range(100):
    for b in range(100):
        t = sum(list(map(int, str(a ** b))))
        if t > ans:
            ans = t

print(ans)