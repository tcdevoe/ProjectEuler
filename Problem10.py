import Problem3

total=0

for i in range(2,2000000):
	if (Problem3.isPrime(i)):
		total+=i
print total