import math

def isPalindrome(val):
	if ( len(val) == 1 or len(val) == 0):
		return 1
	elif ( val[:1] == val[len(val)-1:]):
		return isPalindrome(val[1:len(val)-1])
	else:
		return 0

lrg=0
for i in range(100,999):
	for j in range(100,999):
		prod = i * j
		string = str(prod)
		if (isPalindrome(string)):
			if (int(string) > lrg ):
				lrg = int(string)
print lrg
