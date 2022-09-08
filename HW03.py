"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: product()
Parameters: nums(str)
Returns: product(int)
"""
def product(nums):
    product = 1
    for i in nums:
        x = int(i)
        product *= x

    return product

#########################################
"""
Function Name: recipeCount()
Parameters: recipe(str)
Returns: totalTeaspoons(int)
"""
def recipeCount(recipe):
    totalTeaspoons = 0
    for i in recipe:
        if i in "123456789":
            totalTeaspoons += int(i)
    return totalTeaspoons
#########################################
"""
Function Name: instagraminator()
Parameters: usernames(str)
Returns: decodedUsernames(str)
"""
def instagraminator(usernames):
    decodedUsernames = ""
    for i in usernames:
        if i not in "@_$":
            decodedUsernames += i

    return decodedUsernames
#########################################
"""
Function Name: studentLoans()
Parameters: loanAmount(int)
Returns: forgivenessCount(int)
"""
def studentLoans(loanAmount):
    forgivenessCount = 0
    while loanAmount > 0:
        loanAmount -= 10000
        forgivenessCount += 1

    return forgivenessCount
#########################################
"""
Function Name: playoffs()
Parameters: team1name (str), team2name (str), scoreCount (str) 
Returns: winningTeam (str) 
"""
def playoffs(team1name, team2name, scoreCount):
    score1 = 0
    score2 = 0
    winningTeam = ""
    for i in scoreCount:
        if i == "1":
            score1 += 1
        if i == "2":
            score2 += 1

    if score1 > score2:
        winningTeam = team1name + " has won the game!"

    elif score1 < score2:
        winningTeam = team2name + " has won the game!"
        
    elif score1 == score2:
        winningTeam = "It was a tie :("
        

    return winningTeam 
