num = []
for a in range(2, 101):
    for b in range(2, 101):
        p = a**b
        num.append(p)

print(len(set(num)))