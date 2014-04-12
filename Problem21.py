import math

def sumDivisors(n):
	divs = []
	divs.append(1)
	for i in range (2, int(math.ceil(math.sqrt(n)))+1):
		if (n % i == 0 ):
			if ( i*i == n):
				divs.append(i)
			else:
				divs.append(n/i)
				divs.append(i)
	
	tot = 0
	for i in range(0, len(divs)):
		tot += divs[i]

	return tot

def amicNums(n,m):
	if (sumDivisors(n) == m and sumDivisors(m) == n and m != n):
		return 1
	else:
		return 0


# added = []
# tot = 0
# for i in range(1, 10000):
# 	other = sumDivisors(i)
# 	if (amicNums(i, other)):
# 		if i not in added:
# 			print i, " AND  ", other
# 			added.append(i)
# 			added.append(other)
# 			tot += i
# 			tot += other

# print tot