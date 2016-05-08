from random import randint

def getSides():
    while True:
        try:
            sides = int(raw_input("How many sides do you want on your dice?: "))
            break
        except ValueError:
            print "Please enter a number. Try again"
    return sides

def getThrows():
    while True:
        try:
            throws = int(raw_input("How many times do you want to throw the dice?: "))
            break
        except ValueError:
            print "Please enter a number. Try again"
    return throws

def dice():
    sides = getSides()
    throws = getThrows()
    results = []
    for i in range(1, throws):
        results.append(randint(1, sides))
    print results

dice()
