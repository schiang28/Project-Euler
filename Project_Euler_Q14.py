ma = -1
num = 0
for chain in range(1, 1000000):
    ls = [chain]
    while chain > 1:
        if chain % 2 == 0:
            chain = chain/2
        else:
            chain = chain*3+1
        ls.append(chain)
    if len(ls) > ma:
        ma = len(ls)
        num = ls[0]

print(num)
