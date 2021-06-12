from math import sqrt

square = []
for i in range(1, 100):
	square.append(i**2*2)

def prime(n):
	if n==1:
		return False
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def conjecture(n):
	for i in square:
		if i < n:
			p = n-i
			if prime(p):
				return True
		else:
			return False

n=33
while True:
	if not prime(n) and not conjecture(n):
		print(n)
		break
	n+=2