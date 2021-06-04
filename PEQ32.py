from math import sqrt
t = 0

def pandigital(n):
    pan = False
    if len(set(str(n))) == len(str(n)):
        if int(max(list(str(n)))) == 9 and int(min(list(str(n)))) == 1:
            pan = True
    return pan

def product(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            if len(str(i)) + len(str(n//i)) + len(str(n)) == 9:
                full = str(i) + str(n//i) + str(n)
                if pandigital(full):
                    return n
    return 0

for j in range(1000, 10000):
    t += product(j)

print(t)