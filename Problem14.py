#Collatz Chain Sequence
def getCollatzLength(n, i = 1) :
	if ( n == 1 ):
		return i
	elif ( n % 2 == 0):
		return getCollatzLength(n/2, i+1)
	else :
		return getCollatzLength(3*n+1, i+1)
print getCollatzLength(13)

lrg=1
sol=1
for i in range(1, 1000000):
	leng = getCollatzLength(i)
	if ( leng > lrg ):
		lrg = leng
		sol=i

print lrg
print sol