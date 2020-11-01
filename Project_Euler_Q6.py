total1 = 0
for i in range(1,101):
    total1 += i*i

total2 = 0
for i in range(1,101):
    total2 += i
total3 = total2 * total2
difference = total3 - total1
print(difference)
