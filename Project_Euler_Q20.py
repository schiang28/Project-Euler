num = 100
total = 1
count = 1
while count <= num:
    total *= count
    count += 1

factor = str(total)
counter = 0
for i in factor:
    counter += int(i)

print(counter)
