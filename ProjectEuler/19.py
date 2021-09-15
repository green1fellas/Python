month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
year = 1901
monthIndex = 0
dayIndex = 2
dayNum = 1

def increaseMonth(maxDayNum):
    global monthIndex
    global dayNum
    global year
    
    if(monthIndex < 11):
        if(dayNum  == 1):
            monthIndex += 1
    else:
        if(dayNum == 1):
            monthIndex = 0
            year += 1

def month31():
    global dayNum
    if(dayNum < 31):
        dayNum += 1
    else:
        dayNum = 1

def month30():
    global dayNum
    if(dayNum < 30):
        dayNum += 1
    else:
        dayNum = 1

def monthLeap():
    global dayNum
    global year

    leapDays = 28
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leapDays = 29
        else:
            if(year % 4 == 0):
                leapDays = 29

    if(dayNum < leapDays):
        dayNum += 1
    else:
        dayNum = 1

    return leapDays

def dayIncrease():
    global dayIndex
    if(dayIndex < 6):
        dayIndex += 1
    else:
        dayIndex = 0

def main():
    numOfSundaysOnFirst = 0
    while(not(monthIndex == 0 and year == 2001)):
        if(dayIndex == 0 and dayNum == 1):
            numOfSundaysOnFirst += 1

        if(monthIndex != 8 and 
        monthIndex != 3 and 
        monthIndex != 5 and 
        monthIndex != 10 and
        monthIndex != 1):
            month31()
            increaseMonth(31)

        elif(monthIndex == 1):
            leapDays = monthLeap()
            increaseMonth(leapDays)
        else:
            month30()
            increaseMonth(30)
        dayIncrease()
    # print(day[dayIndex] + " " + month[monthIndex] + " " + str(dayNum) + " " + str(year))
    print("Sundays On 1st Count: " + str(numOfSundaysOnFirst))
main()
