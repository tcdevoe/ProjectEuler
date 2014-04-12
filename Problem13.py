line_no=1
num=[]

with open("Problem13_Source") as f:
	for line in f:
		num.append(int(line))
	line_no+=1

sum=0

for i in range(0, len(num)):
	sum+=num[i]
	print sum

print sum