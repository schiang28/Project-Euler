ans = 0

for i in range(1, 30):
    x = 1
    while True:
        a = x ** i
        if len(str(a)) == i:
            ans += 1
        if len(str(a)) > i:
            break
        x += 1

print(ans)