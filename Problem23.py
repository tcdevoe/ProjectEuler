import Problem21

## TODO : Fix the calculation of abundant nums

def isAbundant(num):
	if ( num < Problem21.sumDivisors(num) ):
		return 1
	return 0

def isSumOfAbun(num, abun):
	i = 0
	while ( abun[i] < num/2 ):
		i += 1
	while ( abun[i] < num ):

		j = 0
		print "j ", j
		print "i ", i
		while ( abun[j] <= abun[i] ) :
			if ( abun[i] + abun[j] == num):
				return 1
			j += 1
			i += 1

abun = []
for i in range (1, 28124):
	if (isAbundant(i)):
		abun.append(i)

print isSumOfAbun(23, abun)

