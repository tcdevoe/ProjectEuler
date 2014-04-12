import math

def isPrime(n):
	sqrt=math.sqrt(n)
	for i in range(2,int(sqrt)+1):
		if (n % i == 0):
			return 0
	return 1


num_prime=0
i = 2

while (1):
	if (isPrime(i)):
		print i
		num_prime+=1
	if (num_prime==10001):
		print i
		break
	i+=1
	
