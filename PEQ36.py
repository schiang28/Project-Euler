ans = 0
for n in range(1000000):
    bn = bin(n)[2:]
    if str(n) == str(n)[::-1] and str(bn) == str(bn)[::-1]:
        ans += n

print(ans)