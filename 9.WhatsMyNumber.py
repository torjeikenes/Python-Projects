
def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            print "not prime"
            return False
            break
    else:
        return True
def is1or7(num):
    for i in str(num):
        if((i == "1") or (i == "7")):
            return False
    else:
        return True

for i in range(1, 1000):
    if(i>=10):
        if(isPrime(i) == True):
            if(is1or7(i) == True):
                print i
            else:
                print " 1 or 7"
        #else:
            #print "not prime"
    else:
        print "under 10"

