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
    done = []
    for i in range(0, throws):
        results.append(randint(1, sides))
    print results
    print "after " + str(throws) + " throws. The following numbers were rolled: "
    for i in results:
        print i,
    print "\n"
    for i in results:
        if i not in done: 
            occurance = results.count(i)
            print str(i) + " was rolled " + str(occurance) + " times. " + \
            str(percentage(occurance, results)) + "% of all throws"
            done.append(i)

    dice()

def percentage(occurance, resultList):
    return 100 * float(occurance)/float(len(resultList))

dice()
