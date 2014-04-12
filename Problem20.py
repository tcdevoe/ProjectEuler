def fac(n):
	if ( n==1 ):
		return 1
	return fac(n-1)*n


def sumDigits(n):
	nums = list(str(n))
	tot = 0
	for i in range (0, len(nums)):
		tot += int(nums[i])
	return tot


print sumDigits(fac(100))