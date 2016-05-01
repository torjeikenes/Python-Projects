def lyrics(amount):
	amount2 = amount - 1
	print "%i bottles of beer on the wall, %i bottles of beer. Take one down and pass it around, %i bottles of beer on the wall.." % (amount, amount, amount2)

def singular(amount):
	amount2 = amount - 1
	print "%i bottle of beer on the wall, %i bottle of beer. Take one down and pass it around, %i bottle of beer on the wall.." % (amount, amount, amount2)

bottles = 99

while(bottles > 1):
	lyrics(bottles)
	bottles -= 1
else:
	singular(bottles)
	bottles -= 1
