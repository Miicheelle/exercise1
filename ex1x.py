import exx1x
#this is importing the script being used
g = exx1x.Cont()
#this is giving access to the class from the script
h = g.generateArray(8,12,10)
#the above is an example of the use of method generateArray
print (h)

j = g.uniqueElement(h)
#the for loop below is to check the length of the array in the range
for x in range(len(j)):
	l = g.oneElement(h,j[x])

	print(l)

y = g.modes(h)
print(y)

u = g.medians(h)
print(u)