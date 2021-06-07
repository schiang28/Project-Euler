from math import sqrt
m = 0
pf = 0

for p in range(840, 845):
    s = 0
    for a in range(1,p):
        for b in range(1,p):
            c= sqrt(a**2 + b**2)
            if a+b+c==p and a>=b:
                s+=1

    if s>m:
        m = s
        pf = p
        print(pf, m)