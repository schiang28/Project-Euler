import math
import time
ans = 1
start_time = time.time()

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(3, 1000000, 2):
    n = []
    for d in str(i):
        n.append(d)
    for _ in range(len(n)):
        fir = n[0]
        del n[0]
        n.append(fir)
        p = True
        if not prime(int(''.join(n))):
            p = False
            break
    if p == True:
        ans+=1

print(ans)
print("--- %s seconds ---" % (time.time() - start_time))