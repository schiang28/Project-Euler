'''total = 2
counter = 3
while counter < 2000000:
    for i in range(2,counter):
        if counter % i == 0:
            counter += 1
            break
    else:
        total += counter
        counter += 1

print(total)'''

import math
total = 2
for num in range(3,2000000,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       total += num

print(total)
