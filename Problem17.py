def splitNums(n):
	hun = 0
	ten = 0
	while (len(str(n)) == 3):
		hun += 1
		n-=100
	if ( len(str(n)) == 2 ) :
		ten = str(n)[:1]
		n = str(n)[1:]
	one = str(n)[:1]
	return getWordLength(hun,ten,one)

	# print "Hundreds"+str(hun)
	# print "Tens"+str(ten)
	# print "Ones"+str(one)


def convertNumToWord(num):
#	print num
	i = 0
	with open("Problem17.txt") as f:
		for line in f:
			val = str(line).split(",")[1].translate(None,'\r\n')
			if ( i == int(num) ):
				return val
			if (i < 20):
				i += 1
			else:
				i += 10


def getWordLength(hun,ten,one):
	out = ""
 	#print str(hun)+" "+str(ten)+"  "+str(one)

	if ( int(hun) != 0 ):
		out += str(convertNumToWord(hun)+"hundredand")
	if ( int(ten) > 1 ):
		out += str(convertNumToWord(str(ten)+"0"))
	if (  and int(ten) == 1 ):
		out += str(convertNumToWord(str(ten)+str(one)))
### TO DO : ADD CASES 10-19 and all multiples of ten ( currently output as twozero )
	elif ( int(one) > 0 ):
		out += str(convertNumToWord(one))
	print out
	return len(out)


# print splitNums(130)

# print getWordLength(0,1,0)
# print getWordLength(0,1,2)


tot=len("onethousand")


for i in range(1, 1000):
	lng=splitNums(i)
	tot+=lng
	print str(i)+"   "+str(tot)+"   +"+str(lng)

print tot