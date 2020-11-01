counter = 1
count = 3
ls = [2]
while counter < 10001:
    for i in range(2, count):
        if count % i == 0:
            count +=1
            break
    else:
        ls.append(count)
        count += 1
        counter += 1

print(max(ls))
