def palindromic(n):
    for _ in range(50):
        ans = n + int(str(n)[::-1])
        if ans == int(str(ans)[::-1]):
            return True
        n = ans
    return False


count = 0
for n in range(10000):
    if not palindromic(n):
        count += 1

print(count)