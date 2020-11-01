count = 1
t = False
while t == False:
    for i in range(1,21):
        if count % i != 0:
            count += 1
            t = False
            break
        t = True
    if t == True:
        break

print(count)
