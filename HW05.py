"""
Georgia Institute of Technology - CS1301
HW05 -  Lists, Tuples, and Modules
"""
#########################################
"""
Function Name: teamPicker()
Parameters: sportInterests (list), intramural (str)
Returns: team (list)
"""
def teamPicker(sportInterests, intramural):
    team = []
    for i in sportInterests:
        for j in i[1]:
            if j.lower == intramural.lower:
                team.append(i[0])
                

    if len(team) > 0:
        team.sort()
        return team

    else:
        return "Free agent :/"
#########################################
"""
Function Name: vacationPlanner()
Parameters: trips (list), costs (list)
Returns: vacationSpots (tuple)
"""

def vacationPlanner(trips,costs):
    full_list = []
    for i in trips:
        element = (i, costs[trips.index(i)])
        full_list.append(element)

    full_list.sort()
    vacationSpots = []

    if len(costs) != 0:
        j = min(costs)
        for x in range(0, len(costs)):
            if j == costs[x]:
                vacationSpots.append(trips[x])


    else:
        vacationSpots.append("")

    vacationSpots.sort()
    vacationSpots.append(full_list)

    return tuple(vacationSpots)

#########################################
"""
Function Name: fastFood()
Parameters: foods (list), costs (list)
Returns: friendsOwed (list)
"""
def fastFood(foods,costs):
    friendsOwned = []
    friends = ""
    for i in foods:
        cost = 0
        if i[0] not in friends:
            for x in foods:
                if x[0] == i[0]:
                    for j in costs:
                        if x[1] == j[0]:
                            cost += j[1]

            element = (i[0], cost)
            friendsOwned.append(element)
            friends += i[0]
    friendsOwned.sort()
    return friendsOwned
#########################################
"""
Function Name: reviewSession()
Parameters: rooms (list), dates (list)
Returns: roomsAvailable (list)
"""
import calendar
def reviewSession(rooms,dates):
    roomsAvailable = []
    already_rooms = ""
    for i in range(0,len(dates)):
        if (calendar.weekday(2022,dates[i][0],dates[i][1]) == 3 or calendar.weekday(2022,dates[i][0],dates[i][1]) == 4) and rooms[i] not in already_rooms:
            roomsAvailable.append(rooms[i])
            already_rooms += rooms[i]

    roomsAvailable.sort()
    return roomsAvailable
#########################################
"""
Function Name: esportsBracket()
Parameters: tourneyList (list)
Returns: tourneyWinner (str)
"""
def matchHistory(team1, team2):
    matchDict = {'Liquid': 4, 'The Guard': 6, 'Mang0':10000, 'Hbox': -1, 'Plup': 100, 'Leffen': 8,'Fnatic': 3, 'Armada': 7, 'Paper Rex': 1000, 'DRX': 500, 'Optic': 300, 'OG': 1000, 'Alliance': 1}
    if team1 not in matchDict.keys() or team2 not in matchDict.keys():
        return None
    else:
        if matchDict[team1] > matchDict[team2]:
            return team1
        else:
            return team2

def esportsBracket(tourneyList):
    new_list = []
    for i in tourneyList:
        new_list.append(matchHistory(i[0],i[1]))

    tourneyWinner = matchHistory(new_list[0],new_list[1])
    return tourneyWinner
