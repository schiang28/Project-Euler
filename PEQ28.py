c,l,num=0,1001*1001,[]
num.append(l)

for _ in range(1001//2):
    for _ in range(4):
        l = l - (1001-1-c)
        num.append(l)
    c+=2

print(sum(num))