
def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
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

def digitSum(num):
    digits = list(str(num))
    sum = 0 
    for i in digits:
        sum += int(i)
    return sum

def firstDigits(num):
    digits = list(str(num))
    sum = 0
    for i in range(0, 1):
        sum += int(digits[i])
    if(sum % 2 == 1):
        return True
    else:
        return False

def isEven(num):
    digits = list(str(num))
    if((int(digits[len(digits)-2]) % 2 == 0) and (int(digits[len(digits)-2]) > 0)):
        return True
    else:
        return False
    
def lastDigit(num):
    digits = list(str(num))
    if(int(digits[len(digits)-1]) == len(digits)):
        return True
    else:
        return False
            
for i in range(1, 1000):
    if(i>=10):
        if(isPrime(i) == True):
            if(is1or7(i) == True):
                if(digitSum(i) <= 10):
                    if(firstDigits(i) == True):
                        if(isEven(i) == True):
                            if(lastDigit(i) == True):
                                print str(i) + """ is the only number the follow
these criteria: 
The number has two or more digits.
The number is prime.
The number does NOT contain a 1 or 7 in it.
The sum of all of the digits is less than or equal to 10.
The first two digits add up to be odd.
The second to last digit is even.
The last digit is equal to how many digits are
in the number."""
