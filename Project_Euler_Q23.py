import math
abundant, sums = [],[]

# finding all abundant numbers up to 28123 and adding them to a list 
for n in range(12,28123):
    t = [1]
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            t.append(i)
            t.append(n//i)
    if sum(list(set(t)))>n:
        abundant.append(n)

#creating a list of all the possible sums of those abundant numbers that are less than 28123
for x in abundant:
    for y in abundant:
        if x+y <= 28123:
            sums.append(x+y)
sums = list(set(sums))

#creates a list from 1 to 28124 and removing all the numbers that are abundant leaving the non-abundant sums
x = list(range(1,28124))
for i in sums:
    x.remove(i)

print(sum(x))