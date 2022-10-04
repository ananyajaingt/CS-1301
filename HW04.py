"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: decodeString()
Parameters: encodedStr(str)
Returns: decodedList(list)
"""
def decodeString(encodedStr):

    reversedStr = encodedStr[::-1]
    newStr = ""

    for i in reversedStr:
        if i != "@":
            newStr += i

    newStr = newStr.lower()

    newList = newStr.split("#")
    return(newList)
#########################################
"""
Function Name: goodBrunch()
Parameters: ashList(list), nickList (list)
Returns: brunchDecision(list)
"""
def goodBrunch(ashList,nickList):
    brunchDecision = []

    for i in ashList:
        if i in nickList:
            brunchDecision.append(i)
            brunchDecision.sort()
    
    if len(brunchDecision) > 1:
        return brunchDecision
        
    elif len(brunchDecision) == 1:
        return brunchDecision[0]

    else:
        return ("Brunch at home it is!")


#print(goodBrunch(["Le Bon Nosh", "Petit Chou"], ["Le Bon Nosh", "Bread and Butterfly"]))

#########################################
"""
Function Name: room_dist()
Parameters: dormMap (list), name1 (str), name2 (str)
Returns: distance (int)
"""
def room_dist(dormMap, name1, name2):
    first_index = 0
    second_index = 0

    for i in dormMap:
        for j in i:
            if j == name1:
                first_index = dormMap.index(i)
                print(first_index)

            elif j == name2:
                second_index = dormMap.index(i)
                print(second_index)

    if first_index > second_index:
        distance = first_index - second_index

    elif second_index > first_index:
        distance = second_index - first_index

    elif second_index == first_index:
        distance = 0

    return(distance)

#########################################
"""
Function Name: freshProduce()
Parameters: veggies (list), prices (list)
Returns: veggieList (list)
"""
def freshProduce(veggies, prices):
    veggieList = []
    price_veggies = 0

    for i in prices:
        if i < 4.0:
            price_veggies += i
            i_index = prices.index(i)
            veggieList.append(veggies[i_index])

    veggieList.append(price_veggies)

    if len(veggieList) > 1:
        return veggieList

    else:
        return []

#########################################
"""
Function Name: find_roommate()
Parameters: my_interests(list), candidates (list), candidate_interests(list)
Returns: match (list)
"""
def find_roommate(my_interests,candidates,candidates_interests):

    match = []

    for x in candidates_interests:
        count = 0
        for y in x:
            if y in my_interests:
                count += 1

        if count >= 2:
            match.append(candidates[candidates_interests.index(x)])

    return(match)
    
