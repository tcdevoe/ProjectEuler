import math


def isPrime(n):
	sqt = math.sqrt(n)
	j = 2
	prime=1
	while ( j <= sqt ):
		if ( n % j == 0 and n != j) :
			prime=0
			break
		j += 1
	return prime


# n = 600851475143 
# sqt = math.sqrt(n)
# j = 1

# while ( j < sqt ):
# 	if ( n % j == 0 and isPrime(j) ):
# 		print j
# 	j += 1


