"""def fallActivities(fileName,interestedList,month,minimumRatio):
    import csv
    activities = []
    ratings = []
    time = []
    months = []
    l = []
    l.clear()
    activities.clear()
    ratings.clear()
    time.clear()
    months.clear()

    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            l.append(row)

    for i in range(1, len(l)):
        activities.append(l[i][0])
        ratings.append(l[i][1])
        time.append(l[i][2])
        months.append(l[i][3])

    print(activities)
    print(ratings)
    print(time)
    print(months)

    l2 = []
    ratio = []
    for x in interestedList:
        if x in activities:
            i = activities.index(x)
            ratio.append(int(ratings[i]) / int(time[i]))

    l2.append(interestedList[ratio.index(max(ratio))])
    l2.append(max(ratio))

    if len(l2)!= 0:
        return(tuple(l2))

    else:
        return("No activities this month!")
"""
def fallActivities(fileName,interestedList,month,minimumRatio):
    import csv
    activities = []
    ratio = []
    f = open(fileName)
    reader1 = csv.reader(f)
    for row in reader1:
        if (row[0] in interestedList):
            ratio1 = int(row[1]) / int(row[2])
            if ratio1>minimumRatio and row[3] == month:
                activities.append(row[0])
                ratio.append(ratio1)

    if len(activities) != 0:

        a = max(ratio)
        b = activities[ratio.index(a)]
        tup1 = b,a
        return tup1
    else:
        return "No activities this month!"


# print(fallActivities('activity.csv', ['pumpkin patch', 'trick or treating', 'jump in leaves', 'drink chai latte', 'visit haunted house', 'make caramel apples'], 'October', 35.0))

def funFallFavs(fileName,letter):
    import csv
    f = open(fileName)
    reader1 = csv.reader(f)
    l = []
    d = {}
    for row in reader1:
        if (row[3] != "Month") and (letter.lower() in row[0]):
            l.append(row)

    for i in l:
        if i[3] not in d:
            d[i[3]] = 1
        else:
            d[i[3]] += 1

    if len(d) == 0:
        return "Letter not found."

    else:
        return d

#print(funFallFavs('activity.csv', 't'))
"""filename = "activity.csv"
letter = "b"
print(funFallFavs(filename,letter))"""

#print(fallActivities('activity.csv', ['pumpkin patch', 'trick or treating', 'jump in leaves', 'drink chai latte', 'visit haunted house', 'make caramel apples'], 'October', 35.0))
#print(fallActivities("activity.csv",['pumpkin patch', 'trick or treating', 'jump in leaves', 'drink chai latte', 'visit haunted house', 'make caramel apples'], 'October', 35.0))

import requests
def shareBorder(country1,country2):

    reader1 = requests.get(f"https://restcountries.com/v2/name/{country1}")
    reader2 = requests.get(f"https://restcountries.com/v2/name/{country2}")
    data1 = reader1.json()
    data2 = reader2.json()

    dict1 = data1[0]
    dict2 = data2[0]
    print(dict1)
    print(dict2)

    c2 = dict2["alpha3Code"]
    if c2 in dict1["borders"]:
        return True

    else:
        return False


#print(shareBorder("United States of America", "Canada"))


def currencyRatio(continent,currency):

    reader1 = requests.get(f"https://restcountries.com/v2/region/{continent}")
    data1 = reader1.json()
    count_currency = 0
    count_country = 0


    for i in data1:
        count_country += 1
        for x in i["currencies"]:
            if currency == x["name"]:
                count_currency += 1

    # print(count_currency)
    # print(count_country)
    ratio = round(count_currency/count_country,2)

    return(ratio)

#print(currencyRatio("Europe","Euro"))


def countriesInfo(countriesList):
    f = open("countries.csv","w")
    l2 = []
    for i in countriesList:
        try:
            l = []

            reader = requests.get(f"https://restcountries.com/v2/name/{i}")
            data1 = reader.json()
            dict1 = data1[0]
            l.append(i)
            l.append(dict1['capital'])
            l.append(str(dict1['population']))
            if len(dict1['languages'])==1:
                l.append(dict1['languages'][0]["name"])
            else:
                for i in range(len(dict1["languages"])):
                    if i == 0:
                        x = dict1['languages'][i]["name"] + "-"
                    else:
                        x += dict1['languages'][i]["name"]

                l.append(x)

            if len(dict1['currencies'])==1:
                l.append(dict1['currencies'][0]["name"])
            else:
                for i in range(len(dict1["currencies"])):
                    if i == 0:
                        y = dict1['currencies'][i]["name"] + "-"
                    else:
                        y += dict1['currencies'][i]["name"]

                l.append(y)

            l2.append(l)

        except:
            continue
    #print(l2)

    f.write("Country,Capital,Population,Languages,Currencies")

    if len(l2) != 0:
        f.write("\n")

    for i in range(0,len(l2)-1):
        f.write(l2[i][0])
        f.write(",")
        f.write(l2[i][1])
        f.write(",")
        f.write(l2[i][2])
        f.write(",")
        f.write(l2[i][3])
        f.write(",")
        f.write(l2[i][4])
        #print(l2[i])
        f.write("\n")

    if len(l2) != 0:
        f.write(l2[-1][0])
        f.write(",")
        f.write(l2[-1][1])
        f.write(",")
        f.write(l2[-1][2])
        f.write(",")
        f.write(l2[-1][3])
        f.write(",")
        f.write(l2[-1][4])




