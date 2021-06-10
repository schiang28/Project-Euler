from itertools import permutations

pnum = list(permutations([0,1,2,3,4,5,6,7,8,9], 10))
pnum = [int(''.join(map(str, idx)))for idx in pnum]
pnum = [x for x in pnum if "0" in str(x)]
t = 0

for i in pnum:
    i = str(i)
    if int(i[1:4])%2==0 and int(i[2:5])%3==0 and int(i[3:6])%5==0 and int(i[4:7])%7==0 and int(i[5:8])%11==0 and int(i[6:9])%13==0 and int(i[7:10])%17==0:
        print(i)
        t+=int(i)

print(t)