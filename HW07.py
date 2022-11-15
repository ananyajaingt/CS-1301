import functools


def lazyMeal(maxPrepTime):
    f = open("cookBook.txt","r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    l2.remove("Recipes")
    meals = l2[::3]

    price = []
    for x in l2:
        if x.isdigit():
            price.append(int(x))

    recipe = []

    for j in price:
        if j <= maxPrepTime:
            y = price.index(j)
            recipe.append(meals[y])

    if len(recipe) != 0:
        recipe.sort()
        return recipe

    else:
        return "Waffle House it is!"


def groupCountries(countries):
    f = open("cookBook.txt", "r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    l2.remove("Recipes")
    country = l2[2::3]
    meals = l2[::3]

    recipeDict = {}

    for i in countries:
        l = []
        for j in range(0,len(country)):
            if i[1] == country[j]:

                l.append(meals[j])
        l.sort()
        recipeDict[i[0]] = l

    for x in recipeDict:
        if recipeDict[x] == []:
            return "Throw the book or get new friends!"
    else:
        return recipeDict

"""
def favRecipes(recipeList):
    f = open("cookBook.txt", "r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    l2.remove("Recipes")
    country = l2[2::3]
    price = l2[1::3]
    meals = l2[::3]


    f2 = open("favRecipe.txt","w")

    if recipeList == []:
        f2.write("No information found")

    else:
        f2.write("Recipes")

        for i in recipeList:
            for j in range(0,len(meals)):
                if meals[j] == i:
                    f2.write('\n')
                    f2.write('\n')
                    f2.write(i)
                    f2.write('\n')
                    f2.write(price[j])
                    f2.write('\n')
                    f2.write(country[j])
    f2.close()"""


def favRecipes(recipeList):
    f = open("cookBook.txt", "r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    l2.remove("Recipes")

    country = l2[2::3]
    price = l2[1::3]
    meals = l2[::3]

    #print(recipeList)
    #print(meals)

    f2 = open("favRecipes.txt","w")
    l = []

    for i in recipeList:
        for j in range(0,len(meals)):
            if meals[j] == i:
                l.append(meals[j])
                l.append(price[j])
                l.append(country[j])

    #print(l)

    x = "No information found."

    if len(l) != 0:
        f2.write("Recipes")
        i = 0
        while i <len(l):
            f2.write("\n")
            f2.write("\n")
            f2.write(l[i])
            f2.write("\n")
            f2.write(l[i+1])
            f2.write("\n")
            f2.write((l[i+2]))
            i += 3

    elif len(l) == 0:
        f2.write(x)

    f2.close()



#favRecipes(["Sushi","Mofongo"])



def orderCandy(prices,maxCost):
    f = open("friends.txt", "r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    #print(l2)

    people = l2[::4]
    rating = l2[1::4]
    d = {}
    f.close()
    i = 2
    a = 0
    while i < len(l2):
        l1 = []
        l1.append(l2[i])
        l1.append(l2[i+1])
        i += 4
        d[people[a]] = l1
        a += 1



    #print(d)
    #print(prices)
    l3 = []
    for j in prices:
        if prices[j] <= maxCost:
            l3.append(j)

    #print(l3)

    f3 = open("candyOrder.txt","w")

    l4 = []
    for i in l3:
        count = 0
        for x in d:
            for j in d[x]:
                if j== i:
                    count += 1


        if count >= 3:
            x = (i,count)
            l4.append(x)

    #print(l4)
    if len(l4) != 0:
        for y in range(0,len(l4)-1):

            f3.write(l4[y][0])
            f3.write(": ")
            f3.write(str(l4[y][1]))
            f3.write("\n")

        f3.write(l4[-1][0])
        f3.write(": ")
        f3.write(str(l4[-1][1]))

    elif len(l4) == 0:
        f3.write("Ask again.")

    f3.close()
"""
prices = {'KitKats': 2.0, 'M&Ms': 3.0, 'Hersheys': 3.5, 'Reeses': 1.5, 'Starburst': 2.0, 'Twix': 3.2, 'Jolly Ranchers': 2.6}
orderCandy(prices,3.0)"""

def moviePicker(potentialMovie):
    global potential_rating
    f = open("friends.txt", "r")
    l1 = f.read()
    l2 = l1.split("\n")
    for i in l2:
        if i == '':
            l2.remove('')
    rating = l2[1::4]
    rating_int = []

    for x in rating:
        rating_int.append(int(x))

    lowestRating = min(rating_int)
    #print(lowestRating)
    f.close()

    f2 = open("movies.txt", "r")
    l3 = f2.read()
    l4 = l3.split("\n")
    for i in l4:
        if i == '':
            l4.remove('')

    f2.close()
    movies = l4[0::2]
    movie_ratings = l4[1::2]


    for j in movies:
        if j == potentialMovie:
            potential_rating = movie_ratings[movies.index(j)]
            #print(potential_rating)
            if int(potential_rating) <= lowestRating:
                return True
            else:
                return False

    else:
        return False

def write_stuff(name,sentence):
    l = sentence.split(" ")
    f = open(name,"w")
    for i in range(0,len(l)-1):
        f.write(l[i])
        f.write("\n")

    f.write(l[-1])

write_stuff("day24miniquiz.txt","My favorite class is CS1301!")
