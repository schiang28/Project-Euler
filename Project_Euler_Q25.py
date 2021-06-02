fib = [1,1]
i = 0

# appends next fibonacci number until the length is 1000
while True:
    fib.append(fib[i]+fib[i+1])
    if len(str(fib[i] + fib[i+1])) == 1000:
        break
    i+=1

print(fib[-1])
print(len(fib))