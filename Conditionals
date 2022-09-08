"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: availableDate()
Parameters: date(int), isWeekend(bool)
Returns: availability(str)
"""
def availableDate(date, isWeekend):
    if isWeekend == True or date % 2 == 0:
        return("Available on {}!".format(date))
    else:
        return("Not available :(")

#print(availableDate(12,False))    
    
        

#########################################

"""
Function Name: buyGame()
Parameters: gameTitle(str), budget(float), cost(float), positiveRating(float)
Returns: None(NoneType)
"""
def buyGame(gameTitle, budget, cost, positiveRating):
    if cost > budget:
        print("{} is over ${}!".format(gameTitle, budget))

    elif cost < budget and positiveRating >= 0.70:
        print("Sasuke will buy {}!".format(gameTitle))

    elif cost < budget and positiveRating < 0.70:
        print("Let's find another game.")
        

#########################################

"""
Function Name: foodTime()
Parameters: restaurant(str), time(int)
Returns: howLong(float or int)
"""
def foodTime(restaurant, time):
    distance = 0
    wait = 0
    if restaurant == "Cafe Leblanc":
        distance = 620
        wait = 5
    elif restaurant == "The Roost":
        distance = 700
        wait = 10
    elif restaurant == "Lumpy Pumpkin":
        distance = 850
        wait = 12
    elif restaurant == "The Milk Bar":
        distance = 1200
        wait = 3

    howLong = time - (distance*2)/80 - wait - 10

    if howLong < 0:
        return -1

    else:
        return howLong

#print(foodTime("Cafe Leblanc", 50))
#print(foodTime("Lumpy Pumpkin", 40))
#########################################

"""
Function Name: restaurantReservation()
Parameters: total(int), toSave(int), average(int)
Returns: canReserve(bool)
"""
def restaurantReservation(total, toSave, average):
    if total - toSave > average*2:
        canReserve = True

    else:
        canReserve = False

    return canReserve


#########################################

"""
Function Name: halloweenHeist()
Parameters: num1(int), num2(int), name(str)
Returns: message(str)
"""
def halloweenHeist(num1, num2, name):
    message = ""
    if num2 - num1 < 0:
        message = "{} has the package.".format(name)

    elif num2 - num1 > 0:
        message = "{} does not have the package.".format(name)

    elif num2 - num1 == 0:
        message = "{} has taken over.".format(name)

    return message

#print(halloweenHeist(20,16,"Jake"))

        
        
    
