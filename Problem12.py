import math
import sys

sys.setrecursionlimit(10000000)

def getNumFactors(n):
	fact = []
	for i in range(1, int(math.ceil(math.sqrt(n)))):
		if ( n % i == 0) :
			fact.append(i)
			fact.append(n/i)
	return len(fact)

def getTriangleNumber(n): #gets the nth triangle number
	if ( n == 1 ):
		return n
	else:
		return n+getTriangleNumber(n-1)



i=1

lrg_fac = 1

for i in range(1, 100000000):
	num = getTriangleNumber(i) 
	fac = getNumFactors(num)
	if ( fac > lrg_fac ) :
		lrg_fac = fac
		print "NEW LARGEST : "+str(fac)
	if ( fac > 500 ) :
		print "SOLUTION :"+str(i)
		break
	print i

print "SOLUTION"+str(i)



