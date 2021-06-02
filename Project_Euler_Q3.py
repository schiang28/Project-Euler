from math import sqrt
factors = []
for i in range(1, 600851475143):
    if 600851475143 % i ==0:
        factors.append(i)
'''
print(factors)
for i in factors:
    p=True
    for j in range(2, int(sqrt(i))+1):
        if i%j==0:
            p=False
    if not p:
        print(i)'''