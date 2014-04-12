def convertCharToNum(char):
	with open("Problem22.txt") as f:
		for line in f:
			val = str(line).split(",")
			if (char == str(val[0])):
				return str(val[1]).translate(None,'\r\n')


def getNameValue(name):
	chars = list(str(name))
	value = 0
	for i in chars:
		value += int(convertCharToNum(i))
	return value 


with open("names.txt") as f:
	for row in f :
		names = str.split(str.translate(row, None, '"'), ',')
	names.sort()


ct = 1 
tot = 0
for name in names:
	tot += getNameValue(name)*ct
	ct += 1

print tot
