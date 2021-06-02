m=0
for i in range(100,1000):
    for j in range(100,1000):
        p = str(i*j)
        if p == p[::-1]:
            if int(p) > m:
                m=int(p)

print(m)