n = 1389026630
while True:
    r = str(n ** 2)
    if len(r) == 19:
        if r[::2] == "1234567890":
            print(n)
            break
    n -= 10
