


print "Write a side"
side1 = int(raw_input())
print "Write another side"
side2 = int(raw_input())
print "Write the last side"
side3 = int(raw_input())


if((side1 > side2) and (side1 > side3)):
	h = side1
	k1= side2
	k2= side3
elif((side2 > side1) and (side2 > side3)):
	h = side2
	k1 = side1
	k2 = side3
elif((side3 > side1) and (side3 > side2)):
	h = side3
	k1 = side1
	k2 = side2

 

if(h**2==k1**2+k2**2):
	print "The triangle is a Pytagorean tripple"
else:
	print "The triangle is not a Pytagorean tripple"

