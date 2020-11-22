amicable = []
final_sum = 0

for num in range(2, 10000):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    total1 = 0
    for x in range(1, total):
        if total % x == 0:
            total1 += x

    if total1 == num and total1 != total:
        present = False
        for x in amicable:
            if x == total1 or x == total:
                present = True
        if present == False:
            final_sum = final_sum + total1 + total
            amicable.append(total1)
            amicable.append(total)

print(final_sum)
