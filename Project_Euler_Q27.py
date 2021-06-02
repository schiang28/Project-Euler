from math import sqrt
maximum = 0

def prime(num): #tests if the number is prime
    p = True
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            p = False
            break
    return p
    
for a in range(-991, 1000, 2): #looping through all possible values of a and b
    for b in range(-991, 1000, 2):
        n=0
        while True:
            result = n**2 + a*n + b
            if result > 0:
                pr = prime(result)
                if pr == False:
                    break
                n += 1 #n is the number of consectuve primes
            else:
                break
        if n > maximum:
            maximum = n
            fa,fb=a,b

print(maximum,fa,fb)
print(fa*fb)