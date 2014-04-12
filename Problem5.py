def isDiv20(n):
	b=1
	for i in range(2,20):
		if ( n % i != 0 ):
			b = 0 
			break
	return b

print isDiv20(2432902008176640000)

i=20
while (1):
	if(isDiv20(i)):
		print i
		break
	i += 20