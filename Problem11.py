value = [[0 for x in range(21)] for x in range(21)]

line_no=1
with open("Problem11.txt") as f:
	for line in f:
		for i in range(1,20):
			value[line_no] = line.split()
		line_no+=1 

lrg=0

for i in range(0,17):
	for j in range(0,17):
		#Vertical Product
		vert=int(value[i][j])*int(value[i+1][j])*int(value[i+2][j])*int(value[i+3][j])
		#print "Vertical Product "+str(vert)
		if (vert > lrg):
			lrg=vert
		#Horizontal Product
		hor=int(value[i][j])*int(value[i][j+1])*int(value[i][j+2])*int(value[i][j+3])
		#print "Horizontal Product "+str(hor)
		if (hor > lrg):
			lrg=hor
		#diagonal product
		diag=int(value[i][j])*int(value[i+1][j+1])*int(value[i+2][j+2])*int(value[i+3][j+3])
		#print "diagonal product"+str(diag)
		if (diag > lrg):
			lrg=diag
for i in range(17,20):
	for j in range(17,20):
		vert=int(value[i][j])*int(value[i-1][j])*int(value[i-2][j])*int(value[i-3][j])
		print "Vertical Product "+str(vert)
		if (vert > lrg):
			lrg=vert
		#Horizontal Product
		hor=int(value[i][j])*int(value[i][j-1])*int(value[i][j-2])*int(value[i][j-3])
		print "Horizontal Product "+str(hor)
		if (hor > lrg):
			lrg=hor
		#diagonal product
		diag=int(value[i][j])*int(value[i-1][j-1])*int(value[i-2][j-2])*int(value[i-3][j-3])
		print "diagonal product"+str(diag)
		if (diag > lrg):
			lrg=diag
print lrg