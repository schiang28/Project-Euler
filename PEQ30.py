total = 0
for n in range(4150,1000000):
    t = 0
    for i in str(n):
        t+= int(i)**5
    if t == n:
        print(t)
        total+=t

print(total)