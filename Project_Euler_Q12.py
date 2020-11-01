import math
total = 0
i = 1
while True:
    total += i
    i += 1
    count = 0
    for c in range(1, int(math.sqrt(total)+1)):       # loops from 1 to square root of total + 1
        if total % c == 0:
            count += 2
    if count > 500:
        break

print(total, ":", count)
