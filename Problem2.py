j, a , b, n = 0 , 0 , 1, 50000000
tot = 0
while (j < n):
	print "TOTAL",tot
	if (a > 4000000):
		break
	elif (b > 4000000):
		break
	elif (j % 2 == 0):
		a += b
		print "EVEN VALUE", a
		if (a % 2 == 0):
			tot += a
	else:
		b += a
		print "EVEN VALUE ",b
		if (b % 2 == 0):
			tot += b
	j += 1
print "Total",tot

