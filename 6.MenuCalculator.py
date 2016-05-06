
todaysMenu = {"1" : 3.50, 
        "2" : 2.50,
        "3" : 4.00,
        "4" : 3.50,
        "5" : 1.75,
        "6" : 1.50,
        "7" : 2.25,
        "8" : 3.75,
        "9" : 1.25}

todaysMenu = {"1" : 3.50, 
        "2" : 2.50,
        "3" : 4.00,
        "4" : 3.50,
        "5" : 1.75,
        "6" : 1.50,
        "7" : 2.25,
        "8" : 3.75,
        "9" : 1.25}

def getOrder():
    order = raw_input("What would you like to order?: ")
    order = list(order)
    return order

def sortOrder():
    order = getOrder()
    cost = 0
    for i in order:
        cost = cost + todaysMenu[i]
    print cost
    sortOrder()

sortOrder()
