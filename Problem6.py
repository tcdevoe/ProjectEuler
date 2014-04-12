import math

sqr_tot = 0

rng=range(1,101)

for i in rng:
	val=math.pow(i,2)
	sqr_tot+=val
print sqr_tot

sum_tot=math.pow(sum(rng),2) 
print sum_tot-sqr_tot