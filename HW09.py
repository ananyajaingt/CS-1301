def hoursWorked(clockedHours):
    if clockedHours == []:
        return 0

    else:
        return (clockedHours[0]) + hoursWorked(clockedHours[1:])


# print(hoursWorked([2,4,1,4,6]))

def secretLocation(location):
    if location == "":
        return ""

    else:
        if location[0].islower() or location[0] == " ":
            return location[0] + secretLocation(location[1:])

        else:
            return secretLocation(location[1:])


# print(secretLocation("!cSKu1lL3c$"))

# def springRegistration(originalCRNs):
#     newl = []
#     if originalCRNs == []:
#         return []
#
#     else:
#         if originalCRNs[-1] not in originalCRNs[0:-1]:
#             return list(originalCRNs[-1]) + originalCRNs[0:-1]
#
#         else:
#             return list(originalCRNs[0:-1])
#
# #print(springRegistration([22275,25594,21942,22275]))

# def springRegistration(originalCRNs):
#
#
#     if originalCRNs[-1] in originalCRNs[0:-1]:
#         originalCRNs.remove(originalCRNs[-1])
#         return springRegistration(originalCRNs[0:-1])
#
#     else:
#         return originalCRNs
#
#
# print(springRegistration([22275, 25594, 21942, 22275]))

def springRegistration(originalCRNs):
    new_list = []
    if originalCRNs == []:
        new_list = []
    else:
        if originalCRNs[0] not in originalCRNs[1:]:
            new_list = [originalCRNs[0]] + springRegistration(originalCRNs[1:])
        else:
            new_list = springRegistration(originalCRNs[1:])

    return new_list


def poncePlanner(restaurantChoice):
    d = {}
    if restaurantChoice == []:
        d = {}

    else:
        d[restaurantChoice[0][0]] = restaurantChoice[0][1]

        d.update(poncePlanner(restaurantChoice[1:]))

    return d

"""
restaurantChoice = [("Paige", "Dancing Goats"), ("Fareeda", "Botiwala"),("Ramya", "Minero"), ("Jane", "Pancake Social")]
print(poncePlanner(restaurantChoice))"""
"""
def poncePlanner(restaurantChoice):
    for i in restaurantChoice:
        if type(item) == StringType or type(item) == UnicodeType:
            print item
        elif type(item) == BooleanType:
            pass
        else:
            tuple2dict(item)"""


def drawRectangle(width,height):
    if width >= 3:

        if height == 0 or height == width:
            print("*" * width)
            height -= 2
            drawRectangle(width, height)

        elif height > 0:
            print("*" + " "*(width-2) +"*")
            height -= 1
            drawRectangle(width, height)

    else:
        print("You're cutting corners!")


d = {"a":1,"b":2}
print(d[0])
