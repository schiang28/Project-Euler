def pandigital(n):
    pan = False
    if len(set(str(n))) == len(str(n)):
        if int(max(list(str(n)))) == 9 and int(min(list(str(n)))) == 1:
            pan = True
    return pan

m = 0
for num in range(9, 10000):
    s = ''
    c = 1
    while True:
        s+=str(num*c)
        c+=1
        if len(s) >= 9:
            break
    if pandigital(int(s)):
        if int(s) > m:
            m = int(s)

print(m)