ls = []
for i in range(1000, 10000):
	ls.append(((3 * i - 1) * i) / 2)

for i in ls:
	for j in ls:
		if i + j in ls and abs(i - j) in ls:
			print(abs(i - j), i, j)
			break