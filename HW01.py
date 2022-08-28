"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""

#########################################

"""
Function Name: tasteOfTech()
Parameters: N/A
Returns: None
"""


def tasteOfTech():
    name = input("What is your first name? ")
    td_spend = float(input("How much did you spend at Tin Drum? "))
    wh_spend = float(input("How much did you spend at Waffle House? "))
    bww_spend = float(input("How much did you spend at Buffalo Wild Wings? "))
    total_spend = round(td_spend + wh_spend + bww_spend, 2)
    total_doge = round(total_spend * 14.57, 2)
    print("Congratulations {}! You spent ${} in total and earned ${} DOGE.".format(name,total_spend,total_doge))

tasteOfTech()

#########################################

"""
Function Name: shoppingMoney()
Parameters: N/A
Returns: None
"""


def shoppingMoney():
    monthly_income = int(input("How much is your monthly income? "))
    expenses = 700 + 80 * 4
    savings = round(0.6 * (monthly_income - expenses), 2)
    spare = round(monthly_income - expenses - savings, 2)
    print("You can save ${} and spend the remaining ${} on anything this month".format(savings, spare))


shoppingMoney()

#########################################

"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""


def houseParty():
    chicken_nuggets = int(input("How many chicken nuggets will each guest eat? "))
    onion_rings = int(input("How many onion rings will each guest eat? "))
    donuts = int(input("How many donuts will each guest eat? "))
    cookies = int(input("How many cookies will each guest eat? "))
    guests = int(input("How may guests are you expecting at the party? "))
    print("You need to buy {} chicken nuggets, {} onion rings, {} donuts and {} cookies for {} guests.".format(chicken_nuggets * guests, onion_rings * guests, donuts * guests, cookies * guests, guests))


houseParty()

#########################################

"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""


def spareTime():
    credits = int(input("How many credits are you taking? "))
    week_hours = 16 * 7
    study_hours = credits * 3 + credits
    spare_weekly = week_hours - study_hours

    spare_hours = spare_weekly // 7
    spare_mins = round(((spare_weekly % 7) * 60) / 7, 1)

    print("You have {} hours and {} mins per day to spare for other activities.".format(spare_hours, spare_mins))
    


spareTime()

#########################################

"""
Function Name: ratsNight()
Parameters: N/A
Returns: None
"""


def ratsNight():
    video_games = int(input("How many slots would you like to book for video games? "))
    trivia = int(input("How many slots would you like to book for trivia? "))
    arts_crafts = int(input("How many slots would you like to book for arts/crafts? "))
    total_time = video_games * 30 + trivia * 10 + arts_crafts * 45
    print("You will spend", total_time // 60, "hours and", total_time % 60, "minutes at the Rats Night.")
    


ratsNight()
