num = str(2 ** 1000)

tot=0

for i in range(0, len(num)):
	tot+=int(num[i:i+1])

print tot