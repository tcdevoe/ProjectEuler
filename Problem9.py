import sys

for a in range(1,1000):
	for b in range(1,1000):
		for c in range(1,1000):
			add=a+b+c
			if (add == 1000 and a*a+b*b==c*c):
				print "*************** SOLUTION : "+str(a)+","+str(b)+","+str(c)