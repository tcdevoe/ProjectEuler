class Date:
	"A representation of a date"
	def isSunday(self):
		if (self.dow == 0):
			return 1
		else :
			return 0

	def isLeapYear(self):
		if (self.year % 4 == 0 and self.year != 1900):
			return 1
		else: 
			return 0

	def getNumDays(self):
		if (self.month == 9 or 
			self.month == 4 or 
			self.month == 6 or
			self.month == 11):
			
			return 30

		elif (self.month == 2 ):
			if (self.isLeapYear()):
				return 29
			else:
				return 28
		else:
			return 31



	def getNextDay(self):
		if (self.day+1 > self.getNumDays()):
			if (self.month == 12):
				self.__dict__['month'] = 1
				self.__dict__['day'] = 1
				self.__dict__['year'] = self.year + 1
			else:
				self.__dict__['month'] = self.month + 1
				self.__dict__['day'] = 1
		else: 
			self.__dict__['day'] = self.day + 1

		self.__dict__['dow'] = (self.dow + 1) % 7

	def __str__(self):
		return str(self.month)+"/"+str(self.day)+"/"+str(self.year)+"\nDay of week : "+str(self.dow)

	def __eq__(self, other):
		if (self.day == other.day and self.month == other.month and self.year == other.year):
			return 1
		else:
			return 0


date = Date()

#initializing date to 1/1/1900
date.dow = 1
# 0 is Sunday, 1 is Monday ... 6 is Saturday
date.day = 1
date.month = 1
date.year = 1900

endDate = Date()
endDate.dow = 0
# 0 is Sunday, 1 is Monday ... 6 is Saturday
endDate.day = 31
endDate.month = 12
endDate.year = 2000


date2 = Date()
endDate.dow = 0
# 0 is Sunday, 1 is Monday ... 6 is Saturday
date2.day = 1
date2.month = 1
date2.year = 1901


tot = 0

while (not (date == date2)):
	date.getNextDay()


while (not (date == endDate)):
	if (date.day == 1 and date.dow == 0):
		tot += 1
		print date
		print tot
	date.getNextDay()
print tot