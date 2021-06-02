fib=[1,2]

while fib[-1] < 4000000:
    n = fib[-1] + fib[-2]
    fib.append(n)

t = 0
for i in range(len(fib)):
    if fib[i] % 2 ==0:
        t+=fib[i]

print(t)